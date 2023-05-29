
salario = float(input("Digite o salário do funcionário: "))

if salario > 8250:
  taxa_aumento = 0.1  
else: 
  taxa_aumento = 0.15 

aumento = salario * taxa_aumento

novo_salario = salario + aumento

print("O valor do aumento é de R$ {:.2f}".format(aumento))
print("O novo salário é de R$ {:.2f}".format(novo_salario)) 