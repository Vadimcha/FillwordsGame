import itertools
import random
import os
import pandas as pd

n = 0
m = 0
pole = []
lens = []
dictionary = []
attempt = []
words = []
words_copy = []

def init_pole():
    global pole
    pole = [["#"] * (n + 2) for _ in range(n + 2)]
    for h in range(0, n + 1):
        pole[0][h] = pole[h][0] = pole[n + 1][h] = pole[h][n + 1] = pole[n + 1][n + 1] = "*"

def generate_word_lens():
    global n, m
    target_sum = n * n
    possible_numbers = list(range(4, 11))
    suitable = []
    for combination in itertools.product(possible_numbers, repeat=m):
        if sum(combination) == target_sum:
            suitable.append(combination)
    return list(random.choice(suitable))

def print_pole():
    r = []
    for y in range(1, n + 1):
        row = []
        for x in range(1, n + 1):
            row.append(pole[y][x])
        print(row)
        r.append(row)
    return r

def generate_word_begins():
    global words, pole, dictionary
    init_pole()
    words = [[] for _ in range(m)]
    for word in range(1, m + 1):
        x, y = random.randint(1, n), random.randint(1, n)
        while pole[y][x] != '#':
            x, y = random.randint(1, n), random.randint(1, n)
        words[word - 1].append([y, x])
        pole[y][x] = dictionary[word - 1][-1]

def get_random_word(length):
    file_path = os.path.join('words', f'Words with len {length}.csv')
    if not os.path.isfile(file_path):
        print(f"Файл {file_path} не существует.")
        return None
    data = pd.read_csv(file_path, header=None)
    if data.empty:
        print(f"Файл {file_path} пустой.")
        return None
    random_word = random.choice(data[0].tolist())
    return random_word

def dfs(x, y, word_number, leng):
    global attempt, dictionary
    attempt[y][x] = dictionary[word_number][leng]
    if leng == 0:
        return 1
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    random.shuffle(directions)
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if pole[ny][nx] == "#":
            return dfs(nx, ny, word_number, leng - 1)
    return 0

def generate_pole():
    global attempt, words, pole
    attempt = pole
    flag = 1
    for num in range(m):
        res = dfs(words[num][-1][1], words[num][-1][0], num, lens[num] - 1)
        if not res:
            flag = 0
            break
    if flag:
        pole = attempt
    return flag

def getGame(size):
    global n, m, pole, lens, dictionary, attempt, words

    n = size
    m = random.choice(range(n * n // 10 + 1, n * n // 4))
    print(f"Game {n}×{n} with {m} words")
    lens = generate_word_lens()
    dictionary = [get_random_word(i) for i in lens]
    attempt = pole
    words = [[] for _ in range(m)]

    print(f"Lens: {lens}")
    print(f"Dictionary: {dictionary}")

    while True:
        generate_word_begins()
        if generate_pole():
            pole = attempt
            break

    result = print_pole()
    return dictionary, result


from fastapi import FastAPI
from typing import List, Dict
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/getWords/{size}")
def read_root(size: int) -> Dict[str, List[str]]:
    dictio, resul = getGame(size)
    formatted_result = [''.join(row) for row in resul]

    return {
        "answers": dictio,
        "dictionary": formatted_result
    }
