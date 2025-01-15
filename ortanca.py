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

def fill_cells(game_list, starting_index, h_b_n_list, col_num):
    print("\nin fill cells!")
    see_list(game_list)

    for cell_index in range(starting_index, len(game_list)):

        if game_list[cell_index][1] == "":

            if cell_index % col_num != 0:
                if game_list[cell_index - 1][1] in h_b_n_list and game_list[cell_index - 1][1] != "N" and game_list[cell_index][0] != "R":
                    h_b_n_list.remove(game_list[cell_index - 1][1])
            if (cell_index + 1) % col_num != 0:
                if game_list[cell_index + 1][1] in h_b_n_list and game_list[cell_index + 1][1] != "N" and game_list[cell_index][0] != "L":
                    h_b_n_list.remove(game_list[cell_index + 1][1])
            if not cell_index < col_num:
                if game_list[cell_index - col_num][1] in h_b_n_list and game_list[cell_index - col_num][1] != "N" and game_list[cell_index][0] != "D":
                    h_b_n_list.remove(game_list[cell_index - col_num][1])
            if not cell_index > (len(game_list) - col_num - 1):
                if game_list[cell_index + col_num][1] in h_b_n_list and game_list[cell_index + col_num][1] != "N" and game_list[cell_index][0] != "U":
                    h_b_n_list.remove(game_list[cell_index + col_num][1])

            print(f"\nhere are the possibilities for {cell_index}:")
            print(h_b_n_list)

            game_list[cell_index][1] = h_b_n_list[0]

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
        else:
            continue
    return game_list

