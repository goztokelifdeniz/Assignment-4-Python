import sys


def make_constraints_list():
    with open(sys.argv[1], "r") as input_as_a_file:
        input_string = input_as_a_file.read()
        list_of_constraints = input_string.split("\n")[0:4]
        for strings in range(len(list_of_constraints)):
            list_of_constraints[strings] = list_of_constraints[strings].split(" ")
        for strings in range(len(list_of_constraints)):
            for nums in range(len(list_of_constraints[strings])):
                list_of_constraints[strings][nums] = int(list_of_constraints[strings][nums])
    return list_of_constraints


def make_template_list():
    with open(sys.argv[1], "r") as input_as_a_file:
        input_string = input_as_a_file.read()
        temporary_list = input_string.split("\n")[4:]
        template_list = [[chars, ""] for lines in temporary_list for chars in lines if chars != " "]
    return template_list


def find_row_amount_of_template():
    with open(sys.argv[1], "r") as input_as_a_file:
        input_string = input_as_a_file.read()
        row_amount = input_string.count("\n") - 3
    return row_amount


def find_column_amount_of_template():
    column_amount = len(make_template_list()) // find_row_amount_of_template()
    return column_amount


def it_fits_the_constraints(game_list, row_num, col_num, list_of_const):
    highs_in_rows_list = []
    bases_in_rows_list = []
    highs_in_columns_list = []
    bases_in_columns_list = []

    for outer_index in range(0, row_num * col_num, col_num):
        number_of_highs = 0
        number_of_bases = 0
        for inner_index in range(col_num):
            if game_list[outer_index + inner_index][1] == "H":
                number_of_highs += 1
            if game_list[outer_index + inner_index][1] == "B":
                number_of_bases += 1
        highs_in_rows_list.append(number_of_highs)
        bases_in_rows_list.append(number_of_bases)

    for outer_index in range(col_num):
        number_of_highs = 0
        number_of_bases = 0
        for inner_index in range(0, row_num * col_num, col_num):
            if game_list[outer_index + inner_index][1] == "H":
                number_of_highs += 1
            if game_list[outer_index + inner_index][1] == "B":
                number_of_bases += 1
        highs_in_columns_list.append(number_of_highs)
        bases_in_columns_list.append(number_of_bases)

    current_template_const = [highs_in_rows_list, bases_in_rows_list, highs_in_columns_list, bases_in_columns_list]

    for sub_lists in range(len(list_of_const)):
        for const in range(len(list_of_const[sub_lists])):
            if (list_of_const[sub_lists][const] != (-1)
                    and list_of_const[sub_lists][const] != current_template_const[sub_lists][const]):
                return False
    return True


def find_the_next_index(game_list, index):
    index = index + 1
    while not (game_list[index][0] == "L" or game_list[index][0] == "U"):
        index = index + 1
    return index


def find_the_former_index(game_list, index):
    index = index - 1
    while not (game_list[index][0] == "L" or game_list[index][0] == "U"):
        index = index - 1
    return index


def fill_the_cell(game_list, index, tile_options_list, col_num):
    # If the given cell has upper or left neighbors, I am eliminating the tile options neighbors constrain
    if index % col_num != 0 and game_list[index - 1][1] in tile_options_list and game_list[index - 1][1] != "N":
        tile_options_list.remove(game_list[index - 1][1])
    if index >= col_num and game_list[index - col_num][1] in tile_options_list and game_list[index - col_num][1] != "N":
        tile_options_list.remove(game_list[index - col_num][1])

    # Placing the first option
    game_list[index][1] = tile_options_list[0]
    if game_list[index][0] == "L":
        if game_list[index][1] == "H":
            game_list[index + 1][1] = "B"
        elif game_list[index][1] == "B":
            game_list[index + 1][1] = "H"
        else:
            game_list[index + 1][1] = "N"
    if game_list[index][0] == "U":
        if game_list[index][1] == "H":
            game_list[index + col_num][1] = "B"
        elif game_list[index][1] == "B":
            game_list[index + col_num][1] = "H"
        else:
            game_list[index + col_num][1] = "N"

    # If the tile is not the last tile, I am removing the further tiles
    # So that I can look for options without any mistake
    if index < (len(game_list) - 2):
        to_start_deleting_index = index + 1
        while not (game_list[index][0] == "L" or game_list[index][0] == "U"):
            to_start_deleting_index = to_start_deleting_index + 1

        for deleting_index in range(to_start_deleting_index, len(game_list)):
            if game_list[deleting_index][0] == "L":
                game_list[deleting_index][1] = ""
                game_list[deleting_index + 1][1] = ""
            elif game_list[deleting_index][0] == "U":
                game_list[deleting_index][1] = ""
                game_list[deleting_index + col_num][1] = ""
    return game_list


def play_game(game_list, index, tile_options_list):

    row_num = find_row_amount_of_template()
    col_num = find_column_amount_of_template()
    list_of_constraints = make_constraints_list()

    if game_list[index][1] == "N":  # If the tile inside is the Neutral tile
        if index == 0:
            return "No solution!"
        else:
            index = find_the_former_index(game_list, index)
            tile_options_list = ["H", "B", "N"]
            if game_list[index][1] == "B":
                tile_options_list.remove("H")
            if game_list[index][1] != "N":
                tile_options_list.remove(game_list[index][1])
            return play_game(game_list, index, tile_options_list)

    else:  # The tile placed is not the Neutral tile, which means there exists at least 1 other option for that tile
        fill_the_cell(game_list, index, tile_options_list, col_num)
        if index == (len(game_list) - 2):  # The tile I just placed is the last tile of the template
            if it_fits_the_constraints(game_list, row_num, col_num, list_of_constraints):
                return game_list
            else:
                if game_list[index][1] == "N":
                    return play_game(game_list, index, tile_options_list)
                else:
                    tile_options_list = ["H", "B", "N"]
                    if game_list[index][1] == "B":
                        tile_options_list.remove("H")
                    if game_list[index][1] != "N":
                        tile_options_list.remove(game_list[index][1])
                    return play_game(game_list, index, tile_options_list)
        else:  # The tile last placed is not the last tile of the template, there are other tiles to put
            index = find_the_next_index(game_list, index)
            tile_options_list = ["H", "B", "N"]
            return play_game(game_list, index, tile_options_list)


def print_the_output_to_output_file(end_game_template, col_num):
    with open(sys.argv[2], "w") as output_file:
        if end_game_template == "No solution!":
            output_file.write(end_game_template)
        else:
            for char_index in range(len(end_game_template)):
                output_file.write(end_game_template[char_index][1])
                if (char_index + 1) % col_num == 0 and char_index != (len(end_game_template) - 1):
                    output_file.write("\n")
                else:
                    output_file.write(" ")


def main():
    print_the_output_to_output_file(play_game(make_template_list(), 0, ["H", "B", "N"]),
                                    find_column_amount_of_template())


if __name__ == "__main__":
    main()
