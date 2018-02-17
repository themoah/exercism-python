def rotate(text, key):
    abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    #Letter-to-Integer
    L2I = dict(zip(abc,range(26)))
    #Integer-to-Letter
    I2L = dict(zip(range(26), abc))
    
    response = ""
    for c in text:
        if c.upper() in abc:
            is_up = c.istitle()
            position = L2I[ c.upper() ]
            new_letter = str(I2L[ (position + key)%26 ])
            if is_up:
                response += new_letter.upper()
            else:
                response += new_letter.lower()
        else:
            response += c

    return response
