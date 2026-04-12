
# alocação de memória
teste1 = 0

teste2 = 0

prova = 0

nota_final = 0

rec = 0

nota_final_pos_rec = 0

# entrada de dados

teste1 = float(input("Informe a nota do teste 1: \n"))

teste2 = float(input("Informe a nota do teste 2: \n"))

prova = float(input("Informe a nota da prova: \n"))

# processamento de dados

nota_final = teste1*0.15 + teste2*0.15 + prova*0.70

if nota_final < 6:
    rec = float(input("Informe a nota da recuperação: \n"))
    nota_final_pos_rec = ((3*rec) + (2*nota_final))/5

# saída de dados

if nota_final_pos_rec == 0:
    print("Você foi aprovado")
elif nota_final_pos_rec > 6:
    print("Você foi aprovado")
else:
    print("Você foi reprovado")

