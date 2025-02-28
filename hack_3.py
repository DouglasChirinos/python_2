"""
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
"""


def fn_hack_3(s):
    result = s
    xfilters =  {'a': '@', 'e': '3',  'i': '¡', 'o': '0', 'u': 'v' }
    vlist = list(xfilters.keys())
    #print(vlist)
    for x in range(len(result)):
        # print(result[x])
        if not result[x] in vlist:
            if x==0 or x==len(result)-1: result = result[:x] + result[x].upper() + result[x+1:]
        else: result = result.replace(result[x], xfilters[result[x]])
    return result

print(fn_hack_3('fooziman'))
print(fn_hack_3('barziman'))
print(fn_hack_3('3q'))
print(fn_hack_3('qu'))
print(fn_hack_3('qux'))