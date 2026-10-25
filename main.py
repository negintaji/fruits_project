# https://github.com/negintaji/fruits_project

def fruits(**kwargs):
    print(f"You have {len(kwargs)} fruits in your shopping list")
    print(f"The total cost of the shopping list is {sum(kwargs.values())}")

    expensive = max(kwargs, key=kwargs.get)
    cheapest = min(kwargs, key=kwargs.get)

    print(f"The most expensive fruit is {expensive.title()} with the price of {kwargs[expensive]}")
    print(f"The cheapest fruit is {cheapest.title()} with the price of {kwargs[cheapest]}")


fruits_list = {}

while True:
    data = input()

    if data == "finish":
        break

    name, price = data.split()
    fruits_list[name] = int(price)

fruits(**fruits_list)
