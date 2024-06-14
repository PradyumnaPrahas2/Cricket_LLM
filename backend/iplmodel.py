try:
    import warnings
    warnings.filterwarnings('ignore')
    import pickle
    model=pickle.load(open("bestiplmodel","rb"))
    model2=pickle.load(open("2ndbestmodel","rb"))
    import sys
    team1=str(sys.argv[1])
    # team1="SRH"
    team2=str(sys.argv[2])
    # team2="MI"
    venue=str(sys.argv[3])
    # venue="Hyderabad"
    toss_winner=str(sys.argv[4])
    toss_decision=str(sys.argv[5])
    teams={'RR': 0,'RCB': 1,'SRH': 2,'DC': 3,'CSK': 4,'GT': 5,'LSG': 6,'KKR': 7,'PBKS': 8,'MI': 9,'RPS': 10,'GL': 11,'PW': 12,'DEC': 13,'KTK': 14}
    venues={'Ahmedabad': 0,
    'Kolkata': 1,
    'Mumbai': 2,
    'Navi Mumbai': 3,
    'Pune': 4,
    'Dubai': 5,
    'Sharjah': 6,
    'Abu Dhabi': 7,
    'Delhi': 8,
    'Chennai': 9,
    'Hyderabad': 10,
    'Visakhapatnam': 11,
    'Chandigarh': 12,
    'Bengaluru': 13,
    'Jaipur': 14,
    'Indore': 15,
    'Kanpur': 16,
    'Rajkot': 17,
    'Raipur': 18,
    'Ranchi': 19,
    'Cuttack': 20,
    'Dharamsala': 21,
    'Kochi': 22,
    'Nagpur': 23,
    'Johannesburg': 24,
    'Centurion': 25,
    'Durban': 26,
    'Bloemfontein': 27,
    'Port Elizabeth': 28,
    'Kimberley': 29,
    'East London': 30,
    'Cape Town': 31}
    toss={'bat':0,'field':1}
    team1=teams[team1]
    team2=teams[team2]
    venue=venues[venue]
    toss_winner=teams[toss_winner]
    toss_decision=toss[toss_decision]
    import numpy as np
    x_test=np.array([np.array([venue,team2,team1,toss_winner,toss_decision])])
    ans=model.predict(x_test)
    if(ans!=team2 and ans!=team1):
        ans=model2.predict(x_test)
    for key,values in teams.items():
        if(teams[key]==ans):
            print(key)
except Exception as e:
    print(e)