import articlesData from "@/articles.json";
import { Article } from "./types";

export default function getArticlesFromJSON(): Article[] {
    return articlesData as Article[];
}