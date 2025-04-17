class Date:
    day: int
    month: int
    year: int

    def __init__(
        self,
        day: int,
        month: int,
        year: int
    ) -> None:
        self.day = day
        self.month = month
        self.year = year

    def __lt__(
        self,
        other: 'Date'
    ) -> bool:
        return (
            self.year, self.month, self.day
        ) < (
            other.year, other.month, other.day
        )

    def __eq__(self, other: 'Date') -> bool:
        return (
            self.year == other.year and
            self.month == other.month and
            self.day == other.day
        )

    def __le__(self, other: 'Date') -> bool:
        return self < other or self == other


class Lifetime:
    birthday: Date
    death_date: Date

    def __init__(
        self,
        birthday: Date,
        death_date: Date
    ) -> None:
        self.birthday = birthday
        self.death_date = death_date

    def __lt__(
        self,
        other: 'Lifetime'
    ) -> bool:
        return self.birthday < other.birthday


def solve(lifetimes):
    events = []

    for life in lifetimes:
        birth = life.birthday
        death = life.death_date

        start_active = Date(birth.day, birth.month, birth.year + 18)

        end_active_80 = Date(birth.day, birth.month, birth.year + 80)
        end_active = death if death < end_active_80 else end_active_80

        if start_active < end_active:
            events.append((start_active, 1))
            events.append((end_active, -1))

    events.sort(key=lambda x: (x[0], x[1]))

    max_contemporaries = 0
    current_contemporaries = 0

    for event in events:
        current_contemporaries += event[1]
        if current_contemporaries > max_contemporaries:
            max_contemporaries = current_contemporaries

    return max_contemporaries


n = int(input())
lifes = []

for _ in range(n):
    numbers = list(map(int, input().split()))
    birthday = Date(*numbers[:3])
    death_date = Date(*numbers[3:])
    lifetime = Lifetime(birthday, death_date)
    lifes.append(lifetime)

print(solve(lifes))
