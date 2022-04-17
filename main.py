from fastapi import FastAPI
import json
import os
import random


this_file_folder = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(this_file_folder, "words.txt"), "r") as input:
    available_words = [word.replace("\n", "") for word in input.readlines()]


app = FastAPI()


@app.get("/{seed}/")
async def words(seed):
    random.seed(seed)
    selected_words = random.sample(available_words, k=min(len(available_words), 25))

    words_per_team_count = len(selected_words) // 3

    blue_words = selected_words[:words_per_team_count]
    red_words = selected_words[words_per_team_count : words_per_team_count * 2]
    black_words = [selected_words[words_per_team_count * 2]]
    white_words = selected_words[words_per_team_count + 1 :]

    words = (
        [{"name": word, "role": "blue"} for word in blue_words]
        + [{"name": word, "role": "red"} for word in red_words]
        + [{"name": word, "role": "black"} for word in black_words]
        + [{"name": word, "role": "white"} for word in white_words]
    )

    random.shuffle(words)

    return {"words": words}
