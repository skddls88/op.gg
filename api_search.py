import requests
import json

api_key = 'RGAPI-2d852cb0-f46b-4ce0-9284-01ddf8ccbd95' #마스터 api_key

def summoner_data(nick_name): # 소환사명으로 userid, uuid , 데이타등 전체적으로 가져옴

    url = 'https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/'+nick_name

    my_header = {
        "Origin": "https://developer.riotgames.com",
        "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Riot-Token": api_key,
        "Accept-Language": "ko,en-US;q=0.9,en;q=0.8,ko-KR;q=0.7,zh-CN;q=0.6,zh;q=0.5",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36"
    }
    
    req = requests.get(url=url, headers=my_header)
    if req.status_code == 200:
        json_data = json.loads(req.text)
        user_id = json_data['id']
        user_accountId = json_data['accountId']
        user_puuid = json_data['puuid']
        user_nickname = json_data['name'] # 소환사 이름
        user_icon = json_data['profileIconId'] # 소환사 아이콘
        user_level = json_data['summonerLevel'] # 소환사 레벨
        
        return {'id':user_id, 'accountId': user_accountId, 
            'puuid' : user_puuid, 'name': user_nickname,
            'profileIconId': user_icon, 'summonerLevel' : user_level}
            
    else:
        return False

def league_info(user_key): #게임 승/패 판수정보 , 리그정보 , 티어 , 리그포인트 가져옴
    # 도환작업 #
    url = 'https://kr.api.riotgames.com/lol/league/v4/entries/by-summoner/' + user_key
    my_header = {
    "Origin": "https://developer.riotgames.com",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Riot-Token": api_key,
    "Accept-Language": "ko,en-US;q=0.9,en;q=0.8,ko-KR;q=0.7,zh-CN;q=0.6,zh;q=0.5",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
        }
    req = requests.get(url=url, headers=my_header)
    if req.status_code == 200:
        json_data = json.loads(req.text)
        if len(json_data) == 2: # 솔로랭크,자유랭크가 전부다 존재할때
            if json_data[0]['queueType'] == 'RANKED_SOLO_5x5': # 솔로랭크일때

                # 솔로랭크 데이터 #

                league_type = json_data[0]['queueType'] # 리그타입 => RANKED_FLEX_SR(자유랭크) , RANKED_SOLO_5x5(솔로랭크)
                win_count = json_data[0]['wins'] # 승리수 int
                lose_count = json_data[0]['losses'] #패배수 int
                rank_level = json_data[0]['rank'] # 랭크티어 (1~4티어)
                rank_tier = json_data[0]['tier'] # 티어 아이언,브론즈,실버,골드,플레티넘,다이아 ~~~~
                rank_point = json_data[0]['leaguePoints'] # 리그포인트 골드1티어 (59포인트)

                # 솔로랭크 데이터 #


                # 자유랭크(팀랭) 데이타 #
                league_type2 = json_data[1]['queueType'] # 리그타입 => RANKED_FLEX_SR(자유랭크) , RANKED_SOLO_5x5(솔로랭크)
                win_count2 = json_data[1]['wins'] # 승리수 int
                lose_count2 = json_data[1]['losses'] #패배수 int
                rank_level2 = json_data[1]['rank'] # 랭크티어 (1~4티어)
                rank_tier2= json_data[1]['tier'] # 티어 아이언,브론즈,실버,골드,플레티넘,다이아 ~~~~
                rank_point2 = json_data[1]['leaguePoints'] # 리그포인트 골드1티어 (59포인트)
                # 자유랭크(팀랭) 데이타 #

                solo_rank_data = {'league_type':'RANKED_SOLO_5x5', 'win_count':win_count, 'lose_count':lose_count,
                'rank_level':rank_level, 'rank_tier':rank_tier, 'rank_point':rank_point }

                team_rank_data = {'league_type':'RANKED_FLEX_SR', 'win_count':win_count2, 'lose_count':lose_count2,
                'rank_level':rank_level2, 'rank_tier':rank_tier2, 'rank_point':rank_point2 }

                return solo_rank_data,team_rank_data
            

            if json_data[0]['queueType'] == 'RANKED_FLEX_SR': # 자유랭크일때
                # 자유랭크(팀랭) 데이타 #
                league_type2 = json_data[0]['queueType'] # 리그타입 => RANKED_FLEX_SR(자유랭크) , RANKED_SOLO_5x5(솔로랭크)
                win_count2 = json_data[0]['wins'] # 승리수 int
                lose_count2 = json_data[0]['losses'] #패배수 int
                rank_level2 = json_data[0]['rank'] # 랭크티어 (1~4티어)
                rank_tier2 = json_data[0]['tier'] # 티어 아이언,브론즈,실버,골드,플레티넘,다이아 ~~~~
                rank_point2 = json_data[0]['leaguePoints'] # 리그포인트 골드1티어 (59포인트)
                # 자유랭크(팀랭) 데이타 #


                # 솔로랭크 데이터 #
                league_type = json_data[1]['queueType'] # 리그타입 => RANKED_FLEX_SR(자유랭크) , RANKED_SOLO_5x5(솔로랭크)
                win_count = json_data[1]['wins'] # 승리수 int
                lose_count = json_data[1]['losses'] #패배수 int
                rank_level = json_data[1]['rank'] # 랭크티어 (1~4티어)
                rank_tier = json_data[1]['tier'] # 티어 아이언,브론즈,실버,골드,플레티넘,다이아 ~~~~
                rank_point = json_data[1]['leaguePoints'] # 리그포인트 골드1티어 (59포인트)
                # 솔로랭크 데이터 #

                solo_rank_data = {'league_type':'RANKED_SOLO_5x5', 'win_count':win_count, 'lose_count':lose_count,
                'rank_level':rank_level, 'rank_tier':rank_tier, 'rank_point':rank_point }

                team_rank_data = {'league_type':'RANKED_FLEX_SR', 'win_count':win_count2, 'lose_count':lose_count2,
                'rank_level':rank_level2, 'rank_tier':rank_tier2, 'rank_point':rank_point2 }

                return solo_rank_data,team_rank_data
                
        elif len(json_data) == 1:
            if json_data[0]['queueType'] == 'RANKED_SOLO_5x5': # 솔로랭크만 있을때

                # 솔로랭크 데이터 #
                league_type = json_data[0]['queueType'] # 리그타입 => RANKED_FLEX_SR(자유랭크) , RANKED_SOLO_5x5(솔로랭크)
                win_count = json_data[0]['wins'] # 승리수 int
                lose_count = json_data[0]['losses'] #패배수 int
                rank_level = json_data[0]['rank'] # 랭크티어 (1~4티어)
                rank_tier = json_data[0]['tier'] # 티어 아이언,브론즈,실버,골드,플레티넘,다이아 ~~~~
                rank_point = json_data[0]['leaguePoints'] # 리그포인트 골드1티어 (59포인트)
                # 솔로랭크 데이터 #

                solo_rank_data = {'league_type':'RANKED_SOLO_5x5', 'win_count':win_count, 'lose_count':lose_count,
                'rank_level':rank_level, 'rank_tier':rank_tier, 'rank_point':rank_point }

                team_rank_data = {'league_type':"RANKED_FLEX_SR", 'win_count':"", 'lose_count':"",
                'rank_level':"", 'rank_tier':"UN_RANK", 'rank_point':"" }

                return solo_rank_data,team_rank_data
            
            if json_data[0]['queueType'] == 'RANKED_FLEX_SR': # 자유랭크만 있을때
                # 자유랭크(팀랭) 데이타 #
                league_type = json_data[0]['queueType'] # 리그타입 => RANKED_FLEX_SR(자유랭크) , RANKED_SOLO_5x5(솔로랭크)
                win_count = json_data[0]['wins'] # 승리수 int
                lose_count = json_data[0]['losses'] #패배수 int
                rank_level = json_data[0]['rank'] # 랭크티어 (1~4티어)
                rank_tier = json_data[0]['tier'] # 티어 아이언,브론즈,실버,골드,플레티넘,다이아 ~~~~
                rank_point = json_data[0]['leaguePoints'] # 리그포인트 골드1티어 (59포인트)
                # 자유랭크(팀랭) 데이타 #

                solo_rank_data = {'league_type':'RANKED_SOLO_5x5', 'win_count':'', 'lose_count':'',
                'rank_level':'', 'rank_tier':'', 'rank_point':'' }

                team_rank_data = {'league_type':'RANKED_FLEX_SR', 'win_count':win_count, 'lose_count':lose_count,
                'rank_level':rank_level2, 'rank_tier':rank_tier, 'rank_point':rank_point }

                return solo_rank_data,team_rank_data
        
        else: # 솔로,팀랭 둘다 정보가 없을때 (언랭임)
            solo_rank_data = {'league_type':"RANKED_SOLO_5x5", 'win_count':"", 'lose_count':"",
                'rank_level':"", 'rank_tier':"UN_RANK", 'rank_point':"" }
            
            team_rank_data = {'league_type':"RANKED_FLEX_SR", 'win_count':"", 'lose_count':"",
                'rank_level':"", 'rank_tier':"UN_RANK", 'rank_point':"" }

            return solo_rank_data,team_rank_data


        
