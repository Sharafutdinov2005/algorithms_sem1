class str_container:
    value: str

    def __init__(
        self,
        value: str,
    ) -> None:
        self.value = value

    def __lt__(
        self,
        other: 'str_container'
    ) -> bool:
        for i in range(
            min(len(self.value), len(other.value))
        ):
            if self.value[i] == other.value[i]:
                continue
            return self.value[i] < other.value[i]
        return len(self.value) < len(other.value)

    def __str__(self):
        return self.value


n = int(input())
a = [str_container(input()) for _ in range(n)]
a.sort()

print(*a, sep="\n")
