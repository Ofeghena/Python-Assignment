# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(str1, str2):
    # Solution to assignment!
    str1 = input("Enter your first word:")
    str2 = input("Enter your second word:"

    if (sorted(str1) == sorted(str2)):    
      return True
    else:
      return False
print(find_anagram("str1","str2"))      
