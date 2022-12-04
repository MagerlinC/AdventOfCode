from enum import Enum

WIN_AMOUNT = 6
DRAW_AMOUNT = 3

class GameOutcome(Enum):
    LOSE = 0
    DRAW = 1
    WIN = 2

class Move(Enum):
    ROCK = 0
    PAPER = 1
    SCISSOR = 2

def parse_recorded_move(recorded_move: str):
    match recorded_move:
        case "A":
            return Move.ROCK
        case "X":
            return Move.ROCK
        case "B":
            return Move.PAPER
        case "Y":
            return Move.PAPER
        case "C":
            return Move.SCISSOR
        case "Z":
            return Move.SCISSOR

def parse_recorded_move_2(recorded_move: str):
    match recorded_move:
        case "A":
            return Move.ROCK
        case "B":
            return Move.PAPER
        case "C":
            return Move.SCISSOR
        case "X":
            return GameOutcome.LOSE
        case "Y":
            return GameOutcome.DRAW
        case "Z":
            return GameOutcome.WIN

def move_to_value(move: Move):
    match move:
        case Move.ROCK:
            return 1
        case Move.PAPER:
            return 2
        case Move.SCISSOR:
            return 3

def get_move_for_outcome(their_move: Move, desired_outcome: GameOutcome):
    match desired_outcome:
        case GameOutcome.DRAW:
            return their_move
        case GameOutcome.WIN:
            match their_move:
                case Move.ROCK:
                    return Move.PAPER
                case Move.PAPER:
                    return Move.SCISSOR
                case Move.SCISSOR:
                    return Move.ROCK
        case GameOutcome.LOSE:
            match their_move:
                case Move.ROCK:
                    return Move.SCISSOR
                case Move.PAPER:
                    return Move.ROCK
                case Move.SCISSOR:
                    return Move.PAPER
        
def get_value_of_round(their_move: Move, my_move: Move):
    result_amount = 0
    value_of_my_move = move_to_value(my_move)
    if (their_move == my_move):
        result_amount = DRAW_AMOUNT
    match their_move:
        case Move.ROCK:
            if(my_move == Move.PAPER):
                result_amount = WIN_AMOUNT
        case Move.PAPER:
            if(my_move == Move.SCISSOR):
                result_amount = WIN_AMOUNT
        case Move.SCISSOR:
            if(my_move == Move.ROCK):
                result_amount = WIN_AMOUNT
    return result_amount + value_of_my_move

def part_one():
    with open("input.txt") as file:
        total_score = 0
        for line in file:
            parts = line.replace("\n", "").split(" ")
            their_move = parse_recorded_move(parts[0])
            my_move = parse_recorded_move(parts[1])
            total_score += get_value_of_round(their_move, my_move)
        #print(total_score)

def part_two():
    with open("input.txt") as file:
        total_score = 0
        for line in file:
            parts = line.replace("\n", "").split(" ")
            their_move = parse_recorded_move_2(parts[0])
            desired_outcome = parse_recorded_move_2(parts[1])
            my_move = get_move_for_outcome(their_move, desired_outcome)
            total_score += get_value_of_round(their_move, my_move)
        print(total_score)


    
if __name__ == "__main__":
    part_two()