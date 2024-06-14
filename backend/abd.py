import sys,re,time
que=str(sys.argv[1])
def delayed_print(message):
    for i in message:
        print(i,end='')
        time.sleep(0.01)
    print()
def message_probability(user_message,recognised_words,single_response=False,required_words=[]):
    message_certainity=0
    has_required_words=True
    for word in user_message:
        if word in recognised_words:
            message_certainity+=1
    percentage=float(message_certainity)/float(len(recognised_words))
    for word in required_words:
        if word not in user_message:
            has_required_words=False
            break
    if has_required_words or single_response:
        return int(percentage*100)
    else:
        return 0
def check_all_messages(message):
    highest_prob_list={}
    def response(bot_response,list_of_words,single_response=False,required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response]=message_probability(message,list_of_words,single_response,required_words)
    response('Nice talking to you , Bye!',['bye',"farewell","goodbye","adios","see you later","cheerio","au revoir","ciao","ta-ta","so long","until we meet again"],single_response=True)
    response('hello',['hello','hi','heya','hola','sup'],single_response=True)
    response('I am doing fine wht about you?',['how','are','you','doing'],required_words=['how'])
    response('Thank you',['i','like','love','bert'],required_words=['like','love','bert'])
    response("Cricket is the national sport of India.", ["national", "sport", "india", "cricket"])
    response("Sachin Tendulkar is known as the 'God of Cricket'.", ["sachin", "tendulkar", "god", "cricket"])
    response("England won the ICC Cricket World Cup in 2019.", ["england", "icc", "world", "cup", "2019"])
    response("The three formats of cricket are Test, One Day International (ODI), and Twenty20 (T20).",
             ["three", "formats", "test", "one", "day", "international", "odi", "twenty20", "t20"])
    response("Brian Lara holds the record for the highest individual score in Test cricket.", ["brian", "lara", "record", "highest", "score", "test", "cricket"])
    response("India won the first-ever ICC T20 World Cup.", ["india", "first", "icc", "t20", "world", "cup"])
    response("Virat Kohli is the current captain of the Indian cricket team in Test matches.",
             ["virat", "kohli", "current", "captain", "indian", "team", "test", "matches"])
    response("LBW stands for Leg Before Wicket in cricket.", ["lbw", "leg", "before", "wicket", "cricket"])
    response("There are 11 players in a cricket team.", ["11", "players", "cricket", "team"])
    response("A Test cricket match typically lasts for five days.", ["test", "cricket", "match", "five", "days"])
    response("Rohit Sharma holds the record for the most runs scored in a single edition of the ICC Cricket World Cup.",
             ["rohit", "sharma", "record", "most", "runs", "single", "edition", "icc", "cricket", "world", "cup"])
    response("The nickname of the Australian cricket team is the 'Baggy Greens'.", ["nickname", "australian", "team", "baggy", "greens"])
    response("Muttiah Muralitharan has taken the most wickets in international cricket.", ["muttiah", "muralitharan", "most", "wickets", "international", "cricket"])
    response("Wasim Akram is known as the 'Sultan of Swing' in cricket.", ["wasim", "akram", "sultan", "swing", "cricket"])
    response("The trophy awarded to the winner of the Ashes series between England and Australia is called 'The Ashes'.",
             ["trophy", "winner", "ashes", "series", "england", "australia"])
    response("The Indian Premier League (IPL) is a professional Twenty20 cricket league in India.", ["indian", "premier", "league", "ipl"])
    response("The Mumbai Indians is the most successful team in IPL history with the most titles.", ["mumbai", "indians", "most", "successful", "team", "ipl"])
    response("The Chennai Super Kings has won the IPL title the second most number of times.", ["chennai", "super", "kings", "second", "most", "times", "ipl"])
    response("The Orange Cap is awarded to the leading run-scorer in each IPL season.", ["orange", "cap", "leading", "run-scorer", "ipl", "season"])
    response("The Purple Cap is awarded to the leading wicket-taker in each IPL season.", ["purple", "cap", "leading", "wicket-taker", "ipl", "season"])
    response("The IPL was founded by the Board of Control for Cricket in India (BCCI) in 2008.", ["founded", "board", "control", "cricket", "india", "bcci", "2008"])
    response("The Mumbai Indians won the IPL in 2020.", ["mumbai", "indians", "won", "ipl", "2020"])
    response("The Kolkata Knight Riders won the IPL in 2012 and 2014.", ["kolkata", "knight", "riders", "won", "ipl", "2012", "2014"])
    response("The Rajasthan Royals won the inaugural IPL season in 2008.", ["rajasthan", "royals", "won", "inaugural", "ipl", "2008"])
    # IPL-related responses (continued)
    response("The Orange Cap is awarded to the leading run-scorer in each IPL season.",
             ["orange", "cap", "leading", "run-scorer", "ipl", "season"])
    response("The Purple Cap is awarded to the leading wicket-taker in each IPL season.",
             ["purple", "cap", "leading", "wicket-taker", "ipl", "season"])
    response("The IPL playoffs consist of Qualifier 1, Eliminator, Qualifier 2, and the Final.",
             ["ipl", "playoffs", "qualifier", "eliminator", "final"])
    response("The IPL auction is held annually to buy players for each team.",
             ["ipl", "auction", "annually", "buy", "players", "team"])
    response("The Sunrisers Hyderabad won the IPL in 2016.", ["sunrisers", "hyderabad", "won", "ipl", "2016"])
    response("The Delhi Capitals reached the IPL final for the first time in 2020.", ["delhi", "capitals", "reached", "final", "ipl", "2020"])
    response("The Rajasthan Royals won the IPL under the captaincy of Shane Warne in 2008.", ["rajasthan", "royals", "won", "captaincy", "shane", "warne", "ipl", "2008"])
    response("The Mumbai Indians have won the IPL five times, the most by any team.", ["mumbai", "indians", "won", "ipl", "five", "times"])
    response("Chennai Super Kings made a comeback in IPL 2018 after a two-year suspension.", ["chennai", "super", "kings", "comeback", "ipl", "2018", "suspension"])
    response("Chris Gayle holds the record for the highest individual score in an IPL match.", ["chris", "gayle", "record", "highest", "individual", "score", "ipl", "match"])
    response("The IPL 2021 season was held in the United Arab Emirates (UAE) due to the COVID-19 pandemic.", ["ipl", "2021", "season", "united", "arab", "emirates", "uae", "covid-19", "pandemic"])
    response("The Royal Challengers Bangalore has not won an IPL title yet.", ["royal", "challengers", "bangalore", "not", "won", "ipl", "title", "yet"])
    response("Kolkata Knight Riders won consecutive IPL titles in 2012 and 2014.", ["kolkata", "knight", "riders", "consecutive", "ipl", "titles", "2012", "2014"])
    response("Virat Kohli holds the record for the most runs in IPL history.", ["virat", "kohli", "record", "most", "runs", "ipl", "history"])
    response("The IPL 2020 season was played in the United Arab Emirates (UAE) due to the COVID-19 pandemic.",
             ["ipl", "2020", "season", "played", "united", "arab", "emirates", "uae", "covid-19", "pandemic"])
    response("Mumbai Indians won the IPL title in 2019.", ["mumbai", "indians", "won", "ipl", "2019"])
    response("The Delhi Capitals reached their first IPL final in 2020.", ["delhi", "capitals", "reached", "first", "ipl", "final", "2020"])
    response("Kolkata Knight Riders won the IPL in 2012 and 2014 under the captaincy of Gautam Gambhir.", ["kolkata", "knight", "riders", "won", "ipl", "2012", "2014", "captaincy", "gautam", "gambhir"])
    response("Rajasthan Royals won the inaugural IPL season in 2008 under the captaincy of Shane Warne.", ["rajasthan", "royals", "won", "inaugural", "ipl", "2008", "captaincy", "shane", "warne"])
    response("Sunrisers Hyderabad won the IPL in 2016 under the captaincy of David Warner.", ["sunrisers", "hyderabad", "won", "ipl", "2016", "captaincy", "david", "warner"])
    response("The IPL 2021 season saw the emergence of young talent like Harshal Patel and Avesh Khan.", ["ipl", "2021", "season", "emergence", "young", "talent", "harshal", "patel", "avesh", "khan"])
    
    response("AB de Villiers' exceptional batting prowess was a cornerstone of the Royal Challengers Bangalore's IPL campaign.", ["ab", "de", "villiers", "exceptional", "batting", "prowess", "cornerstone", "royal", "challengers", "bangalore", "ipl", "campaign"])
    response("AB de Villiers' ability to play innovative shots made him a standout performer for the Royal Challengers Bangalore in the IPL.", ["ab", "de", "villiers", "ability", "play", "innovative", "shots", "standout", "performer", "royal", "challengers", "bangalore", "ipl"])
    response("The Royal Challengers Bangalore's success in the IPL was often fueled by AB de Villiers' explosive batting displays.", ["royal", "challengers", "bangalore", "success", "ipl", "fueled", "ab", "de", "villiers", "explosive", "batting", "displays"])
    response("AB de Villiers' ability to change the course of a game single-handedly was a key asset for the Royal Challengers Bangalore in the IPL.", ["ab", "de", "villiers", "ability", "change", "course", "game", "single-handedly", "key", "asset", "royal", "challengers", "bangalore", "ipl"])
    response("The Royal Challengers Bangalore often relied on AB de Villiers' batting brilliance to propel them to victory in the IPL.", ["royal", "challengers", "bangalore", "relied", "ab", "de", "villiers", "batting", "brilliance", "propel", "victory", "ipl"])
    response("AB de Villiers' extraordinary talent with the bat made him a prized asset for the Royal Challengers Bangalore in the IPL.", ["ab", "de", "villiers", "extraordinary", "talent", "bat", "prized", "asset", "royal", "challengers", "bangalore", "ipl"])
    response("The Royal Challengers Bangalore's fortunes in the IPL often hinged on AB de Villiers' ability to score quick runs.", ["royal", "challengers", "bangalore", "fortunes", "ipl", "hinged", "ab", "de", "villiers", "ability", "score", "quick", "runs"])
    response("AB de Villiers' remarkable consistency with the bat was a key factor in the Royal Challengers Bangalore's IPL campaigns.", ["ab", "de", "villiers", "remarkable", "consistency", "bat", "key", "factor", "royal", "challengers", "bangalore", "ipl", "campaigns"])
    response("The Royal Challengers Bangalore's batting lineup was formidable, with AB de Villiers often leading the charge in the IPL.", ["royal", "challengers", "bangalore", "batting", "lineup", "formidable", "ab", "de", "villiers", "often", "leading", "charge", "ipl"])
    response("AB de Villiers' ability to adapt to different match situations was crucial for the Royal Challengers Bangalore in the IPL.", ["ab", "de", "villiers", "ability", "adapt", "different", "match", "situations", "crucial", "royal", "challengers", "bangalore", "ipl"])
    response("The Royal Challengers Bangalore's success in the IPL was often synonymous with AB de Villiers' batting masterclasses.", ["royal", "challengers", "bangalore", "success", "ipl", "synonymous", "ab", "de", "villiers", "batting", "masterclasses"])
    response("AB de Villiers' ability to accelerate the run rate was a game-changer for the Royal Challengers Bangalore in the IPL.", ["ab", "de", "villiers", "ability", "accelerate", "run", "rate", "game-changer", "royal", "challengers", "bangalore", "ipl"])
    response("The Royal Challengers Bangalore often looked to AB de Villiers to anchor their innings and build big totals in the IPL.", ["royal", "challengers", "bangalore", "looked", "ab", "de", "villiers", "anchor", "innings", "build", "big", "totals", "ipl"])
    response("AB de Villiers' ability to find gaps and score boundaries consistently made him a nightmare for opposing bowlers in the IPL.", ["ab", "de", "villiers", "ability", "find", "gaps", "score", "boundaries", "consistently", "nightmare", "opposing", "bowlers", "ipl"])
    response("The Royal Challengers Bangalore's middle-order stability was often provided by the reliable presence of AB de Villiers in the IPL.", ["royal", "challengers", "bangalore", "middle-order", "stability", "provided", "reliable", "presence", "ab", "de", "villiers", "ipl"])
    response("AB de Villiers' ability to innovate and play unorthodox shots set him apart as one of the most exciting batsmen in the IPL.", ["ab", "de", "villiers", "ability", "innovate", "play", "unorthodox", "shots", "set", "apart", "exciting", "batsmen", "ipl"])
    response("The Royal Challengers Bangalore's batting lineup gained confidence knowing AB de Villiers was at the crease in the IPL.", ["royal", "challengers", "bangalore", "batting", "lineup", "gained", "confidence", "knowing", "ab", "de", "villiers", "crease", "ipl"])
    response("AB de Villiers' ability to read the game and adapt his gameplay accordingly made him a valuable asset for the Royal Challengers Bangalore in the IPL.", ["ab", "de", "villiers", "ability", "read", "game", "adapt", "gameplay", "accordingly", "valuable", "asset", "royal", "challengers", "bangalore", "ipl"])
    response("The Royal Challengers Bangalore's strategy often revolved around AB de Villiers' ability to accelerate the run rate in the IPL.", ["royal", "challengers", "bangalore", "strategy", "revolved", "around", "ab", "de", "villiers", "ability", "accelerate", "run", "rate", "ipl"])
    response("AB de Villiers' uncanny ability to find gaps and rotate the strike consistently kept the scoreboard ticking for the Royal Challengers Bangalore in the IPL.", ["ab", "de", "villiers", "uncanny", "ability", "find", "gaps", "rotate", "strike", "consistently", "kept", "scoreboard", "ticking", "royal", "challengers", "bangalore", "ipl"])
    response("The Royal Challengers Bangalore's batting lineup boasted depth, with AB de Villiers often providing stability in the middle overs of the IPL.", ["royal", "challengers", "bangalore", "batting", "lineup", "boasted", "depth", "ab", "de", "villiers", "often", "providing", "stability", "middle", "overs", "ipl"])
    response("AB de Villiers' ability to hit boundaries at will was a nightmare for opposing captains in the IPL.", ["ab", "de", "villiers", "ability", "hit", "boundaries", "will", "nightmare", "opposing", "captains", "ipl"])
    response("The Royal Challengers Bangalore's batting lineup was often steered to victory by AB de Villiers' calculated aggression in the IPL.", ["royal", "challengers", "bangalore", "batting", "lineup", "steered", "victory", "ab", "de", "villiers", "calculated", "aggression", "ipl"])
    response("AB de Villiers' batting versatility allowed the Royal Challengers Bangalore to adapt to various match situations in the IPL.", ["ab", "de", "villiers", "batting", "versatility", "allowed", "royal", "challengers", "bangalore", "adapt", "various", "match", "situations", "ipl"])
    response("The Royal Challengers Bangalore's IPL campaigns often revolved around AB de Villiers' ability to finish matches with his explosive batting.", ["royal", "challengers", "bangalore", "ipl", "campaigns", "revolved", "around", "ab", "de", "villiers", "ability", "finish", "matches", "explosive", "batting"])
    response("AB de Villiers' calm demeanor under pressure made him a reliable finisher for the Royal Challengers Bangalore in the IPL.", ["ab", "de", "villiers", "calm", "demeanor", "pressure", "reliable", "finisher", "royal", "challengers", "bangalore", "ipl"])
    response("The Royal Challengers Bangalore's middle-order stability was often provided by the cool-headed presence of AB de Villiers in the IPL.", ["royal", "challengers", "bangalore", "middle-order", "stability", "provided", "cool-headed", "presence", "ab", "de", "villiers", "ipl"])
    response("AB de Villiers' ability to score boundaries at crucial moments turned the tide in favor of the Royal Challengers Bangalore in the IPL.", ["ab", "de", "villiers", "ability", "score", "boundaries", "crucial", "moments", "turned", "tide", "favor", "royal", "challengers", "bangalore", "ipl"])
    response("The Royal Challengers Bangalore's batting lineup often looked to AB de Villiers to provide impetus during crucial phases of the IPL.", ["royal", "challengers", "bangalore", "batting", "lineup", "looked", "ab", "de", "villiers", "provide", "impetus", "crucial", "phases", "ipl"])
    response("AB de Villiers' ability to build partnerships and rotate the strike effectively was instrumental for the Royal Challengers Bangalore in the IPL.", ["ab", "de", "villiers", "ability", "build", "partnerships", "rotate", "strike", "effectively", "instrumental", "royal", "challengers", "bangalore", "ipl"])
    response("The Royal Challengers Bangalore's success in the IPL often coincided with AB de Villiers' explosive innings at crucial junctures.", ["royal", "challengers", "bangalore", "success", "ipl", "coincided", "ab", "de", "villiers", "explosive", "innings", "crucial", "junctures"])
    response("AB de Villiers' ability to dissect the field with precision placement of shots was a nightmare for opposition captains in the IPL.", ["ab", "de", "villiers", "ability", "dissect", "field", "precision", "placement", "shots", "nightmare", "opposition", "captains", "ipl"])
    response("The Royal Challengers Bangalore's batting lineup was often anchored by AB de Villiers' masterful innings in the IPL.", ["royal", "challengers", "bangalore", "batting", "lineup", "anchored", "ab", "de", "villiers", "masterful", "innings", "ipl"])
    response("AB de Villiers' ability to clear the boundary with ease was a sight to behold for fans of the Royal Challengers Bangalore in the IPL.", ["ab", "de", "villiers", "ability", "clear", "boundary", "ease", "sight", "behold", "fans", "royal", "challengers", "bangalore", "ipl"])
    response("The Royal Challengers Bangalore often found themselves in winning positions thanks to AB de Villiers' heroics with the bat in the IPL.", ["royal", "challengers", "bangalore", "found", "winning", "positions", "thanks", "ab", "de", "villiers", "heroics", "bat", "ipl"])
    response("AB de Villiers' ability to take the game away from the opposition in a matter of overs was a game-changer for the Royal Challengers Bangalore in the IPL.", ["ab", "de", "villiers", "ability", "take", "game", "away", "opposition", "matter", "overs", "game-changer", "royal", "challengers", "bangalore", "ipl"])
    response("The Royal Challengers Bangalore often looked to AB de Villiers to provide stability and impetus during crucial phases of the IPL.", ["royal", "challengers", "bangalore", "looked", "ab", "de", "villiers", "provide", "stability", "impetus", "crucial", "phases", "ipl"])
    response("AB de Villiers' ability to accelerate the scoring rate was a crucial asset for the Royal Challengers Bangalore in the IPL.", ["ab", "de", "villiers", "ability", "accelerate", "scoring", "rate", "crucial", "asset", "royal", "challengers", "bangalore", "ipl"])
    response("The Royal Challengers Bangalore's batting lineup often relied on AB de Villiers' ability to play match-winning innings in the IPL.", ["royal", "challengers", "bangalore", "batting", "lineup", "relied", "ab", "de", "villiers", "ability", "play", "match-winning", "innings", "ipl"])
    response("AB de Villiers' ability to handle pressure situations and finish games with composure was invaluable for the Royal Challengers Bangalore in the IPL.", ["ab", "de", "villiers", "ability", "handle", "pressure", "situations", "finish", "games", "composure", "invaluable", "royal", "challengers", "bangalore", "ipl"])
    response("The Royal Challengers Bangalore often looked to AB de Villiers to provide fireworks in the middle overs of the IPL.", ["royal", "challengers", "bangalore", "looked", "ab", "de", "villiers", "provide", "fireworks", "middle", "overs", "ipl"])
    response("AB de Villiers' ability to read the game and adapt his batting style accordingly made him a versatile asset for the Royal Challengers Bangalore in the IPL.", ["ab", "de", "villiers", "ability", "read", "game", "adapt", "batting", "style", "accordingly", "versatile", "asset", "royal", "challengers", "bangalore", "ipl"])
    response("The Royal Challengers Bangalore often found themselves in strong positions thanks to AB de Villiers' ability to accelerate the scoring rate in the IPL.", ["royal", "challengers", "bangalore", "found", "strong", "positions", "thanks", "ab", "de", "villiers", "ability", "accelerate", "scoring", "rate", "ipl"])
    response("AB de Villiers' ability to innovate and play unconventional shots made him a nightmare for opposing bowlers in the IPL.", ["ab", "de", "villiers", "ability", "innovate", "play", "unconventional", "shots", "nightmare", "opposing", "bowlers", "ipl"])
    response("The Royal Challengers Bangalore often relied on AB de Villiers' ability to anchor the innings and build partnerships in the IPL.", ["royal", "challengers", "bangalore", "relied", "ab", "de", "villiers", "ability", "anchor", "innings", "build", "partnerships", "ipl"])
    response("AB de Villiers' ability to find gaps and manipulate the field with precise shots was a key strength for the Royal Challengers Bangalore in the IPL.", ["ab", "de", "villiers", "ability", "find", "gaps", "manipulate", "field", "precise", "shots", "key", "strength", "royal", "challengers", "bangalore", "ipl"])
    response("The Royal Challengers Bangalore often relied on AB de Villiers' ability to stabilize the innings and provide a platform for late onslaughts in the IPL.", ["royal", "challengers", "bangalore", "relied", "ab", "de", "villiers", "ability", "stabilize", "innings", "provide", "platform", "late", "onslaughts", "ipl"])
    response("AB de Villiers' ability to read the game and adjust his batting accordingly was a crucial asset for the Royal Challengers Bangalore in the IPL.", ["ab", "de", "villiers", "ability", "read", "game", "adjust", "batting", "accordingly", "crucial", "asset", "royal", "challengers", "bangalore", "ipl"])
    response("The Royal Challengers Bangalore often looked to AB de Villiers to provide stability and acceleration in the middle overs of the IPL.", ["royal", "challengers", "bangalore", "looked", "ab", "de", "villiers", "provide", "stability", "acceleration", "middle", "overs", "ipl"])
    response("AB de Villiers' ability to counterattack and turn the game in his team's favor made him a vital player for the Royal Challengers Bangalore in the IPL.", ["ab", "de", "villiers", "ability", "counterattack", "turn", "game", "team's", "favor", "vital", "player", "royal", "challengers", "bangalore", "ipl"])
    response("The Royal Challengers Bangalore often found themselves in winning positions thanks to AB de Villiers' ability to accelerate the scoring rate in the IPL.", ["royal", "challengers", "bangalore", "found", "winning", "positions", "thanks", "ab", "de", "villiers", "ability", "accelerate", "scoring", "rate", "ipl"])
    response("AB de Villiers' exceptional batting prowess was instrumental in the Royal Challengers Bangalore's success in the IPL.", ["ab", "de", "villiers", "exceptional", "batting", "prowess", "instrumental", "royal", "challengers", "bangalore", "success", "ipl"])
    response("The Royal Challengers Bangalore often looked to AB de Villiers to provide stability and firepower in the middle overs of the IPL.", ["royal", "challengers", "bangalore", "looked", "ab", "de", "villiers", "provide", "stability", "firepower", "middle", "overs", "ipl"])
    response("AB de Villiers' ability to find gaps and manipulate the field with his innovative stroke play was a key asset for the Royal Challengers Bangalore in the IPL.", ["ab", "de", "villiers", "ability", "find", "gaps", "manipulate", "field", "innovative", "stroke", "play", "key", "asset", "royal", "challengers", "bangalore", "ipl"])
    response("The Royal Challengers Bangalore often found themselves in strong positions thanks to AB de Villiers' ability to accelerate the scoring rate in the IPL.", ["royal", "challengers", "bangalore", "found", "strong", "positions", "thanks", "ab", "de", "villiers", "ability", "accelerate", "scoring", "rate", "ipl"])
    response("AB de Villiers' ability to innovate and play unconventional shots made him a nightmare for opposing bowlers in the IPL.", ["ab", "de", "villiers", "ability", "innovate", "play", "unconventional", "shots", "nightmare", "opposing", "bowlers", "ipl"])
    response("The Royal Challengers Bangalore often relied on AB de Villiers' ability to anchor the innings and build partnerships in the IPL.", ["royal", "challengers", "bangalore", "relied", "ab", "de", "villiers", "ability", "anchor", "innings", "build", "partnerships", "ipl"])
    response("AB de Villiers' ability to find gaps and manipulate the field with precise shots was a key strength for the Royal Challengers Bangalore in the IPL.", ["ab", "de", "villiers", "ability", "find", "gaps", "manipulate", "field", "precise", "shots", "key", "strength", "royal", "challengers", "bangalore", "ipl"])
    best_match=max(highest_prob_list,key=highest_prob_list.get)
    #print(highest_prob_list)
    if(highest_prob_list[best_match]==0):
        return "Sorry i am not trained on this topic by the developers,please ask any other question"
    return best_match
def get_response(question):
    split_message=re.split(r'\s+|[,;?!.-]\s*',question.lower())
    response=check_all_messages(split_message)
    return response
print(get_response(que))