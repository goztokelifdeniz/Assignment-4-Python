import sys

def see_list(game_list):
    print(game_list)
    a = [indices[1] for indices in game_list]
    print(a)

def make_constraints_list():
    with open(sys.argv[1], "r") as input_as_a_file:
        input_string = input_as_a_file.read()
        cons_list = input_string.split("\n")[0:4]
        for lines in range(len(cons_list)):
            cons_list[lines] = cons_list[lines].split(" ")
        for lines in range(len(cons_list)):
            for nums in range(len(cons_list[lines])):
                cons_list[lines][nums] = int(cons_list[lines][nums])
        #print("\nconstraints list: ")
        #print(cons_list)
    return cons_list

def make_template_list():
    with open(sys.argv[1], "r") as input_as_a_file:
        input_string = input_as_a_file.read()

        # print("\n file as head string:\n\n" + input_string)
        temporary_list = input_string.split("\n")[4:]

        # print("\nlist 2: ")
        # print(temporary_list)

        temp_list = [[chars, ""] for lines in temporary_list for chars in lines if chars != " "]

        # print("\n temp_list: ")
        # print(temp_list)
    return temp_list

def find_row_amount_of_template():
    with open(sys.argv[1], "r") as input_as_a_file:
        input_string = input_as_a_file.read()
        row_amount = input_string.count("\n") - 3
        # print("\n row_amount: " + str(row_amount))
    return row_amount

def find_column_amount_of_template():
    column_amount = len(make_template_list()) // find_row_amount_of_template()
    # print("\n column_amount: " + str(column_amount))
    return column_amount

def it_fits_the_constraints(last_list, row_num, col_num, list_of_const):
    print("\n\ncheck if it fits!")
    highs_in_rows_list = []
    bases_in_rows_list = []
    highs_in_columns_list = []
    bases_in_columns_list = []

    for outer_index in range(0, row_num * col_num, col_num):
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
        for inner_index in range(0, row_num * col_num, col_num):
            if last_list[outer_index + inner_index][1] == "H":
                number_of_highs += 1
            if last_list[outer_index + inner_index][1] == "B":
                number_of_bases += 1
        highs_in_columns_list.append(number_of_highs)
        bases_in_columns_list.append(number_of_bases)

    current_template_const = [highs_in_rows_list, bases_in_rows_list, highs_in_columns_list, bases_in_columns_list]
    #print("current template const list: ")
    #print(current_template_const)

    if list_of_const == current_template_const:
        print("it fits\n")
        return True
    print("it doesn't fit\n")
    return False

def game_play(game_list, index, h_b_n_list):

    """
def game_play(h_b_n_list, index, game_list):

    if it_fits == True:   ----------------------------------
        return game_list  ----------------------------------
    else:
        if len(h_b_n_list) > 0: ----------------------------------

            game_list[index][1] = h_b_n_list[0] ----------------------------------
            h_b_n_list.pop(0) ----------------------------------

            h_b_n_list = ["H", "B", "N"] ----------------------------------

            return game_play(h_b_n_list, (index + 1), game_list) ----------------------------------

        else:
            if index >= 1:
                return game_play(h_b_n_list, (index - 1), game_list) ----------------------------------
            else:
                return "No solution!"
    """

    print("\nback in game play with this list:")
    #see_list(game_list)
    print(game_list)
    print(f"current index: {index} ")
    print(f"game_list[index]: {game_list[index]}")
    print("\n")

    row_num = find_row_amount_of_template()
    col_num = find_column_amount_of_template()
    list_of_constraints = make_constraints_list()

    is_the_list_fully_done = True

    print(game_list)
    for checking_index in range(len(game_list)):
        print(game_list[checking_index])
        print(game_list[checking_index][1])
        if game_list[checking_index][1] == "":
            is_the_list_fully_done = False
            break
    print(is_the_list_fully_done)

    if is_the_list_fully_done:
        if it_fits_the_constraints(game_list, row_num, col_num, list_of_constraints):
            return game_list
    else:
        print("\nthe list under this line didn't fit")
        #see_list(game_list)

        if game_list[index][0] == "L" or game_list[index][0] == "U":

            # komşular yüzünden olmayacak ihtimalleri çıkar
            if index % col_num != 0:
                if game_list[index - 1][1] in h_b_n_list and game_list[index - 1][1] != "N" and game_list[index][0] != "R":
                    h_b_n_list.remove(game_list[index - 1][1])
            if (index + 1) % col_num != 0:
                if game_list[index + 1][1] in h_b_n_list and game_list[index + 1][1] != "N" and game_list[index][0] != "L":
                    h_b_n_list.remove(game_list[index + 1][1])
            if not index < col_num:
                if game_list[index - col_num][1] in h_b_n_list and \
                        game_list[index - col_num][1] != "N" and game_list[index][0] != "D":
                    h_b_n_list.remove(game_list[index - col_num][1])
            if not index > (len(game_list) - col_num - 1):
                if game_list[index + col_num][1] in h_b_n_list and \
                        game_list[index + col_num][1] != "N" and game_list[index][0] != "U":
                    h_b_n_list.remove(game_list[index + col_num][1])

            if len(h_b_n_list) > 0: # koyulabilecek seçenek var

                print(f"\n\nönce h_b_n_list[0]: {h_b_n_list[0]}")
                print(f"önce game_list[index][1]: {game_list[index][1]}")

                game_list[index][1] = h_b_n_list[0]

                print(f"\n\nsonra h_b_n_list[0]: {h_b_n_list[0]}")
                print(f"sonra game_list[index][1]: {game_list[index][1]}")

                if game_list[index][0] == "L":
                    if game_list[index][1] == "H":
                        game_list[index + 1][1] = "B"
                    elif game_list[index][1] == "B":
                        game_list[index + 1][1] = "H"
                    else:
                        game_list[index + 1][1] = "N"
                elif game_list[index][0] == "U":           # direkt "else:" şeklinde de yazılabilir sanki
                    if game_list[index][1] == "H":
                        game_list[index + col_num][1] = "B"
                    elif game_list[index][1] == "B":
                        game_list[index + col_num][1] = "H"
                    else:
                        game_list[index + col_num][1] = "N"


                print("we changed whats inside game_list[index][1]")
                #see_list(game_list)

                h_b_n_list = ["H", "B", "N"]

                return game_play(game_list, (index+1), h_b_n_list)

            else: # koyulabilecek seçenek yok

                if index >= 1: # daha geride bir index var

                    game_list[index][1] = h_b_n_list[0]

                    if game_list[index][0] == "L":
                        if game_list[index][1] == "H":
                            game_list[index + 1][1] = "B"
                        elif game_list[index][1] == "B":
                            game_list[index + 1][1] = "H"
                        else:
                            game_list[index + 1][1] = "N"
                    elif game_list[index][0] == "U":
                        if game_list[index][1] == "H":
                            game_list[index + col_num][1] = "B"
                        elif game_list[index][1] == "B":
                            game_list[index + col_num][1] = "H"
                        else:
                            game_list[index + col_num][1] = "N"

                    h_b_n_list.pop(0)

                    print("the list didn't fit and we ")
                    #see_list(game_list)

                    return game_play(h_b_n_list, (index - 1), game_list)

                else: # daha geride bir index yok
                    return "No solution!"
        else:
            return game_play(h_b_n_list, (index + 1), game_list)


def printing_the_end_game_to_output_file(end_game_template, col_num):
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
    printing_the_end_game_to_output_file(game_play(make_template_list(), 0, ["H", "B", "N"]), find_column_amount_of_template())


if __name__ == "__main__":

    main()




