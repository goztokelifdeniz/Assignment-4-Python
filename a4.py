import sys
import copy


def make_constraints_list():
    with open(sys.argv[1], "r") as input_as_a_file:
        input_string =  input_as_a_file.read()
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

        #print("\nfile as head string:\n\n" + input_string)
        temporary_list = input_string.split("\n")[4:]

        #print("\nlist 2: ")
        #print(temporary_list)

        temp_list = [[chars, ""] for lines in temporary_list for chars in lines if chars != " "]

        #print("\nlist 3: ")
        #print(temp_list)

    return temp_list

def find_row_amount_of_template():
    with open(sys.argv[1], "r") as input_as_a_file:
        input_string = input_as_a_file.read()
        row_amount = input_string.count("\n") - 3
        #print("\nrow_amount: " + str(row_amount))
    return row_amount

def find_column_amount_of_template():
    column_amount = len(make_template_list()) // find_row_amount_of_template()
    #print("\ncolumn_amount: " + str(column_amount))
    return column_amount


def find_possible_placement_of_the_cell(template_list, cell_index, row_num, col_num):
    h_b_n_list = ["H", "B"]

    if cell_index % col_num != 0:
        if len(h_b_n_list) > 0:
            for index in range(len(h_b_n_list)):
                if h_b_n_list[index] == template_list[cell_index - 1][1]:
                    h_b_n_list.remove(h_b_n_list[index])
                    print(h_b_n_list)
    if (cell_index + 1) % col_num != 0:
        if len(h_b_n_list) > 0:
            for index in range(len(h_b_n_list)):
                if h_b_n_list[index] == template_list[cell_index + 1][1]:
                    h_b_n_list.remove(h_b_n_list[index])
    if not cell_index >= (len(template_list) - col_num):
        if len(h_b_n_list) > 0:
            for index in range(len(h_b_n_list)):
                if h_b_n_list[index] == template_list[cell_index + col_num][1]:
                    h_b_n_list.remove(h_b_n_list[index])
    if not cell_index < col_num:
        if len(h_b_n_list) > 0:
            for index in range(len(h_b_n_list)):
                if h_b_n_list[index] == template_list[cell_index - col_num][1]:
                    h_b_n_list.remove(h_b_n_list[index])
    h_b_n_list.append("N")
    return h_b_n_list


def blind_valley_game(template_list):
    row_num = find_row_amount_of_template()
    col_num = find_column_amount_of_template()
    cons_list = make_constraints_list()

    initial_temp_list = copy.deepcopy(template_list)

    for cells in range(len(template_list)):
        if not template_list[cells][0] == "R" or template_list[cells][0] == "D":

            h_b_n_list = ["H", "B", "N"]
            if cells % col_num != 0 and len(h_b_n_list) > 0:
                for index in range(len(h_b_n_list)):
                    if h_b_n_list[index] == template_list[cells - 1][1]:
                        h_b_n_list.remove(h_b_n_list[index])
                        print(h_b_n_list)

            if "H" in h_b_n_list:
                if template_list[cells][0] == "U":
                    template_list[cells][1] = "H"
                    template_list[cells + col_num][1] = "B"

                    print(template_list)

                elif template_list[cells][0] == "L":
                    template_list[cells][1] = "H"
                    template_list[cells + 1][1] = "B"
                    print(template_list)

            elif "B" in  h_b_n_list:
                if template_list[cells][0] == "U":
                    template_list[cells][1] = "B"
                    template_list[cells + col_num][1] = "H"
                    print(template_list)

                elif template_list[cells][0] == "L":
                    template_list[cells][1] = "B"
                    template_list[cells + 1][1] = "H"
                    print(template_list)


            else:
                if template_list[cells][0] == "U":
                    template_list[cells][1] = "N"
                    template_list[cells + col_num][1] = "N"
                    print(template_list)


                elif template_list[cells][0] == "L":
                    template_list[cells][1] = "N"
                    template_list[cells + 1][1] = "N"
                    print(template_list)

    print(template_list)





def main():
    input_file = open(sys.argv[1], "r")
    #output_file = open(sys.argv[2], "w")
    #output_file.write("bir şeyler")

    make_constraints_list()
    make_template_list()
    find_row_amount_of_template()
    find_column_amount_of_template()
    blind_valley_game(make_template_list())

    input_file.close()
    #output_file.flush()
    #output_file.close()

# take input file
# make constraints list from input file [[H-R1,H-R2,H-R3],[B-R1,B-R2,B-R3],[H-C1,H-C2,H-C3,H-C4],[B-C1,B-C2,B-C3,B-C4]]
# make template list from input file
#
# main function to play the game(first empty place in template):
#       if it is up-down:
#           if up-H down-B is ok:
#
#       if it is left-right:
#

if __name__ == "__main__":
    main()