from stats import get_word_count
from stats import count_characters

def get_book_text(file_path):
   file_contents = None
   
   with open(file_path) as f:
      file_contents = f.read()
   
   return file_contents

def main():
   content = get_book_text("books/frankenstein.txt")

   word_count = get_word_count(content)
   character_count = count_characters(content)

   print(f"{word_count} words found in the document")
   print(character_count)


main()