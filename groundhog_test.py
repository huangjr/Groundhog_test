
# find max substring
def find_max(target, dict_word):
    result, length = '', 0
    for i in range(len(target)):

        if length < len(dict_word) and target[i] == dict_word[length]:
            result += dict_word[length]
            length += 1

    return length, result


# The input dictionary and target
dictionary = {"bze", "apple", "monkey", "plea"} 
target = "apcplea"


# find max substring in dictionary
answer, max_lenghth = '',0
for word in dictionary:

    if find_max(target, word)[0] > max_lenghth:
        max_lenghth = find_max(target, word)[0]
        answer = find_max(target, word)[1]
print(answer, max_lenghth)