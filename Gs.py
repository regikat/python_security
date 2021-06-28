#Gerador de senhas
import random, string
tamanho = int(input('Digite o tamanho de senha que voce deseja'))

chars   = string.ascii_letters + string.digits + 'ç][{}!@#$%¨&*()-=+,.;:'
rnd     = random.SystemRandom()
#para cara i no range tamanho vai gerar novo caracter aleatorio.
#ate 16 caracteres.
print(''.join(rnd.choice(chars)for i in range(tamanho)))