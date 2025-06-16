def get_word_count(book_content):
   words = book_content.split()
   return len(words)

def get_chars_dict(book_content):
   charcter_count = {}

   for char in book_content:
      lowercase = char.lower()

      if lowercase in charcter_count:
         charcter_count[lowercase] += 1
      else:
         charcter_count[lowercase] = 1
      
   return charcter_count

# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(dict):
    return dict["num"]

def get_sorted_chars_dicts(chars_dict):
   sorted_chars_list = []

   for char in chars_dict:
      sorted_chars_list.append({"char": char, "num": chars_dict[char]})

   sorted_chars_list.sort(reverse=True, key=sort_on) 
   return sorted_chars_list