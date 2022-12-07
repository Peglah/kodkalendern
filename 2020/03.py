# Beräkna 1*2*3*4, …., hela vägen upp till 100 (multiplicera alltså alla heltal mellan 1 och 100, inklusive 100)
# Beräkna också 2*4*6*8, …., hela vägen upp till 164 (multiplicera alltså vartannat heltal mellan 2 och 164, inklusive 164)
# Dividera de två talen och avrunda till närmaste heltal

def factorial(num):
    product = 1
    for i in range(1, num+1):
        product *= i
    return(product)
    
def factorial_evens(num):
    product = 1
    for i in range(2, num+1, 2):
        product *= i
    return(product)
    
print(round(factorial(100)/factorial_evens(164)))
