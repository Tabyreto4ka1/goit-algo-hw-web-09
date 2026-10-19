from models import Author, Quote
import json

import connect

def read(filepath):
    with open (filepath, "r", encoding='utf-8') as f:
         list_of_dictionary=json.load(f)
    return list_of_dictionary

def authors(authors):
    for author in authors:
        Author(**author).save()

def quotes(quotes):
    for quote_data in quotes:
        author_name= quote_data["author"]
        author=Author.objects(fullname=author_name).first()
        quote_data["author"]=author
        Quote(**quote_data).save()

if __name__=="__main__":
    authors((read(r"authors.json")))
    quotes((read(r"quotes.json")))



