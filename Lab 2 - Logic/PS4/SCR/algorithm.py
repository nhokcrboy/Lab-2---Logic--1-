
def read_input(input_path: str) -> (list,str):
    KB = []
    alpha = ""
    with open(input_path) as file:
        alpha = file.readline()
        # bo ky tu xuong dong
        alpha = alpha[:-1]
        n = int(file.readline())

        for i in range(n):
            line = file.readline()
            if (line[-1] == '\n'):
                line = line[:-1]
            literals = line.split(' OR ')
            KB.append(tuple(literals))

    return KB,alpha            

def write_output(output_path: str,info: list,res: bool):
    with open(output_path,'w') as file:
        for item in info:
            file.write(str(len(item)) + '\n')
            for literals in item:
                outstr = ""
                if (len(literals) == 0):
                    outstr = "{}"
                elif (len(literals) == 1):
                    outstr += str(literals[0])
                else:
                    for literal in literals[:-1]:
                        outstr = outstr + literal + " OR "
                    outstr += literals[-1]

                file.write(outstr + '\n')
        
        if (res):
            file.write("YES")
        else: file.write("NO")

def get_uni_ele_from_a_list(l1: list,l2: list) -> list:
    res = []
    for i in l1:
        if  i not in l2:
            res.append(i)
    return res 

def get_negative_literal(literal: str) -> str:
    if (literal[0] == '-'): return literal[1:]
    else: return "-" + literal

def get_negative_literal_long(literal:str) -> list:
    literals = literal.split(' OR ')
    for i in range(len(literals)):
        literals[i] = get_negative_literal(literals[i])
    return literals

def get_literal_alpha(literal: str) -> str:
    if (literal[0] == '-'):
        return literal[1]
    else:
        return literal[0]

# 0: bang nhau
# 1: literal 1 lon hon 
# 2: literal 2 lon hon    
def compare_literal(l1:str, l2:str) -> int:
    if (get_literal_alpha(l1) > get_literal_alpha(l2)):
        return 1
    elif (get_literal_alpha(l1) < get_literal_alpha(l2)):
        return 2
    else:
        if (l1[0] == '-' and l2[0] != '-'):
            return 2
        elif (l1[0] != '-' and l2[0] == '-'):
            return 1
        else:
            return 0

def PL_RESOLVE(clause1: list,clause2: list) -> list:
    resolvents = []

    # de su dung ham union ghep 2 menh de nay lai voi nhau 
    # ta se chuyen doi 2 list tu input thanh set
    c1 = set(clause1)
    c2 = set(clause2)


    for i in c1:
        if get_negative_literal(i) in c2:
            new_clause = c1.union(c2) - {i,get_negative_literal(i)}
            
            # kiem tra xem co menh de co dang literal V True khong
            check = True
            
            for literal in new_clause:
                if get_negative_literal(literal) in new_clause:
                    check = False
                    break
            
            if(check): 
                # sap xep cac literal theo thu tu ban chu cai
                new_clause = list(new_clause)
                if '-' in new_clause:
                    print(c1)
                    print(c2)
                for i in range(len(new_clause)):
                    for j in range(i+1,len(new_clause)):
                        if compare_literal(new_clause[i],new_clause[j]) == 1:
                            new_clause[i],new_clause[j] = new_clause[j],new_clause[i]
                            
                resolvents.append(tuple(new_clause))


    return resolvents
            

def PL_RESOLUTION(KB: list,alpha: str) -> (bool,list):
    if (len(alpha) <= 2):
        alpha = get_negative_literal(alpha)
        clause = KB + [(alpha,)]
    else:
        alpha = get_negative_literal_long(alpha)
        for items in alpha:
            KB += [(items,)]
        clause = KB

    new = set()

    running_list = []
    
    while 1:
        n = len(clause)

        for i in range(n):
            for j in range(i+1,n):
                resolvent = PL_RESOLVE(clause[i],clause[j])
                new.update(resolvent)
        
        new_ele = get_uni_ele_from_a_list(new,clause)
        
        running_list.append(new_ele)

        if(len(new_ele) == 0):
            return False,running_list

        if (() in new):
            return True,running_list

        clause.extend(new)


