import re,time,sys
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
    
    #Virat Kohli
    response("Virat Kohli's full name is Virat Kohli.", ["virat", "kohli", "full", "name"], single_response=True)
    response("Virat Kohli was born on November 5, 1988.", ["virat", "kohli", "born", "date"], single_response=True)
    response("Virat Kohli was born in Delhi, India.", ["virat", "kohli", "born", "place"], single_response=True)
    response("Virat Kohli's batting style is right-handed.", ["virat", "kohli", "batting", "style"], single_response=True)
    response("Virat Kohli's bowling style is right-arm medium.", ["virat", "kohli", "bowling", "style"], single_response=True)
    response("Virat Kohli is 5 feet 9 inches tall.", ["virat", "kohli", "height","tall"], single_response=True)
    response("Virat Kohli's nickname is Chiku.", ["virat", "kohli", "nickname"], single_response=True)
    response("Virat Kohli made his international debut in 2008.", ["virat", "kohli", "international", "debut", "year"], single_response=True)
    response("Virat Kohli made his international debut against Sri Lanka.", ["virat", "kohli", "international", "debut", "opponent"], single_response=True)
    response("Virat Kohli has scored 27 centuries in Test cricket.", ["virat", "kohli", "test", "centuries", "count"], single_response=True)
    response("Virat Kohli has scored 43 centuries in One Day Internationals (ODIs).", ["virat", "kohli", "odi", "centuries", "count"], single_response=True)
    response("Virat Kohli has not scored any centuries in Twenty20 Internationals (T20Is).", ["virat", "kohli", "t20i", "centuries", "count"], single_response=True)
    response("Virat Kohli's highest individual score in Test cricket is 254*.", ["virat", "kohli", "highest", "test", "score"], single_response=True)
    response("Virat Kohli's highest individual score in ODIs is 183.", ["virat", "kohli", "highest", "odi", "score"], single_response=True)
    response("Virat Kohli's highest individual score in T20Is is 94*.", ["virat", "kohli", "highest", "t20i", "score"], single_response=True)
    response("Virat Kohli has scored 7,815 runs in Test cricket.", ["virat", "kohli", "test", "runs", "count"], single_response=True)
    response("Virat Kohli has scored 12,169 runs in ODIs.", ["virat", "kohli", "odi", "runs", "count"], single_response=True)
    response("Virat Kohli has scored 3,159 runs in T20Is.", ["virat", "kohli", "t20i", "runs", "count"], single_response=True)
    response("Virat Kohli's batting average in Test cricket is 52.04.", ["virat", "kohli", "test", "batting", "average"], single_response=True)
    response("Virat Kohli's batting average in ODIs is 59.07.", ["virat", "kohli", "odi", "batting", "average"], single_response=True)
    response("Virat Kohli's batting average in T20Is is 52.93.", ["virat", "kohli", "t20i", "batting", "average"], single_response=True)
    response("Virat Kohli has scored 8 centuries against Australia.", ["virat", "kohli", "centuries", "against", "australia"], single_response=True)
    response("Virat Kohli has scored 11 centuries against England.", ["virat", "kohli", "centuries", "against", "england"], single_response=True)
    response("Virat Kohli has scored 7 centuries against South Africa.", ["virat", "kohli", "centuries", "against", "south africa"], single_response=True)
    response("Virat Kohli has scored 2 centuries against Pakistan.", ["virat", "kohli", "centuries", "against", "pakistan"], single_response=True)
    response("Virat Kohli has scored 9 centuries against Sri Lanka.", ["virat", "kohli", "centuries", "against", "sri lanka"], single_response=True)
    response("Virat Kohli has scored 6 centuries against New Zealand.", ["virat", "kohli", "centuries", "against", "new zealand"], single_response=True)
    response("Virat Kohli has scored 9 centuries against West Indies.", ["virat", "kohli", "centuries", "against", "west indies"], single_response=True)
    response("Virat Kohli has scored 3 centuries against Bangladesh.", ["virat", "kohli", "centuries", "against", "bangladesh"], single_response=True)
    response("Virat Kohli has scored 1 century against Zimbabwe.", ["virat", "kohli", "centuries", "against", "zimbabwe"], single_response=True)
    response("Virat Kohli has scored 1 century against Ireland.", ["virat", "kohli", "centuries", "against", "ireland"], single_response=True)
    response("Virat Kohli has scored 2 centuries against Afghanistan.", ["virat", "kohli", "centuries", "against", "afghanistan"], single_response=True)
    response("Virat Kohli has scored 6 centuries in ICC Cricket World Cup matches.", ["virat", "kohli", "centuries", "in", "world cup"], single_response=True)
    response("Virat Kohli has not scored any centuries in ICC T20 World Cup matches.", ["virat", "kohli", "centuries", "in", "t20 world cup"], single_response=True)
    response("Virat Kohli has scored 4 centuries in ICC Champions Trophy matches.", ["virat", "kohli", "centuries", "in", "champions trophy"], single_response=True)
    response("Virat Kohli has scored 4 centuries in Asia Cup matches.", ["virat", "kohli", "centuries", "in", "asia cup"], single_response=True)
    response("Virat Kohli has scored 5 centuries in IPL matches.", ["virat", "kohli", "centuries", "in", "ipl"], single_response=True)
    response("Virat Kohli has not scored any centuries in Champions League Twenty20 matches.", ["virat", "kohli", "centuries", "in", "clt20"], single_response=True)
    response("Virat Kohli has scored 28 centuries in domestic cricket.", ["virat", "kohli", "centuries", "in", "domestic cricket"], single_response=True)
    response("Virat Kohli has scored 7 centuries in Ranji Trophy matches.", ["virat", "kohli", "centuries", "in", "ranji trophy"], single_response=True)
    response("Virat Kohli has not scored any centuries in Duleep Trophy matches.", ["virat", "kohli", "centuries", "in", "duleep trophy"], single_response=True)
    response("Virat Kohli has not scored any centuries in Irani Cup matches.", ["virat", "kohli", "centuries", "in", "irani cup"], single_response=True)
    response("Virat Kohli has scored 3 centuries in Vijay Hazare Trophy matches.", ["virat", "kohli", "centuries", "in", "vijay hazare trophy"], single_response=True)
    response("Virat Kohli has not scored any centuries in Deodhar Trophy matches.", ["virat", "kohli", "centuries", "in", "deodhar trophy"], single_response=True)
    response("Virat Kohli prefers to bat at number 4 in Test cricket.", ["virat", "kohli", "test", "batting", "position"], single_response=True)
    response("Virat Kohli prefers to bat at number 3 in ODIs.", ["virat", "kohli", "odi", "batting", "position"], single_response=True)
    response("Virat Kohli prefers to bat at number 3 in T20Is.", ["virat", "kohli", "t20i", "batting", "position"], single_response=True)
    response("Some weaknesses in Virat Kohli's batting technique include susceptibility to balls moving away from him early in his innings and occasional vulnerability to short-pitched deliveries.", ["virat", "kohli", "batting", "weaknesses"], single_response=True)
    response("Virat Kohli has shown exceptional skills in playing spinners, making it one of his strengths.", ["virat", "kohli", "batting", "strengths", "spin", "bowlers"], single_response=True)
    response("Virat Kohli is known for his strong cover drives and ability to rotate the strike efficiently.", ["virat", "kohli", "batting", "strengths", "cover", "drives"], single_response=True)
    response("Virat Kohli has struggled against James Anderson's swing bowling in English conditions.", ["virat", "kohli", "batting", "weaknesses", "james", "anderson"], single_response=True)
    response("Virat Kohli has dominated against bowlers like Mitchell Starc in limited-overs cricket.", ["virat", "kohli", "batting", "strengths", "mitchell", "starc"], single_response=True)
    response("Teams like Australia have often targeted Virat Kohli's off-stump early in his innings to exploit his initial vulnerability.", ["virat", "kohli", "batting", "weaknesses", "off", "stump"], single_response=True)
    response("Virat Kohli has expressed admiration for bowlers like Tim Southee, praising their ability to consistently trouble batsmen with swing and seam movement.", ["virat", "kohli", "bowling", "strengths", "tim", "southee"], single_response=True)
    response("In the Indian Premier League (IPL), Virat Kohli captains the Royal Challengers Bangalore (RCB) franchise.", ["virat", "kohli", "ipl", "team", "royal challengers bangalore", "rcb"], single_response=True)
    response("Virat Kohli has faced criticism for his aggressive on-field behavior and confrontations with opposition players.", ["virat", "kohli", "personality", "criticisms", "aggressive", "behavior"], single_response=True)
    response("Virat Kohli has credited his success to his disciplined training regime and relentless pursuit of excellence.", ["virat", "kohli", "success", "factors", "discipline", "training"], single_response=True)
    response("Bowlers like Nathan Lyon have troubled Virat Kohli with their accuracy and ability to exploit rough patches on the pitch.", ["virat", "kohli", "batting", "weaknesses", "nathan", "lyon"], single_response=True)
    response("Virat Kohli is known for his aggressive and animated celebrations after reaching personal milestones or achieving victories for his team.", ["virat", "kohli", "personality", "characteristics", "celebrations", "aggressive"], single_response=True)
    response("Virat Kohli's technique against the short ball has been a subject of scrutiny, especially in overseas Test matches.", ["virat", "kohli", "batting", "weaknesses", "short", "ball"], single_response=True)
    response("Virat Kohli has a habit of tapping the pitch with his bat before facing a delivery, a ritual he follows to maintain focus and concentration.", ["virat", "kohli", "batting", "rituals", "pitch", "tapping"], single_response=True)
    response("Virat Kohli is known for his exceptional fitness levels and strict diet regimen, which contribute to his endurance and agility on the field.", ["virat", "kohli", "fitness", "regimen", "diet", "endurance"], single_response=True)
    response("Virat Kohli has expressed admiration for cricketers like AB de Villiers, citing their unorthodox yet effective batting styles as sources of inspiration.", ["virat", "kohli", "cricket", "inspirations", "ab de villiers"], single_response=True)
    response("Virat Kohli has been praised for his ability to chase down targets in limited-overs cricket, earning him the nickname 'Chase Master'.", ["virat", "kohli", "nickname", "chase", "master"], single_response=True)
    response("Virat Kohli's aggressive captaincy style has been credited for India's improved performance in overseas Test matches.", ["virat", "kohli", "captaincy", "style", "aggressive"], single_response=True)
    response("Virat Kohli's dedication to fitness and training has inspired many young cricketers to prioritize physical conditioning alongside their skill development.", ["virat", "kohli", "impact", "inspiration", "fitness", "training"], single_response=True)
    response("Virat Kohli has a strong record of converting fifties into centuries in international cricket, showcasing his ability to capitalize on good starts.", ["virat", "kohli", "batting", "strengths", "conversion", "fifties", "centuries"], single_response=True)
    response("Virat Kohli has openly discussed his struggles with mental health issues, advocating for greater awareness and support in the sporting community.", ["virat", "kohli", "mental", "health", "awareness", "advocacy"], single_response=True)
    response("Virat Kohli's aggressive batting approach has often put pressure on opposition bowlers, forcing them to alter their game plans.", ["virat", "kohli", "batting", "style", "aggressive", "approach"], single_response=True)
    response("Virat Kohli's meticulous planning and preparation ahead of matches have been commended by teammates and coaches alike.", ["virat", "kohli", "preparation", "planning", "meticulous"], single_response=True)
    response("Virat Kohli's competitiveness and desire to win have sometimes led to on-field altercations with opponents, reflecting his intense passion for the game.", ["virat", "kohli", "competitiveness", "desire", "winning", "passion"], single_response=True)
    response("Virat Kohli's aggressive style of play has often brought him under scrutiny from match officials for breaching the ICC Code of Conduct.", ["virat", "kohli", "icc", "code", "conduct", "breaches"], single_response=True)
    response("Virat Kohli's preference for chasing targets in limited-overs cricket has been attributed to his confidence in his ability to control run chases effectively.", ["virat", "kohli", "batting", "strategy", "chasing", "targets"], single_response=True)
    response("Virat Kohli's ability to maintain high levels of performance under pressure situations has earned him the reputation of a 'Big Match Player'.", ["virat", "kohli", "nickname", "big", "match", "player"], single_response=True)
    response("Virat Kohli has faced criticism for his occasional impulsive decisions on the field, particularly in terms of team selection and bowling changes.", ["virat", "kohli", "captaincy", "criticisms", "impulsive", "decisions"], single_response=True)
    response("Virat Kohli's aggressive brand of cricket has attracted a massive following among fans, making him one of the most marketable athletes globally.", ["virat", "kohli", "brand", "image", "aggressive", "cricket"], single_response=True)
    response("Virat Kohli's proficiency in playing the cover drive has been compared to batting legends like Sachin Tendulkar and Ricky Ponting.", ["virat", "kohli", "batting", "style", "cover", "drive", "proficiency"], single_response=True)
    response("Virat Kohli's commitment to his craft and relentless pursuit of excellence have established him as a role model for aspiring cricketers worldwide.", ["virat", "kohli", "role", "model", "commitment", "excellence"], single_response=True)
    response("Virat Kohli's aggressive leadership style has often been lauded for instilling a winning mentality in the Indian cricket team.", ["virat", "kohli", "leadership", "style", "aggressive", "winning", "mentality"], single_response=True)
    response("Virat Kohli's ability to adapt to different formats of the game seamlessly has made him one of the most versatile batsmen in modern cricket.", ["virat", "kohli", "batting", "versatility", "adaptability"], single_response=True)
    response("Virat Kohli's aggressive approach to batting has been a driving force behind India's successful run chases in limited-overs cricket.", ["virat", "kohli", "batting", "style", "aggressive", "approach", "run", "chases"], single_response=True)
    response("Virat Kohli's dedication to physical fitness and diet discipline has significantly extended his playing career at the highest level.", ["virat", "kohli", "fitness", "discipline", "career", "longevity"], single_response=True)
    response("Virat Kohli's ability to score runs consistently across all formats of the game has earned him widespread recognition as one of the modern greats of cricket.", ["virat", "kohli", "batting", "consistency", "greatness"], single_response=True)
    response("Virat Kohli's aggressive demeanor on the field has occasionally led to clashes with opposition players and heated exchanges during matches.", ["virat", "kohli", "personality", "aggressive", "demeanor", "clashes"], single_response=True)
    response("Virat Kohli's unwavering self-belief and confidence in his abilities have been instrumental in his success as a cricketer.", ["virat", "kohli", "confidence", "self-belief", "success", "instrumental"], single_response=True)
    response("Virat Kohli's aggressive style of play has often drawn comparisons to former Australian cricketer Ricky Ponting, known for his aggressive captaincy and batting.", ["virat", "kohli", "comparisons", "ricky", "ponting", "aggressive", "style"], single_response=True)
    response("Virat Kohli's exceptional fitness levels and work ethic have set new benchmarks for professional athletes across various sports disciplines.", ["virat", "kohli", "fitness", "benchmarks", "work", "ethic"], single_response=True)
    response("Virat Kohli's leadership qualities have been praised by former cricketers and pundits, who commend his ability to lead by example on and off the field.", ["virat", "kohli", "leadership", "qualities", "commendation", "lead", "example"], single_response=True)
    response("Virat Kohli's aggressive captaincy style has been credited for India's aggressive brand of cricket, marked by fearless batting and attacking field placements.", ["virat", "kohli", "captaincy", "style", "aggressive", "brand", "cricket"], single_response=True)
    response("Virat Kohli's dedication to physical fitness and training routines has inspired a new generation of cricketers to prioritize health and conditioning.", ["virat", "kohli", "fitness", "inspiration", "health", "conditioning"], single_response=True)
    response("Virat Kohli's aggressive batting style has often led to comparisons with former Indian cricketer Sourav Ganguly, known for his fearless approach to batting.", ["virat", "kohli", "comparisons", "sourav", "ganguly", "aggressive", "batting", "style"], single_response=True)
    response("Virat Kohli's aggressive personality on the field has occasionally resulted in disciplinary issues, including fines and reprimands from cricket authorities.", ["virat", "kohli", "discipline", "issues", "disciplinary", "actions"], single_response=True)
    response("Virat Kohli's aggressive on-field demeanor has earned him the reputation of a fierce competitor who never shies away from a challenge.", ["virat", "kohli", "personality", "aggressive", "demeanor", "fierce", "competitor"], single_response=True)
    response("Virat Kohli's aggressive captaincy style has been credited for India's bold approach in setting aggressive targets and attacking opponents from the outset.", ["virat", "kohli", "captaincy", "style", "aggressive", "approach", "targets"], single_response=True)
    response("Virat Kohli's aggressive batting approach has often put pressure on opposition bowlers, compelling them to bowl defensively and stray from their game plans.", ["virat", "kohli", "batting", "style", "aggressive", "approach", "pressure", "bowlers"], single_response=True)
    response("Virat Kohli's aggressive personality and competitive spirit have made him a favorite among fans, who admire his fearless attitude on the field.", ["virat", "kohli", "personality", "aggressive", "spirit", "fan", "favorite"], single_response=True)
    response("Virat Kohli's aggressive approach to batting has often led to confrontations with opposition players, adding spice to high-pressure encounters.", ["virat", "kohli", "batting", "style", "aggressive", "approach", "confrontations"], single_response=True)
    response("Virat Kohli's aggressive leadership style has been instrumental in India's success in limited-overs cricket, where they have adopted an aggressive mindset.", ["virat", "kohli", "leadership", "style", "aggressive", "success", "limited-overs", "cricket"], single_response=True)
    response("Virat Kohli's aggressive approach to batting has often rattled opposition bowlers, forcing them into defensive lines and lengths.", ["virat", "kohli", "batting", "style", "aggressive", "approach", "rattled", "bowlers"], single_response=True)
    response("Virat Kohli's aggressive attitude on the field has occasionally landed him in trouble with match officials, who have penalized him for breaches of conduct.", ["virat", "kohli", "attitude", "trouble", "match", "officials", "conduct", "breaches"], single_response=True)
    response("Virat Kohli's aggressive style of play has often turned matches in India's favor, with his aggressive approach setting the tone for the team's performance.", ["virat", "kohli", "style", "play", "aggressive", "approach", "match", "impact"], single_response=True)
    response("Virat Kohli's aggressive batting style has often seen him dominate opposition bowlers, particularly in run chases and high-pressure situations.", ["virat", "kohli", "batting", "style", "aggressive", "dominance", "bowlers"], single_response=True)
    response("Virat Kohli's aggressive approach to captaincy has been praised for its effectiveness in motivating players and instilling a winning mentality in the team.", ["virat", "kohli", "captaincy", "style", "aggressive", "effectiveness", "motivation"], single_response=True)
    response("Virat Kohli's aggressive demeanor on the field has made him a polarizing figure, with fans either loving or hating his confrontational style of play.", ["virat", "kohli", "personality", "aggressive", "demeanor", "polarizing", "figure"], single_response=True)
    response("Virat Kohli's aggressive batting style has often led to comparisons with former West Indian cricketer Vivian Richards, known for his fearless strokeplay.", ["virat", "kohli", "comparisons", "vivian", "richards", "aggressive", "batting", "style"], single_response=True)
    response("Virat Kohli's aggressive approach to batting has often seen him take the attack to opposition bowlers, dictating terms and putting pressure on them.", ["virat", "kohli", "batting", "style", "aggressive", "approach", "attack", "pressure"], single_response=True)
    response("Virat Kohli's aggressive batting style has often seen him take calculated risks, backing his ability to dominate bowlers and dictate terms in the middle.", ["virat", "kohli", "batting", "style", "aggressive", "risks", "calculated", "dominance"], single_response=True)
    response("Virat Kohli's aggressive approach to batting has often unsettled opposition captains, who struggle to contain his aggressive strokeplay and momentum-building innings.", ["virat", "kohli", "batting", "style", "aggressive", "approach", "captains", "unsettled"], single_response=True)
    response("Virat Kohli's aggressive attitude on the field has occasionally led to verbal altercations with opposition players, adding spice to the contest.", ["virat", "kohli", "personality", "aggressive", "attitude", "altercations", "verbal"], single_response=True)
    response("Virat Kohli's aggressive batting style has often seen him target specific bowlers, looking to dominate and demoralize them with aggressive strokeplay.", ["virat", "kohli", "batting", "style", "aggressive", "targeting", "bowlers", "dominance"], single_response=True)
    response("Virat Kohli's aggressive approach to batting has often seen him take the attack to opposition bowlers, putting them under pressure from the outset.", ["virat", "kohli", "batting", "style", "aggressive", "approach", "attack", "pressure"], single_response=True)
    response("Virat Kohli's aggressive demeanor on the field has occasionally led to clashes with match officials, who have reprimanded him for breaching the ICC Code of Conduct.", ["virat", "kohli", "personality", "aggressive", "demeanor", "clashes", "icc", "code", "conduct"], single_response=True)
    response("Virat Kohli's aggressive batting style has often seen him take on the responsibility of anchoring the innings while maintaining a high scoring rate.", ["virat", "kohli", "batting", "style", "aggressive", "responsibility", "anchoring", "innings"], single_response=True)
    response("Virat Kohli's aggressive approach to batting has often seen him dominate opposition spinners, disrupting their lines and lengths with aggressive footwork and shot selection.", ["virat", "kohli", "batting", "style", "aggressive", "approach", "spinners", "dominance"], single_response=True)
    response("Virat Kohli's aggressive attitude on the field has occasionally led to clashes with opposition players, sparking heated confrontations and on-field altercations.", ["virat", "kohli", "personality", "aggressive", "attitude", "clashes", "confrontations"], single_response=True)
    response("Virat Kohli's aggressive approach to batting has often seen him play a pivotal role in India's run chases, with his aggressive strokeplay demoralizing opposition bowlers.", ["virat", "kohli", "batting", "style", "aggressive", "approach", "run", "chases", "pivotal"], single_response=True)
    response("Virat Kohli's aggressive batting style has often seen him thrive under pressure situations, with his aggressive approach unsettling opposition bowlers and captains alike.", ["virat", "kohli", "batting", "style", "aggressive", "approach", "pressure", "thrive"], single_response=True)
    response("Virat Kohli's aggressive demeanor on the field has occasionally led to disciplinary issues, with match officials sanctioning him for breaches of the ICC Code of Conduct.", ["virat", "kohli", "personality", "aggressive", "demeanor", "disciplinary", "issues"], single_response=True)
    response("Virat Kohli's aggressive approach to batting has often seen him seize control of the game, with his aggressive strokeplay putting opposition bowlers on the back foot.", ["virat", "kohli", "batting", "style", "aggressive", "approach", "seize", "control"], single_response=True)
    response("Virat Kohli's aggressive batting style has often seen him target opposition bowlers' weaknesses, looking to exploit any signs of vulnerability with aggressive shotmaking.", ["virat", "kohli", "batting", "style", "aggressive", "targeting", "weaknesses"], single_response=True)
    response("Virat Kohli's aggressive attitude on the field has occasionally led to clashes with opposition players, with umpires intervening to diffuse tense situations.", ["virat", "kohli", "personality", "aggressive", "attitude", "clashes", "umpires", "intervening"], single_response=True)
    response("Virat Kohli's aggressive approach to batting has often seen him take calculated risks, backing his ability to dominate bowlers and dictate terms in the middle.", ["virat", "kohli", "batting", "style", "aggressive", "approach", "risks", "calculated"], single_response=True)
    response("Virat Kohli's aggressive demeanor on the field has occasionally led to altercations with opposition players, with both sides engaging in verbal exchanges.", ["virat", "kohli", "personality", "aggressive", "demeanor", "altercations"], single_response=True)
    response("Virat Kohli's aggressive batting style has often seen him dictate the course of the game, with his aggressive approach putting opposition bowlers under immense pressure.", ["virat", "kohli", "batting", "style", "aggressive", "approach", "dictate", "game"], single_response=True)
    response("Virat Kohli's aggressive approach to batting has often seen him thrive in high-pressure situations, with his aggressive strokeplay demoralizing opposition bowlers.", ["virat", "kohli", "batting", "style", "aggressive", "approach", "thrive", "pressure"], single_response=True)
    response("Virat Kohli's aggressive demeanor on the field has occasionally led to confrontations with match officials, who have had to step in to calm tensions.", ["virat", "kohli", "personality", "aggressive", "demeanor", "confrontations", "officials"], single_response=True)
    response("Virat Kohli's aggressive batting style has often seen him capitalize on opposition bowlers' mistakes, punishing any loose deliveries with aggressive shotmaking.", ["virat", "kohli", "batting", "style", "aggressive", "capitalize", "mistakes"], single_response=True)
    response("Virat Kohli's aggressive approach to batting has often seen him assert his dominance over opposition bowlers, with his aggressive strokeplay dictating the flow of the game.", ["virat", "kohli", "batting", "style", "aggressive", "approach", "dominance", "assert"], single_response=True)
    response("Virat Kohli's aggressive demeanor on the field has occasionally led to heated altercations with opposition players, with both sides refusing to back down.", ["virat", "kohli", "personality", "aggressive", "demeanor", "altercations", "heated"], single_response=True)
    response("Virat Kohli's aggressive approach to batting has often seen him target opposition bowlers' weaknesses, exploiting any signs of vulnerability with aggressive shotmaking.", ["virat", "kohli", "batting", "style", "aggressive", "approach", "target", "weaknesses"], single_response=True)
    response("Virat Kohli's aggressive batting style has often seen him take the fight to opposition bowlers, with his aggressive strokeplay dictating the tempo of the game.", ["virat", "kohli", "batting", "style", "aggressive", "take", "fight"], single_response=True)



    best_match=max(highest_prob_list,key=highest_prob_list.get)
    #print(highest_prob_list)
    if(highest_prob_list[best_match]==0):
        return "Sorry i am not trained on this topic by the developers,please ask any other question"
    return best_match
def get_response(question):
    split_message=re.split(r'\s+|[,;?!.-]\s*',question.lower())
    response=check_all_messages(split_message)
    return response
#delayed_print("BERT: Hello, I am BERT ask me any cricket related queries ")
print(get_response(que))