import csv
from datetime import datetime
from os import path
from collections import Counter

GAME_ID_INDEX = 0
GAME_NAME_INDEX = 1
CATEGORY_INDEX = 2
MIN_PLAYER_INDEX = 3
MAX_PLAYER_INDEX = 4
PLAY_TIME_INDEX = 5
PUBLISHED_YEAR_INDEX = 6

SESSION_ID_INDEX = 0
SESSION_GAME_ID_INDEX = 1
SESSION_GAME_NAME_INDEX = 2
DATE_PLAYED_INDEX = 3
PLAYERS_INDEX = 4
WINNER_INDEX = 5
DURATION_INDEX = 6

menu_options = [
    "View Collection",
    "Game Play Count",
    "Most recent Play",
    "Most Played Game",
    "Game Stats",
    "Add New Game",
    "Player Rankings",
    "Player Win Count",
    "Log New Session",
    "Exit"
]

def load_collection(csv_file):
    dic = {}
    with open(path.join(path.dirname(__file__), csv_file), "rt") as f:
        reader = csv.reader(f)
        next(reader)
        for line in reader:
            dic[line[GAME_ID_INDEX]] = {
                "id": line[GAME_ID_INDEX],
                "game_name": line[GAME_NAME_INDEX],
                "category": line[CATEGORY_INDEX],
                "min_player": line[MIN_PLAYER_INDEX],
                "max_player": line[MAX_PLAYER_INDEX],
                "play_time": line[PLAY_TIME_INDEX],
                "published_year": line[PUBLISHED_YEAR_INDEX]
            }
    return dic

def load_sessions(csv_file):
    dic = {}
    with open(path.join(path.dirname(__file__), csv_file), "rt") as f:
        reader = csv.reader(f)
        next(reader)
        for line in reader:
            dic[line[SESSION_ID_INDEX]] = {
                "id": line[SESSION_ID_INDEX],
                "game_id": line[SESSION_GAME_ID_INDEX],
                "game_name": line[SESSION_GAME_NAME_INDEX],
                "date_played": datetime.strptime(line[DATE_PLAYED_INDEX], "%Y-%m-%d"),
                "players": line[PLAYERS_INDEX].split(";"),
                "winner": line[WINNER_INDEX],
                "duration": line[DURATION_INDEX]
            }
    return dic

def get_last_id(file_name):
    with open(path.join(path.dirname(__file__), file_name), newline='') as f:
        reader = csv.DictReader(f)
        last_id = 0
        for row in reader:
            last_id = int(row["id"])
    return last_id

