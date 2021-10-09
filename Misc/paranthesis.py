# Given a number n, generate all possible paranthesis combinations of () paranthesis possible
# n=3 --> ()()(), (())(), ()(()),(()()) ((()))

def generate_possible_paranthesis_strings(n: int):

    prev_list = ['(']
    new_list = ['(']
    for i in range(1, 2*n+1):
        prev_list = new_list
        new_list = []
        for l in prev_list:
            o = 0
            c = 0
            for s in l:
                if s=='(':
                    o+=1
                else:
                    c+=1
            if o < n:
                new_list.append(l+"(")
            if o > c:
                new_list.append(l+")")
    return prev_list
            

if __name__=='__main__':
    n = 4
    possibilities = generate_possible_paranthesis_strings(n)
    for p in possibilities:
        print(p)