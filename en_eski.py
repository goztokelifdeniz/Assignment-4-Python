import sys

def see_list(game_list):
    a = [indices[1] for indices in game_list]
    print(a)
    return

def make_constraints_list():
    with open(sys.argv[1], "r") as input_as_a_file:
        input_string = input_as_a_file.read()
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
    print("i am in check_if_the_placed_template_fits_the_constraints!")
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
    print("current template const list: ")
    print(current_template_const)

    if list_of_const == current_template_const:
        print("true\n")
        return True
    print("false\n")
    return False

def fill_cells(game_list, last_tile_first_index, h_b_n_list, col_num):
    for cell_index in range(last_tile_first_index, len(game_list)):
        if game_list[cell_index][1] == "":
            if cell_index % col_num != 0:
                if game_list[cell_index - 1][1] in h_b_n_list and game_list[cell_index - 1][1] != "N":
                    h_b_n_list.remove(game_list[cell_index - 1][1])
            if (cell_index + 1) % col_num != 0:
                if game_list[cell_index + 1][1] in h_b_n_list and game_list[cell_index + 1][1] != "N":
                    h_b_n_list.remove(game_list[cell_index + 1][1])
            if not cell_index < col_num:
                if game_list[cell_index - col_num][1] in h_b_n_list and game_list[cell_index - col_num][1] != "N":
                    h_b_n_list.remove(game_list[cell_index - col_num][1])
            if not cell_index > (len(game_list) - col_num - 1):
                if game_list[cell_index + col_num][1] in h_b_n_list and game_list[cell_index + col_num][1] != "N":
                    h_b_n_list.remove(game_list[cell_index + col_num][1])

            print(f"here are the possibilities for {cell_index}:")
            print(h_b_n_list)

            game_list[cell_index][1] = h_b_n_list[0]
            """
            if game_list[index][0] == "R":
                starting_index = (index - 1)
            elif game_list[index][0] == "D":
                starting_index = (index - col_num)
            """
            if game_list[cell_index][0] == "L":
                if game_list[cell_index][1] == "H":
                    game_list[cell_index + 1][1] = "B"
                elif game_list[cell_index][1] == "B":
                    game_list[cell_index + 1][1] = "H"
                else:
                    game_list[cell_index + 1][1] = "N"
            elif game_list[cell_index][0] == "U":
                if game_list[cell_index][1] == "H":
                    game_list[cell_index + col_num][1] = "B"
                elif game_list[cell_index][1] == "B":
                    game_list[cell_index + col_num][1] = "H"
                else:
                    game_list[cell_index + col_num][1] = "N"

            see_list(game_list)

            h_b_n_list = ["H", "B", "N"]
    return game_list

