def decode(args):
    """ go away pylint """
    if args == '':
        return ''
    response = ''
    t1 = ''
    for i in args:
        if i.isdigit():
            t1 += i
        else:
            if t1 == '':
                response += i
            else:
                t2 = int(t1)
                t3 = t2 * i
                response += t3
                t1 = ''
    return response


def encode(args):
    """ go away pylint """
    if args == '':
        return ''
    response = ''
    lastChar = args[0]
    lastCharCounter = 1
    index = 0
    for i in args:
        if index == 0:
            index += 1
            continue
        if i == lastChar:
            lastCharCounter += 1
        else:
            if not lastCharCounter == 1:
                response += str(lastCharCounter)
            response += lastChar
            lastCharCounter = 1
            lastChar = i

    if not lastCharCounter == 1:
        response += str(lastCharCounter)
    response += lastChar
    return response