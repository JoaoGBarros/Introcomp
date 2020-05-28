import random


class Ataque:

    def __init__(self, move, dano, energia):
        self.__move = move
        self.__dano = dano
        self.__energia = energia

    def set_move(self, move):
        self.__move = move

    def set_dano(self, dano):
        self.__dano = dano

    def set_energia(self, energia):
        self.__energia = energia

    def get_move(self):
        return self.__move

    def get_dano(self):
        return self.__dano

    def get_energia(self):
        return self.__energia


class Pokemon:

    def __init__(self, nome, vida, stamina):
        self.__nome = nome
        self.__vida = vida
        self.__stamina = stamina
        self.__atq1 = Ataque(0, 0, 0)
        self.__atq2 = Ataque(0, 0, 0)

    def set_nome(self, nome):
        self.__nome = nome

    def set_vida(self, vida):
        self.__vida = vida

    def set_stamina(self, stamina):
        self.__stamina = stamina

    def set_atq1(self, move, dano, energia):
        self.__atq1.set_move(move)
        self.__atq1.set_dano(dano)
        self.__atq1.set_energia(energia)

    def set_atq2(self, move, dano, energia):
        self.__atq2.set_move(move)
        self.__atq2.set_dano(dano)
        self.__atq2.set_energia(energia)

    def get_nome(self):
        return self.__nome

    def get_vida(self):
        return self.__vida

    def get_stamina(self):
        return self.__stamina

    def get_atq1_move(self):
        return self.__atq1.get_move()

    def get_atq1_dano(self):
        return self.__atq1.get_dano()

    def get_atq1_energia(self):
        return self.__atq1.get_energia()

    def get_atq2_move(self):
        return self.__atq2.get_move()

    def get_atq2_dano(self):
        return self.__atq2.get_dano()

    def get_atq2_energia(self):
        return self.__atq2.get_energia()

    def Comabte(self, movimento, play2):
        life = play2.get_vida()

        if movimento < 0.5:
            if self.__stamina >= self.__atq1.get_energia():
                life = life - self.__atq1.get_dano()
                self.__stamina = self.__stamina - self.__atq1.get_energia()
                print(f"{self.__nome} usa {self.__atq1.get_move()}.\n")
            else:
                if self.__stamina >= self.__atq2.get_energia():
                    life = life - self.__atq2.get_dano()
                    self.__stamina = self.__stamina - self.__atq2.get_energia()
                    print(f"{self.__nome} usa {self.__atq2.get_move()}.\n")
                else:
                    print(f"{self.get_nome()} nao pode fazer nada!\n")
                    return life
        else:
            if self.__stamina >= self.__atq2.get_energia():
                life = life - self.__atq2.get_dano()
                self.__stamina = self.__stamina - self.__atq2.get_energia()
                print(f"{self.__nome} usa {self.__atq2.get_move()}.\n")

            else:
                if self.__stamina >= self.__atq1.get_energia():
                    life = life - self.__atq1.get_dano()
                    self.__stamina = self.__stamina - self.__atq1.get_energia()
                    print(f"{self.__nome} usa {self.__atq1.get_move()}.\n")
                else:
                    print(f"{self.get_nome()} nao pode fazer nada!\n")
                    return life

        return life

    def RestauraEnergia(self):
        self.__stamina = self.__stamina + 20


def ChecaDerrota(play1, play2):
    vida1 = play1.get_vida()
    vida2 = play2.get_vida()

    if vida1 <= 0:
        play1.set_vida(0)
        return True
    elif vida2 <= 0:
        play2.set_vida(0)
        return True
    else:
        return False

def InformaPokemon():
    pk = Pokemon(0, 0, 0)
    atributos = input()
    nome, vida, stamina = atributos.split()
    vida = int(vida)
    stamina = int(stamina)
    pk.set_nome(nome)
    pk.set_vida(vida)
    pk.set_stamina(stamina)
    ataques = input()
    move1, dano1, energia1, move2, dano2, energia2 = ataques.split()
    pk.set_atq1(move1, int(dano1), int(energia1))
    pk.set_atq2(move2, int(dano2), int(energia2))
    return pk


def Vencedor(play1):
    print("O vencedor foi " + play1.get_nome() + "!!!")


def Turno(pkm1, pkm2):
    print(pkm1.get_nome() + ":")
    print("{:.2f} de vida".format(pkm1.get_vida()))
    print("{:.2f} de energia\n".format(pkm1.get_stamina()))
    print(pkm2.get_nome() + ":")
    print("{:.2f} de vida".format(pkm2.get_vida()))
    print("{:.2f} de energia\n".format(pkm2.get_stamina()))


def Inicializacao():
    turnos = 0
    pkm1 = InformaPokemon()
    pkm2 = InformaPokemon()
    random.seed("pokemon")
    a = random.randint(0, 1)

    if a <= 0.5:
        jogador1 = pkm1
        jogador2 = pkm2
    else:
        jogador1 = pkm2
        jogador2 = pkm1

    while True:

        if turnos % 2 == 0:
            play1 = jogador1
            play2 = jogador2
        else:
            play1 = jogador2
            play2 = jogador1

        movimento = random.randint(0, 1)
        play2.set_vida(play1.Comabte(movimento, play2))
        play1.RestauraEnergia()
        if ChecaDerrota(play1, play2):
            Turno(pkm1, pkm2)
            Vencedor(play1)
            break
        Turno(pkm1, pkm2)
        turnos += 1


Inicializacao()
