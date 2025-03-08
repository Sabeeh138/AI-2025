products = [
    {"id": 1, "frequency": 15, "volume": 2},
    {"id": 2, "frequency": 8, "volume": 1},
    {"id": 3, "frequency": 20, "volume": 3},
]

slots = [
    {"id": 1, "distance": 1},
    {"id": 2, "distance": 2},
    {"id": 3, "distance": 3},
]

products.sort(key=lambda x: -x["frequency"])
slots.sort(key=lambda x: x["distance"])

assignment = []
for product, slot in zip(products, slots):
    assignment.append((product["id"], slot["id"]))

for prod_id, slot_id in assignment:
    print(f"Product {prod_id} is assigned to Slot {slot_id}")
