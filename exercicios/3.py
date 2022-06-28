def ler(nome):
    arquivo = open('pessoas.txt','r')

    for linha in arquivo:
        print(linha)

def salvar(nome,texto):
    arquivo = open(nome,'a')
    arquivo.write(texto)

salvar("pessoas.txt","Matheus 02")
ler("pessoas.txt")