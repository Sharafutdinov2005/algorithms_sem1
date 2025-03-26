class Queue:
    elements_in_append_order: list
    elements_in_pop_order: list

    def __init__(self):
        self.elements_in_append_order = []
        self.elements_in_pop_order = []

    def front(self):
        if not self.elements_in_pop_order:
            self._update()
        return self.elements_in_pop_order[-1]

    def pop(self):
        if len(self.elements_in_pop_order) <= 1:
            self._update()
        return self.elements_in_pop_order.pop()

    def append(self, element):
        self.elements_in_append_order.append(element)

    def _update(self):
        if not self.elements_in_append_order:
            raise IndexError("queue is empty")

        self.elements_in_pop_order = []

        while self.elements_in_append_order:
            self.elements_in_pop_order.append(
                self.elements_in_append_order.pop()
            )
