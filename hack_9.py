"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""


def fn_hack_9(s):
    result = s
    xchar = 'k'
    xlist = list(result.keys()) # crea una lista con las clave
    xlast =xlist[len(xlist)-1]
    del  result[xlast]
    for OldKey in list(result):
        NewKey =OldKey[0:1].upper()+OldKey[1:]
        result[NewKey] = result.pop(OldKey)
        xvalor = result[NewKey]
        xvalor = xvalor.replace(xchar,'' )
        result[NewKey] = xvalor[0:1].upper()+ xvalor[1:]
    return result

print(fn_hack_9({"foo":"fookziman","bar":"barziman"}))