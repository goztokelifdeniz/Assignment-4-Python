import sys

game_list1 = [['L', ''], ['R', ''], ['L', ''], ['R', ''], ['U', ''], ['U', ''], ['L', ''], ['R', ''], ['D', ''], ['D', ''], ['L', ''], ['R', '']]

def see_list(game_list):
    a = [indices[1] for indices in game_list]
    print(a)

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

    if list_of_const == current_template_const:
        print("it fits\n")
        return True
    print("it doesn't fit\n")
    return False

def game_play(game_list, index, h_b_n_list):
    #print(f"\n\ngame_list: \n{game_list}\n")
    see_list(game_list)
    print(f"index: {index}")

    row_num = 3
    col_num = 4
    list_of_constraints = [[2, -1, -1], [-1, -1, 2], [-1, 2, -1, -1], [-1, -1, -1, 0]]

    is_the_list_fully_done = True

    for checking_index in range(len(game_list)):
        if game_list[checking_index][1] == "":
            is_the_list_fully_done = False
            break

    if is_the_list_fully_done or index >= len(game_list):     # zaten aynı anlama geliyor olması lazım ama hadi bakalım
        if it_fits_the_constraints(game_list, row_num, col_num, list_of_constraints):
            return game_list

        else: # bu yerleştitrme biçimi yanlışmış

            index = index - 1

            if game_list[index][1] == "N":

                for index in range(index, len(game_list)):
                    if str(game_list[index][0]) == "L" or str(game_list[index][0]) == "U":
                        game_list[index][1] = ""



                return game_play(game_list, index, h_b_n_list)

            else: # oradaki taş N değilmiş

                h_b_n_list = ["H", "B", "N"]

                if game_list[index][1] == "B" and "H" in h_b_n_list:      # buraya gerek olacak mı bilmiyorum
                    h_b_n_list.remove("H")

                h_b_n_list.remove(game_list[index][1]) # ----------------------------------------------

                # komşular yüzünden olmayacak ihtimalleri çıkar
                if index % col_num != 0:
                    if game_list[index - 1][1] in h_b_n_list and game_list[index - 1][1] != "N" and game_list[index][
                        0] != "R":
                        h_b_n_list.remove(game_list[index - 1][1])
                if (index + 1) % col_num != 0:
                    if game_list[index + 1][1] in h_b_n_list and game_list[index + 1][1] != "N" and game_list[index][
                        0] != "L":
                        h_b_n_list.remove(game_list[index + 1][1])
                if not index < col_num:
                    if game_list[index - col_num][1] in h_b_n_list and \
                            game_list[index - col_num][1] != "N" and game_list[index][0] != "D":
                        h_b_n_list.remove(game_list[index - col_num][1])
                if not index > (len(game_list) - col_num - 1):
                    if game_list[index + col_num][1] in h_b_n_list and \
                            game_list[index + col_num][1] != "N" and game_list[index][0] != "U":
                        h_b_n_list.remove(game_list[index + col_num][1])

                game_list[index][1] = h_b_n_list[0]

                if game_list[index][0] == "L":
                    if game_list[index][1] == "H":
                        game_list[index + 1][1] = "B"
                    elif game_list[index][1] == "B":
                        game_list[index + 1][1] = "H"
                    else:
                        game_list[index + 1][1] = "N"
                elif game_list[index][0] == "U":  # direkt "else:" şeklinde de yazılabilir sanki
                    if game_list[index][1] == "H":
                        game_list[index + col_num][1] = "B"
                    elif game_list[index][1] == "B":
                        game_list[index + col_num][1] = "H"
                    else:
                        game_list[index + col_num][1] = "N"

                h_b_n_list = ["H", "B", "N"]

                return game_play(game_list, (index + 1), h_b_n_list)

    else: # daha tam dolmamış listemiz
        if game_list[index][0] == "L" or game_list[index][0] == "U":

            # komşular yüzünden olmayacak ihtimalleri çıkar
            if index % col_num != 0:
                if game_list[index - 1][1] in h_b_n_list and game_list[index - 1][1] != "N" and game_list[index][
                    0] != "R":
                    h_b_n_list.remove(game_list[index - 1][1])
            if (index + 1) % col_num != 0:
                if game_list[index + 1][1] in h_b_n_list and game_list[index + 1][1] != "N" and game_list[index][
                    0] != "L":
                    h_b_n_list.remove(game_list[index + 1][1])
            if not index < col_num:
                if game_list[index - col_num][1] in h_b_n_list and \
                        game_list[index - col_num][1] != "N" and game_list[index][0] != "D":
                    h_b_n_list.remove(game_list[index - col_num][1])
            if not index > (len(game_list) - col_num - 1):
                if game_list[index + col_num][1] in h_b_n_list and \
                        game_list[index + col_num][1] != "N" and game_list[index][0] != "U":
                    h_b_n_list.remove(game_list[index + col_num][1])

            if len(h_b_n_list) > 0:  # koyulabilecek seçenek var
                game_list[index][1] = h_b_n_list[0]

                if game_list[index][0] == "L":
                    if game_list[index][1] == "H":
                        game_list[index + 1][1] = "B"
                    elif game_list[index][1] == "B":
                        game_list[index + 1][1] = "H"
                    else:
                        game_list[index + 1][1] = "N"
                elif game_list[index][0] == "U":  # direkt "else:" şeklinde de yazılabilir sanki
                    if game_list[index][1] == "H":
                        game_list[index + col_num][1] = "B"
                    elif game_list[index][1] == "B":
                        game_list[index + col_num][1] = "H"
                    else:
                        game_list[index + col_num][1] = "N"

                h_b_n_list = ["H", "B", "N"]

                return game_play(game_list, (index + 1), h_b_n_list)
            else:
                return game_play(game_list, (index - 1), h_b_n_list)
        else:
            return game_play(game_list, (index + 1), h_b_n_list)

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
    printing_the_end_game_to_output_file(game_play(game_list1, 0, ["H", "B", "N"]), 4)


if __name__ == "__main__":

    main()


"""    if is_the_list_fully_done or index >= len(game_list):
        if it_fits_the_constraints(game_list, row_num, col_num, list_of_constraints):
            return game_list
        else:
            
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
                    game_list[index][1] = h_b_n_list[0]
                    
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
                        return game_play(game_list, (index - 1), h_b_n_list)
                    else: # daha geride bir index yok
                        return "No solution!"
            else:
                return game_play(game_list, (index + 1), h_b_n_list)
    else: # daha tam dolmamış listemiz
    """
