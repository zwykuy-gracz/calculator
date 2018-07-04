"""
Simple calculator with 4 basic math operations such as: + - * /
"""

def calc(a,b,op):
    if op not in '+-*/':
        print("Don't know this '{}' operation".format(op))
        main()

    if op == '+':
        return a + b
    if op == '-':
        return a - b
    if op == '*':
        return a * b
    if op == '/':
        return a / b

def main():
    while True:
        try:
            a = int(input('Enter first number: '))
            operation = input('What kind of opration ? + - * / :')
            b = int(input('Enter second number: '))

            if operation == '/' and b == 0:
                print("can't devide by 0")
                continue

            break
        except:
            print('Enter an intiger')

    print(calc(a, b, operation))

if __name__ == '__main__':
    main()
