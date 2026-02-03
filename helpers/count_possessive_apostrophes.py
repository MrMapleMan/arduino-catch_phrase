

def count_possessive_apostrophes(file_path):
    count = 0
    total_words = 0
    with open(file_path, 'r') as f:
        for line in f:
            words = line.strip().split()
            total_words += len(words)
            for word in words:
                if word.endswith("'s") or word.endswith("’s"):
                    count += 1
    print(f"Total possessive apostrophes found: {count:,} of {total_words:,} words ({count/total_words*100:.2f}%).")

def main():
    count_possessive_apostrophes("/usr/share/dict/words")
    
if __name__ == "__main__":
    main()