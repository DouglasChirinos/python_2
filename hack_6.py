"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""


def fn_hack_6(s):
    result = s
    if len(result) == 0:
        result =["0"]
    else:
        for k in range(len(result)):
            if k % 2 != 0: xchar = "-"
            else: xchar = str(k+1)     
            result[k] = xchar
    return result

print(fn_hack_6(["a","b","c","d","e"]))
print(fn_hack_6([]))
