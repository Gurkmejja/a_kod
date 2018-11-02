"""
('FRA', 'Frankfurt Airport', 8.570556, 50.033333),
"""

filename = input("Please write filename: ")

def read_file(filene):
    """
    Reads file
    """
    with open(filene, 'rb') as fh:
        return str(fh.read()).split("\n")

output = read_file(filename)

l1 = output[0].split("\\n")

l2 = []

for item in l1:
    l2.append(str(item).strip("\\r'b"))


l3 = [] # Lista för flygplatsnamn
l3_1 = [] # lista för förkortningar

for item in l1:
    name = ""
    for l in item:
        if l == "r" or l == "b" or l == "-":
            if name[-1:].isalpha():
                name += l
        elif l.isalpha() or l == "-":
            name += l
        elif l == " ":
            if name[-1:].isalpha():
                name += l

    l3.append(name[4:-1])
    l3_1.append(name[0:3])

l3 = l3[0:11]
l3_1 = l3_1[0:11]






l_numbers = [] # lista för latituder
l_numbers2 = [] # lista för longituder

for item in l1:
    number = ""
    for l in item:
        if l == "-" or l == ".":
            if number[:] == "-":
                continue
            number += l
        elif l == "|":
            if number[-3:].isnumeric():
                number += l
        elif l.isnumeric():
            number += l


    num1 = number.split("|")

    l_numbers.append(num1[0])
    l_numbers2.append(num1[1:])


l_numbers = l_numbers[0:11]
l_numbers2 = l_numbers2[0:11]

l_numbers3 = []

for item in l_numbers2:
    for letter in item:
        l_numbers3.append(letter)



final_list = []

counter = 0
for items in l3:
    final_list.append((str(l3_1[counter]) + ", " + str(l3[counter])\
    + ", " + str(l_numbers[counter]) + ", " + str(l_numbers3[counter])))
    counter += 1


def write_to_f(filen):
    with open(filen, "a") as filehandle:
        for item in final_list:
            filehandle.write(str(item) + "\n")

write_to_f(filename)
print("Done")
