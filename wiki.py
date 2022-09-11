import wikipediaapi
import sys
import gensim
from gensim.summarization import summarize

def main():
	wiki = wikipediaapi.Wikipedia('en')
	query = sys.argv[1]
	page = wiki.page(query)

	if not page.exists():
		print('nothing found for: ' + query)

	summary = page.summary.splitlines()
	print("\n" + "SUMMARAY:" + "\n")
	print(summary)
	print("\n" + "COMPRESSED ARTICLE: " + "\n")
	summarize_text_by_ratio(page.text)



def summarize_text_by_ratio(text):
	summary_by_ratio = summarize(text,ratio=0.1)
	print(summary_by_ratio)

if __name__=="__main__":
	main()

