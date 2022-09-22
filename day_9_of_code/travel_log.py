travel_log = [
    {
        "state_visited":"Sao_Paulo",
        "cities_visited":["sao_jose_do_rio_preto", "holambra", "campinas", "sao_paulo_capital"]
    },
    {
        "state_visited":"Minas_Gerais",
        "cities_visited": ["uberaba", "conquista", "araguari", "carmo_do_paranaiba", "abadia_dos_dourados"]
    },
    {
        "state_visited":"Goias",
        "cities_visited": "catalao"
    },
    {
        "state_visited":"Santa_Catarina",
        "cities_visited": "florianopolis"
    }
]

def add_new_states(state_visited, cities_visited):
    new_state = {}
    new_state["state_visited"] = state_visited
    new_state["cities_visited"] = cities_visited
    travel_log.append(new_state)

add_new_states("Ceara", ["Jericoacoara"])
print(travel_log)

#Como adicionar uma nova chave&valor no dicionário
starting_dictionary = {
    "a": 9,
    "b": 8,
}


final_dictionary = {
    "a": 9,
    "b": 8,
    "c": 7,
}

starting_dictionary["c"] = 7
final_dictionary = starting_dictionary
print(final_dictionary)

order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}
print(order["main"][2][0])