"""You're given an unsorted array of integers where every integer appears exactly twice,
except for one integer which appears only once. Wrie an algorithm(in a language of your choice)
that find the integer that appears only once."""


# ps1.py
def onlyOnce(list_of_num):
    nums_set = set(list_of_num)
    for num in nums_set:
        if list_of_num.count(num) == 1:
            return num
    return None

nums = [1, 2, 3, 4, 5, 6, 7, 6, 4, 3, 2, 1, 5, 0, 0, 9]
print("Least occuring element is: " + str(onlyOnce(nums)))
