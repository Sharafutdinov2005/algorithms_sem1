class Solution:
    current: str = "."
    parent: str = ".."
    slash: str = "/"
    path: str

    def read_next_word(self, index: int) -> str:
        for i in range(index, len(self.path)):
            if self.path[i] == self.slash:
                return self.path[index:i]
        return self.path[index:]

    def skip_slash(self, index: int = 0) -> int:
        while index < len(self.path) and self.path[index] == self.slash:
            index += 1
        return index

    def generate_path(self, names: list[str]) -> str:
        result = ""
        while names:
            result += self.slash + names.pop(0)
        return result

    def simplifyPath(self, path: str) -> str:
        self.path = path
        index = self.skip_slash()
        names = []
        while index < len(path):
            name = self.read_next_word(index)
            print(name)
            if name == self.parent:
                if names:
                    names.pop()
            elif name != self.current:
                names.append(name)
            index += len(name) + 1
            index = self.skip_slash(index)

        return self.generate_path(names)


print(Solution().simplifyPath("/home/user/Documents/../Pictures"))