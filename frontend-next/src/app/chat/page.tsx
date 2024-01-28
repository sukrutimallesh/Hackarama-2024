"use client";

import ChatSection from "@/components/ChatSection";
import { Button } from "@/components/ui/button";
import { useState } from "react";
import { ChatHistoryObj } from "@/lib/types";
import { Textarea } from "@/components/ui/textarea";
import Link from "next/link";
import { Sparkles } from "lucide-react";

const baseChatHistory: ChatHistoryObj[] = [
	{
		role: "system",
		content:
			"You are a helpful assistant with information about financial news. Utilize the context that is given to you to answer the user's questions. If the context does not provide an answer to you, then simply state \"I don't know the answer to that.\"",
	},
];

export default function ChatPage() {
	const [chatMessage, setChatMessage] = useState<string>("");
	const [chatHistory, setChatHistory] =
		useState<ChatHistoryObj[]>(baseChatHistory);

	// Filter out system chats
	const chatsToDisplay = chatHistory.filter((chat) => chat.role !== "system");

	async function getAIResponse() {
		// Add the new message to a "fake" chat history essentially
		let historyToSend = chatHistory;
		historyToSend.push({
			role: "user",
			content: chatMessage,
		});

		const res = await fetch("/api", {
			method: "POST",
			body: JSON.stringify(historyToSend),
			headers: {
				"Content-Type": "application/json",
			},
		});

		const json = await res.json();
		setChatHistory(json["data"] as ChatHistoryObj[]);
	}

	return (
		<main className="flex flex-col gap-12">
			<ChatSection
				isAI={true}
				text={
					"Hello! You can ask me anything about recent financial news and stocks! What would you like to know?"
				}
			/>
			{chatsToDisplay.map((chatObj) => {
				return (
					<ChatSection
						isAI={chatObj.role === "assistant"}
						text={chatObj.content}
					/>
				);
			})}
			<div className="flex flex-col gap-4 fixed bottom-16 left-1/2 transform -translate-x-1/2 min-w-[512px]">
				<Textarea
					value={chatMessage}
					onChange={(e) => setChatMessage(e.target.value)}
					placeholder="Ask a question here"
					className="resize-y drop-shadow-lg w-full"
				/>
				<div className="flex flex-col gap-2">
					<Button
						onClick={getAIResponse}
						className="w-full flex gap-1"
					>
						<span>Ask</span>
						<Sparkles className="w-4 h-4" />
					</Button>
					<Link href="/" className="w-full">
						<Button
							variant="outline"
							className="border-zinc-300 w-full"
						>
							Go back to News
						</Button>
					</Link>
				</div>
			</div>
		</main>
	);
}
