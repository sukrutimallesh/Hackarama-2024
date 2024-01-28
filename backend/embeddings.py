import yahoo
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain_community.vectorstores.pinecone import Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
import pprint
from dotenv import load_dotenv
import os
from pinecone import Pinecone
import openai


def main() -> None:
    # Get info for embeddings and Pinecone
    load_dotenv()
    pinecone_api_key: str = os.environ.get("PINECONE_API_KEY")
    openai_api_key: str = os.environ.get("OPENAI_API_KEY")

    article_infos: list[dict] = yahoo.main()
    
    article_texts: list[str] = [article["article_content"] for article in article_infos]
    article_metadatas : list[dict] = [
        {
            "title": article["title"],
            "article_url": article["article_url"],
            "image_url": article["image_url"] if isinstance(article["image_url"], str) else "",
            "tags": [],
        } for article in article_infos
    ]

    # Split all the texts into chunks (Documents)
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=25,
        length_function=len,
        is_separator_regex=False,
    )
    documents = text_splitter.create_documents(article_texts, article_metadatas)

    # Create Pinecone information
    pc = Pinecone(api_key=pinecone_api_key)
    index = pc.Index("lpl-financial-hackathon")

    for i, document in enumerate(documents):
        res = openai.embeddings.create(
            input=document.page_content,
            model="text-embedding-3-small",
        )
        embedding: list[float] = res.data[0].embedding

        index.upsert(
            vectors=[
                (
                    str(i), 
                    embedding, 
                    {
                        "title": document.metadata["title"],
                        "article_url": document.metadata["article_url"],
                        "image_url": document.metadata["image_url"],
                        "tags": document.metadata["tags"],
                        "text_chunk": document.page_content
                    }
                )
            ]
        )

        # TODO: Delete to do all embeddings
        break
    
    print("DONE!")


if __name__ == "__main__":
    main()
