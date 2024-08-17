import math


def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    primes = []

    for num in range(2, int(math.sqrt(limit)) + 1):
        if is_prime[num]:
            for multiple in range(num * num, limit + 1, num):
                is_prime[multiple] = False

    primes = [num for num in range(2, limit + 1) if is_prime[num]]
    return primes


def optimal_move(candies_in_box):
    primes = sieve_of_eratosthenes(candies_in_box)
    possible_moves = []

    for prime in primes:
        max_power = int(math.log(candies_in_box, prime))
        possible_moves.append(int(pow(prime, max_power)))

    return max(possible_moves) if possible_moves else candies_in_box


def game_round(candy_dict):
    turn_counter = 0

    while sum(candy_dict[1]) > 0:
        is_sherlock_turn = (turn_counter % 2 == 0)
        max_candies_box_index = candy_dict[1].index(max(candy_dict[1]))
        candies_in_box = candy_dict[1][max_candies_box_index]

        candy_dict[1][max_candies_box_index] -= optimal_move(candies_in_box)
        turn_counter += 1

    return 'Sherlock' if is_sherlock_turn else 'Moriarty'


def main():
    test_cases = int(input())
    test_inputs = [input() for _ in range(2 * test_cases)]

    box_numbers = test_inputs[0::2]
    candy_counts = test_inputs[1::2]

    test_dicts = {
        int(box_num): list(map(int, candy_counts[idx].split()))
        for idx, box_num in enumerate(box_numbers)
    }

    results = [game_round(test_case) for test_case in test_dicts.items()]
    print(*results, sep='\n')


if __name__ == '__main__':
    main()
