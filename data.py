MEDIAS_REPERTORY = "./medias/"

train_colors = ["grey", "white", "yellow", "red", "orange", "blue", "green", "pink", "locomotive"]
players_colors = ["black", "yellow", "red", "blue", "green"]

cities = [
    "Amsterdam",
    "Angora",
    "Athina",
    "Barcelona",
    "Berlin",
    "Brest",
    "Brindisi",
    "Bruxelles",
    "Bucuresti",
    "Budapest",
    "Cadiz",
    "Constantinople",
    "Danzig",
    "Dieppe",
    "Edinburgh",
    "Erzurum",
    "Essen",
    "Frankfurt",
    "Kharkov",
    "Kobenhavn",
    "Kyiv",
    "Lisboa",
    "London",
    "Madrid",
    "Marseille",
    "Moskva",
    "Munchen",
    "Palermo",
    "Pamplona",
    "Paris",
    "Petrograd",
    "Riga",
    "Roma",
    "Rostov",
    "Sarajevo",
    "Sevastopol",
    "Smolensk",
    "Smyrna",
    "Sochi",
    "Sofia",
    "Stockholm",
    "Venezia",
    "Warszawa",
    "Wien",
    "Wilno",
    "Zagrab",
    "Zurich"
]


tickets_short = [
    {
        "city_a": "Athina",
        "city_b": "Angora",
        "value": 5
    },
    {
        "city_a": "Budapest",
        "city_b": "Sofia",
        "value": 5
    },
    {
        "city_a": "Frankfurt",
        "city_b": "Kobenhavn",
        "value": 5
    },
    {
        "city_a": "Rostov",
        "city_b": "Erzurum",
        "value": 5
    },
    {
        "city_a": "Sofia",
        "city_b": "Smyrna",
        "value": 5
    },
    {
        "city_a": "Kyiv",
        "city_b": "Petrograd",
        "value": 6
    },
    {
        "city_a": "Warszawa",
        "city_b": "Smolensk",
        "value": 6
    },
    {
        "city_a": "Zagrab",
        "city_b": "Brindisi",
        "value": 6
    },
    {
        "city_a": "Zurich",
        "city_b": "Brindisi",
        "value": 6
    },
    {
        "city_a": "Zurich",
        "city_b": "Budapest",
        "value": 6
    },
    {
        "city_a": "Amsterdam",
        "city_b": "Pamplona",
        "value": 7
    },
    {
        "city_a": "Brest",
        "city_b": "Marseille",
        "value": 7
    },
    {
        "city_a": "Edinburgh",
        "city_b": "paris",
        "value": 7
    },
    {
        "city_a": "London",
        "city_b": "Berlin",
        "value": 7
    },
    {
        "city_a": "Paris",
        "city_b": "Zagrab",
        "value": 7
    },
    {
        "city_a": "Barcelona",
        "city_b": "Muchen",
        "value": 8
    },
    {
        "city_a": "Barcelona",
        "city_b": "Bruxelles",
        "value": 8
    },
    {
        "city_a": "Berlin",
        "city_b": "Bucuresti",
        "value": 8
    },
    {
        "city_a": "Brest",
        "city_b": "Venezia",
        "value": 8
    },
    {
        "city_a": "Kyiv",
        "city_b": "Sochi",
        "value": 8
    },
    {
        "city_a": "Madrid",
        "city_b": "Dieppe",
        "value": 8
    },
    {
        "city_a": "Madrid",
        "city_b": "Zurich",
        "value": 8
    },
    {
        "city_a": "Marseille",
        "city_b": "Essen",
        "value": 8
    },
    {
        "city_a": "Palermo",
        "city_b": "Constantinople",
        "value": 8
    },
    {
        "city_a": "Paris",
        "city_b": "Wien",
        "value": 8
    },
    {
        "city_a": "Roma",
        "city_b": "Smyrna",
        "value": 8
    },
    {
        "city_a": "Sarajevo",
        "city_b": "Sevastopl",
        "value": 8
    },
    {
        "city_a": "Smolensk",
        "city_b": "Rostov",
        "value": 8
    },
    {
        "city_a": "Berlin",
        "city_b": "Roma",
        "value": 9
    },
    {
        "city_a": "Bruxelles",
        "city_b": "Danzig",
        "value": 9
    },
    {
        "city_a": "Angora",
        "city_b": "Kharkov",
        "value": 10
    },
    {
        "city_a": "Essen",
        "city_b": "Kyiv",
        "value": 10
    },
    {
        "city_a": "London",
        "city_b": "Wien",
        "value": 10
    },
    {
        "city_a": "Riga",
        "city_b": "Bucuresti",
        "value": 10
    },
    {
        "city_a": "Venizia",
        "city_b": "Constantinople",
        "value": 10
    },
    {
        "city_a": "Athina",
        "city_b": "Wilno",
        "value": 11
    },
    {
        "city_a": "Stockholm",
        "city_b": "Wien",
        "value": 11
    },
    {
        "city_a": "Amsterdam",
        "city_b": "Wilno",
        "value": 12
    },
    {
        "city_a": "Berlin",
        "city_b": "Moskva",
        "value": 12
    },
    {
        "city_a": "Frankfurt",
        "city_b": "Smolensk",
        "value": 13
    }
]
    
