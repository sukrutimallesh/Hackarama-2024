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
import json
import tiktoken

def num_tokens_from_string(string: str, encoding_name: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

def main() -> None:
    # Get info for embeddings and Pinecone
    load_dotenv()
    pinecone_api_key: str = os.environ.get("PINECONE_API_KEY")
    openai_api_key: str = os.environ.get("OPENAI_API_KEY")

    # Read JSON data from the file into a list of dictionaries
    with open("articles.json", 'r') as json_file:
        articles: list[dict] = json.load(json_file)

    article_texts: list[str] = [article["article_content"] for article in articles]
    article_metadatas : list[dict] = [
        {
            "title": article["title"] if isinstance(article["title"], str) else "",
            "article_url": article["article_url"],
            "image_url": article["image_url"] if isinstance(article["image_url"], str) else "",
            "tags": [],
        } for article in articles
    ]

    # Split all the texts into chunks (Documents)
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=25,
        length_function=len,
        is_separator_regex=False,
    )
    documents = text_splitter.create_documents(article_texts, article_metadatas)

    # Print out cost
    num_tokens = 0
    num_of_words = 0
    for document in documents:
        num_tokens += num_tokens_from_string(document.page_content, "cl100k_base")
        num_of_words += len(document.page_content.split())

    print("Total number of text chunks: " + str(len(documents)))
    print("Total number of words: " + str(num_of_words))
    print("Total number of tokens: " + str(num_tokens))
    print("Total cost: ${:.2f}".format((num_tokens / 1000) * 0.00002))

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
    
    print("DONE!")


if __name__ == "__main__":
    main()
