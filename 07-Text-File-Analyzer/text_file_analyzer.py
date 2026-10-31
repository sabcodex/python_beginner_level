
print("================================")
print("       TEXT FILE ANALYZER       ")
print("================================")

file_name = input("Enter the text file name (example: sample.txt): ")

try:
    with open(file_name, "r") as file:
        text = file.read()

    words = text.split()
    lines = text.splitlines()
    characters = len(text)

    print("----- FILE ANALYSIS -----")
    print("Number of words:", len(words))
    print("Number of characters:", characters)
    print("Number of lines:", len(lines))

except FileNotFoundError:
    print("Sorry! The file was not found.")
    print("Please check the file name and try again.")
