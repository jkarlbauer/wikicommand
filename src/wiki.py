#!/usr/bin/python3

import wikipediaapi
import sys
from summarizer import TransformerSummarizer

def main():
	wiki = wikipediaapi.Wikipedia('en')
	query = sys.argv[1]
	page = wiki.page(query)

	if not page.exists():
	    return

	wikipedia_page_summary = page.summary
	print("\n" + "SUMMARAY:" + "\n")
	print(wikipedia_page_summary)
	print("\n" + "COMPRESSED ARTICLE: " + "\n")
	compressed_article = compress_article(page.text)
	print(compressed_article)

def compress_article(body):
    GPT2_model = TransformerSummarizer(transformer_type="GPT2",transformer_model_key="gpt2")
    full = ''.join(GPT2_model(body, min_length=60))
    return full

if __name__=="__main__":
	main()

