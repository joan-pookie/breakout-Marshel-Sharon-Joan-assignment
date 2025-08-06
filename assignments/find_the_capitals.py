def capital(capitals): 
    sentences = []
    for item in capitals:
        
        place_type = 'state' if 'state' in item else 'country'
        place_name = item[place_type]
        capital_name = item['capital']
        
        sentences.append(f"The capital of {place_name} is {capital_name}")
    return sentences
