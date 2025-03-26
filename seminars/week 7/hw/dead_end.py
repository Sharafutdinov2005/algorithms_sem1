class Train:
    arrival: int
    departure: int

    def __init__(self, arrival: int, departure: int):
        self.arrival = arrival
        self.departure = departure

    def __repr__(self):
        return f"Train(arrival={self.arrival}, departure={self.departure})"


def sift_down(
    dead_ends: list[Train],
    i: int,
) -> None:
    while True:
        child1 = 2 * i + 1
        child2 = 2 * i + 2

        # no child
        if child1 >= len(dead_ends):
            break

        # single child

        # if child is greater than parent
        if child2 >= len(dead_ends):
            if dead_ends[child1].departure < dead_ends[i].departure:
                dead_ends[child1], dead_ends[i] = (
                    dead_ends[i],
                    dead_ends[child1]
                )
            break

        # two children

        # if child1 is greater than parent
        if (
            dead_ends[child1].departure < dead_ends[child2].departure and
            dead_ends[child1].departure < dead_ends[i].departure
        ):
            dead_ends[child1], dead_ends[i] = dead_ends[i], dead_ends[child1]
            i = child1

        # if child2 is greater than parent
        elif dead_ends[child2].departure < dead_ends[i].departure:
            dead_ends[child2], dead_ends[i] = dead_ends[i], dead_ends[child2]
            i = child2

        # no child is greater than parent
        else:
            break


def sift_up(
    dead_ends: list[Train],
    i: int,
) -> None:
    while i > 0:
        parent = (i - 1) // 2
        if dead_ends[parent].departure <= dead_ends[i].departure:
            break
        dead_ends[parent], dead_ends[i] = dead_ends[i], dead_ends[parent]
        i = parent


def insert(
    dead_ends: list[Train],
    train: Train,
) -> None:
    dead_ends.append(train)
    sift_up(dead_ends, len(dead_ends) - 1)


def delete_max_departure(
    dead_ends: list[Train],
) -> None:
    end = dead_ends.pop()

    if len(dead_ends) == 0:
        return

    dead_ends[0] = end
    sift_down(dead_ends, 0)


def check_DE(
    trains: list[Train],
    DE: int
) -> bool:
    # trains are sorted by arrival time

    dead_ends = []

    for train in trains:
        while dead_ends and dead_ends[0].departure < train.arrival:
            delete_max_departure(dead_ends)

        insert(dead_ends, train)

        if len(dead_ends) > DE:
            return False

    return True


def count_min_DE_amount(
    trains: list[Train]
) -> int:
    left = 0
    right = len(trains)
    while left < right - 1:
        mid = (left + right) // 2
        if check_DE(trains, mid):
            right = mid
        else:
            left = mid + 1

    return left if check_DE(trains, left) else right


n = int(input())
trains = [Train(*map(int, input().split())) for _ in range(n)]

print(count_min_DE_amount(trains))
