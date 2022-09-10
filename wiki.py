import wikipediaapi
import sys

def main():
	wiki = wikipediaapi.Wikipedia('en')
	query = sys.argv[1]
	page = wiki.page(query)

	if not page.exists():
		print('nothing found for: ' + query)

	summary = page.summary.splitlines()

	print_sparse(summary)

def print_sparse(str_in):
	for line in str_in:
		print(line)
		print('\n')


if __name__=="__main__":
	main()

