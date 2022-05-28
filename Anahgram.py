 # Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here 
 if(sorted(word) == sorted(anagram)):
       
        answer = True
       
       else:

        answer = False
        
     print(answer)
   # return True

   str1 = input("Enter first word: ")
   str2 = input("Enter second word: ")
   find_anagram(str1, str2)