def game_play(game_list, counter, head, sub, h_b_n_list):  # B AZALAN ALGORİTMA (SON BAŞTAN A'YA DOĞRU)

    print("\n\ni am in game_play!")
    see_list(game_list)
    print(f"\nhead: {head}")
    print(f"index: {sub}")
    #see_list(game_list)

    row_num = find_row_amount_of_template()
    col_num = find_column_amount_of_template()
    list_of_constraints = make_constraints_list()

    # ilk ihtimali deniyorum
    if counter == 0:
        game_list = fill_cells(game_list, 0, h_b_n_list, col_num)
        counter = 1
        head = len(make_template_list()) - 2
        sub = len(make_template_list()) - 2

    if it_fits_the_constraints(game_list, row_num, col_num, list_of_constraints):
        return game_list

    else: # constraintlere uymadı

        # komşular yüzünden olmayacak ihtimalleri çıkar
        if sub % col_num != 0:
            if game_list[sub - 1][1] in h_b_n_list and game_list[sub - 1][1] != "N" and game_list[sub][0] != "R":
                h_b_n_list.remove(game_list[sub - 1][1])
        if (sub + 1) % col_num != 0:
            if game_list[sub + 1][1] in h_b_n_list and game_list[sub + 1][1] != "N" and game_list[sub][0] != "L":
                h_b_n_list.remove(game_list[sub + 1][1])
        if not sub < col_num:
            if game_list[sub - col_num][1] in h_b_n_list and \
                    game_list[sub - col_num][1] != "N" and game_list[sub][0] != "D":
                h_b_n_list.remove(game_list[sub - col_num][1])
        if not sub > (len(game_list) - col_num - 1):
            if game_list[sub + col_num][1] in h_b_n_list and \
                    game_list[sub + col_num][1] != "N" and game_list[sub][0] != "U":
                h_b_n_list.remove(game_list[sub + col_num][1])




        if game_list[sub][1] == "N":  # o index için başka seçenek yokmuş "if len(h_b_n_list) == 1"
            print("index için başka seçenek yokmuş")
            #if head == -1 and index == -1 and len(h_b_n_list) == 1: # oyun bitti
                #return "No solution!"
            #else: # index'ın değişme vakti
            if sub > head: # aynı sette başka index'lar var
                print("\naynı sette başka index'lar var / başlangıç")
                print(f"head: {head}")
                print(f"index: {sub}")

                #if (head == 0 or head == -1) and index == 0: # index == -1 tanımından emin değilim
                #    index = -1
                #else:
                    # bir önceki index'ı buluyorum
                sub -= 1
                while (game_list[sub][0] != "L") and (game_list[sub][0] != "U"):
                    sub -= 1

                print("\naynı set yeni index / orta")
                print(f"head: {head}")
                print(f"index: {sub}")

                #if index == -1:
                #    index = 0

                h_b_n_list = ["H", "B", "N"]
                h_b_n_list.remove(game_list[sub][1])

                # yeni index'ın ve devamının başlarını temizliyorum
                for index in range(sub, len(game_list)):
                    if str(game_list[index][0]) == "L" or str(game_list[index][0]) == "U":
                        game_list[index][1] = ""

                see_list(game_list)

                # komşular yüzünden olmayacak ihtimalleri çıkar
                if sub % col_num != 0:
                    if game_list[sub - 1][1] in h_b_n_list and game_list[sub - 1][1] != "N" and game_list[sub][
                        0] != "R":
                        h_b_n_list.remove(game_list[sub - 1][1])
                if (sub + 1) % col_num != 0:
                    if game_list[sub + 1][1] in h_b_n_list and game_list[sub + 1][1] != "N" and game_list[sub][
                        0] != "L":
                        h_b_n_list.remove(game_list[sub + 1][1])
                if not sub < col_num:
                    if game_list[sub - col_num][1] in h_b_n_list and \
                            game_list[sub - col_num][1] != "N" and game_list[sub][0] != "D":
                        h_b_n_list.remove(game_list[sub - col_num][1])
                if not sub > (len(game_list) - col_num - 1):
                    if game_list[sub + col_num][1] in h_b_n_list and \
                            game_list[sub + col_num][1] != "N" and game_list[sub][0] != "U":
                        h_b_n_list.remove(game_list[sub + col_num][1])

                print("yeni index'dan itibaren sildim:")
                # temizlendikten sonra başka bir şekilde tekrar dolduruyorum
                game_list = fill_cells(game_list, head, h_b_n_list, col_num)

                print("\naynı sette başka index'lar var / son")
                print(f"head: {head}")
                print(f"index: {sub}")

                return game_play(game_list, 1, head, sub, ["H", "B", "N"])

            else: # o setteki tüm index'lar bitti, head değişecek

                print("\no setteki tüm index'lar bitti / başlangıç")
                print(f"head: {head}")
                print(f"index: {sub}")
                head -= 1

                if head != -1:
                    # bir önceki head'i buluyorum
                    while (game_list[head][0] != "L") and (game_list[head][0] != "U"):
                        head -= 1

                    h_b_n_list = ["H", "B", "N"]
                    h_b_n_list.remove(game_list[head][1])

                    sub = (len(game_list) - 2)

                    print("\nhead değiştirdik / orta")
                    print(f"head: {head}")
                    print(f"index: {sub}")

                    # yeni index'ın ve devamının başlarını temizliyorum
                    #for index in range(head, len(game_list)):
                    #    if str(game_list[index][0]) == "L" or str(game_list[index][0]) == "U":
                    #        game_list[index][1] = ""

                    #see_list(game_list)

                    # temizlendikten sonra başka bir şekilde tekrar dolduruyorum
                    #game_list = fill_cells(game_list, head, h_b_n_list, col_num)

                    #print("\no setteki tüm index'lar bitmişti yeni sete ilk denemeyi yaptık / son")
                    #print(f"head: {head}")
                    #print(f"index: {index}")

                    return game_play(game_list, 1, head, sub, ["H", "B", "N"])

                else: # tüm headler bitti. oyunun cevabı neyse onu yazdırıcam
                    if it_fits_the_constraints(game_list, row_num, col_num, list_of_constraints):
                        return game_list
                    else:
                        return "No solution!"

        else: # o index için başka seçenek var
            #see_list(game_list)

            print("\no index için başka seçenek var / başlangıç")
            print(f"head: {head}")
            print(f"index: {sub}")
            print(h_b_n_list)
            see_list(game_list)

            # en son deneneni çıkar
            h_b_n_list.remove(game_list[sub][1])

            for index in range(sub, len(game_list)):
                if str(game_list[index][0]) == "L" or str(game_list[index][0]) == "U":
                    game_list[index][1] = ""

            see_list(game_list)

            game_list = fill_cells(game_list, sub, h_b_n_list, col_num)

            print("\no index için başka seçenek var / son")
            print(f"head: {head}")
            print(f"index: {sub}")

            return game_play(game_list, 1, head, sub, h_b_n_list)


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
    printing_the_end_game_to_output_file(game_play(make_template_list(), 0, 0, 0, ["H", "B", "N"]), find_column_amount_of_template())


if __name__ == "__main__":

    main()



"""
BASİTÇE ALGORİTMA

def game_play(game_list, index, h_b_n_list):  # B AZALAN ALGORİTMA (SON BAŞTAN A'YA DOĞRU)

    row_num = find_row_amount_of_template()
    col_num = find_column_amount_of_template()
    list_of_constraints = make_constraints_list()

    if it_fits_the_constraints(game_list, row_num, col_num, list_of_constraints):
        return game_list

    else: # constraintlere uymadı
        # komşular yüzünden olmayacak ihtimalleri çıkar
        # o index için başka seçenek yokmuş "if len(h_b_n_list) == 1"
            # aynı sette başka index'lar var
                # bir önceki index'ı buluyorum

                h_b_n_list = ["H", "B", "N"]
                h_b_n_list.remove(game_list[index][1])

            # o setteki tüm index'lar bitti, head değişecek
                # bir önceki head'i buluyorum
                index = (len(game_list) - 2)
                print("\nhead değiştirdik / orta")
                #print("\no setteki tüm index'lar bitmişti, yeni head setindee ilk denemeyi yaptık / son")
            # tüm headler bitti. oyunun cevabı neyse onu yazdırıcam
         # o index için başka seçenek var
            # en son deneneni çıkar
"""