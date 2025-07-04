def no_of_notes(amount):
    notes = [100, 200, 500, 1000]
    result = {}
    for i in notes:
        count = amount // i
        if count > 0:
            result[notes] = count
            amount -= notes * count
    return result
amount = int(input())
print(no_of_notes(amount))