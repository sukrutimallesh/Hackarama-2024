import { Bot, UserRound } from "lucide-react";

export default function ChatSection({ isAI }: { isAI: boolean }) {
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
			<p className="col-start-2 col-span-full">
				Lorem, ipsum dolor sit amet consectetur adipisicing elit. Autem
				reiciendis dignissimos molestiae laborum error reprehenderit?
				Molestiae accusamus harum, ratione, omnis veniam ut illum
				doloremque tempore eaque nam facilis, voluptas officiis? In
				tempora natus commodi debitis, non quia tenetur ullam architecto
				repellendus incidunt neque veniam praesentium nesciunt
				voluptatibus deserunt sed esse? Nesciunt delectus cum ipsum
				possimus praesentium, deserunt fuga debitis nobis. Eveniet
				officiis quia cum. Veritatis tempore hic mollitia,
				necessitatibus aperiam dolorem. Illo, impedit rem. Ratione at
				adipisci, eos beatae voluptatem similique molestias excepturi
				iste exercitationem odio iusto. Quasi, blanditiis optio! Saepe
				itaque expedita aperiam est vitae ut dolorum, tempore
				consequuntur qui aliquam excepturi molestiae officiis vero rem
				corrupti ex eaque perferendis explicabo minus. Non deserunt,
				provident ea commodi ipsum nisi. Ut, veritatis laboriosam.
				Assumenda dolore similique perspiciatis temporibus voluptatibus
				reprehenderit ea pariatur exercitationem esse numquam,
				laboriosam omnis beatae architecto eius est voluptate ducimus
				incidunt repellat et suscipit aliquam vero. Eum.
			</p>
		</div>
	);
}
