import operator
def parse(equation):
    '''Takes a string representing a math equation, returns lists of operators and numbers by
     order of occurrence'''

    operators = set('+-*/')
    op_out = []    #This holds the operators that are found in the string (left to right)
    num_out = []   #this holds the non-operators that are found in the string (left to right)
    buff = []
    for c in equation:  #examine 1 character at a time
        if c in operators:
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
