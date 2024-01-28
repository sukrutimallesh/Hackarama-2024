import Link from "next/link";

export default function Navbar() {
	return (
		<nav className="flex justify-between pb-16">
			<span>NewsAI</span>
			<div className="flex gap-4">
				<Link
					href={"/"}
					className="hover:cursor-pointer hover:underline"
				>
					News
				</Link>
				<Link
					href={"/chat"}
					className="hover:cursor-pointer hover:underline"
				>
					Chat with AI
				</Link>
			</div>
		</nav>
	);
}
