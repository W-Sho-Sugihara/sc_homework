import pytest
from datetime import datetime
from collections import Counter
from game_manager import (
    sort_collection_by_name,
    get_play_count,
    game_in_collection,
    get_last_played,
    get_most_played,
    get_stats,
    player_rankings,
    player_wins,
)

# test data 

collection = {
    "1": {"game_name": "Catan"},
    "2": {"game_name": "Ticket to Ride"},
    "3": {"game_name": "Pandemic"},
}

sessions = {
    "1": {"game_name": "Catan",          "date_played": datetime(2024, 1, 10), "winner": "Alice",   "duration": "90"},
    "2": {"game_name": "Ticket to Ride", "date_played": datetime(2024, 2, 15), "winner": "Bob",     "duration": "60"},
    "3": {"game_name": "Catan",          "date_played": datetime(2024, 3, 20), "winner": "Charlie", "duration": "75"},
}

# sort_collection_by_name

def test_sort_collection_by_name():
    result = sort_collection_by_name(collection)
    names = [data["game_name"] for data in result.values()]
    assert names == ["Catan", "Pandemic", "Ticket to Ride"]

def test_sort_collection_empty():
    assert sort_collection_by_name({}) == {}

# game_in_collection

def test_game_in_collection_found():
    assert game_in_collection("Catan", collection) is True

def test_game_in_collection_not_found():
    assert game_in_collection("Chess", collection) is False

def test_game_in_collection_case_insensitive():
    assert game_in_collection("catan", collection) is True
    assert game_in_collection("CATAN", collection) is True

# get_play_count

def test_get_play_count_multiple():
    assert get_play_count("Catan", sessions) == 2

def test_get_play_count_single():
    assert get_play_count("Ticket to Ride", sessions) == 1

def test_get_play_count_not_played():
    assert get_play_count("Pandemic", sessions) == 0

def test_get_play_count_case_insensitive():
    assert get_play_count("catan", sessions) == 2

# get_last_played

def test_get_last_played_returns_most_recent():
    assert get_last_played("Catan", sessions) == datetime(2024, 3, 20)

def test_get_last_played_single_session():
    assert get_last_played("Ticket to Ride", sessions) == datetime(2024, 2, 15)

def test_get_last_played_not_played():
    assert get_last_played("Pandemic", sessions) == datetime.min

# get_most_played

def test_get_most_played_game_name():
    assert get_most_played(sessions)["game_name"] == "Catan"

def test_get_most_played_count():
    assert get_most_played(sessions)["count"] == 2

# get_stats

def test_get_stats_total_plays():
    total, _ = get_stats("Catan", sessions)
    assert total == 2

def test_get_stats_last_played():
    _, last_played = get_stats("Catan", sessions)
    assert last_played == datetime(2024, 3, 20)

def test_get_stats_unplayed_game():
    total, last_played = get_stats("Pandemic", sessions)
    assert total == 0
    assert last_played == datetime.min

# player_rankings

def test_player_rankings_returns_counter():
    assert isinstance(player_rankings(sessions), Counter)

def test_player_rankings_correct_counts():
    rankings = player_rankings(sessions)
    assert rankings["Alice"] == 1
    assert rankings["Bob"] == 1
    assert rankings["Charlie"] == 1

def test_player_rankings_multiple_wins():
    multi_sessions = {
        "1": {"game_name": "Catan", "date_played": datetime(2024, 1, 1), "winner": "Alice", "duration": "60"},
        "2": {"game_name": "Catan", "date_played": datetime(2024, 1, 2), "winner": "Alice", "duration": "60"},
        "3": {"game_name": "Catan", "date_played": datetime(2024, 1, 3), "winner": "Bob",   "duration": "60"},
    }
    rankings = player_rankings(multi_sessions)
    assert rankings["Alice"] == 2
    assert rankings["Bob"] == 1

# player_wins

def test_player_wins_known_player():
    rankings = player_rankings(sessions)
    assert player_wins("Alice", rankings) == 1

def test_player_wins_unknown_player():
    rankings = player_rankings(sessions)
    assert player_wins("Zara", rankings) is None

pytest.main(["-v", "--tb=line", "-rN", __file__])