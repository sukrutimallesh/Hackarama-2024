// Components Imports
import NewsPage from "@/components/NewsPage";

// Helper Function Imports
import { getArticlesFromJSON } from "@/lib/utils";

export default function Home() {
	const articles = getArticlesFromJSON();

	return (
		<>
			<NewsPage articles={articles} />
		</>
	);
}
