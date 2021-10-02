import operator

operators = set('+-*/')

def is_char_operator(c,idx,equation):
    if c in operators:
        if c == '-':
            # if the operator is - we need to make sure its indeed an operator and not a minus valie;
            if idx == 0 or equation[idx - 1] in operators:
                return False
        return True
    return False


def parse(equation):
    '''Takes a string representing a math equation, returns lists of operators and numbers by
     order of occurrence'''

    op_out = []    #This holds the operators that are found in the string (left to right)
    num_out = []   #this holds the non-operators that are found in the string (left to right)
    buff = []
    for idx,c in enumerate(equation):  #examine 1 character at a time
        if is_char_operator(c,idx, equation):
            #found an operator.  Everything we've accumulated in `buff` is
            #a single "number". Join it together and put it in `num_out`.
            num_out.append(float(''.join(buff)))
            buff = []
            op_out.append(c)
        else:
            #not an operator.  Just accumulate this character in buff.
            buff.append(c)
    num_out.append(float(''.join(buff)))
    return num_out,op_out


op_dict = {'*':operator.mul,
           '/':operator.truediv,
           '+':operator.add,
           '-':operator.sub}

def no_precedence_eval(nums,ops):
    result = nums[0]
    next_num = 1
    for op in ops:
        values=[result,nums[next_num]]
        result = op_dict[op](*values)
        next_num+=1
    return (result)
