import os;
os.system("cls");
print("------------------------- Programa Calcular Media -----------------------------");
def calcularMedia():
    disciplina = input("Produto: ");
    nota1 = float(input("Nota do 1 Bimestre: "));
    nota2 = float(input("Nota do 2 Bimestre: "));
    media = (nota1 + nota2 ) / 2;
    if (media >= 7):
       print(f"Sua media é de{media:.1f}e voce foi APROVADO na disciplina de {disciplina}");
    else:
       print(f"Sua media é de{media:.1f}e voce foi REPROVADO na disciplina de {disciplina}");
    print("----------------------------------------")
    resposta = input("Você deseja sair[S + Enter] ou continuar [Qualquer Tecla + Enter]?");
    if (resposta == "S"):
        print("Tchauzinho fofinho(a)");
    else:
     calcularMedia();
calcularMedia();
 