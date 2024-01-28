import { Bot, UserRound } from "lucide-react";

export default function ChatSection({
	isAI,
	text,
}: {
	isAI: boolean;
	text: string;
}) {
	return (
		<div className="gap-x-4 gap-y-2 grid grid-cols-16 items-center">
			{isAI ? (
				<Bot className="h-8 w-8 stroke-zinc-950 col-span-1" />
			) : (
				<UserRound className="h-8 w-8 stroke-zinc-950 col-span-1" />
			)}
			<span className="font-bold col-start-2 col-span-full">
				{isAI ? "NewsBot" : "You"}
			</span>
			<p className="col-start-2 col-span-full">{text}</p>
		</div>
	);
}
