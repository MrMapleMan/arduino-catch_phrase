import random

categories = [
    "Animals",
    "Countries",
    "Famous People",
    "Movies",
    "Food & Drink",
    "Sports",
    "Technology",
    "Music",
    "Books",
    "Historical Events"
]

def gen_word_list(dict_path, word_list_path, num_words = 10000):
    with open(dict_path, 'r') as f:
        words = [line.strip() for line in f if line.strip()]
    rand_words = [random.choice(words) for _ in range(num_words)]
    with open(word_list_path, 'w') as f:
        for word in rand_words:
            f.write(word + ',[' + ';'.join([random.choice(categories) for _ in range(random.randint(1, 3))]) + ']\n')
            
if __name__ == "__main__":
    gen_word_list('/usr/share/dict/canadian-english', 'resources/word_lists.csv', num_words=10000)