def game_play(game_list, counter, last_tile_first_index):
    print("\n\ni am in game_play!")

    see_list(game_list)

    row_num = find_row_amount_of_template()
    col_num = find_column_amount_of_template()
    list_of_constraints = make_constraints_list()
    h_b_n_list = ["H", "B", "N"]

    # ilk ihtimali deniyorum
    if counter == 0:
        game_list = fill_cells(game_list, 0, h_b_n_list, col_num)
        counter += 1
        last_tile_first_index = len(make_template_list()) - 2

    if it_fits_the_constraints(game_list, row_num, col_num, list_of_constraints):
        return game_list

    else: # constraintlere uymadı
        h_b_n_list = ["H", "B", "N"]

        if last_tile_first_index % col_num != 0:
            if game_list[last_tile_first_index - 1][1] in h_b_n_list and game_list[last_tile_first_index - 1][1] != "N":
                h_b_n_list.remove(game_list[last_tile_first_index - 1][1])
        if (last_tile_first_index + 1) % col_num != 0:
            if game_list[last_tile_first_index + 1][1] in h_b_n_list and game_list[last_tile_first_index + 1][1] != "N":
                h_b_n_list.remove(game_list[last_tile_first_index + 1][1])
        if not last_tile_first_index < col_num:
            if game_list[last_tile_first_index - col_num][1] in h_b_n_list and \
                    game_list[last_tile_first_index - col_num][1] != "N":
                h_b_n_list.remove(game_list[last_tile_first_index - col_num][1])
        if not last_tile_first_index > (len(game_list) - col_num - 1):
            if game_list[last_tile_first_index + col_num][1] in h_b_n_list and \
                    game_list[last_tile_first_index + col_num][1] != "N":
                h_b_n_list.remove(game_list[last_tile_first_index + col_num][1])

        print(f"starting_index: {last_tile_first_index}")
        print(f"game_list[starting_index][1]: {game_list[last_tile_first_index][1]}")

        if game_list[last_tile_first_index][1] == "N":
            h_b_n_list.pop(0)
        h_b_n_list.remove(game_list[last_tile_first_index][1])
        print(f"\n{last_tile_first_index}'e önceki koyulan taşın ihtimalini çıkardım. now: {h_b_n_list}")

        if len(h_b_n_list) == 0:  # o cell için başka seçenek yokmuş

            if last_tile_first_index == 0: # ilk cell'miş, oyunun çözümü yok
                return "No solution!"

            else:  # ilk cell değilmiş, bir önceki cell'in başını bulana kadar geri gitme vakti

                print(last_tile_first_index)
                print(game_list[last_tile_first_index][0]) # kontrol

                #if game_list[starting_index][0] == "R" or game_list[starting_index][0] == "D":
                last_tile_first_index -= 1

                # bir önecki cellin başını buluyorum
                while (game_list[last_tile_first_index][0] != "L") and (game_list[last_tile_first_index][0] != "U"):
                    last_tile_first_index -= 1
                    #print(f"one less, new starting_index: {starting_index}") # kontrol


                print(f"bir önceki cell'in başını buldum. indexi: {last_tile_first_index}")


                h_b_n_list = ["H", "B", "N"]

                # bir önceki cell'in komşularından kurtuluyorum
                if last_tile_first_index % col_num != 0:
                    if game_list[last_tile_first_index - 1][1] in h_b_n_list and game_list[last_tile_first_index - 1][
                        1] != "N":
                        h_b_n_list.remove(game_list[last_tile_first_index - 1][1])
                if (last_tile_first_index + 1) % col_num != 0:
                    if game_list[last_tile_first_index + 1][1] in h_b_n_list and game_list[last_tile_first_index + 1][
                        1] != "N":
                        h_b_n_list.remove(game_list[last_tile_first_index + 1][1])
                if not last_tile_first_index < col_num:
                    if game_list[last_tile_first_index - col_num][1] in h_b_n_list and \
                            game_list[last_tile_first_index - col_num][1] != "N":
                        h_b_n_list.remove(game_list[last_tile_first_index - col_num][1])
                if not last_tile_first_index > (len(game_list) - col_num - 1):
                    if game_list[last_tile_first_index + col_num][1] in h_b_n_list and \
                            game_list[last_tile_first_index + col_num][1] != "N":
                        h_b_n_list.remove(game_list[last_tile_first_index + col_num][1])


                if game_list[last_tile_first_index][1] == "N":
                    h_b_n_list.pop(0)

                    #game_play(game_list, 2, starting_index)
                else:
                    # bir önceki cell'de denediğim ve olmayan ihtimali çıkarıyorum
                    h_b_n_list.remove(game_list[last_tile_first_index][1])

                # kontrol
                print(f"{last_tile_first_index}'nın özellikleri: \n")
                print(f"left or up: {game_list[last_tile_first_index][0]}") # kontrol
                print(f"high, base or neutral: {game_list[last_tile_first_index][1]}") # kontrol
                print(f"burada\n{last_tile_first_index}'e önceki koyulan taşın ihtimalini çıkardım. now: {h_b_n_list}")

                # bir önceki cell'in ve devamının başlarını temizliyorum
                for index in range(last_tile_first_index, len(game_list)):
                    if str(game_list[index][0]) == "L" or str(game_list[index][0]) == "U":
                        game_list[index][1] = ""

                # temizlendikten sonra başka bir şekilde tekrar dolduruyorum
                game_list = fill_cells(game_list, last_tile_first_index, h_b_n_list, col_num)
                return game_play(game_list, 2, last_tile_first_index)

        else: # aynı cell için başka seçenek var

            # kontrol
            see_list(game_list)

            print(last_tile_first_index)
            print(game_list[last_tile_first_index][0] + game_list[last_tile_first_index][1])
            print(h_b_n_list)

            for index in range(last_tile_first_index, len(game_list)):
                if str(game_list[index][0]) == "L" or str(game_list[index][0]) == "U":
                    game_list[index][1] = ""

            see_list(game_list)

            game_list = fill_cells(game_list, last_tile_first_index, h_b_n_list, col_num)

            return game_play(game_list, 1, last_tile_first_index)


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
    printing_the_end_game_to_output_file(
        game_play(make_template_list(), 0, 0)
        , find_column_amount_of_template())


if __name__ == "__main__":
    main()