import { Article } from "@/lib/types";
import ArticleCard from "./ArticleCard";

interface NewsPageInterface {
	articles: Article[];
}

export default function NewsPage({ articles }: NewsPageInterface) {
	return (
		<main className="flex flex-col gap-8">
			<h1 className="text-5xl font-bold tracking-tight">News</h1>
			<div className="grid grid-flow-row grid-cols-3 gap-4">
				{articles.map((article: Article) => {
					return <ArticleCard article={article} />;
				})}
			</div>
		</main>
	);
}
