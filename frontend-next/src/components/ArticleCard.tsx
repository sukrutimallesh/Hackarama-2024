import { Article } from "@/lib/types";
import { Button } from "./ui/button";

interface ArticleCardProps {
	article: Article;
}

export default function ArticleCard({ article }: ArticleCardProps) {
	return (
		<div className="outline outline-1 outline-zinc-200 shadow rounded-lg flex flex-col overflow-hidden h-full w-full">
			{article.image_url ? (
				<img
					className="aspect-video object-cover"
					src={article.image_url}
					alt={article.title}
				/>
			) : (
				<div className="aspect-video object-cover bg-gradient-to-r h-full from-cyan-500 to-blue-600"></div>
			)}
			<div className="p-4 flex flex-col gap-4 justify-between h-full">
				<h2 className="font-semibold text-xl">{article.title}</h2>
				<div className="flex justify-end">
					<a href={article.article_url}>
						<Button>Read More</Button>
					</a>
				</div>
			</div>
		</div>
	);
}
