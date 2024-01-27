import "./App.css";
import { useState } from "react";
import Layout from "@/components/Layout";
import { Button } from "@/components/ui/button";
import {
	Card,
	CardContent,
	CardDescription,
	CardFooter,
	CardHeader,
	CardTitle,
} from "@/components/ui/card";

type Article = {
	title: string;
	date: string;
	link: string;
};

const exampleData: Article[] = [
	{
		title: "Small Boeing suppliers lament new turmoil around 737 planes",
		date: "January 25, 2024",
		link: "https://www.reuters.com/business/aerospace-defense/small-boeing-suppliers-lament-new-turmoil-around-737-planes-2024-01-26/",
	},
	{
		title: "Forbes' unionized journalists stage first walk-out in magazine's history",
		date: "January 25, 2024",
		link: "https://www.reuters.com/business/media-telecom/forbes-unionized-journalists-stage-first-walk-out-magazines-history-2024-01-25/",
	},
	{
		title: "PayPal to launch AI-based products as new CEO aims to revive share price",
		date: "January 25, 2024",
		link: "https://www.reuters.com/business/paypal-launch-ai-based-products-new-ceo-aims-revive-share-price-2024-01-25/",
	},
];

function App() {
	return (
		<Layout>
			{exampleData.map((article) => {
				return (
					<a href={article.link}>
						<Card>
							<CardHeader>
								<CardTitle>{article.title}</CardTitle>
								<CardDescription>
									{article.date}
								</CardDescription>
							</CardHeader>
						</Card>
					</a>
				);
			})}
		</Layout>
	);
}

export default App;
