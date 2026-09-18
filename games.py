def show_games(games):
    print("=== Catalog of table games ===")
    for number, game in enumerate(games, start=1):
        print(f"{number}. {game['name']}")
        print(f"Genre: {game['genre']}")