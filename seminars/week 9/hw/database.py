from typing import Tuple, List


class _DatabaseLine:
    name: str
    elements: List[int]

    def __init__(
        self,
        name: str,
        elements: List[int]
    ) -> None:
        self.name = name
        self.elements = elements

    def __gt__(
        self,
        other: '_DatabaseLine'
    ) -> bool:
        return self.elements > other.elements

    def __str__(
        self,
    ) -> str:
        return self.name


class Database:
    lines: List[_DatabaseLine] = []
    column_priorities: List[int]

    def load_database(
        self,
    ) -> dict:
        """
        This functions loads the database from a console.
        """
        n = int(input())  # number of lines
        _ = int(input())

        # dictionary to store the priorities of each column
        self.column_priorities = list(map(int, input().split()))

        for _ in range(n):
            line, elements = self._load_line()
            self.lines.append(
                _DatabaseLine(
                    name=line,
                    elements=elements
                )
            )

        self.lines.sort(reverse=True)

    def _load_line(
        self,
    ) -> Tuple[str, list[int]]:
        line = input().split()
        class_members = [int(line[i]) for i in self.column_priorities]
        return line[0], class_members

    def __str__(
        self
    ) -> str:
        lables = [str(line) for line in self.lines]
        return '\n'.join(lables)


data = Database()
data.load_database()
print(data)
