# WikiCommand

WikiCommand prints a Wikipedia summary from a given query.

Wikipedia articles are retrieved using the Wikipedia API: https://pypi.org/project/Wikipedia-API/

Summaries are generated using GPT2

To use, create and activate a virtual environment: 
$ python3 venv my_env
$ source my_env/bin/activate

install requirements:
pip instal -r requirements.txt

run:
python3 wiki.py "<your_query"
