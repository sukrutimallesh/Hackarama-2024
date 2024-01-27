import "./App.css";
import { useState } from "react";
import Layout from "@/components/Layout";
import { Button } from "@/components/ui/button";
import {
	Card,
	CardContent,
	CardDescription,
	CardFooter,
	CardHeader,
	CardTitle,
} from "@/components/ui/card";

function App() {
	const [count, setCount] = useState<number>(0);

	return (
		<Layout>
			{/* <div className="w-full h-32 bg-white shadow rounded-2xl p-4">
				<Button onClick={() => setCount(count + 1)}>
					Count: {count}
				</Button>
			</div> */}
			<Card>
				<CardHeader>
					<CardTitle>Example Card</CardTitle>
					<CardDescription>
						A description would go here.
					</CardDescription>
				</CardHeader>
				<CardContent>
					<p>Some content here.</p>
					<Button onClick={() => setCount(count + 1)}>
						Count: {count}
					</Button>
				</CardContent>
				<CardFooter>Footer here.</CardFooter>
			</Card>
		</Layout>
	);
}

export default App;
