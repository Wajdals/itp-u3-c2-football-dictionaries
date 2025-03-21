def players_by_country_and_position(squads_list):
    res = {}

    for player in squads_list:
        position = player[1]  
        country = player[6]   
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

        if country not in res:
            res[country] = {}
        if position not in res[country]:
            res[country][position] = []
        res[country][position].append(player_dict)

    return res