def league_match_data(user_match_data): #최근게임 데이터 (최대 100개까지 적다면 적은만큼만 가져옴)
    url = 'https://kr.api.riotgames.com/lol/match/v4/matchlists/by-account/'+user_match_data
    my_header = {
        "Origin": "https://developer.riotgames.com",
        "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Riot-Token": api_key,
        "Accept-Language": "ko,en-US;q=0.9,en;q=0.8,ko-KR;q=0.7,zh-CN;q=0.6,zh;q=0.5",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36"
    }
    req = requests.get(url=url, headers=my_header)
    
    if req.status_code == 200:
        
        json_data = json.loads(req.text)
        match_list = [0 for _ in range(len(json_data['matches']))]
        
        for i in range(len(json_data['matches'])):
            match_data = json_data['matches'][i]
            match_lane = match_data['lane']
            match_gameId = match_data['gameId']
            match_champion = match_data['champion']
            match_platformId = match_data['platformId']
            match_season = match_data['season']
            match_queue = match_data['queue']
            match_role = match_data['role']
            match_timestamp = match_data['timestamp']
            
            match_list[i] = {'lane':match_lane, 'gameId':match_gameId, 'champion':match_champion,
                'platformId':match_platformId, 'season':match_season, 'queue':match_queue,
                'role':match_role, 'timestamp':match_timestamp  }

        return match_list
            
    else:
        return False


