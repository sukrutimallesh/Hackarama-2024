import "./App.css";
import { useState } from "react";
import { Button } from "./components/ui/button";

function App() {
	const [count, setCount] = useState<number>(0);

	return (
		<div className="px-96 py-8 bg-zinc-200 min-w-full min-h-screen">
			<div className="w-full h-32 bg-white shadow rounded-2xl p-4">
				<Button onClick={() => setCount(count + 1)}>
					Count: {count}
				</Button>
			</div>
		</div>
	);
}

export default App;
