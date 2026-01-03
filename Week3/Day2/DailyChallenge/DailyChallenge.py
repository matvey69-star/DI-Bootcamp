#Daily Challenge : Pagination
import math


class Pagination:
    def __init__(self, items=None, page_size=10):
        if items is None:
            items = []
        if not isinstance(items, list):
            raise TypeError("items must be a list (or None).")
        if not isinstance(page_size, int) or page_size <= 0:
            raise ValueError("page_size must be a positive integer.")

        self.items = items
        self.page_size = page_size
        self.current_idx = 0  # internal page index (0-based)
        self.total_pages = math.ceil(len(self.items) / self.page_size) if self.items else 1

    def get_visible_items(self):
        start = self.current_idx * self.page_size
        end = start + self.page_size
        return self.items[start:end]

    def go_to_page(self, page_num):
        # user gives 1-based page numbers
        if not isinstance(page_num, int):
            raise TypeError("page_num must be an integer.")
        if page_num < 1 or page_num > self.total_pages:
            raise ValueError(f"page_num must be between 1 and {self.total_pages}.")

        self.current_idx = page_num - 1
        return self  # for chaining

    def first_page(self):
        self.current_idx = 0
        return self

    def last_page(self):
        self.current_idx = self.total_pages - 1
        return self

    def next_page(self):
        if self.current_idx < self.total_pages - 1:
            self.current_idx += 1
        return self

    def previous_page(self):
        if self.current_idx > 0:
            self.current_idx -= 1
        return self

    def __str__(self):
        return "\n".join(str(x) for x in self.get_visible_items())


# ------------------ TESTS ------------------

alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

print(p.get_visible_items())
# ['a', 'b', 'c', 'd']

p.next_page()
print(p.get_visible_items())
# ['e', 'f', 'g', 'h']

p.last_page()
print(p.get_visible_items())
# ['y', 'z']

try:
    p.go_to_page(10)
    print(p.current_idx + 1)
except ValueError as e:
    print("ValueError:", e)

try:
    p.go_to_page(0)
except ValueError as e:
    print("ValueError:", e)

# Bonus chaining example:
print(p.first_page().next_page().next_page().next_page().get_visible_items())
# ['m', 'n', 'o', 'p']