# 처음 만든 함수입니다. 
def detail_match_data(detail_match_data):

    url = 'https://kr.api.riotgames.com/lol/match/v4/matches/' + str(detail_match_data)

    my_header = {
    "Origin": "https://developer.riotgames.com",
    "Accept-Charset": "application / x-www-form-urlencoded; charset = UTF-8",
    "X-Riot-Token": api_key,
    "Accept-Language": "ko-KR, ko; q = 0.9, en-US; q = 0.8, en; q = 0.7",
    "User-Agent": "Mozilla / 5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit / 537.36 (Kcko, Gecko) Chrome / 78.0.3904.108 Safari / 537.36"
    }
    
    req = requests.get(url=url, headers=my_header)
    
    if req.status_code == 200:
        
        player_list = [0 for _ in range(10)]
        item_list = [0 for _ in range(7)]
        user_item_list = [0 for _ in range(10)]

        json_data = json.loads(req.text)
        for i in range(10):
            player_data = json_data['participantIdentities'][i]['player']
            player_list[i] = player_data
            # 예시 key
            # player_data = {
            #     "currentPlatformId": "KR",
            #         "summonerName": "착한태준입니다",
            #         "matchHistoryUri": "/v1/stats/player_history/KR/6011598",
            #         "platformId": "KR",
            #         "currentAccountId": "HjQhwfugFTy49AT1IxwFDIXjxkxe5XEjdtgGZJr4l5lV",
            #         "profileIcon": 14,
            #         "summonerId": "qNj6pbOcELUcHCrQDTammS_SlzjNdYAAGoUrmCtYUrS7qQ",
            #         "accountId": "HjQhwfugFTy49AT1IxwFDIXjxkxe5XEjdtgGZJr4l5lV"
            # }
            for v in range(7):
                item_data = json_data['participants'][i]['stats']['item' + str(v)]
                item_list[v] = item_data
            user_item_list[i] = item_list
        return player_list, user_item_list
        

    else:
        return False


