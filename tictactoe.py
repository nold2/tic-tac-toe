# write your code here

horizontal_border = "---------"
vertical_border = "|"


def formatter_matrix(matrix):
    """Convert 3x3 matrix into String format for printing"""
    lines = list(range(3))

    def get_char(v):
        """Available Characters to print are X, O and _"""
        return v if v else "_"

    for index, val in enumerate(matrix):
        lines[index] = \
            f"{vertical_border} {get_char(val[0])} {get_char(val[1])} {get_char(val[2])} {vertical_border}"

    return "\n".join(lines)


def is_complete(move):
    """Closure that checks if a `move` within a list is complete """
    def execute(array):
        return all([val if val == move else None for val in array])

    return execute


def is_occupied(array):
    """Check if all the values within the list is occupied"""
    return all(array)


def show(board):
    """Print the board"""
    print(f"{horizontal_border}\n{formatter_matrix(board)}\n{horizontal_border}")


def regroup(board):
    """group the board into a list of list based TTC's winning condition"""
    first_row = board[0]
    second_row = board[1]
    third_row = board[2]

    first_column = [board[0][0], board[1][0], board[2][0]]
    second_column = [board[0][1], board[1][1], board[2][1]]
    third_column = [board[0][1], board[1][1], board[2][1]]

    left_diagonal = [board[0][0], board[1][1], board[2][2]]
    right_diagonal = [board[0][2], board[1][1], board[2][0]]

    return [first_row, second_row, third_row, first_column, second_column, third_column, left_diagonal, right_diagonal]


def win_condition(lists, condition):
    """Check if a win condition has been full-filled"""
    return any(
        [condition(val) for val in lists]
    )


def draw_condition(lists, condition):
    """Check if a draw condition has been full-filled"""
    return all(
        [condition(val) for val in lists]
    )


def main():
    # Initial board state
    board = [[None] * 3, [None] * 3, [None] * 3]

    show(board)

    # X is a first mover
    is_x_turn = True

    while True:
        try:
            # Ask for coordinate, and can throw ValueError
            coordinate_x, coordinate_y = [int(val) for val in input("Enter coordinates: ").split()]

            # Validate coordinate
            coordinate_map = {
                (1, 1): (2, 0),
                (1, 2): (1, 0),
                (1, 3): (0, 0),

                (2, 1): (2, 1),
                (2, 2): (1, 1),
                (2, 3): (0, 1),

                (3, 1): (2, 2),
                (3, 2): (1, 2),
                (3, 3): (0, 2),
            }

            # Validation that can throw KeyError
            x, y = coordinate_map[(coordinate_x, coordinate_y)]

            # occupied check
            if board[x][y]:
                print("This cell is occupied! Choose another one!")
                continue

            # assign coordinate to board
            move = board[x][y] = "X" if is_x_turn else "O"

            # print the current board
            show(board)

            # analyze current board status
            lists = regroup(board)

            if win_condition(lists, is_complete(move)):
                """If a move wins, stop the game"""
                print(f"{move} wins")
                break

            elif draw_condition(lists, is_occupied):
                """If draw appears, stop the game"""
                print("Draw")
                break
            else:
                """Else get ready for the next move"""
                is_x_turn = not is_x_turn
                continue

        except ValueError:
            print("You should enter numbers!")
            continue
        except KeyError:
            print("Coordinates should be from 1 to 3!")
            continue
        except EOFError:
            break


main()
