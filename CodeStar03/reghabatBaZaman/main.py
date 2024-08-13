def calculate_time(k, n):
    t = 0
    for i in range(0, len(n) - 1):
        distance = abs(n[i + 1] - n[i])
        t += int(distance / k)
        t += 1 if (distance % k) != 0 else 0
        # print(f"Time taken: {t}")
    return t


if __name__ == "__main__":
    speed = int(input())
    buildings = int(input())
    heights = [eval(i) for i in input().split()]
    heights.insert(0, 0)
    heights.append(0)

    time = buildings
    time += calculate_time(speed, heights)

    print(time)
