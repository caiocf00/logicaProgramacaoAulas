'''# atributos -  caracteristicas do objeto

# metodos - que são ações desse objeto

# nome e vida - e como vai atacar
# self = quando quero acessar me referir a algum atributo da classe
# construtor = quando quero criar um novo objeto, chamo o construtor para acessar os atributos

class Personagem:
    # construtor 
    def __init__(self, nome, vida):
        # encapsulalamento = o '__' para deixar privado
        self.__nome = nome 
        self.__vida = vida

# para acessar os atributos já que eles estão privados

        # definindo GET para chamar o nome (ler)
    @property
    def nome(self):
        return self.__nome
        
        # definindo SET para mudar o nome do personagem
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @ property
    def vida(self):
        return self.__vida
        
    @vida.setter
    def vida(self, vida):
        self.__vida = vida

    def atacar(self, personagem):
        personagem.vida -= 20
        print(f'{self.nome} atacou {personagem.nome} e tirou 20 pontos de vida.')
        print(f'Agora esta com {personagem.vida}')
            



personagem1 = Personagem('Gandof', 100)
personagem2 = Personagem('Legolas', 100)

personagem1.atacar(personagem2)
personagem2.atacar(personagem1)

class Guerreiro:
    ...'''

# atributos -  caracteristicas do objeto

# metodos - que são ações desse objeto

# nome e vida - e como vai atacar
# self = quando quero acessar me referir a algum atributo da classe
# construtor = quando quero criar um novo objeto, chamo o construtor para acessar os atributos

class Personagem:
    # construtor 
    def __init__(self, nome, vida):
        # encapsulalamento = o '__' para deixar privado
        self.__nome = nome 
        self.__vida = vida

# para acessar os atributos já que eles estão privados

        # definindo GET para chamar o nome (ler)
    @property
    def nome(self):
        return self.__nome
        
        # definindo SET para mudar o nome do personagem
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @ property
    def vida(self):
        return self.__vida
        
    @vida.setter
    def vida(self, vida):
        self.__vida = vida

    def atacar(self, personagem):
        personagem.vida -= 20
        print(f'{self.nome} atacou {personagem.nome} e tirou 20 pontos de vida.')
        print(f'Agora esta com {personagem.vida}')
            

class Guerreiro(Personagem):
    def __init__(self, nome, vida, escudo=False):
        super().__init__(nome, vida)
        self.__escudo = escudo

    @property
    def escudo(self):
        return self.__escudo
    
    @escudo.setter 
    def escudo(self, escudo):
        self.__escudo = escudo
    
    def atacar(self, personagem):
        personagem.vida -=40
        print(f'{self.nome} atacou {personagem.nome} .')
        print(f'Agora esta com {personagem.vida}')

    
    def protecao(self, personagem):
        self.__vida +=10

class Mago(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)

    def curar(self, personagem):
        personagem.vida += 15
        print(f'{self.__nome} usou poder de cura em {personagem.nome}')
        print(f'A vida de {personagem.nome} agora e de {personagem.vida}')

frodo = Personagem('Frodo', 100)
gandof = Mago('Gandof', 100)
aragorn = Guerreiro('Aragorn', 100)















