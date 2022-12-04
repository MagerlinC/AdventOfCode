
from functools import reduce

class Elf:
    items_held: list[int]
    def __init__(self, items: list[int]) -> None:
        self.items_held = items
    def __str__(self):
        return "Elf: " +  str(self.items_held)


def get_max_elf(elves: list[Elf]):
    return reduce(lambda acc, elf: max(acc, sum(elf.items_held)), elves, -1)

def get_top_n_elves(elves: list[Elf], num: int):
    sums = list(map(lambda elf: sum(elf.items_held), elves))
    sums.sort(reverse=True)
    return sum(sums[0:3])


def main():
    elves: list[Elf] = []
    with open("input.txt") as file:
        cur_elf_items: list[int] = []
        for line in file:
            if line == "\n":
                elves.append(Elf(cur_elf_items))
                cur_elf_items = []
            else:
                cur_elf_items.append(int(line))
    print(get_max_elf(elves))
    print(get_top_n_elves(elves, 3))

                

if __name__ == "__main__":
    main()