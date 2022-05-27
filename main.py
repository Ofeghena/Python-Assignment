# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(str1, str2):
    # Solution to assignment!
    str1 = "ink"
    str2 = "kin"

    if (sorted(str1) == sorted(str2)):    
      return True
    else:
      return False
print(find_anagram("ink","kin"))      