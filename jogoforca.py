import random

lista = ["casa","carro","gato","arvore","futebol","escola","amigo","lua","sol","fruta","vermelho","azul","livro","filme","praia","parque","floresta","passeio","pizza","musica","cidade",
    "computador","brincadeira","diversao","estudo","ferias","trabalho","televisao","janela","porta","telefone","sapato","relogio","oculos",
    "colher","garfo","facil","dificil","bolo","gelado","chocolate","banana"
]

palavra = random.choice(lista)
letras_usuario = []
ganhou = False
tentativas = 8

while True:
    
    for letra in palavra:
        if letra in letras_usuario:
            print(letra, end=' ')
        else:
            print('_', end=' ')

    tentativa_user = str(input('escreve uma letra para adivinhar: '))
    letras_usuario.append(tentativa_user)
    if tentativa_user not in palavra:
        tentativas -= 1
    
    ganhou = True
    for letra in palavra:
        if letra not in letras_usuario:
            ganhou = False


    if tentativas == 0 or ganhou:
        break
    
    
    


if ganhou:
    print('ganhaste')
else:
    print(f'Perdeste, a palavra era {palavra}')

