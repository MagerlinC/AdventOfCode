import string

letter_values = dict()
letters = string.ascii_lowercase + string.ascii_uppercase
for index, letter in enumerate(letters):
    letter_values[letter] = index + 1

def main():
    with open("input.txt") as file:
        common_elements: list[str] = []
        for line in file:
            mid_point = int(len(line) / 2)
            compartmentA: list[str] = [*line[0 : mid_point]]
            compartmentB: list[str] = [*line[mid_point: len(line) - 1]]
            
            compartmentA.sort()
            compartmentB.sort()

            compartmentAPointer: int = 0
            compartmentBPointer: int = 0

            while(compartmentAPointer < len(compartmentA) and compartmentBPointer < len(compartmentB)):
                itemA = compartmentA[compartmentAPointer]
                itemB = compartmentB[compartmentBPointer]
                if itemA == itemB:
                    # Match!
                    common_elements.append(itemA)
                    break
                elif itemA < itemB:
                    # Go next
                    compartmentAPointer+= 1
                elif itemB < itemA:
                    # Look ahead in B
                    compartmentBPointer+= 1
        print(sum(list(map(lambda element: letter_values[element], common_elements))))


if __name__ == "__main__":
    main()