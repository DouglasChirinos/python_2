"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""


def fn_hack_10(s):
    result = s
    cont=0
    for J in range(len(result)):
        if type(result[J])==dict:
            OldKey =  list(result[J].keys())
            for M in OldKey:
                cont = cont+1
                S = str(cont)
                result[J][S] = result[J].pop(M)
                cont = cont + 1
                result[J][S] = str(cont)
        if type(result[J])==set:
            Pset = list(result[J])
            for Z in range(len(Pset)):
                cont=cont+1
                Pset[Z]= str(cont)
            result[J] = set(sorted(Pset))
    return result

print(fn_hack_10([{"a":"b"},{"c","d"},{"e":"f"}] ))
