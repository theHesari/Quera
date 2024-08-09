def separator(ls):
    odds = []
    evens = []
    [odds.append(number) if (number % 2 == 0) else evens.append(number) for number in ls]
    return odds, evens


if __name__ == '__main__':
    print(separator([5, 9, 65, 43, 41, 21, 71, 1]))
