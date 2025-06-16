from stats import get_word_count
from stats import get_chars_dict
from stats import get_sorted_chars_dicts

def get_book_text(file_path):
   file_contents = None
   
   with open(file_path) as f:
      file_contents = f.read()
   
   return file_contents

def main():
   content = get_book_text("books/frankenstein.txt")

   word_count = get_word_count(content)
   chars_dict = get_chars_dict(content)
   sorted_chars_dicts = get_sorted_chars_dicts(chars_dict)

   print("============ BOOKBOT ============")
   print("Analyzing book found at books/frankenstein.txt...")
   print("----------- Word Count ----------")
   print(f"Found {word_count} total words")
   print("--------- Character Count -------")
   
   for dict in sorted_chars_dicts:
      char = dict["char"]
      count = dict["num"]

      if char.isalpha():
         print(f"{char}: {count}")
   
   print("============= END ===============")


main()