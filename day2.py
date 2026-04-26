def find_top_seller(products: dict, sales: dict) -> str:
    revenue = {}

    for product in products:
        revenue[product] = products[product] * sales[product]

    best = max(revenue, key=lambda x: revenue[x])

    return best
print(find_top_seller(
    {"Olma": 5000, "Banan": 8000, "Uzum": 7000},
    {"Olma": 10,   "Banan": 5,    "Uzum": 8}
))
# Kutilgan natija: "Uzum"