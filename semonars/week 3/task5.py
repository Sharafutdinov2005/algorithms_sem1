class Building:
    plan: list[list[int]]

    def __init__(self, some_plan):
        self.plan = some_plan

    @property
    def high(self):
        return len(self.plan)

    def is_in_floor(self, room, floor):
        return (
            self._plan[floor][0] < room < self._plan[floor][-1]
        )

    def find_floor(self, room):
        f = self.high
        s = 0

        if room < 0 or room > self._plan[-1][-1]:
            return None

        while s < f:
            m = (s + f) // 2
            if self.is_in_floor(room, m):
                return m
            if self._plan[m][0] > room:
                f = m
            else:
                s = m