def add_game(file_name, game_name, category, min_players, max_players, play_time, year_published):
    next_id = get_last_id(file_name) + 1
    with open(path.join(path.abspath(path.dirname(__file__)), file_name), "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([next_id, game_name, category, min_players, max_players, play_time, year_published])

def sort_collection_by_name(collection):
    sorted_collection = dict(sorted(collection.items(), key=lambda item: item[1]["game_name"]))
    return sorted_collection

def display_collection(collection) :
    sorted_collection = sort_collection_by_name(collection)
    for _, game in sorted_collection.items():
        print(f"{game["game_name"]}, Category: {game["category"]}, Players: {game["min_player"]}~{game["max_player"]}, Play Time: {game["play_time"]}, Published: {game["published_year"]}")

def get_play_count(game_name, sessions):
    count = 0

    for _, game in sessions.items():
        if game["game_name"].lower() == game_name.lower():
            count += 1
    return count

def game_in_collection(game_name, collection):
    for _, game in collection.items():
        if game["game_name"].lower() == game_name.lower():
            return True
    return False 

def get_last_played(game_name, sessions):
    latest_date = datetime.min
    for session in sessions.values():
        if session["game_name"].lower() == game_name.lower():
            if session["date_played"] > latest_date:
                latest_date = session["date_played"]
    return latest_date

def get_most_played(sessions):
    session_counts = {}
    most_sessions = {"game_name": "", "count": 0}

    for session in sessions.values():
        if session_counts.get(session["game_name"]):
            session_counts[session["game_name"]] += 1
        else: 
            session_counts[session["game_name"]] = 1
    
    for game_name, count in session_counts.items():
        if count > most_sessions["count"]:
            most_sessions["game_name"] = game_name
            most_sessions["count"] = count

    return most_sessions

def get_stats(game_name, sessions):
    total_played = 0
    last_play_date = datetime.min

    for session in sessions.values():
        if session["game_name"].lower() == game_name.lower():
            total_played += 1
            if session["date_played"] > last_play_date:
                last_play_date = session["date_played"]
    
    return [total_played, last_play_date]

def player_rankings(sessions):
    return Counter(session["winner"] for session in sessions.values())

def player_wins(player_name, rankings):
    return rankings.get(player_name)

def get_game_id(game_name):
    with open(path.join(path.abspath(path.dirname(__file__)), "games.csv"), "rt", newline="") as f:
        reader = csv.reader(f)
        next(reader)
        for game in reader:
            if game[GAME_NAME_INDEX].lower() == game_name.lower():
                return game[GAME_ID_INDEX]
    return ""

def log_new_session(file_name, game_id, game_name, date_played, players, winner, duration_minutes):
    next_id = get_last_id(file_name) + 1
    with open(path.join(path.abspath(path.dirname(__file__)), file_name), "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([next_id, game_id, game_name, date_played, players, winner, duration_minutes])

def main():
    collection= load_collection("games.csv")
    sessions = load_sessions("sessions.csv")

    while True:
        print("Please select one of the following: ")
        for i, option in enumerate(menu_options):
            print(f"{i+1}. {option}")
        try:
            selected_action = int(input("Please enter an action: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        while selected_action < 1 or selected_action > 11:
            selected_action = int(input("Not a valid action. Please enter a valid action: "))
        match selected_action:
            case 1:
                display_collection(collection)
            case 2:
                game_name = input("Enter game name: ")
                if game_in_collection(game_name, collection):
                    count = get_play_count(game_name, sessions)
                    print(f"\n{count} total games of {game_name.upper()} played.\n")
                else:
                    print(f"\n'{game_name.upper()}' not in collection.\n")
            case 3:
                game_name = input("Enter game name: ")
                if game_in_collection(game_name, collection):
                    date = get_last_played(game_name, sessions)
                    if date == datetime.min:
                        print("\nThis game has not been played yet.\n")
                    else:
                        print(f"\nLast played date of {game_name.upper()} was {date.strftime('%b %d, %Y')}.\n")
                else:
                    print(f"\n'{game_name.upper()}' not in collection.\n")
            case 4:
                game_data = get_most_played(sessions) # returns {"game_name": "", "count": 0}
                print(f"\nMost played game is {game_data["game_name"]}, with {game_data["count"]} games played.\n")
            case 5:
                game_name = input("Enter game name: ")
                if game_in_collection(game_name, collection):
                    [total_plays, last_played] = get_stats(game_name, sessions)
                    print(f"\n{total_plays} total games played. Last played: {last_played.strftime('%B %d, %Y')}.\n")
                else:
                    print(f"\n'{game_name.upper()}' not in collection.\n")
            case 6:
                game_name = input("Enter game name: ")
                category = input("Enter category: ")
                min_players = int(input("Enter minimum number of players: "))
                max_players = int(input("Enter maximum number of players: "))
                play_time = int(input("Enter play time (minutes): "))
                year_published = int(input("Enter year published: "))
                add_game("games.csv", game_name, category, min_players, max_players, play_time, year_published)
            case 7:
                rankings = player_rankings(sessions)
                print("")
                for winner, wins in rankings.items():
                    print(f"{winner}, {wins} wins")
                print("")
            case 8:
                name = input("Input name: ").capitalize()
                rankings = player_rankings(sessions)
                wins = rankings.get(name, 0)
                print(f"\n{name}: {wins} wins\n")
            case 9:
                game_name = input("Enter game name: ").capitalize()
                game_id = get_game_id(game_name)
                while game_id == "":
                    game_name = input("Game not in collection, please enter a valid game name: ").capitalize()
                    game_id = get_game_id(game_name)
                while True:
                    date_played = input("Enter date played (YYYY-MM-DD): ")
                    try:
                        datetime.strptime(date_played, "%Y-%m-%d")
                        break
                    except ValueError:
                        print("Invalid date format, please use YYYY-MM-DD")

                players = players = ";".join(p.strip() for p in input("Enter players (space-separated): ").split(" "))
                winner = input("Enter winner: ").capitalize()
                duration_minutes = int(input("Enter duration (minutes): "))
                log_new_session("sessions.csv", game_id, game_name, date_played, players, winner, duration_minutes)
            case 10:
                print("Goodbye")
                break    

if __name__ == "__main__":
    main()