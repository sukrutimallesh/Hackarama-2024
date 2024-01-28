import ChatSection from "@/components/ChatSection";

export default function ChatPage() {
	return (
		<main className="flex flex-col gap-12">
			<ChatSection isAI={true} />
			<ChatSection isAI={false} />
		</main>
	);
}
