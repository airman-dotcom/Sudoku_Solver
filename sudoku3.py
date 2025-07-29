import sys
arr = []
nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
ref = {
        "0": "0",
        "1": "0",
        "2": "0",
        "3": "1",
        "4": "1",
        "5": "1",
        "6": "2",
        "7": "2",
        "8": "2"
}
"""arr = [['6', '_', '_', '_', '_', '4', '_', '_', '1'],
['_', '_', '1', '_', '_', '_', '_', '4', '9'],
['5', '_', '_', '_', '1', '_', '_', '_', '7'],
['1', '5', '7', '_', '_', '_', '_', '9', '6'],
['_', '_', '4', '_', '9', '6', '_', '_', '3'],
['3', '_', '_', '_', '4', '5', '_', '1', '8'],
['_', '_', '_', '_', '7', '_', '_', '6', '2'],
['7', '6', '_', '_', '2', '_', '_', '8', '5'],
['_', '_', '8', '5', '6', '_', '3', '7', '4']]"""

#arr = [['_', '6', '_', '_', '_', '7', '_', '9', '3'], ['_', '4', '_', '_', '_', '5', '8', '6', '_'], ['_', '_', '_', '_', '8', '_', '5', '_', '_'], ['_', '2', '6', '_', '_', '1', '_', '_', '_'], ['_', '7', '3', '_', '_', '6', '9', '_', '1'], ['_', '_', '_', '_', '4', '9', '_', '7', '_'], ['_', '_', '_', '_', '_', '_', '_', '5', '8'], ['_', '_', '_', '_', '_', '_', '6', '1', '2'], ['6', '_', '5', '1', '_', '_', '_', '_', '9']]

#arr = [['_', '3', '_', '5', '_', '1', '9', '_', '6'], ['_', '4', '7', '9', '_', '_', '_', '2', '_'], ['6', '9', '_', '_', '4', '2', '5', '_', '3'], ['_', '6', '_', '_', '_', '9', '_', '3', '4'], ['_', '2', '_', '_', '_', '_', '8', '1', '_'], ['_', '7', '3', '1', '_', '_', '6', '9', '2'], ['4', '_', '_', '_', '2', '6', '3', '_', '_'], ['_', '1', '_', '_', '9', '5', '2', '_', '_'], ['_', '5', '2', '_', '_', '_', '_', '_', '_']]
#arr = [['_', '_', '_', '_', '_', '1', '5', '_', '6'], ['_', '_', '5', '6', '_', '_', '_', '_', '_'], ['8', '_', '_', '_', '4', '_', '_', '_', '9'], ['_', '_', '8', '1', '_', '_', '7', '4', '_'], ['_', '_', '2', '_', '_', '_', '_', '_', '_'], ['_', '_', '4', '5', '8', '_', '_', '_', '1'], ['5', '_', '_', '8', '_', '9', '_', '3', '_'], ['7', '_', '_', '3', '_', '_', '_', '6', '_'], ['4', '_', '9', '_', '6', '2', '_', '1', '5']]


def get_box(n,x,p,q):
    #n is the across
    #x is the down
    i = (int(n)*3)
    j = (int(x)*3)
    use = []
    for b in range(i, i+3):
        for c in range(j, j+3):
            if b != p and c != q:
                use.append(arr[b][c])
    return(use)

for i in range(9):
    d = input("Enter row: ")
    d = d.replace("0","_")
    arr.append(list(d))
print(arr)
debug = False
darr = arr
NUM_NEWLY_ADDED = []
n = 0
def check():
    d = str(arr)
    return "_" in d

def boxes():
    jarr = []
    for i in range(3):
        for j in range(3):
            use = []
            use.append([arr[j*3][i*3], arr[j*3][i*3+1], arr[j*3][i*3+2]])
            use.append([arr[j*3+1][i*3], arr[j*3+1][i*3+1], arr[j*3+1][i*3+2]])
            use.append([arr[j*3+2][i*3], arr[j*3+2][i*3+1], arr[j*3+2][i*3+2]])
            jarr.append(use)
    return jarr;

box_reference = [[0,0], [3,0], [6,0], [0,3], [3,3], [6,3], [0,6], [3,6], [6,6]]
#[row_offset, col_offset]
def get_row(row_number):
    return arr[row_number]

def get_column(col_number):
    use = []
    for i in arr:
        use.append(i[col_number])
    return use


def dimensional_array_analysis(array_to_use):
    use = []
    for i in array_to_use:
        for j in i:
            use.append(j)
    return use