tickets_long = [
    {
        "city_a": "Brest",
        "city_b": "Petrograd",
        "value": 20
    },
    {
        "city_a": "Lisboa",
        "city_b": "Danzig",
        "value": 20
    },
    {
        "city_a": "Palermo",
        "city_b": "Moskva",
        "value": 20
    },
    {
        "city_a": "Cadiz",
        "city_b": "Stockholm",
        "value": 21
    },
    {
        "city_a": "Edinburgh",
        "city_b": "Athena",
        "value": 21
    },
    {
        "city_a": "Kobenhavn",
        "city_b": "Erzurum",
        "value": 21
    }
]


scoresGuide = {
    1:1,
    2:2,
    3:4,
    4:7,
    5:10,
    6:15
}


routes = [
    {
        "city_a": "Amsterdam",
        "city_b": "London",
        "color" : "",
        "lenght": 2,
        "locomotive": 2,
        "tunnel" : False
    },
    {
        "city_a": "Amsterdam",
        "city_b": "Bruxelles",
        "color" : "grey",
        "lenght": 1,
        "locomotive": 0,
        "tunnel" : False
    },
    {
        "city_a": "Amsterdam",
        "city_b": "Essen",
        "color" : "yellow",
        "lenght": 3,
        "locomotive": 0,
        "tunnel" : False
    },
    ###############################
    {
        "city_a": "Angora",
        "city_b": "Smyrna",
        "color" : "orange",
        "lenght": 2,
        "locomotive": 0,
        "tunnel" : True
    },
    {
        "city_a": "Angora",
        "city_b": "Constantinople",
        "color" : "",
        "lenght": 2,
        "locomotive": 0,
        "tunnel" : True
    },
    {
        "city_a": "Angora",
        "city_b": "Erzurum",
        "color" : "grey",
        "lenght": 3,
        "locomotive": 0,
        "tunnel" : False
    },
    ###############################
    {
        "city_a": "Athina",
        "city_b": "Brindisi",
        "color" : "",
        "lenght": 4,
        "locomotive": 1,
        "tunnel" : False
    },
    {
        "city_a": "Athina",
        "city_b": "Sarajevo",
        "color" : "green",
        "lenght": 4,
        "locomotive": 0,
        "tunnel" : False
    },
    {
        "city_a": "Athina",
        "city_b": "Sofia",
        "color" : "pink",
        "lenght": 3,
        "locomotive": 0,
        "tunnel" : False
    },
    {
        "city_a": "Athina",
        "city_b": "Smyrna",
        "color" : "",
        "lenght": 2,
        "locomotive": 1,
        "tunnel" : False
    },
    ###############################
    {
        "city_a": "Barcelona",
        "city_b": "Madrid",
        "color" : "yellow",
        "lenght": 2,
        "locomotive": 0,
        "tunnel" : False
    },
    {
        "city_a": "Barcelona",
        "city_b": "Pamplona",
        "color" : "",
        "lenght": 2,
        "locomotive": 0,
        "tunnel" : True
    },
    {
        "city_a": "Barcelona",
        "city_b": "Marseille",
        "color" : "",
        "lenght": 4,
        "locomotive": 0,
        "tunnel" : False
    },
    ###############################
    {
        "city_a": "Berlin",
        "city_b": "Frankfurt",
        "color" : "grey",
        "lenght": 3,
        "locomotive": 0,
        "tunnel" : False
    },
    {
        "city_a": "Berlin",
        "city_b": "Frankfurt",
        "color" : "red",
        "lenght": 3,
        "locomotive": 0,
        "tunnel" : False
    },
    {
        "city_a": "Berlin",
        "city_b": "Essen",
        "color" : "blue",
        "lenght": 2,
        "locomotive": 0,
        "tunnel" : False
    },
    {
        "city_a": "Berlin",
        "city_b": "Danzig",
        "color" : "",
        "lenght": 4,
        "locomotive": 0,
        "tunnel" : False
    },
    {
        "city_a": "Berlin",
        "city_b": "Warszawa",
        "color" : "pink",
        "lenght": 4,
        "locomotive": 0,
        "tunnel" : False
    },
    {
        "city_a": "Berlin",
        "city_b": "Warszawa",
        "color" : "yellow",
        "lenght": 4,
        "locomotive": 0,
        "tunnel" : False
    },
    {
        "city_a": "Berlin",
        "city_b": "Wien",
        "color" : "green",
        "lenght": 3,
        "locomotive": 0,
        "tunnel" : False
    },
    ###############################
    {
        "city_a": "Brest",
        "city_b": "Dieppe",
        "color" : "orange",
        "lenght": 2,
        "locomotive": 0,
        "tunnel" : False
    },
    {
        "city_a": "Brest",
        "city_b": "Paris",
        "color" : "grey",
        "lenght": 3,
        "locomotive": 0,
        "tunnel" : False
    },
    {
        "city_a": "Brest",
        "city_b": "Pamplona",
        "color" : "pink",
        "lenght": 4,
        "locomotive": 0,
        "tunnel" : False
    },
    ###############################
    {
        "city_a": "Brindisi",
        "city_b": "Roma",
        "color" : "white",
        "lenght": 2,
        "locomotive": 0,
        "tunnel" : False
    },
    {
        "city_a": "Brindisi",
        "city_b": "Palermo",
        "color" : "",
        "lenght": 3,
        "locomotive": 0,
        "tunnel" : False
    },
    ###############################
    {
        "city_a": "Bruxelles",
        "city_b": "Paris",
        "color" : "yellow",
        "lenght": 2,
        "locomotive": 0,
        "tunnel" : False
    },
    {
        "city_a": "Bruxelles",
        "city_b": "Paris",
        "color" : "red",
        "lenght": 2,
        "locomotive": 0,
        "tunnel" : False
    },
    {
        "city_a": "Bruxelles",
        "city_b": "Dieppe",
        "color" : "green",
        "lenght": 2,
        "locomotive": 0,
        "tunnel" : False
    },
    {
        "city_a": "Bruxelles",
        "city_b": "Frankfurt",
        "color" : "blue",
        "lenght": 2,
        "locomotive": 0,
        "tunnel" : False
    },
    ###############################
    {
        "city_a": "Bucuresti",
        "city_b": "Sofia",
        "color" : "",
        "lenght": 2,
        "locomotive": 0,
        "tunnel" : True
    },
    {
        "city_a": "Bucuresti",
        "city_b": "Budapest",
        "color" : "",
        "lenght": 4,
        "locomotive": 0,
        "tunnel" : True
    },
    {
        "city_a": "Bucuresti",
        "city_b": "Kyiv",
        "color" : "",
        "lenght": 4,
        "locomotive": 0,
        "tunnel" : False
    },
    {
        "city_a": "Bucuresti",
        "city_b": "Sevastopol",
        "color" : "white",
        "lenght": 4,
        "locomotive": 0,
        "tunnel" : False
    },
    {
        "city_a": "Bucuresti",
        "city_b": "Constantinople",
        "color" : "yellow",
        "lenght": 3,
        "locomotive": 0,
        "tunnel" : False
    },
    ###############################
    {
        "city_a": "Budapest",
        "city_b": "Sarajevo",
        "color" : "pink",
        "lenght": 3,
        "locomotive": 0,
        "tunnel" : False
    },
    {
        "city_a": "Budapest",
        "city_b": "Zagrab",
        "color" : "orange",
        "lenght": 2,
        "locomotive": 0,
        "tunnel" : False
    },
    {
        "city_a": "Budapest",
        "city_b": "Wien",
        "color" : "red",
        "lenght": 1,
        "locomotive": 0,
        "tunnel" : False
    },
    {
        "city_a": "Budapest",
        "city_b": "Wien",
        "color" : "white",
        "lenght": 1,
        "locomotive": 0,
        "tunnel" : False
    },
    {
        "city_a": "Budapest",
        "city_b": "Kyiv",
        "color" : "",
        "lenght": 6,
        "locomotive": 0,
        "tunnel" : True
    },
    ###############################
    {
        "city_a": "Cadiz",
        "city_b": "Madrid",
        "color" : "orange",
        "lenght": 3,
        "locomotive": 0,
        "tunnel" : False
    },
    {
        "city_a": "Cadiz",
        "city_b": "Lisboa",
        "color" : "blue",
        "lenght": 2,
        "locomotive": 0,
        "tunnel" : False
    },
    ###############################
    {
        "city_a": "Constantinople",
        "city_b": "Smyrna",
        "color" : "",
        "lenght": 2,
        "locomotive": 0,
        "tunnel" : True
    },
    {
        "city_a": "Constantinople",
        "city_b": "Sofia",
        "color" : "blue",
        "lenght": 3,
        "locomotive": 0,
        "tunnel" : False
    },
    {
        "city_a": "Constantinople",
        "city_b": "Sevastopol",
        "color" : "",
        "lenght": 4,
        "locomotive": 2,
        "tunnel" : False
    },
    ###############################
    {
        "city_a": "Danzig",
        "city_b": "Riga",
        "color" : "grey",
        "lenght": 3,
        "locomotive": 0,
        "tunnel" : False
    },
    {
        "city_a": "Danzig",
        "city_b": "Warszawa",
        "color" : "",
        "lenght": 2,
        "locomotive": 0,
        "tunnel" : False
    },
    ###############################
    {
        "city_a": "Dieppe",
        "city_b": "Paris",
        "color" : "pink",
        "lenght": 1,
        "locomotive": 0,
        "tunnel" : False
    },
    {
        "city_a": "Dieppe",
        "city_b": "London",
        "color" : "",
        "lenght": 2,
        "locomotive": 1,
        "tunnel" : False
    },
    {
        "city_a": "Dieppe",
        "city_b": "London",
        "color" : "",
        "lenght": 2,
        "locomotive": 1,
        "tunnel" : False
    },
    ###############################
    {
        "city_a": "Edinburgh",
        "city_b": "London",
        "color" : "orange",
        "lenght": 4,
        "locomotive": 0,
        "tunnel" : False
    },
    {
        "city_a": "Edinburgh",
        "city_b": "London",
        "color" : "grey",
        "lenght": 4,
        "locomotive": 0,
        "tunnel" : False
    },
    ###############################
    {
        "city_a": "Erzurum",
        "city_b": "Sochi",
        "color" : "red",
        "lenght": 3,
        "locomotive": 0,
        "tunnel" : True
    },
    {
        "city_a": "Erzurum",
        "city_b": "Sevastopol",
        "color" : "",
        "lenght": 4,
        "locomotive": 2,
        "tunnel" : False
    },
    ###############################
    {
        "city_a": "Essen",
        "city_b": "Frankfurt",
        "color" : "green",
        "lenght": 2,
        "locomotive": 0,
        "tunnel" : False
    },
    {
        "city_a": "Essen",
        "city_b": "Kobenhavn",
        "color" : "",
        "lenght": 3,
        "locomotive": 1,
        "tunnel" : False
    },
    {
        "city_a": "Essen",
        "city_b": "Kobenhavn",
        "color" : "",
        "lenght": 3,
        "locomotive": 1,
        "tunnel" : False
    },
    ###############################
    {
        "city_a": "Frankfurt",
        "city_b": "Munchen",
        "color" : "pink",
        "lenght": 2,
        "locomotive": 0,
        "tunnel" : False
    },
    {
        "city_a": "Frankfurt",
        "city_b": "Paris",
        "color" : "white",
        "lenght": 3,
        "locomotive": 0,
        "tunnel" : False
    },
    {
        "city_a": "Frankfurt",
        "city_b": "Paris",
        "color" : "orange",
        "lenght": 3,
        "locomotive": 0,
        "tunnel" : False
    },
    ###############################
    {
        "city_a": "Kharkov",
        "city_b": "Moskva",
        "color" : "",
        "lenght": 4,
        "locomotive": 0,
        "tunnel" : False
    },
    {
        "city_a": "Kharkov",
        "city_b": "Kyiv",
        "color" : "",
        "lenght": 4,
        "locomotive": 0,
        "tunnel" : False
    },
    {
        "city_a": "Kharkov",
        "city_b": "Rostov",
        "color" : "green",
        "lenght": 2,
        "locomotive": 0,
        "tunnel" : False
    },
    ###############################
    {
        "city_a": "Kobenhavn",
        "city_b": "Stockholm",
        "color" : "white",
        "lenght": 3,
        "locomotive": 0,
        "tunnel" : False
    },
    {
        "city_a": "Kobenhavn",
        "city_b": "Stockholm",
        "color" : "yellow",
        "lenght": 3,
        "locomotive": 0,
        "tunnel" : False
    },
    ###############################
    {
        "city_a": "Kyiv",
        "city_b": "Warszawa",
        "color" : "",
        "lenght": 4,
        "locomotive": 0,
        "tunnel" : False
    },
    {
        "city_a": "Kyiv",
        "city_b": "Wilno",
        "color" : "",
        "lenght": 2,
        "locomotive": 0,
        "tunnel" : False
    },
    {
        "city_a": "Kyiv",
        "city_b": "Smolensk",
        "color" : "red",
        "lenght": 3,
        "locomotive": 0,
        "tunnel" : False
    },
    ###############################
    {
        "city_a": "Lisboa",
        "city_b": "Madrid",
        "color" : "pink",
        "lenght": 3,
        "locomotive": 0,
        "tunnel" : False
    },
    ###############################
    {
        "city_a": "Madrid",
        "city_b": "Pamplona",
        "color" : "grey",
        "lenght": 3,
        "locomotive": 0,
        "tunnel" : True
    },
    {
        "city_a": "Madrid",
        "city_b": "Pamplona",
        "color" : "white",
        "lenght": 3,
        "locomotive": 0,
        "tunnel" : True
    },
    ###############################
    {
        "city_a": "Marseille",
        "city_b": "Pamplona",
        "color" : "red",
        "lenght": 4,
        "locomotive": 0,
        "tunnel" : False
    },
    {
        "city_a": "Marseille",
        "city_b": "Paris",
        "color" : "",
        "lenght": 4,
        "locomotive": 0,
        "tunnel" : False
    },
    {
        "city_a": "Marseille",
        "city_b": "Zurich",
        "color" : "pink",
        "lenght": 2,
        "locomotive": 0,
        "tunnel" : True
    },
    {
        "city_a": "Marseille",
        "city_b": "Roma",
        "color" : "",
        "lenght": 4,
        "locomotive": 0,
        "tunnel" : True
    },
    ###############################
    {
        "city_a": "Moskva",
        "city_b": "Petrograd",
        "color" : "white",
        "lenght": 4,
        "locomotive": 0,
        "tunnel" : False
    },
    {
        "city_a": "Moskva",
        "city_b": "Smolensk",
        "color" : "orange",
        "lenght": 2,
        "locomotive": 0,
        "tunnel" : False
    },
    ###############################
    {
        "city_a": "Munchen",
        "city_b": "Zurich",
        "color" : "yellow",
        "lenght": 2,
        "locomotive": 0,
        "tunnel" : True
    },
    {
        "city_a": "Munchen",
        "city_b": "Venezia",
        "color" : "blue",
        "lenght": 2,
        "locomotive": 0,
        "tunnel" : True
    },
    {
        "city_a": "Munchen",
        "city_b": "Wien",
        "color" : "orange",
        "lenght": 3,
        "locomotive": 0,
        "tunnel" : False
    },
    ###############################
    {
        "city_a": "Palermo",
        "city_b": "Roma",
        "color" : "",
        "lenght": 4,
        "locomotive": 1,
        "tunnel" : False
    },
    {
        "city_a": "Palermo",
        "city_b": "Smyrna",
        "color" : "",
        "lenght": 6,
        "locomotive": 2,
        "tunnel" : False
    },
    ###############################
    {
        "city_a": "Pamplona",
        "city_b": "Paris",
        "color" : "blue",
        "lenght": 4,
        "locomotive": 0,
        "tunnel" : False
    },
    {
        "city_a": "Pamplona",
        "city_b": "Paris",
        "color" : "green",
        "lenght": 4,
        "locomotive": 0,
        "tunnel" : False
    },
    ###############################
    {
        "city_a": "Paris",
        "city_b": "Zurich",
        "color" : "",
        "lenght": 3,
        "locomotive": 0,
        "tunnel" : True
    },
    ###############################
    {
        "city_a": "Petrograd",
        "city_b": "Stockholm",
        "color" : "",
        "lenght": 8,
        "locomotive": 0,
        "tunnel" : True
    },
    {
        "city_a": "Petrograd",
        "city_b": "Riga",
        "color" : "",
        "lenght": 4,
        "locomotive": 0,
        "tunnel" : False
    },
    {
        "city_a": "Petrograd",
        "city_b": "Wilno",
        "color" : "blue",
        "lenght": 4,
        "locomotive": 0,
        "tunnel" : False
    },
    ###############################
    {
        "city_a": "Riga",
        "city_b": "Wilno",
        "color" : "green",
        "lenght": 4,
        "locomotive": 0,
        "tunnel" : False
    },
    ###############################
    {
        "city_a": "Roma",
        "city_b": "Venezia",
        "color" : "grey",
        "lenght": 2,
        "locomotive": 0,
        "tunnel" : False
    },
    ###############################
    {
        "city_a": "Rostov",
        "city_b": "Sochi",
        "color" : "",
        "lenght": 2,
        "locomotive": 0,
        "tunnel" : False
    },
    {
        "city_a": "Rostov",
        "city_b": "Sevastopol",
        "color" : "",
        "lenght": 4,
        "locomotive": 0,
        "tunnel" : False
    },
    ###############################
    {
        "city_a": "Sarajevo",
        "city_b": "Zagrab",
        "color" : "red",
        "lenght": 3,
        "locomotive": 0,
        "tunnel" : False
    },
    {
        "city_a": "Sarajevo",
        "city_b": "Sofia",
        "color" : "",
        "lenght": 2,
        "locomotive": 0,
        "tunnel" : True
    },
    ###############################
    {
        "city_a": "Sevastopol",
        "city_b": "Sochi",
        "color" : "",
        "lenght": 2,
        "locomotive": 1,
        "tunnel" : False
    },
    ###############################
    {
        "city_a": "Smolensk",
        "city_b": "Wilno",
        "color" : "yellow",
        "lenght": 3,
        "locomotive": 0,
        "tunnel" : False
    },
    ###############################
    {
        "city_a": "Venezia",
        "city_b": "Zurich",
        "color" : "green",
        "lenght": 2,
        "locomotive": 0,
        "tunnel" : True
    },
    {
        "city_a": "Venezia",
        "city_b": "Zagrab",
        "color" : "",
        "lenght": 2,
        "locomotive": 0,
        "tunnel" : False
    },
    ###############################
    {
        "city_a": "Warszawa",
        "city_b": "Wilno",
        "color" : "red",
        "lenght": 3,
        "locomotive": 0,
        "tunnel" : False
    },
    {
        "city_a": "Warszawa",
        "city_b": "Wien",
        "color" : "blue",
        "lenght": 4,
        "locomotive": 0,
        "tunnel" : False
    },
    ###############################
    {
        "city_a": "Wien",
        "city_b": "Zagrab",
        "color" : "",
        "lenght": 2,
        "locomotive": 0,
        "tunnel" : False
    }
]