def repeated_letter(word: str):

    my_letters = list(set([c for c in word]))
    number_of_times = [{'letter':letter, 'times': word.count(letter)} for letter in my_letters]
    sorted_letters = sorted(number_of_times, key=lambda k: k.get('times'), reverse=True)

    for letter in sorted_letters:
        print(f'The letter {letter.get("letter")} is {letter.get("times")} times')
