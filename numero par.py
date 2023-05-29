def verificar_par(numero):

 if numero % 2 == 0:
  return True
 else:
  return False
 
num=int(input("digite um número: "))
    
par = verificar_par(num)
print("Seu Numero é",num,":",par)