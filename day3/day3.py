import string

letter_values = dict()
letters = string.ascii_lowercase + string.ascii_uppercase
for index, letter in enumerate(letters):
    letter_values[letter] = index + 1


def get_common_element(bagA: list[str], bagB: list[str]) -> str:
    bagA.sort()
    bagB.sort()

    bagAPointer: int = 0
    bagBPointer: int = 0

    while(bagAPointer < len(bagA) and bagBPointer < len(bagB)):
        itemA = bagA[bagAPointer]
        itemB = bagB[bagBPointer]
        if itemA == itemB:
            # Match!
            return itemA
        elif itemA < itemB:
            # Go next
            bagAPointer+= 1
        elif itemB < itemA:
            # Look ahead in B
            bagBPointer+= 1

def get_badge_for_group(group: list[str]) -> str:
    bagA = group[0]
    bagB = group[1]
    bagC = group[2]
    common_elements = get_common_element(bagA, bagB)

    return ""


def main_2():
    with open("input.txt") as file:
        badges_found: list[str] = []
        cur_group: list[str] = []
        for line, index in file:
            if(index % 3 == 0):
                group_badge = get_badge_for_group(cur_group)
                badges_found.append(group_badge)
                cur_group = []
            cur_group.append(line)
            

def main():
    with open("input.txt") as file:
        common_elements: list[str] = []
        for line in file:
            mid_point = int(len(line) / 2)
            compartmentA: list[str] = [*line[0 : mid_point]]
            compartmentB: list[str] = [*line[mid_point: len(line) - 1]]
            common_elements.appen(get_common_element(compartmentA, compartmentB))
            
        print(sum(list(map(lambda element: letter_values[element], common_elements))))


if __name__ == "__main__":
    main_2()