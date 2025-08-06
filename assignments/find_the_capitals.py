def capital(capitals):
    result = []
    for item in capitals:
        if 'state' in item:
            sentence = "The capital of " + item['state'] + " is " + item['capital']
        else:
            sentence = "The capital of " + item['country'] + " is " + item['capital']
        result.append(sentence)
    return result


if __name__ == "__main__":
    print(capital([{'state': 'Maine', 'capital': 'Augusta'}]))
    print(capital([{'country': 'Spain', 'capital': 'Madrid'}]))
    print(capital([
        {'state': 'Maine', 'capital': 'Augusta'},
        {'country': 'Spain', 'capital': 'Madrid'}
    ]))
