# Given dataset
all_players = [
    {
        "name": "Player 01",
        'position': 'Forward',
        'jersey_number': 9,
        'yards_gained': 150,
        'touchdowns': 2
    },
    {
        "name": "Player 02",
        'position': 'Midfield',
        'jersey_number': 10,
        'yards_gained': 120,
        'touchdowns': 1
    },
    {
        "name": "Player 03",
        'position': 'Defender',
        'jersey_number': 5,
        'yards_gained': 80,
        'touchdowns': 0
    },
    {
        "name": "Player 04",
        'position': 'Goalkeeper',
        'jersey_number': 1,
        'yards_gained': 0,
        'touchdowns': 0
    }
]

# Calculate total yards gained and touchdowns
total_yards = sum(player["yards_gained"] for player in all_players)
total_touchdowns = sum(player["touchdowns"] for player in all_players)

# Calculate average yards gained and touchdowns
average_yards = total_yards / len(all_players)
average_touchdowns = total_touchdowns / len(all_players)

# Print the results
print("Average Statistics:")
print("Average yards gained per player:", average_yards)
print("Average touchdowns per player:", average_touchdowns)


# choosen_player_name = 'Player 01'

# player_positions = [player['position'] for player in all_players]

# print('List of all player positions: ', player_positions)



# chosen_player_name = 'Player 01'

# for player in all_players:
#     if player['name'] == choosen_player_name:
#         player['Position'] = 'Forward'
#         player['jersey_number'] = 11
#         player['name'] = 'Lionel Messi'
#         break

# print('Updated player details: ')

# for player in all_players:
#     print(player)