import random


def random_subset(iterator, k):
    result = []
    n = 0

    for item in iterator:
        n += 1
        if len(result) < k:
            result.append(item)
        else:
            s = int(random.random() * n)
            if s < k:
                result[s] = item

    return result