def box_check():
    box_added = 0
    for i in range(9):
        jarr = boxes()
        box = list(jarr[i])
        uses = {1:0, 2:0, 3:0, 4:0, 5:0,6:0,7:0,8:0,9:0}
        specific_offset = box_reference[i]
        box_1d = list(dimensional_array_analysis(box))
        for n in range(1,10):
            if str(n) not in box_1d:
                for row in range(3):
                    for col in range(3):
                        if box[row][col] == "_" or "*" in box[row][col]:
                            row_check = get_row(specific_offset[0]+row)
                            col_check = get_column(specific_offset[1]+col)
                            if str(n) not in row_check and str(n) not in col_check:
                                if box[row][col] == "_":
                                    box[row][col] = ""
                                box[row][col] += "*"+str(n)
                                uses[n] += 1
        for row in range(3):
            for col in range(3):
                el = box[row][col]
                if "*" in el:
                    print(row+specific_offset[0], el)

                    if len(el) == 2 and uses[int(el[1])] == 1:
                        print("AAAAA"+el[1])
                        if debug and el[1] == "3" and row+specific_offset[0] == 0 and col+specific_offset[1] == 2:
                            print()
                            for j in arr:
                                print(str(j))
                            print()
                            print(box)
                            sys.exit(0)
                        box[row][col] = el[1]
                        box_added += 1
                elif len(el) > 2:
                    different_els = el.split("*")[1:]
                    for l in different_els:
                        if uses[int(l)] == 1:
                            box_added += 1
                            box[row][col] = l
                            print("AAAAA"+j)
                            if debug and l == "3" and row+specific_offset[0] == 0 and col+specific_offset[1] == 2:
                                sys.exit(0)
        for row in range(3):
            for col in range(3):
                el = box[row][col]
                if "*" in el:
                    box[row][col] = "_"
                arr[specific_offset[0]+row][specific_offset[1]+col] = box[row][col]
    return box_added
                
        
"""
            
            if n_possible == 1:
                for row in range(3):
                    for digit in range(3):
                        if "*" in box[row][digit]:
                            box[row][digit] = str(n)
                            arr[specific_offset[0]+row][specific_offset[1]+digit] = str(n)
                            return
            for row in range(3):
                for col in range(3):
                    if "*" in box[row][col]:
                        box[row][col] == "_"
"""
def single_box_check(row, col, n):
    l = -1
    for i in range(len(box_reference)):
        if row >= box_reference[i][0] and box_reference[i][0]+2 >= row:
            if col >= box_reference[i][1] and box_reference[i][1]+2 >= col:
                l = i
                break
    jarr = boxes()
    box = jarr[l]
    box_1d = dimensional_array_analysis(box)
    return(str(n) in box_1d)


def row_check():
    row_added = 0
    for row in range(9):
        uses = {1:0, 2:0, 3:0, 4:0, 5:0,6:0,7:0,8:0,9:0}
        curr_row = list(arr[row])
        for n in range(1,10):
            if str(n) not in curr_row:
                for i in range(len(curr_row)):
                    if curr_row[i] == "_" or "*" in curr_row[i]:
                        col_checkk = get_column(i)
                        ssb = single_box_check(row, i, n)
                        if not ssb and str(n) not in col_checkk:
                            if curr_row[i] == "_":
                                curr_row[i] = ""
                            curr_row[i] += "*" + str(n)
                            uses[n] += 1
        for i in range(len(curr_row)):
            el = curr_row[i]
            if "*" in el:
                print(curr_row, row, el)
                if len(el) == 2 and uses[int(el[1])] == 1:
                    print("RRRRRRRRRRRR"+el[1])
                    if debug and el[1] == "3" and row == 0:
                        sys.exit(0)
                    row_added += 1
                    curr_row[i] = el[1]
                elif len(el) > 2:
                    different_els = el.split("*")[1:]
                    for j in different_els:
                        if uses[int(j)] == 1:
                            curr_row[i] = j
                            row_added += 1
                            print("RRRRRRRRRRRR"+j)
                            if debug and j == "3" and row == 0:
                                sys.exit(0)
        for i in range(len(curr_row)):
            el = curr_row[i]
            if "*" in el:
                curr_row[i] = "_"
        arr[row] = curr_row
    return row_added + col_check()


def col_check():
    col_added = 0
    for col in range(9):
        uses = {1:0, 2:0, 3:0, 4:0, 5:0,6:0,7:0,8:0,9:0}
        curr_col = list(get_column(col))
        for n in range(1,10):
            if str(n) not in curr_col:
                for i in range(len(curr_col)):
                    if curr_col[i] == "_" or "*" in curr_col[i]:
                        row_check = get_row(i)
                        ssb = single_box_check(i, col, n)
                        if not ssb and str(n) not in row_check:
                            if curr_col[i] == "_":
                                curr_col[i] = ""
                            curr_col[i] += "*" + str(n)
                            uses[n] += 1
        for i in range(len(curr_col)):
            el = curr_col[i]
            if "*" in el:
                print(curr_col, col, el)
                if len(el) == 2 and uses[int(el[1])] == 1:
                    print("CCCCCCCCC"+el[1])
                    if debug and el[1] == "3" and col == 2:
                        print(arr)
                        sys.exit(0)
                    col_added += 1
                    curr_col[i] = el[1]
                elif len(el) > 2:
                    different_els = el.split("*")[1:]
                    for j in different_els:
                        if uses[int(j)] == 1:
                            print("CCCCCCCCC"+j)
                            col_added += 1
                            curr_col[i] = j
                            if debug and j == "3" and col == 2:
                                sys.exit(0)
        for i in range(len(curr_col)):
            el = curr_col[i]
            if "*" in el:
                curr_col[i] = "_"
        
        for i in range(9):
            arr[i][col] = curr_col[i]
        
    return col_added + box_check()
    




def run():
    sum = row_check()
    NUM_NEWLY_ADDED.append(sum)

run()
run()
n = 1

while NUM_NEWLY_ADDED[n-1] > 0:
    print("AAAAAAAAAAAAAAAAAAAAAAAAAAA" + str(n))
    run()
    n+=1
    if n == 3000:
        break
for j in arr:
    print(str(j))
    print()
    print()
