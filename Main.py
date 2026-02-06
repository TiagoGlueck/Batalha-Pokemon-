import Pokemon
import Player 
import Batalha

def validar_numero_positivo(mensagem, min_val=1):
    """Função auxiliar para validar números > 0"""
    while True:
        try:
            valor = int(input(mensagem))
            if valor >= min_val:
                return valor
            print(f"Valor deve ser maior ou igual a {min_val}!")
        except ValueError:
            print("Digite um número inteiro válido!")

if __name__ == "__main__":
    players = []
    
    # Criar 2 players
    for i in range(2):
        print(f"\n=== PLAYER {i+1} ===")
        nome = input("Nome do player: ").strip()
        if len(nome) < 2:
            nome = f"Player{i+1}"  # Nome padrão se inválido
        tamanho = validar_numero_positivo("Quantos pokémons na equipe? (1-6): ", 1)
        players.append(Player.Player(nome, tamanho))
    
    # Preencher equipes COM os novos métodos set_*()
    for player in players:
        print(f"\n--- Equipe de {player.nome} ---")
        for j in range(player.tamanho_equipe):
            print(f"\nPokémon {j+1}:")
            nome_poke = input("Nome: ").strip()
            
            # Cria Pokémon básico e usa os métodos interativos
            poke_temp = Pokemon.Pokemon(nome_poke, 1, 100, 50, 30)
            poke_temp.set_id()
            poke_temp.set_hp()
            poke_temp.set_ataque()
            poke_temp.set_defesa()
            
            player.adicionar_pokemon(poke_temp)
    
    # Mostrar todas as equipes
    print("\n"+"="*15)
    print("EQUIPES FINAIS")
    print("="*15)
    for player in players:
        player.exibir_equipe()
    
    print("\nPronto para batalha!")

    print("\nINICIAR BATALHA? ")
    if input("Digite SIM para batalhar: ").upper() == "SIM":
        Batalha.Batalha.batalhar(players[0], players[1])
    else:
        print("Batalha cancelada.")
