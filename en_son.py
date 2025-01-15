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

def fill_cells(game_list, starting_index, h_b_n_list, col_num):
    for cell_index in range(starting_index, len(game_list)):
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

def game_play(game_list, head, sub, h_b_n_list):

    # bir önceki cellin başını buluyorum
    if sub == (len(game_list) - 2) and len(h_b_n_list) == 0:
        while (game_list[head][0] != "L") and (game_list[head][0] != "U"):
            head -= 1

    """
    print("\n\ni am in game_play!")
    see_list(game_list)
    """

    row_num = find_row_amount_of_template()
    col_num = find_column_amount_of_template()
    list_of_constraints = make_constraints_list()

    # index'ye gelebilecek ihtimallere bakıyorum şimdi.
    # zaten önceden denenip sonuç vermeyen ihtimaller h_b_n_list ten silinmişti. h_b_n_list de parametre olarak verildiği için elenmişti.

    if sub % col_num != 0:
        if game_list[sub - 1][1] in h_b_n_list and game_list[sub - 1][1] != "N":
            h_b_n_list.remove(game_list[sub - 1][1])
    if (sub + 1) % col_num != 0:
        if game_list[sub + 1][1] in h_b_n_list and game_list[sub + 1][1] != "N":
            h_b_n_list.remove(game_list[sub + 1][1])
    if not sub < col_num:
        if game_list[sub - col_num][1] in h_b_n_list and game_list[sub - col_num][1] != "N":
            h_b_n_list.remove(game_list[sub - col_num][1])
    if not sub > (len(game_list) - col_num - 1):
        if game_list[sub + col_num][1] in h_b_n_list and game_list[sub + col_num][1] != "N":
            h_b_n_list.remove(game_list[sub + col_num][1])

    h_b_n_list_for_b = h_b_n_list.copy()

    """
    # kontrol
    print(f"h_b_n_list: {h_b_n_list}")
    print(f"h_b_n_list_for_b: {h_b_n_list_for_b}")
    """

    # hatırlatma: oyun index = 0 ile başlıyor
    game_list = fill_cells(game_list, sub, h_b_n_list, col_num)
    what_i_put_in_b = [h_b_n_list[0]] # append mi kullanmam gerekiyor tanımlama mı?

    """
    # kontrol
    print(f"again h_b_n_list: {h_b_n_list}")
    print(f""gain h_b_n_list_for_b: {h_b_n_list_for_b}")
    """


    if it_fits_the_constraints(game_list, row_num, col_num, list_of_constraints):
        return game_list
    else:
        return



# A SONDAN BAŞA B BAŞTAN SONA GİDEN ALGORİTMA (B: A'DAN SONUNCU TILE'IN BAŞINA DOĞRU)
# index'den başlayarak her şeyi doldur
# constraintlere uyuyorsa:
#   return game_list
# constraintlere uymuyor ise:
#
#   index için başka ihtimal yoksa:
#       eğer index + 1 > son tile'ın baş indeksi ise: (index'nin ihtimalleri bitti. içinde olduğumuz set de bitti. ilk set index = head ile başlamıştı, şimdi head bir azalacak.)
#           eğer head-1 < 0 ise: (en uzun set bitti, cevap çıkmadı)
#               return "No solution!"
#           eğer head-1 < 0 değil ise: (daha uzun bir set var, ona bakalım)
#               head = head - 1
#               index = head

#   index'ye bir önceki denediklerimizden kurtul (liste mi kullansan acaba?)
#   (önceki denediklerim listesi olabilir)
#   index nin komşularından kurtul
#
#   elimdeki index için başka seçenek yoksa:
#       index - 1 < 0 ise: (içinde olduğum set bitmişse)
#          head - 1 < 0 ise: (başka set yoksa)
#           return "No solution!"
#           else: (daha başka setler var)
#           head = head - 1 (bir önceki sete geldik)
#           index = len(game_list) - 2 (setin sonundan başlamamız lazım)
#           head'dan başlayarak kalan bütün başları temizle
#           head'dan başlayarak doldur
#           game_play (kontrol etmiş olacak)
#
#       else: (daha içinde olduğum set bitmedi)
#           index = index - 1
#
#   elimdeki index için başka seçenek varsa:
#       index ve index'den sonrasını temizle
#       index'ye o seçeneği yerleştir, kalanını doldur
#

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
        game_play(make_template_list(),(len(make_template_list()) - 2), (len(make_template_list()) - 2),[])
        , find_column_amount_of_template())

if __name__ == "__main__":
    main()