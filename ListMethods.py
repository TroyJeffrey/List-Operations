from collections import Counter

numberList = []


def print_list():
    for i in range(0, 5):
        print("Enter number at location", i, ":")
        item = int(input())
        numberList.append(item)
    print("Here is the list of numbers you entered", numberList)


def sort_list():
    numberList.sort()
    print(f"Here are your numbers sorted from lowest to highest", numberList)


def sum_list():
    print("Here is the sum of the numbers in the list:", sum(numberList))


def product_list():
    result = 1
    for x in numberList:
        result = result * x
    print(f"Here is the product of the numbers in the list :", result)


def mean_list():
    average = sum(numberList) / len(numberList)
    print("The mean of the numbers in the list is :", average)


def mode_list():
    n = len(numberList)

    data = Counter(numberList)
    get_mode = dict(data)
    mode = [k for k, v in get_mode.items() if v == max(list(data.values()))]

    if len(mode) == n:
        get_mode = "No mode found"
    else:
       get_mode = "Mode is / are: " + ', '.join(map(str, mode))


def median_list():
    median = numberList[2]
    print(f"Here is the median for the numbers in the list :", median)


def largest_number():
    print(f"The largest number in the list is :", numberList[-1])


def smallest_number():
    print(f"The smallest number in the list is :", numberList[0])


def remove_even():
    for num in numberList:
        if num % 2 == 0:
            numberList.remove(num)
    print(f"Here is the list with all even numbers removed :", numberList)


def remove_odd():
    for num in numberList:
        if num % 2 != 0:
            numberList.remove(num)
    print(f"Here is the list with all odd numbers removed :", numberList)


def remove_duplicates():
    res = []
    [res.append(x) for x in numberList if x not in res]
    print("The list after removing duplicates : " + str(res))


def user_question():
    number = input("Enter a number and I'll tell you if It's in the list already.")
    if number in numberList:
        print("The number you entered isin the list")
    else:
        print("The number you entered is not in the list.")


def second_largest():
    firstmax = max(numberList[0], numberList[1])
    secondmax = min(numberList[0], numberList[1])

    for i in range(2, len(numberList)):
        if numberList[i] > firstmax:
            secondmax = firstmax
            firstmax = numberList[i]
        else:
            if numberList[i] > secondmax:
                secondmax = numberList[i]

    print("Second highest number is : ", str(secondmax))
