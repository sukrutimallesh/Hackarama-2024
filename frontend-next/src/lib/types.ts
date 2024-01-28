export type Article = {
	title: string;
	article_url: string;
	image_url: string | null;
	tags: string[];
	article_content: string;
};

export type ChatHistoryObj = {
	role: "system" | "user" | "assistant";
	content: string;
}