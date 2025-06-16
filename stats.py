def get_word_count(book_content):
   words = book_content.split()
   return len(words)

def count_characters(book_content):
   charcter_count = {}

   for char in book_content:
      lowercase = char.lower()

      if lowercase in charcter_count:
         charcter_count[lowercase] += 1
      else:
         charcter_count[lowercase] = 1
      
   return charcter_count