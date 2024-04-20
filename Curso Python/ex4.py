# importar pacote do SO
import os;
# limpar a tela
os.system("cls");
salario = input("Digite o seu salário: ");
aumento = input("Digite a % do seu aumento: ");
salario = float(salario);
aumento = float(aumento);
novoSalario = salario + ( salario * aumento / 100 );
print(f"O Novo salário é de R$: {novoSalario:.2f}");

