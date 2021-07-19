# This program accepts a sentence in
# uppercase letters and then converts
# that sentence into pig latin.

def main():
    # Get sentence from user
    my_string = input('Enter your sentence in uppercase letters: ')

    word_list = my_string.split()

    new_string = []

    # Converts sentence into pig latin
    for word in word_list:
        if word[-1].isalpha():
            new_string.append(word[1:] + word[0] + 'AY ')
        else:
            new_string.append(word[1:-1] + word[0] + 'AY ' + word[-1])

    new_sentence = ''.join(new_string)

    # Display the new sentence in pig latin
    print('Here is your new sentence in Pig Latin:')
    print('---------------------------------------')
    print(new_sentence)

# Call the main function
main()
        
