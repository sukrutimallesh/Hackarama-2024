import { type ClassValue, clsx } from "clsx"
import { twMerge } from "tailwind-merge"
import articlesData from "@/articles.json";
import { Article } from "./types";

export function getArticlesFromJSON(): Article[] {
    return articlesData as Article[];
}

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}
