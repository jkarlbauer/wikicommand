import wikipediaapi
import sys
import utils

def main():
	wiki = wikipediaapi.Wikipedia('en')
	query = sys.argv[1]
	page = wiki.page(query)

	if not page.exists():
		print("nothing found for: " + query)
		return

	utils.log(page.summary, "SUMMARY")
	utils.log(utils.gpt2_summarize(page.text), "COMPRESSED ARTICLE")

if __name__=="__main__":
	main()

