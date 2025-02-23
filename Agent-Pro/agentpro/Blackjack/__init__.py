from agentpro.Blackjack.play_blackjack_game import play

if __name__ == "__main__":
    number_of_game = 2
    model = 'gpt-3.5'
    game_style = 'agentpro'
    storage_name = "../data/gpt-3.5/game_1.json"

    play(number_of_game,model,game_style,storage_name)
