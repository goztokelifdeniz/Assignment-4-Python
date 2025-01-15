import sys
import copy

def make_constraints_list():
    print("i am in make_constraints_list!")
    with open(sys.argv[1], "r") as input_as_a_file:
        input_string =  input_as_a_file.read()
        cons_list = input_string.split("\n")[0:4]
        for lines in range(len(cons_list)):
            cons_list[lines] = cons_list[lines].split(" ")
        for lines in range(len(cons_list)):
            for nums in range(len(cons_list[lines])):
                cons_list[lines][nums] = int(cons_list[lines][nums])
        print("\nconstraints list: ")
        print(cons_list)
    return cons_list

def make_template_list():
    print("i am in make_template_list!")
    with open(sys.argv[1], "r") as input_as_a_file:
        input_string = input_as_a_file.read()

        #print("\n file as head string:\n\n" + input_string)
        temporary_list = input_string.split("\n")[4:]

        #print("\nlist 2: ")
        #print(temporary_list)

        temp_list = [[chars, ""] for lines in temporary_list for chars in lines if chars != " "]

        #print("\n temp_list: ")
        #print(temp_list)

    return temp_list

def find_row_amount_of_template():
    print("i am in find_row_amount_of_template!")
    with open(sys.argv[1], "r") as input_as_a_file:
        input_string = input_as_a_file.read()
        row_amount = input_string.count("\n") - 3
        #print("\n row_amount: " + str(row_amount))
    return row_amount

def find_column_amount_of_template():
    print("i am in find_column_amount_of_template!")
    column_amount = len(make_template_list()) // find_row_amount_of_template()
    #print("\n column_amount: " + str(column_amount))
    return column_amount

def place_a_tile(last_list, cell_index, h_b_n_list, col_num):
    print("i am in place_chars!")
    # before_the_last_placement_list = copy.deepcopy(game_list)
    #if game_list[index][0] != ("R" or "D"): # and game_list[index][1] == ""
    if cell_index % col_num != 0:
        if last_list[cell_index - 1][1] in h_b_n_list and last_list[cell_index - 1][1] != "N":
            h_b_n_list.remove(last_list[cell_index - 1][1])
    if (cell_index + 1) % col_num != 0:
        if last_list[cell_index + 1][1] in h_b_n_list and last_list[cell_index + 1][1] != "N":
            h_b_n_list.remove(last_list[cell_index + 1][1])
    if not cell_index < col_num:
        if last_list[cell_index - col_num][1] in h_b_n_list and last_list[cell_index - col_num][1] != "N":
            h_b_n_list.remove(last_list[cell_index - col_num][1])
    if not cell_index > (len(last_list) - col_num - 1):
        if last_list[cell_index + col_num][1] in h_b_n_list and last_list[cell_index + col_num][1] != "N":
            h_b_n_list.remove(last_list[cell_index + col_num][1])

    print(f"here are the possibilities for {cell_index}:")
    print(h_b_n_list)

    last_list[cell_index][1] = h_b_n_list[0]
    last_placed_char = h_b_n_list[0]
    h_b_n_list = ["H", "B", "N"]
    if last_list[cell_index][0] == "L":
        if last_list[cell_index][1] == "H":
            last_list[cell_index + 1][1] = "B"
        elif last_list[cell_index][1] == "B":
            last_list[cell_index + 1][1] = "H"
        else:
            last_list[cell_index + 1][1] = "N"
    else:  # eski hali: elif game_list[index][0] == "U":
        if last_list[cell_index][1] == "H":
            last_list[cell_index + col_num][1] = "B"
        elif last_list[cell_index][1] == "B":
            last_list[cell_index + col_num][1] = "H"
        else:  # elif game_list[index][1] == "N":
            last_list[cell_index + col_num][1] = "N"

    see_list = [indices[1] for indices in last_list]
    print(see_list)
    return last_list, last_placed_char
    #else:
    #    return game_list, ""

