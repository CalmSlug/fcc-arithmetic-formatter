def arithmetic_arranger(problems, answers=False):
    str1 = ""
    str2 = ""
    str3 = ""
    str4 = ""
    err = False
    cnt = False


    # Testing the input for errors
    if len(problems) > 5:
        err = True
        arranged_problems = "Error: Too many problems."
    else:
        for prob in problems:
            data = prob.split()

            if len(data[0]) > 4 or len(data[2]) > 4:
                err = True
                arranged_problems = "Error: Numbers cannot be more than four digits."

            elif data[1] != "+" and data[1] != "-":
                err = True
                arranged_problems = "Error: Operator must be '+' or '-'."

            else:
                for num in data[0]:
                    if num not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
                        err = True
                        arranged_problems = "Error: Numbers must only contain digits."
                for num in data[2]:
                    if num not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
                        err = True
                        arranged_problems = "Error: Numbers must only contain digits."


    # Arranging the problems
    if err == False:
        for prob in problems:

            if cnt == False:
                cnt = True
            else:
                str1 += " " * 4
                str2 += " " * 4
                str3 += " " * 4
                str4 += " " * 4

            data = prob.split()
            length = max(len(data[0]), len(data[2])) + 2
            if data[1] == "+":
                result = str(int(data[0]) + int(data[2]))
            else:
                result = str(int(data[0]) - int(data[2]))

            str1 += " " * (length - len(data[0])) + data[0]
            str2 += data[1] + " " * (length - 1 - len(data[2])) + data[2]
            str3 += "-" * length
            str4 += " " * (length - len(result)) + result

        if answers == False:
            arranged_problems = str1 + "\n" + str2 + "\n" + str3
        else:
            arranged_problems = str1 + "\n" + str2 + "\n" + str3 + "\n" + str4

    return arranged_problems


# Output showcase
print(arithmetic_arranger(['3801 - 2', '123 + 49']), "\n")
print(arithmetic_arranger(['1 + 2', '1 - 9380']), "\n")
print(arithmetic_arranger(['3 + 855', '3801 - 2', '45 + 43', '123 + 49']), "\n")
print(arithmetic_arranger(['11 + 4', '3801 - 2999', '1 + 2', '123 + 49', '1 - 9380']), "\n")
print(arithmetic_arranger(['44 + 815', '909 - 2', '45 + 43', '123 + 49', '888 + 40', '653 + 87']), "\n")
print(arithmetic_arranger(['3 / 855', '3801 - 2', '45 + 43', '123 + 49']), "\n")
print(arithmetic_arranger(['24 + 85215', '3801 - 2', '45 + 43', '123 + 49']), "\n")
print(arithmetic_arranger(['98 + 3g5', '3801 - 2', '45 + 43', '123 + 49']), "\n")
print(arithmetic_arranger(['3 + 855', '988 + 40'], True), "\n")
print(arithmetic_arranger(['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40'], True), "\n")