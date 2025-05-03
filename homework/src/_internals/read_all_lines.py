import os


def read_all_lines():
    counter = {}
    input_file_list = os.listdir("data/input/")
    for filename in input_file_list:
        with open("data/input/" + filename) as f:
            for l in f:
                for w in l.split():
                    w = w.lower().strip(",.!?")
                    counter[w] = counter.get(w, 0) + 1
    return counter
