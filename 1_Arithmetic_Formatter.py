def arithmetic_arranger(problems, show_answers=False):
    first_operand = ''
    second_operand = ''
    seperator = ''
    solution = ''
    
    if len(problems) > 5:
        return 'Error: Too many problems.'
    elif len(problems) < 1:
        return 'Error: Too less problems.'
    else:
        for problem in problems:
            if any(char.isalpha() for char in problem):
                return 'Error: Numbers must only contain digits.'
            if problem.find('+') < 0 and problem.find('-') < 0:
                return 'Error: Operator must be \'+\' or \'-\'.'
            else:
                if problem.find('+') > 0:
                    operands = problem.split(" + ")
                    operator = "+"
                    answer = int(operands[0]) + int(operands[1])
                else:
                    operands = problem.split(" - ")
                    operator = "-"
                    answer = int(operands[0]) - int(operands[1])

                max_length = max(len(operands[0]), len(operands[1]))

                if max_length > 4:
                    return 'Error: Numbers cannot be more than four digits.'
                
                first_operand += ((max_length - len(operands[0]) + 2) * " " + operands[0]) + 4 * " "
                second_operand += (operator + " " + (max_length - len(operands[1])) * " " + operands[1]) + 4 * " "
                seperator += ((max_length + 2) * "-") + 4 * " "
                solution += ((max_length - len(str(answer)) + 2) * " " + str(answer)) + 4 * " "

    if not show_answers:
        return f'{first_operand[:-4]}\n{second_operand[:-4]}\n{seperator[:-4]}'
    else:
        return f'{first_operand[:-4]}\n{second_operand[:-4]}\n{seperator[:-4]}\n{solution[:-4]}'

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 - 49", "196 - 234"], True)}')