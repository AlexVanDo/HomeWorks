def string_slices(string: str) -> str:
    '''Вернёт строку без спецсимволов %%#&.'''
    list_string = list(string)
    list_string.remove("%")
    list_string.remove("%")
    list_string.remove("#")
    list_string.remove("&")
    result = ''.join(list_string) 
    return result


def vote(votes):
    '''Выводит число, которое встречается чаще всего'''
    count_ = 0
    for i in votes:
        n = votes.count(i)
        if n > count_:
            count_ = n
            num = i
        else:
            continue
    return num


def solve(phrases: list):
    '''Выводит все фразы из списка phrases, которые являются палиндромами'''
    result = [] 
    new_phrase = ""
    space = " "
    for phrase in phrases:
        new_phrase = phrase.replace(space, "")
        if new_phrase == new_phrase[::-1]:
           result.append(phrase)
    return result
