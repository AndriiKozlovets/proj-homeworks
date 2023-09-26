def cats_with_hats(num_cats, num_rounds):
    cats = [0] * num_cats

    for round_number in range(1, num_rounds + 1):
        for cat_number in range(round_number - 1, num_cats, round_number):
            cats[cat_number] = 1 - cats[cat_number]

    return [i + 1 for i, hat_status in enumerate(cats) if hat_status == 1]


num_cats = num_rounds = 100
result = cats_with_hats(num_cats, num_rounds)
print("Cats with hats:", result)
