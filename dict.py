

def main():
    word_dict = {}

    while True:
        word = input("Enter a Word press (Enter) for next : ").strip()
        if not word:
            break
        
        first_letter = word[0].lower()

        if first_letter in word_dict:
            word_dict[first_letter].append(word)
        else:
            word_dict[first_letter] = [word]

    print("\nWord Dictionary:")
    for first_letter, words in word_dict.items():
        print(f"Words starting with '{first_letter}'= {', '.join(words)}")

    while True:
        first_letter = input("\n Enter a Latter (press Enter to exit): ").strip().lower()

        if not first_letter:
            break
        if first_letter in word_dict:
            print(f"Words starting with '{first_letter}': {', '.join(word_dict[first_letter])}")
        else:
            print(f"No words found starting with '{first_letter}'.")

main()