"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""


def fn_hack_5(s):
    result = s
    if len(result)>2:
        k = True
        salto = 3
        xchar = '-'
        xvcl = 'aeiou'
        while salto < len(result)+1:
            if k: # unica vez
                k = False
                ctrl = result[salto-1:salto]
                result = result[:salto-1]+ xchar + result[salto:] # remplazo
            else:
                if not ctrl in xvcl: # es consonante
                    ctrl = result[salto-1:salto] # control de insercion o remplazo    
                    result = result[:salto-1]+ xchar + result[salto:]  # remplazar
                else: # es vocal
                    ctrl = result[salto-1:salto] # control de insercion o remplazo    
                    result = result[:salto-1]+ xchar + result[salto-1:]  # insertar
            salto = salto + 3
    return result

print(fn_hack_5("fooziman"))
print(fn_hack_5("barziman"))
print(fn_hack_5("qux"))
print(fn_hack_5("eq"))