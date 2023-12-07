class ElfAssignment:
    assignment_start: int
    assignment_end: int
    def __init__(self, assignment_string: str) -> None:
        parts = assignment_string.split("-")
        self.assignment_start = int(parts[0])
        self.assignment_end = int(parts[1])


def assignments_fully_contain(elfA: ElfAssignment, elfB: ElfAssignment) -> bool:
    a_contains_b = elfA.assignment_start <= elfB.assignment_start and elfA.assignment_end >= elfB.assignment_end
    b_contains_a = elfB.assignment_start <= elfA.assignment_start and elfB.assignment_end >= elfA.assignment_end
    return a_contains_b or b_contains_a

def assignments_overlap(elfA: ElfAssignment, elfB: ElfAssignment) -> bool:
    a_overlaps_b = elfA.assignment_start <= elfB.assignment_start and elfA.assignment_end >= elfB.assignment_start
    b_overlaps_a = elfB.assignment_start <= elfA.assignment_start and elfB.assignment_end >= elfA.assignment_start
    return a_overlaps_b or b_overlaps_a


def main():
    with open("input.txt") as file:
        num_containing_pairs = 0
        for line in file:
            assignments = line.replace("\n", "").split(",")
            assignment_a = ElfAssignment(assignments[0])
            assignment_b = ElfAssignment(assignments[1])
            if assignments_overlap(assignment_a, assignment_b):
                num_containing_pairs += 1
        print(num_containing_pairs)            

if __name__ == "__main__":
    main()