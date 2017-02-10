import random

examples = [
    "schön",
    "weiß",
    "grün",
    "nächster",
    "Österreich",
    "Übertreiben",
    "Änderungen",
    "Exposé"
]


def get():
    ret = []
    while len(ret) < 3:
        example = random.choice(examples)
        if example not in ret:
            ret.append(example)

    return {
        "text": " ".join(ret)
    }, 200
