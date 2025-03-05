"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""


def fn_hack_8(s):
    result = s
    result = result[::-1]
    for J in range(len(result)):
        if len(result)%2==0: result[J] = str(len(result)-J)
        else:   result[J] = result[J] + '-'  +str(len(result)-J)
    return result
print(fn_hack_8(["a","b","c","d","e"] ))
print(fn_hack_8(["a","b","c"] ))
print(fn_hack_8(["a","b","c","d"] ))
print(fn_hack_8(["a","b"] ))