def fibonacci(numero):
    a , b = 0 , 1

    if numero == 0 or numero == 1:
     
     return True
    
    while ( b < numero):
       a, b = b, a + b

    return b == numero

numeroInformado = int(input("Informe um número: "))

if fibonacci(numeroInformado):
    print(f"O número {numeroInformado} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numeroInformado} NÃO pertence à sequência de Fibonacci.")    


