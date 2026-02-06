class Player:
    def __init__(self, nome, tamanho_equipe):
        self._nome = nome
        self._tamanho_equipe = tamanho_equipe
        self._equipe = []
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, valor):
        if not valor or len(valor) < 2:
            raise ValueError("Nome do player inválido")
        self._nome = valor
    
    @property
    def tamanho_equipe(self):
        return self._tamanho_equipe
    
    @property
    def equipe(self):
        return self._equipe
    
    # Adicionar pokemon à equipe
    def adicionar_pokemon(self, pokemon):
        if len(self._equipe) >= self._tamanho_equipe:
            print(f"Equipe cheia! Limite: {self._tamanho_equipe}")
            return False
        self._equipe.append(pokemon)
        print(f"{pokemon.nome} adicionado à equipe!")
        return True
    
    # Remover pokemon da equipe
    def remover_pokemon(self, nome_pokemon):
        for i, pokemon in enumerate(self._equipe):
            if pokemon.nome.lower() == nome_pokemon.lower():
                removido = self._equipe.pop(i)
                print(f"{removido.nome} removido da equipe!")
                return True
        print(f"Pokemon {nome_pokemon} não encontrado!")
        return False
    
    # Exibir equipe completa
    def exibir_equipe(self):
        print(f"\n{'='*25}")
        print(f"Player: {self.nome}")
        print(f"Pokémons na equipe: {len(self._equipe)}/{self._tamanho_equipe}")
        print(f"{'='*25}")
        
        if not self._equipe:
            print("Equipe vazia!")
        else:
            for i, pokemon in enumerate(self._equipe, 1):
                print(f"\n{i}. {pokemon.nome} (ID: {pokemon.id})")
        print(f"{'='*25}\n")
    
    # Verificar se equipe está cheia
    def equipe_cheia(self):
        return len(self._equipe) >= self._tamanho_equipe
    
    # Buscar pokemon por nome
    def buscar_pokemon(self, nome):
        for pokemon in self._equipe:
            if pokemon.nome.lower() == nome.lower():
                return pokemon
        return None
    
    def __str__(self):
        return f"Player: {self.nome} | Equipe: {len(self._equipe)}/{self._tamanho_equipe}"
    