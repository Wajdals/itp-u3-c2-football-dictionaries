def players_as_dictionaries(squads_list):
    res = []
    for i in squads_list :
        di = {
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
        res.append(di)
    return res 



    
