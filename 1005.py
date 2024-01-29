#O arquivo de entrada contém 2 valores com uma casa decimal cada um.
#Saída
#
#Imprima a mensagem "MEDIA" e a média do aluno conforme exemplo abaixo, com 5 dígitos após o ponto decimal e com um espaço em branco antes e depois da igualdade. Utilize variáveis de dupla precisão (double) e como todos os problemas, não esqueça de imprimir o fim de linha após o resultado, caso contrário, você receberá "Presentation Error".
#Exemplos de Entrada 	Exemplos de Saída
#
#       5.0              MEDIA = 6.43182
#       7.1
#
#       0.0              MEDIA = 4.84091
#       7.1
#	
#       10.0             MEDIA = 10.00000
#       10.0
#	
# 

A = round(float(input()), 1)
B = round(float(input()), 1)
media = (A*3.5 + B*7.5) / 11
print(f'MEDIA = {media:.5f}')