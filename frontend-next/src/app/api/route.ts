import { NextRequest, NextResponse } from "next/server";
import { Pinecone } from "@pinecone-database/pinecone"
import OpenAI from "openai";
import { ChatHistoryObj } from "@/lib/types";

export async function POST(req: NextRequest) {
    // Connect to Pinecone and the specific index, as well as OpenAI
    const pc = new Pinecone()
    const index = pc.index("lpl-financial-hackathon")
    const openai = new OpenAI({
        apiKey: process.env.OPENAI_API_KEY,
    });

    // Get the chat history passed in and get the question from it (the last sent message)
    const chatHistory: ChatHistoryObj[] = await req.json();
    const question: string = chatHistory[chatHistory.length - 1]["content"]
    
    // Create an embedding of the question
    const embeddingResponse = await openai.embeddings.create({
        model: "text-embedding-3-small",
        input: question,
    })
    const embedding: number[] = embeddingResponse.data[0].embedding;

    // Get the 3 most similar vectors based on the question embedding (cosine similarity)
    const pineconeResponse = await index.query({
        topK: 3,
        vector: embedding,
        includeMetadata: true,
    });

    // Get the text chunks and append them to the question
    const relevantTextChunks: string[] = pineconeResponse.matches.map((pineMatch) => {
        return pineMatch["metadata"]!["text_chunk"] as string;
    })
    const questionWithContext: string = `### User Question ###\n${question}\n\n### Context ###'''${relevantTextChunks.join("\n-----\n")}'''`

    // Get rid of the old chat message from the user and push the new one to the message history with the new context
    let newChatHistory: ChatHistoryObj[] = chatHistory.slice(0, -1)
    newChatHistory.push({"role": "user", "content": questionWithContext})

    // Get the response and add it to the chat history
    const chatCompletion = await openai.chat.completions.create({
        messages: newChatHistory,
        model: "gpt-3.5-turbo",
    });

    // NOTE: We are leaving out the context message from the user on purpose so that the token context window can remain open for improve memory for the AI
    const message = chatCompletion["choices"][0]["message"] as ChatHistoryObj;
    chatHistory.push(message);

    // Return the new chat history
    return NextResponse.json({
        data: chatHistory,
    });
}