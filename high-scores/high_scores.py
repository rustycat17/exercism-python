def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    res = []
    while len(res) < 3:
        if len(scores) == 0:
            break
        res.append(max(scores))
        scores.pop(scores.index(max(scores)))

    return res
