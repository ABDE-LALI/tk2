from tkinter import *

sdk = Tk()
sdk.title("SOUDOUKOU")
sdk.iconbitmap("173877_sudoku_icon.ico")
sdk.geometry("350x500")
usage = Label(
    sdk, text="enter numbers and click check if its correct", bg="#cccccc")
usage.grid(row=0, column=1, columnspan=10)

isvalid_soudo = Label(sdk, text="")
isvalid_soudo.grid(row=16, column=0, columnspan=10, pady=5)

# isnotvalid_soudo = Label(sdk, text="", bg="red")
# isnotvalid_soudo.grid(row=16, column=1, columnspan=10, pady=5)

answers = {}


def check_entry(val):
    valid = (val.isdigit() or val == "") and len(val) < 2 and val != "0"
    return valid


check_res = sdk.register(check_entry)


def petit_table(row, col, color):
    for i in range(3):
        for j in range(3):
            fild = Entry(sdk, width=5, bg=color, justify="center",
                         validate="key", validatecommand=(check_res, "%P"))
            fild.grid(row=row + i, column=col + j,
                      sticky="nsew", padx=1, pady=1, ipady=5)
            answers[(row + i, col + j)] = fild


def grand_table():
    color = "#dddddd"
    for big_row in range(1, 10, 3):
        for big_col in range(0, 9, 3):
            petit_table(big_row, big_col, color)
            if color == "#dddddd":
                color = "#aaaaaa"
            else:
                color = "#dddddd"


def clean_soudou():
    isvalid_soudo.configure(text="", bg="#f0f0f0")
    # isnotvalid_soudo.configure(text="")

    for i in range(1, 10):
        for j in range(0, 9):
            soudou_cell = answers[(i, j)]
            soudou_cell.delete(0, 1)


def check_rows(matric):
    ris45 = 0
    for i in range(9):
        rows_som = 0
        for j in range(9):
            rows_som += matric[i][j]
            if rows_som == 45:
                ris45 += 1
        # print(rows_som)
    return True if ris45 == 9 else False


def check_cols(matric):
    cis45 = 0
    for i in range(9):
        cols_som = 0
        for j in range(9):
            cols_som += matric[j][i]
            if cols_som == 45:
                cis45 += 1
        # print(cols_som)
    return True if cis45 == 9 else False


def check_squar(matric):
    gis45 = 0
    def group_sums(mat):
        group_sums_dict = {}
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                block_sum = sum(mat[row][col] for row in range(i, i+3) for col in range(j, j+3))
                group_sums_dict[(i // 3, j // 3)] = block_sum

        return group_sums_dict
    result = group_sums(matric)
    # for total_sum in result.items():
    #     print(f"Sum of group {total_sum}")
    #     print("ana")
    # print("houwa")
    for group in result.items():
        if group[1] == 45 :
            gis45 += 1
    return True if gis45 == 9 else False
        
# check_mat = [
#  [5, 3, 4, 6, 7, 8, 9, 1, 2],
#  [6, 7, 2, 1, 9, 5, 3, 4, 8],
#  [1, 9, 8, 3, 4, 2, 5, 6, 7],
#  [8, 5, 9, 7, 6, 1, 4, 2, 3],
#  [4, 2, 6, 8, 5, 3, 7, 9, 1],
#  [7, 1, 3, 9, 2, 4, 8, 5, 6],
#  [9, 6, 1, 5, 3, 7, 2, 8, 4],
#  [2, 8, 7, 4, 1, 9, 6, 3, 5],
#  [3, 4, 5, 2, 8, 6, 1, 7, 9]
# ]   

def check_win():
    board = []
    isvalid_soudo.configure(text="", bg="#f0f0f0")
    # isnotvalid_soudo.configure(text="")
    for i in range(1, 10):
        valeus_row = []
        for j in range(0, 9):
            cell_val = answers[(i, j)].get()
            if cell_val == "":
                valeus_row.append(0)
            else:
                valeus_row.append(int(cell_val))
        board.append(valeus_row)
    print(board)
    if check_rows(board) and check_cols(board) and check_squar(board):
        isvalid_soudo.configure(
            text="its a valid soudoukou", bg="green", width=30)
    else:
        isvalid_soudo.configure(
            text="its not a valid soudoukou", bg="red", width=30)


check_btn = Button(sdk, text="Check", bg="green", width=30,
                   command=check_win).grid(row=17, column=0, columnspan=10)
clear_btn = Button(sdk, text="Clean", bg="red", width=30,
                   command=clean_soudou).grid(row=18, column=0, columnspan=10)
grand_table()
sdk.mainloop()
