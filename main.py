print("================================")
print("       TEXT ANALYZER")
print("================================")

text = input("\nEnter your text: ")

characters = len(text)
characters_without_spaces = len(text.replace(" ", ""))
words = len(text.split())
lines = len(text.splitlines())

print("\n--------- RESULTS ---------")
print(f"Characters              : {characters}")
print(f"Characters (no spaces)  : {characters_without_spaces}")
print(f"Words                   : {words}")
print(f"Lines                   : {lines}")

if characters == 0:
    print("\nYou entered an empty text.")
elif characters < 50:
    print("\nText size: Short")
elif characters < 150:
    print("\nText size: Medium")
else:
    print("\nText size: Long")

print("\n================================")
print("       Analysis Complete")
print("================================")