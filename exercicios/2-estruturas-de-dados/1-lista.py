# Crie uma lista apenas com elementos numéricos
numerico = [1,2,3,4,5]
# Crie uma lista contendo todos os tipos e estrutura de dados que você aprendeu até agora
mista = ['python', '2', '5', '10', 'javascript', 'miguel', '20']
# Imprima na tela apenas os 5 primeiros elementos da lista
print(mista[0:6])
# Crie um slice na lista para que imprima na tela os elementos de índice par
print(mista[0:6:2])
print(mista[-1])
# Remova da lista o último item
mista.pop()
print(mista)
# Insira na lista um novo item
mista.append('30')
print(mista)
# Remova da lista um item específico
mista.remove('python')
print(mista)