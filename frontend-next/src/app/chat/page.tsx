import ChatSection from "@/components/ChatSection";

const lorem =
	"Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque, nulla voluptate praesentium reiciendis unde iste, dolorum vero excepturi accusamus velit numquam pariatur voluptatem enim laborum alias. Debitis itaque pariatur sapiente? Neque officiis, obcaecati aliquam perferendis ex eligendi eius dicta commodi a veniam voluptatem fugiat esse in quaerat magnam, laborum ducimus voluptatibus illum autem, animi quasi necessitatibus impedit itaque? Vel, dolor? Voluptatum dignissimos quod magni, iusto quidem, eligendi vitae rem quae, asperiores ducimus ea illum reiciendis. Quis perspiciatis non assumenda iure quas excepturi laboriosam eligendi, rem doloribus velit consequuntur ratione est! Quidem quisquam at error aperiam dignissimos atque odit ullam tempora aut eligendi mollitia aliquid nobis adipisci minima, ex asperiores voluptatem fuga. Maxime quos asperiores consequatur illo aliquam, eum iure placeat! Quasi sunt voluptas esse cum, qui enim error. Rerum architecto optio error facere possimus nisi mollitia quod tempora nulla sint? Et ab neque, accusantium nam dicta facilis laudantium veritatis quos.";

export default function ChatPage() {
	return (
		<main className="flex flex-col gap-12">
			<ChatSection
				isAI={true}
				text={
					"Hello! You can ask me anything about recent financial news and stocks! What would you like to know?"
				}
			/>
			<ChatSection isAI={false} text={lorem} />
		</main>
	);
}
