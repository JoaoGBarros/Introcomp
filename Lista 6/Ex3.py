class Carro:

    def __init__(self, vm, consumo, capacidade, qtd):
        self.__vm = vm
        self.__consumo = consumo
        self.__capacidade = capacidade
        self.__qtd = qtd

    def set_vm(self, vm):
        self.__vm = vm

    def set_consumo(self, consumo):
        self.__consumo = consumo

    def set_capacidade(self, capacidade):
        self.__capacidade = capacidade

    def set_qtd(self):
        self.__qtd = self.__capacidade

    def get_vm(self):
        return self.__vm

    def get_consumo(self):
        return self.__consumo

    def get_capacidade(self):
        return self.__capacidade

    def get_qtd(self):
        return self.__qtd


    def Viajar(self, km):
        horas = km / self.__vm
        gasolina = km / self.__consumo
        self.__qtd = self.__qtd - gasolina
        print("O carro andou {:.2f} km em {:.2f} horas e gastou {:.2f} litros de combustivel. O carro agora possui "
              "{:.2f} litros de combustivel." .format(km, horas, gasolina, self.__qtd))

    def Abastecer(self, litros):
        maximo = self.__capacidade - self.__qtd
        if litros >= maximo:
            self.__qtd = self.__capacidade
        else:
            self.__qtd = self.__qtd + litros
        print("O carro foi abastecido com {:.2f} litros. O tanque agora esta com {:.2f} litros de combustivel."
              .format(litros, self.__qtd))

    def Completar(self):
        maximo = self.__capacidade - self.__qtd
        self.__qtd = self.__capacidade
        print("O carro foi abastecido com {:.2f} litros e esta com o tanque cheio!" .format(maximo))


def InformaCarro():
    c = Carro(0, 0, 0, 0)
    c.set_vm(float(input()))
    c.set_consumo(float(input()))
    c.set_capacidade(float(input()))
    c.set_qtd()
    return c


def Inicializacao():
    Wolk = InformaCarro()

    while True:
        op = input()

        if op == 'Viaja':
            km = float(input())
            Wolk.Viajar(km)

        elif op == 'Abastece':
            litros = float(input())
            Wolk.Abastecer(litros)

        elif op == 'Completa':
            Wolk.Completar()

        elif op == 'Encerra':
            break


Inicializacao()