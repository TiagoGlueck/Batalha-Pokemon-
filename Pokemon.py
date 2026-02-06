import random

class Pokemon:
    def __init__(self, nome, id, hp, ataque, defesa):
        self._nome = nome
        self._id = id  # Corrigido: consistente com _id
        self._hp = hp
        self._hp_max = hp
        self._ataque = ataque
        self._defesa = defesa
        self._vivo = True

    # Getters (somente leitura)
    @property
    def nome(self):
        return self._nome

    @property
    def id(self):
        return self._id

    @property
    def hp(self):
        return self._hp

    @property
    def ataque(self):
        return self._ataque

    @property
    def defesa(self):
        return self._defesa

    @property
    def vivo(self):
        return self._vivo

    # Métodos para setar atributos com validação interativa
    def set_id(self):
        while True:
            try:
                numero = int(input("Digite o ID do Pokémon (maior que 0): "))
                if numero > 0:
                    self._id = numero
                    print(f"ID definido como {numero}!")
                    break
                else:
                    print("ID inválido! Deve ser maior que 0.")
            except ValueError:
                print("Digite um número inteiro válido!")

    def set_hp(self):
        while True:
            try:
                life = int(input("Digite o HP do Pokémon (maior que 0): "))
                if life > 0:
                    self._hp = life
                    self._hp_max = life  # Atualiza max também
                    print(f"HP definido como {life}!")
                    break
                else:
                    print("HP inválido! Deve ser maior que 0.")
            except ValueError:
                print("Digite um número inteiro válido!")

    def set_ataque(self):
        while True:
            try:
                dano = int(input("Digite o Ataque do Pokémon (maior que 0): "))
                if dano > 0:
                    self._ataque = dano
                    print(f"Ataque definido como {dano}!")
                    break
                else:
                    print("Ataque inválido! Deve ser maior que 0.")
            except ValueError:
                print("Digite um número inteiro válido!")

    def set_defesa(self):
        while True:
            try:
                numero = int(input("Digite a Defesa do Pokémon (maior que 0): "))
                if numero > 0:
                    self._defesa = numero
                    print(f"Defesa definida como {numero}!")
                    break
                else:
                    print("Defesa inválida! Deve ser maior que 0.")
            except ValueError:
                print("Digite um número inteiro válido!")

    def receber_dano(self, dano):
        dano_real = max(1, dano - self._defesa)  # Mínimo 1 de dano
        self._hp -= dano_real
        if self._hp <= 0:
            self._hp = 0
            self._vivo = False
        return dano_real

    def atacar(self, alvo):
        # Dano com variação aleatória (80% a 120% do ataque)
        dano_base = self._ataque
        variacao = random.uniform(0.8, 1.2)
        dano = int(dano_base * variacao)
        # Chance de crítico (20% de chance, 2x dano)
        critico = random.random() < 0.2
        if critico:
            dano *= 2
        dano_causado = alvo.receber_dano(dano)
        return {
            'dano': dano_causado,
            'critico': critico,
            'alvo_derrotado': not alvo.vivo
        }

    def curar(self, quantidade):
        self._hp = min(self._hp + quantidade, self._hp_max)

    def esta_vivo(self):
        return self._vivo

    def resetar_hp(self):
        self._hp = self._hp_max
        self._vivo = True

    def __str__(self):
        barra_hp = "█" * int((self._hp / self._hp_max) * 10)
        return f"{self.nome} | HP: {self._hp}/{self._hp_max} [{barra_hp}]"
