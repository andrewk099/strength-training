
weight = input("Enter nRM (n = any number of reps you choose, RM = rep max): ")
weight = int(weight)

def main(weight):
    
    if weight == 0:
        raise ValueError("cannot calculate 0")

    def round_to_nearest_five(x):
        return round(x / 5) * 5

    def find_percentage(x):
        percentage = x / weight
        rounded_percentage = round(percentage, 2)
        return r"{:}%".format(rounded_percentage * 100)


    print(
        "Week 1", round_to_nearest_five(weight * .80), "80%"
        "\nWeek 2", round_to_nearest_five(weight * .85), "85%"
        "\nWeek 3", round_to_nearest_five(weight * .9), "90%"
        "\nWeek 4", round_to_nearest_five(weight * .95), "95%"
        "\nWeek 5", round_to_nearest_five(weight * .95 + 5), find_percentage(weight * .95 + 5),
        "\nWeek 6", round_to_nearest_five(weight * .95 + 10), find_percentage(weight * .95 + 10),
        "\nWeek 7", round_to_nearest_five(weight * .95 + 15), find_percentage(weight * .95 + 15),
        "\nWeek 8", round_to_nearest_five(weight * .95 + 20), find_percentage(weight * .95 + 20),
    )

main(weight)