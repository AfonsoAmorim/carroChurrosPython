class CarroChurros():
    def __init__(self,nomeCarro,dataFabricacao,kmGasolina):
        self.nomeCarro=nomeCarro
        self.datafabricacao=dataFabricacao
        self.kmgasolina=kmGasolina
    def info(self):
        print("O nome do carro é: " + self.nomeCarro)
        print("A data de fabricação é: " + str(self.datafabricacao))
        print("Quantos km's faz com 1 litro: " + str(self.kmgasolina) + "km")
    def fazerChurros(self):
        tipoDeChurros = input("Insira o seu churros desejado: ")
        print("O churros é de: " + str(tipoDeChurros))
        if(tipoDeChurros == "chocolate"):
            print("O valor é R$ 2.50")
        elif(tipoDeChurros == "caramelo"):
            print("O valor é de R$ 5.00")
        else:
            print("Não possuímos esse churros no momento!")
    def custoTrajetoHoje(self):
        entrada = self.kmgasolina 
        kmTrajetoHoje = input("Digite quantos km's percorreu hoje: ")
        calculo = int(kmTrajetoHoje)/int(entrada)
        print("Foram utilizados {} litros de gasolina para o trajeto de hoje.".format(round(calculo)))
    
