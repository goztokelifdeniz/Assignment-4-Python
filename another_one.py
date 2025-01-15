
game_list1 = [['L', 'B'], ['R', 'H'], ['L', 'B'], ['R', 'H'], ['U', 'H'], ['U', 'B'], ['L', 'H'], ['R', 'B'], ['D', 'B'], ['D', 'H'], ['L', 'B'], ['R', 'H']]

list_of_constraints = [[2, -1, -1], [-1, -1, 2], [-1, 2, -1, -1], [-1, -1, -1, 0]]

def see_list(game_list):
    a = [indices[1] for indices in game_list]
    print(a)

def it_fits_the_constraints(last_list, row_num, col_num, list_of_const):
    print(list_of_constraints)
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
        print(f"\n\nsublists: {sublists}")
        for const in range(len(list_of_const[sublists])):
            print(f"\nconst: {const}")
            print(f"list_of_const[sublists][const]: {list_of_const[sublists][const]}")
            print(f"current_template_const[sublists][const]: {current_template_const[sublists][const]}")
            if list_of_const[sublists][const] != (-1) and list_of_const[sublists][const] != current_template_const[sublists][const]:
                return False
    return True

print(it_fits_the_constraints(game_list1, 3, 4, list_of_constraints))