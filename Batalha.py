class Batalha:
    @staticmethod
    def batalhar(player1, player2):
        print("\n" + "🔥" * 20)
        print("     BATALHA POKÉMON INICIADA!")
        print("🔥" * 20)
        
        idx1, idx2 = 0, 0
        pokemon1 = player1.equipe[idx1]
        pokemon2 = player2.equipe[idx2]
        
        while pokemon1.esta_vivo() and pokemon2.esta_vivo():
            print(f"\n--- TURNO {idx1 + idx2 + 1} ---")
            print(f"{player1.nome}: {pokemon1}")
            print(f"{player2.nome}: {pokemon2}")
            
            input(f"\nPressione ENTER para {player1.nome} atacar...")
            resultado = pokemon1.atacar(pokemon2)
            print(f"💥 {pokemon1.nome} causou {resultado['dano']} dano!")
            
            if not pokemon2.esta_vivo():
                idx2 += 1
                if idx2 >= len(player2.equipe):
                    break
                pokemon2 = player2.equipe[idx2]
            
            if pokemon2.esta_vivo():
                input(f"Pressione ENTER para {player2.nome} atacar...")
                resultado = pokemon2.atacar(pokemon1)
                print(f"💥 {pokemon2.nome} causou {resultado['dano']} dano!")
                
                if not pokemon1.esta_vivo():
                    idx1 += 1
                    if idx1 >= len(player1.equipe):
                        break
                    pokemon1 = player1.equipe[idx1]
        
        print("\n" + "🏆" * 10)
        if idx1 >= len(player1.equipe):
            print(f"🎉 {player2.nome} VENCEU!")
        else:
            print(f"🎉 {player1.nome} VENCEU!")
        print("🏆" * 10)
