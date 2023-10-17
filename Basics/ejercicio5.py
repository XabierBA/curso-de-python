# ENUNCIADO
# Crea una función que defina una multiplicación con únicamente el operador de suma

def mult_sum(n1, n2):
    sum=0
    if(n1<0):

        if(n2>=0):
            for i in range(abs(n1)):
                sum+=n2
            sum = (f"-{sum}")
            return sum
        
        else:
            for i in range(abs(n1)):
                sum+=n2
            return abs(sum)
        
    else:
        for i in range(n1):
            sum+=n2
        return sum

print(mult_sum(4,4))
