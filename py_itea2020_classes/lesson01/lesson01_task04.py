def deposit_result(initial_sum, years, percentage):
    result_sum = initial_sum
    for i in range(years):
        result_sum += result_sum * percentage / 100

    return  result_sum

print(round(deposit_result(1000, 4, 7),2))