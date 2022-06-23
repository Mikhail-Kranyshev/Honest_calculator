import operator


def is_one_digit(n):
    return -10 < n < 10 and n.is_integer()


def check(x, y, oper):
    msg = ""
    if is_one_digit(x) and is_one_digit(y):
        msg += msg_6
    if (x == 1 or y == 1) and oper == "*":
        msg += msg_7
    if (x == 0 or y == 0) and oper in "+-*":
        msg += msg_8
    if msg != "":
        msg = msg_9 + msg
    return msg



msg_0 = "Enter an equation\n"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

operation = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}

memory = 0
while True:
    x, oper, y = input(msg_0).split()
    if oper in operation:
        if x == 'M':
            x = memory
        if y == 'M':
            y = memory
        try:
            x = float(x)
            y = float(y)
            print(check(x, y, oper))
            result = operation[oper](x, y)
            print(result)
            if input(msg_4) == 'y':
                write = True
                if is_one_digit(result):
                    msg_index = 10
                    while msg_index <= 12:
                        if input(eval(f"msg_{msg_index}")) == 'y':
                            msg_index += 1
                        else:
                            write = False
                            break
                if write:
                    memory = result
            if input(msg_5) == 'n':
                break
        except ValueError:
            print(msg_1)
        except ZeroDivisionError:
            print(msg_3)
    else:
        print(msg_2)
