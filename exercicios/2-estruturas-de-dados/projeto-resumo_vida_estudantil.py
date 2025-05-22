# Nesse exercício coletaremos dados de uma estudante, armazenaremos em um dicionário e imprimiremos na tela esse dados em um formato amigável.

# 1. Solicite a estudante os seguintes dados: nome, ano que conheceu o LinkedIn, ano atual e os cursos realizados no LinkedIn Learning separados por virgula em ordem cronológica
estudante = {}
estudante['nome'] = input('Qual é o seu nome? ')
estudante['ano_lk'] = int(input('Em que ano conheceu o LinkedIn? '))
estudante['ano_atual'] = int(input('Qual é o ano atual? '))
cursos = input('Escreva quais cursos você ja realizou no linkedIn Learning, em ordem cronológica. (Separe os cursos por vírgula): ')
# 2. Armazene esses dados em um dicionário
estudante['cursos'] = cursos.split(', ')

# 3. Imprima na tela uma string com as informações de nome, ano_conheceu_linkedin, total de anos transcurridos, total de cursos realizados e (apenas) o primeiro e último curso.
total_cursos = len(estudante['cursos'])
print(f"Olá {estudante['nome']}, você conheceu o LinkedIn no ano {estudante['ano_lk']}, faz {estudante['ano_atual']- estudante['ano_lk']} anos. Neste tempo, você realizou {total_cursos} cursos, sendo o primeiro '{estudante['cursos'][0]}' e o último '{estudante['cursos'][-1]}'.")