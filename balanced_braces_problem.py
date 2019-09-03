def are_brackets_balanced(input_str):
    op_braces=tuple('({[')
    clos_braces=tuple(')}]')
    comb=dict(zip(op_braces,clos_braces))
    #print(comb)
    lt=list()
    for i in input_str:
        if i in op_braces:
            lt.append(comb[i])
        elif i in clos_braces:
            if not lt:
                return False
            if lt[-1]==i:
                lt.pop()
            else:
                return False
    return not lt


def main():
    input_str = '(4*x+y)]'
    test_result = are_brackets_balanced(input_str)
    message = 'Given equation {0}, the test for balanced brackets returns {1}\n'.format(
    input_str, test_result)
    print(message)


if __name__ == '__main__':
  main()
