# python program which merges two seperate dictionarties into a single one

dictionary1 = {
    'country': 'India',
    'state': 'West Bengal'
}

dictionary2 = {
    'PIN': 732101,
    'Landmark': 'Mayabon Resort'
}

dict = dictionary1.copy()
dict.update(dictionary2)

print(dict)