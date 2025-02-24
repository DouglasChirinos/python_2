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
    xfilters =  {'a': '@', 'e': '3',  'i': '!', 'o': '0', 'u': 'v' }
    for xkey in xfilters.items():
        print(len(xkey[0]), len(xkey[1]))
        result = result.replace(xkey[0], xkey[1])
    return result

print(fn_hack_3('fooziman'))
