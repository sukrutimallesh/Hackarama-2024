import { Inter } from "next/font/google";
import "./globals.css";

const inter = Inter({ subsets: ["latin"] });

export default function RootLayout({
	children,
}: Readonly<{
	children: React.ReactNode;
}>) {
	return (
		<html lang="en">
			<body className={`${inter.className} text-zinc-950`}>
				<div className="px-96 py-16 min-w-full min-h-screen">
					{children}
				</div>
			</body>
		</html>
	);
}
