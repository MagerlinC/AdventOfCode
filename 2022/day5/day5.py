
stacks = [
    ["F", "H", "B", "V", "R", "Q", "D", "P"],
    ["L", "D", "Z", "Q", "W", "V"],
    ["H", "L", "Z", "Q", "G", "R", "P", "C"],
    ["R", "D", "H", "F", "J", "V", "B"],
    ["Z", "W", "L", "C"],
    ["J", "R", "P", "N", "T", "G", "V", "M"],
    ["J", "R", "L", "V", "M", "B", "S"],
    ["D", "P", "J"],
    ["D", "C", "N", "W", "V"]
]


def main():
    with open("input.txt") as file:
        for line in file:
           clean_line = line.replace("move ", "").replace("from ", "").replace("to ", "")
           parts = clean_line.split(" ")
           num_crates_to_move = int(parts[0])
           from_stack_index = int(parts[1]) - 1
           to_stack_index = int(parts[2]) - 1
           from_stack = stacks[from_stack_index]
           to_stack = stacks[to_stack_index]
           for i in range(num_crates_to_move):
                moved_elem = from_stack.pop()
                to_stack.append(moved_elem)
    result = ""
    for stack in stacks:
        result += str(stack[len(stack) - 1])
    print(result)

if __name__ == "__main__":
    main()