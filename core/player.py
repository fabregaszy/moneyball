import requests


class Player(dict):
    """ store the information of a Player """

    player_id = None  # the identifier of a player
    player_info_url = "http://stats.nba.com/stats/commonplayerinfo"

    def __parse_common_player_info(self, response_json):
        """ parse the JSON returned by stats.nba api """

        for sets in response_json.get('resultSets'):
            if sets.get('name') == 'CommonPlayerInfo':
                # now we only cares about common player info
                headers = sets.get('headers')
                row_set = sets.get('rowSet')

                for i in range(len(headers)):
                    self[headers[i]] = row_set[0][i]

    def __init__(self, player_id):

        super(Player, self).__init__()

        self.player_id = player_id

        # parameter of GET/
        params = {'PlayerID': player_id, 'LeagueID': '00'}
        res = requests.get(self.player_info_url, params=params)

        if res.status_code != 200:
            print("[%d] GET/ %s" % (res.status_code, res.url))

        self.__parse_common_player_info(res.json())

        print('Player %d generated' % self.player_id)
