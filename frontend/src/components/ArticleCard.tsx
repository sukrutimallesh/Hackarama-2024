import { Article } from "@/lib/types";

interface ArticleCardProps {
	article: Article;
}

export default function ArticleCard({ article }: ArticleCardProps) {
	return (
		<a href={article.article_url}>
			<div className="bg-white shadow rounded-lg flex flex-col gap-4 overflow-hidden h-full w-full">
				{article.image_url ? (
					<img
						className="aspect-video object-cover w-full"
						src={article.image_url}
						alt={article.title}
					/>
				) : (
					<div className="aspect-video object-cover w-full h-full bg-gradient-to-r from-cyan-500 to-blue-500"></div>
				)}
				<h2 className="font-bold px-4 pb-4">{article.title}</h2>
			</div>
		</a>
	);
}
