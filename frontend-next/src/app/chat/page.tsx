"use client";

import ChatSection from "@/components/ChatSection";
import { Button } from "@/components/ui/button";
import { useState } from "react";
import { ChatHistoryObj } from "@/lib/types";

const lorem =
	"Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque, nulla voluptate praesentium reiciendis unde iste, dolorum vero excepturi accusamus velit numquam pariatur voluptatem enim laborum alias. Debitis itaque pariatur sapiente? Neque officiis, obcaecati aliquam perferendis ex eligendi eius dicta commodi a veniam voluptatem fugiat esse in quaerat magnam, laborum ducimus voluptatibus illum autem, animi quasi necessitatibus impedit itaque? Vel, dolor? Voluptatum dignissimos quod magni, iusto quidem, eligendi vitae rem quae, asperiores ducimus ea illum reiciendis. Quis perspiciatis non assumenda iure quas excepturi laboriosam eligendi, rem doloribus velit consequuntur ratione est! Quidem quisquam at error aperiam dignissimos atque odit ullam tempora aut eligendi mollitia aliquid nobis adipisci minima, ex asperiores voluptatem fuga. Maxime quos asperiores consequatur illo aliquam, eum iure placeat! Quasi sunt voluptas esse cum, qui enim error. Rerum architecto optio error facere possimus nisi mollitia quod tempora nulla sint? Et ab neque, accusantium nam dicta facilis laudantium veritatis quos.";

const baseChatHistory: ChatHistoryObj[] = [
	{
		role: "system",
		content:
			"You are a helpful assistant with information about financial news. Utilize the context that is given to you to answer the user's questions. If the context does not provide an answer to you, then simply state \"I don't know the answer to that.\"",
	},
	{
		role: "user",
		content: "This is my first question as a user.",
	},
];

export default function ChatPage() {
	const [chatHistory, setChatHistory] =
		useState<ChatHistoryObj[]>(baseChatHistory);

	// Filter out system chats
	const chatsToDisplay = chatHistory.filter((chat) => chat.role !== "system");

	async function testAPI() {
		const res = await fetch("/api", {
			method: "POST",
			body: JSON.stringify(chatHistory),
			headers: {
				"Content-Type": "application/json",
			},
		});
		const json: ChatHistoryObj[] = await res.json();
		setChatHistory(json);
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
			<Button onClick={testAPI}>Test</Button>
		</main>
	);
}
