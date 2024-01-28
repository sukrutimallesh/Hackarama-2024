import { Article } from "@/lib/types";

interface ArticleCardProps {
	article: Article;
}

export default function ArticleCard({ article }: ArticleCardProps) {
	return (
		<a className="hover:cursor-pointer group" href={article.article_url}>
			<div className="bg-white shadow rounded-lg flex flex-col gap-4 overflow-hidden h-full w-full group-hover:bg-zinc-100">
				{article.image_url ? (
					<img
						className="aspect-video object-cover w-full group-hover:"
						src={article.image_url}
						alt={article.title}
					/>
				) : (
					<div className="aspect-video object-cover w-full h-full bg-gradient-to-r from-zinc-500 to-zinc-600"></div>
				)}
				<h2 className="font-semibold px-4 pb-4 group-hover:text-zinc-800">
					{article.title}
				</h2>
			</div>
		</a>
	);
}
