word1 = input("Enter first word: ").lower()
word2 = input("Enter second word: ").lower()
if sorted(word1) == sorted(word2):
    print(f"{word1} and {word2} are Anagram")
else:
    print(f"{word1} and {word2} are Not Anagram")