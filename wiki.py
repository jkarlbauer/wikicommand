#!/usr/bin/python3

import wikipediaapi
import sys
from summarizer import TransformerSummarizer

def main():
	wiki = wikipediaapi.Wikipedia('en')
	query = sys.argv[1]
	page = wiki.page(query)

	if not page.exists():
		print('nothing found for: ' + query)

	#summary = page.summary.splitlines()
	print("\n" + "SUMMARAY:" + "\n")
	print(page.summary)
	print("\n" + "COMPRESSED ARTICLE: " + "\n" + summarize_text(page.text))

def summarize_text(body):
    GPT2_model = TransformerSummarizer(transformer_type="GPT2",transformer_model_key="gpt2")
    full = ''.join(GPT2_model(body, min_length=60))
    return full

if __name__=="__main__":
	main()

