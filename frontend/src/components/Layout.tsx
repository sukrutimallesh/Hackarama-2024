export default function Layout({ children }: { children: React.ReactNode }) {
	return (
		<div className="px-96 py-8 bg-zinc-200 min-w-full min-h-screen flex flex-col gap-8">
			{children}
		</div>
	);
}
