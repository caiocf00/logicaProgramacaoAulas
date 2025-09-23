'''class Personagem:
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
        personagem.vida -= 50
        print(f'{self.nome} deu uma notificação  {personagem.nome} e tirou 50 pontos de vida, e 5 horas do curso profissionalizante.')
        print(f'Agora esta com {personagem.vida} e com 2 faltas.')

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

class Cavaleiro(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)

    def atacar(self, personagem):
        personagem.vida -= 30
        print(f'{self.nome} jogou um raio no {personagem.nome} e tirou 30 pontos de vida.')
        print(f'Agora esta com {personagem.vida}')


andre = Cavaleiro('Pirobinhachoque', 100)
Soe = Personagem ('SOE' , 100)

Mago.atacar(Cavaleiro)
Cavaleiro.atacar(Personagem)'''

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
        personagem.vida -= 30
        print(f'{self.nome} jogou um raio em {personagem.nome} e tirou 30 pontos de vida.')
        print(f'Agora esta com {personagem.vida}')

class Mago(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)

    def curar(self, personagem):
        personagem.vida -= 999
        print(f'{self.nome} deu uma notificação e ligou para os pais de {personagem.nome} sendo fatality.')
        if personagem.vida <= 0:
            print("Morreu")
        else:
            print(f'A vida de {personagem.nome} agora e de {personagem.vida}')


class pekka(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)

    def desviar(self, personagem):
        personagem.vida += 30
        print(f'{self.nome} Desviou do ataque de {personagem.nome} e não tomou dano.')

andre= Personagem('Pirobas_choque' , 100)
Soe = Mago('Soe', 100)
pedro = pekka ('Pedro', 100)

andre.atacar(Soe)

pedro.desviar(andre)
Soe.curar(andre)