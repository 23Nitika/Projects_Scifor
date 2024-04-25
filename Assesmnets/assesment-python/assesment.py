def count_lines_words(filename):
    total_lines = 0
    total_words = 0
    total_letters = 0
    lines_with_letter = {}

    with open(filename, 'r') as file:
        for line in file:
            total_lines += 1

            words = line.split()
            total_words += len(words)

            total_letters += sum(len(word) for word in words)

            first_letter = line.strip()[0].lower()

            if first_letter.isalpha():
                lines_with_letter[first_letter] = lines_with_letter.get(first_letter, 0)+1
            
            return  total_lines, total_words, total_letters, lines_with_letter
        

total_lines, total_words, total_letters, lines_with_letter = count_lines_words('sample.txt')

print("Total no. of lines: ", total_lines)
print("Total no. of words: ", total_words)
print("Total no. of letters: ", total_letters)
print("Lines starting with alphabet:")
for letter, count in lines_with_letter.items():
    print(f"{letter.upper()}: {count}")
