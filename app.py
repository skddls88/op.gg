from flask import Flask, request, render_template, jsonify
from api_search import summoner_data, league_info, league_match_data, detail_match_data

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search",methods=["GET","POST"])
def summoner_search():
    if request.method == "GET":
        user_nick = request.args.get("username")
        if user_nick == "" or user_nick == None:
            return "사용자 이름을 입력 해주세요."
        else:
            user_data = summoner_data(user_nick) # 전체 회원정보 (id,uuid,key값등등...)
            
            if not user_data == False:
                league_data = league_info(user_data['id']) #리그데이터 (티어,솔랭,자유랭,랭크포인트 등등..)
                user_match_data = str(str(user_data['accountId'])) # 전적데이터(매칭데이터)
                game_data = league_match_data(user_match_data)  #검색한 유저의 최대 100개 게임의 데이터

                
                detail_list = [] #최근전적 게임 플레이어들의 정보를 담을 변수 선언
                for i in range(len(game_data)): # -1을 해준 이유는 하지 않았을 경우 맨 마지막에 나오는 엘리먼트 값이 숫자int 0 이고 엘리먼트의 처음부터 마지막 직전까지는 모두 dict형태 입니다.

                    elems = game_data[i]['gameId']  # 최대 100개의 매칭데이터
                    detail_data = detail_match_data(elems) # 최대 100개의 매칭데이터의 플레이어 상세데이터
                    detail_list.append(detail_data)         #리스트에 값을 넣어줌
                    

                return render_template("sub_page.html", user_data=user_data, league_data=league_data, game_data=game_data, detail_data = detail_list)

            else:
                return "아이디가 없거나 일시적인 에러입니다, 관리자에게 문의해주세요 ^^"
                
if __name__ == "__main__":
    app.run(debug=True)