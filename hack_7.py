"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [0] output => [0] 
"""


def fn_hack_7(s):
    result = s
    for k in range(len(result)):
        if  type(result[k]) == str: 
            if ((k+1) % 2 == 0):
                result[k]  =  (k+1)
            else:
                result[k]  = str(k+1)
        elif type(result[k]) == int:
             result[k]  =  k
       
    return result

print(fn_hack_7(["a","b","c","d","e"]))
print(fn_hack_7([0]))