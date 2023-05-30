def calculate_ticket_cost(ticket_count):
    total_cost = 0

    for i in range(ticket_count):
        age = int(input(f"Введите возраст посетителя {i + 1}: "))

        if age < 18:
            ticket_cost = 0
        elif 18 <= age < 25:
            ticket_cost = 990
        else:
            ticket_cost = 1390

        total_cost += ticket_cost

    if ticket_count > 3:
        total_cost *= 0.9

    return total_cost


ticket_count = int(input("Введите количество билетов: "))
total_cost = calculate_ticket_cost(ticket_count)

print("Общая стоимость билетов:", total_cost, "руб.")
