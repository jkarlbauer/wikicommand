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

	summarize_text_by_ratio(page.summary)


def print_sparse(str_in):
	for line in str_in:
		print(line)
		print('\n')

def summarize_text_by_ratio(text):
	summary_by_ratio = summarize(text,ratio=0.5)
	print(summary_by_ratio)

if __name__=="__main__":
	main()

