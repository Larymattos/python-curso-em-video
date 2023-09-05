#Operadores Aritmeticos:

#Em Python, você pode usar os seguintes operadores aritméticos para realizar várias operações matemáticas:

#Adição (+) : Usado para adicionar dois números. Exemplo:a + b

#Subtração (-) : Usado para subtrair o segundo número do primeiro. Exemplo:a - b

#Multiplicação (*) : Usado para multiplicar dois números. Exemplo:a * b

#Divisão (/) : Usado para dividir o primeiro número pelo segundo. O resultado é um número de ponto flutuante. Exemplo:a / b

#Divisão Inteira (//) : Realiza a divisão e arredonda o resultado para o número inteiro mais próximo (para baixo). Exemplo:a // b

#Módulo (%) : Retorna o resto da divisão entre o primeiro número e o segundo. Exemplo:a % b

#Potência ( ou pow())**: Calcula a potência do primeiro número elevado ao segundo. Exemplo: a ** boupow(a, b)

#Radiciação (sqrt()) : A função sqrt()da biblioteca 'math' usada para calcular a raiz quadrada de um número. Exemplo: 'import math' e 'math.sqrt(a)'.

#5 + 2 == 7
#5 * 2 == 10
#5 - 2 == 3
#5 / 2 == 2.5
#5 ** 2 == 25
#5 // 2 == 2
#5 % 2 == 1

#A ordem de precedência determinada como as operações são agrupadas e realizadas quando você tem uma expressão com vários operadores. Parênteses podem ser usados ​​para alterar a ordem de avaliação e controlar as prioridades. 

#Parênteses ( ) : Avaliação de expressões entre parênteses é realizada primeiro.
#Expoentes ( ** ou pow()) : Potenciação.
#Multiplicação ( *), Divisão ( /), Divisão Inteira ( //), Módulo ( %) : Essas operações são executadas da esquerda para a direita.
#Adição ( +), Subtração ( -) : Essas operações também são executadas da esquerda para a direita.

#resultado = 3 + 4 * 5 ==     # O resultado será 23, pois a multiplicação é feita antes da adição.
#resultado = (3 + 4) * 5 ==   # O resultado será 35, pois a adição é feita primeiro devido aos parênteses.
#resultado = 2 ** 3 + 1 ==    # O resultado será 9, pois a potenciação é feita antes da adição.
#resultado = 10 / 2 * 3 ==    # O resultado será 15.0, pois a divisão e a multiplicação têm a mesma prioridade e são avaliadas da esquerda para a direita.

#nome = input("Qual seu nome? ")
#print('Prazer em te conhecer: {:^20}!'.format(nome))

n1 = int(input("Digite um valor: "))
n2 = int(input("digite outro valor: "))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print("A soma é {}, a multiplicação é {}, e a divisão é {:.3f}".format(s, m, d))
print("Divisão inteira {} e potencia {}".format(di, e))

#Desafios:

#faça um programa que leia um numero inteiro e mostre na tela o seu sucessor e seu antecessor:

#crie um algoritmo que leia um numero e mostre o seu dobre, triplo e rais quadrada.

#desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a media.

#escreva um programa que leia um valor em metros e a exiba convertido em centimetros e milimetros.

#faça um programa que leia um numero inteiro qualquer e mostre na tela a sua tabuada.

#crie um programa que leia quanto dinheiro  uma pessoa temna carteira e mostre quantos dolares ea pode comprar:
    
#faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua area e a quantidade de tinta necessaria para pinta-la, sabendo que cada litro de tinta. pinta uma area de 2m².

#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto:

#faça um algoritmo que leia o salario de um funconario e mostre seu novo salario, com 15% de aumento.    