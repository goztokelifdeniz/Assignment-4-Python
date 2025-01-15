import sys

import time



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
    print("current template const list: ")
    print(current_template_const)

    for sublists in range(len(list_of_const)):
        for const in range(len(list_of_const[sublists])):
            if list_of_const[sublists][const] != (-1) and list_of_const[sublists][const] != current_template_const[sublists][const]:
                return False
    return True

def func(game_list, index, olasilik_listesi):

    row_num = find_row_amount_of_template()
    col_num = find_column_amount_of_template()
    list_of_constraints = make_constraints_list()

    #print(f"current index i'm working with: {index}")
    #see_list(game_list)
    #print(f"olasılık listesinin durumu: {tile_options_list}")

    if game_list[index][1] == "N": # tile'ın içindeki taş == neutral ise:
        if index == 0:
            return "No solution!"
        else:

            index = index - 1
            while not (game_list[index][0] == "L" or game_list[index][0] == "U"):
                index = index - 1

            olasilik_listesi = ["H", "B", "N"]

            if game_list[index][1] == "B":
                olasilik_listesi.remove("H")

            if game_list[index][1] != "N":
                olasilik_listesi.remove(game_list[index][1])
            #print(f"\nA olasılık listesi: {tile_options_list} for {index}")
            return func(game_list, index, olasilik_listesi)

    else: # tile'ın içindeki taş == neutral değilse, DEMEK Kİ AYNI TILE İÇİN BAŞKA SEÇENEK VAR

        # elimdeki olasılık listesinden (varsa) üstteki ve soldaki komşuların kısıtladıklarını çıkarıyorum
        if index % col_num != 0 and game_list[index - 1][1] in olasilik_listesi and game_list[index - 1][1] != "N":
            olasilik_listesi.remove(game_list[index - 1][1])
        if index >= col_num and game_list[index - col_num][1] in olasilik_listesi and game_list[index - col_num][1] != "N":
            olasilik_listesi.remove(game_list[index - col_num][1])

        # yeni ilk ihtimali yerleştiriyorum
        game_list[index][1] = olasilik_listesi[0]
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

        # taş en sondaki taş değilse, bundan sonrakileri de hatasız doldurabilmek için
        # bu taştan sonraki taşları çıkarıyorum
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

        #print("\ni placed a tile!")
        #see_list(game_list)

        if index == (len(game_list) - 2): # taşımı yerleştirdim, bu taş son taşmış
            see_list(game_list)
            print(game_list)
            if it_fits_the_constraints(game_list, row_num, col_num, list_of_constraints): # oldu
                return game_list
            else: # olmadı
                if game_list[index][1] == "N":
                    # aynı şeyi tepede yakalıyor zaten
                    #print(f"\nB olasılık listesi: {tile_options_list} for {index}")
                    return func(game_list, index, olasilik_listesi)
                else:

                    olasilik_listesi = ["H", "B", "N"]

                    if game_list[index][1] == "B":
                        olasilik_listesi.remove("H")

                    if game_list[index][1] != "N":
                        olasilik_listesi.remove(game_list[index][1])

                    #print(f"\nC olasılık listesi: {tile_options_list} for {index}")
                    return func(game_list, index, olasilik_listesi)
        else: # yerleştirdiğim taş son taş değilmiş
            # bir sonraki taşı buluyorum
            index = index + 1
            while not (game_list[index][0] == "L" or game_list[index][0] == "U"):
                index = index + 1

            olasilik_listesi = ["H", "B", "N"]
            #print(f"\nD olasılık listesi: {tile_options_list} for {index}")
            return func(game_list, index, olasilik_listesi)

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
    start = time.time()

    printing_the_end_game_to_output_file(func(make_template_list(), 0, ["H", "B", "N"]), 4)

    end = time.time()
    print(end - start)

if __name__ == "__main__":
    main()