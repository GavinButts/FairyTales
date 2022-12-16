import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
import os

def htmlBook(text):
    book = epub.read_epub(text)
    items = list(book.get_items_of_type(ebooklib.ITEM_DOCUMENT))
    return items

def chapterToString(text):
    soup = BeautifulSoup(text.get_body_content(), 'html.parser')
    text = [para.get_text() for para in soup.find_all('p')]
    return ' '.join(text)

chapters = htmlBook("fairyTales.epub")

book = {}
for c in chapters:
    book[c.get_name()] = chapterToString(c)

print(book)
