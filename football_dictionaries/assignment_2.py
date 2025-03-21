def players_by_position(squads_list):
        res = {}  

    for player in squads_list:
        position = player[1]  

        player_dict = {
            'number': player[0],
            'position': player[1],
            'name': player[2],
            'date_of_birth': player[3],
            'caps': player[4],
            'club': player[5],
            'country': player[6],
            'club_country': player[7],
            'year': player[8],
        }
    
        if position not in res:
            res[position] = []
        res[position].append(player_dict)

    return res
