def linear_search_dictionary(my_dict, target):
    x = list(my_dict.keys())

    for y in range(len(x)):
        if my_dict[x[y]] == target:
            print("Found at key:", x[y])
            return x[y]
    print("Target is not in the dictionary")
    return None


my_dictionary = {"red": 5, "blue": 3, "yellow": 12, "green": 7}
linear_search_dictionary(my_dictionary, 5)
linear_search_dictionary(my_dictionary, 3)
linear_search_dictionary(my_dictionary, 8)


# def linear_search_dictionary(dict,target_value):
#     for key in dict:
#         if dict [key] == target_value:
#             print("Found at key ",key)
#             return key
#     print("Target is not in the dictionary")
#     return -1
