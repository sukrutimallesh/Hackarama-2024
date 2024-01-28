// Components Imports
import ArticleCard from "@/components/ArticleCard";
import NewsPage from "@/components/NewsPage";

// Types Imports
import { Article } from "@/lib/types";

// Helper Function Imports
import getArticlesFromJSON from "@/lib/getArticlesFromJSON";

export default function Home() {
	const articles = getArticlesFromJSON();
	console.log(typeof articles);

	return (
		<>
			<NewsPage articles={articles} />
		</>
	);
}