def check_if_the_placed_template_fits_the_constraints(last_list, row_num, col_num, list_of_const):
    print("i am in check_if_the_placed_template_fits_the_constraints!")
    highs_in_rows_list = []
    bases_in_rows_list = []
    highs_in_columns_list = []
    bases_in_columns_list = []

    for outer_index in range(0, row_num*col_num , col_num):
        number_of_highs = 0
        number_of_bases = 0
        for inner_index in range(col_num):
            if last_list[outer_index + inner_index][1] == "H":
                number_of_highs += 1
            if last_list[outer_index + inner_index][1] == "B":
                number_of_bases += 1
        highs_in_rows_list.append(number_of_highs)
        bases_in_rows_list.append(number_of_bases)

    for outer_index in range(col_num):
        number_of_highs = 0
        number_of_bases = 0
        for inner_index in range(0, row_num*col_num , col_num):
            if last_list[outer_index + inner_index][1] == "H":
                number_of_highs += 1
            if last_list[outer_index + inner_index][1] == "B":
                number_of_bases += 1
        highs_in_columns_list.append(number_of_highs)
        bases_in_columns_list.append(number_of_bases)

    current_template_const = [highs_in_rows_list, bases_in_rows_list, highs_in_columns_list, bases_in_columns_list]
    print("\ncurrent template const list: ")
    print(current_template_const)

    if list_of_const == current_template_const:
        return True
    return False

def try_sth_different_for_the_last_grid_and_the_rest_of_it(before_the_last_list, last_placed_char, col_num):
    see_list = [indices[1] for indices in before_the_last_list]
    where_we_left = see_list.index("")

    h_b_n_list = ["H", "B", "N"]
    for cell_index in range(where_we_left, len(before_the_last_list)):
        h_b_n_list = ["H", "B", "N"]
        if cell_index == where_we_left:
            h_b_n_list.remove(last_placed_char)
            before_the_last_list, last_placed_char = place_a_tile(before_the_last_list, cell_index, h_b_n_list, col_num)
        else:
            before_the_last_list, last_placed_char = place_a_tile(before_the_last_list, cell_index, h_b_n_list, col_num)
    h_b_n_list = ["H", "B", "N"]
    return blind_valley_game(before_the_last_list, h_b_n_list)

def blind_valley_game(game_list, h_b_n_list):
    print("i am in blind_valley_game!")
    before_the_last_list = []
    last_placed_char = ""

    row_num = find_row_amount_of_template()
    col_num = find_column_amount_of_template()
    list_of_const = make_constraints_list()

    #h_b_n_list = ["H", "B", "N"]
    for cell_index in range(len(game_list)):
        h_b_n_list = ["H", "B", "N"]
        if game_list[cell_index][1] == "":
            if cell_index == ((len(game_list) - 2) or (len(game_list) - col_num)):
                before_the_last_list = copy.deepcopy(game_list)
            game_list, last_placed_char = place_a_tile(game_list, cell_index, h_b_n_list, col_num)
            print("idk")

    print(f"last_list: {game_list}")
    print(f"before_the_last_list: {before_the_last_list}")
    print(f"last_placed_char: {last_placed_char}")

    if check_if_the_placed_template_fits_the_constraints(game_list, row_num, col_num, list_of_const):
        return game_list
    else:
        print(f"\n\nIT DOESN'T FIT THE CONSTRAINTS. WE'RE PLAYING THE GAME AGAIN \n{before_the_last_list}\n")
        return try_sth_different_for_the_last_grid_and_the_rest_of_it(before_the_last_list, last_placed_char, col_num)
        # blind_valley_game(before_the_last_list, h_b_n_list) vardı return de


#def printing_the_end_game_to_output_file(game_list, col_num):
#    with open(sys.argv[2], "w") as output_file:
#        for char_index in range(len(game_list)):
#            output_file.write(game_list[1])
#            if (char_index + 1) % col_num == 0 and char_index != (len(game_list) - 1):
#                output_file.write("\n")
#            else:
#                output_file.write(" ")


def main():
    input_file = open(sys.argv[1], "r")
    #output_file.write("bir şeyler")

    #make_constraints_list()
    #make_template_list()
    #find_row_amount_of_template()
    #find_column_amount_of_template()
    blind_valley_game(make_template_list(), ["H", "B", "N"])
    #printing_the_end_game_to_output_file(
        #blind_valley_game(make_template_list(), ["H", "B", "N"]), find_column_amount_of_template())

    input_file.close()
    #output_file.flush()
    #output_file.close()

# take input file
# make constraints list from input file [[H-R1,H-R2,H-R3],[B-R1,B-R2,B-R3],[H-C1,H-C2,H-C3,H-C4],[B-C1,B-C2,B-C3,B-C4]]
# make template list from input file
#
# main function to play the game(first empty place in template):
#
#
#
#
#

if __name__ == "__main__":
    main()