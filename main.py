idade = int(input("Digite a sua idade:\n"))
Total = float(input("Digite o valor total dos produtos:\n")) 

if(idade>=18):
    print("pode ter o desconto")
    desconto = total * 0.1
    final = total - desconto
    print(f"O desconto foi de R${desconto} e o total é de 
    R${final}")
else:
    print(f"Não tem dinheiro ao desconto e o seu valor final é de R${total}")