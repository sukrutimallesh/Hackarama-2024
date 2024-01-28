"use client";

import { useState } from "react";
import Link from "next/link";
import { Article } from "@/lib/types";
import ArticleCard from "./ArticleCard";
import { Input } from "./ui/input";
import { Button } from "./ui/button";
import { Bot } from "lucide-react";
import {
	Tooltip,
	TooltipContent,
	TooltipProvider,
	TooltipTrigger,
} from "@/components/ui/tooltip";

interface NewsPageInterface {
	articles: Article[];
}

export default function NewsPage({ articles }: NewsPageInterface) {
	const [searchText, setSearchText] = useState<string>("");
	const [selectedTag, setSelectedTag] = useState<string | null>(null);

	// Filter articles by the current search text and selected tag
	articles = articles.filter((article) => {
		// Check search text
		if (article.title.toLowerCase().includes(searchText.toLowerCase())) {
			// TODO: Check tag
			return true;
		}

		// Return false if no conditions met
		return false;
	});

	return (
		<main className="flex flex-col gap-8">
			<div className="flex justify-between items-center">
				<h1 className="text-5xl font-bold tracking-tight">News</h1>
				<div className="flex gap-3">
					<TooltipProvider>
						<Tooltip>
							<TooltipTrigger>
								<Link href={"/chat"}>
									<Button
										variant="outline"
										size="icon"
										className="rounded-full p-2 group flex gap-2"
									>
										<Bot className="w-6 h-6 stroke-zinc-950 group-hover:stroke-zinc-800" />
									</Button>
								</Link>
							</TooltipTrigger>
							<TooltipContent>
								<p>Chat with AI</p>
							</TooltipContent>
						</Tooltip>
					</TooltipProvider>
					<Input
						type="email"
						placeholder="Search a title..."
						value={searchText}
						onChange={(e) => setSearchText(e.target.value)}
					/>
				</div>
			</div>
			<div className="grid grid-flow-row grid-cols-3 gap-4">
				{articles.map((article: Article) => {
					return (
						<ArticleCard
							key={article.article_url}
							article={article}
						/>
					);
				})}
			</div>
		</main>
	);
}
