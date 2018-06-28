def reverse(word):
    #To create a list of indices of word with capital letters (if any):
    capital_indices = []
    for count,char in enumerate(word):
        if char.isupper():
            capital_indices.append(count)
    
    # To check if the word has both capital letters and a punctuation:
    if (len(capital_indices) > 0) and (not word[len(word)-1].isalpha()):
        reverse = word[0:len(word)-1][::-1] + word[len(word)-1]
        reverse_capital_list = []
        for count,char in enumerate(reverse):
            if count in capital_indices:
                reverse_capital_list.append(char.upper())
            else:
                reverse_capital_list.append(char.lower())
        return ''.join(reverse_capital_list)
    
    #To check if word only has capital letters:
    elif len(capital_indices) > 0:
        reverse = word[::-1]
        reverse_capital_list = []
        for count,char in enumerate(reverse):
            if count in capital_indices:
                reverse_capital_list.append(char.upper())
            else:
                reverse_capital_list.append(char.lower())
        return ''.join(reverse_capital_list)
    
    #To check if word only has punctuation:
    elif not word[len(word)-1].isalpha():
        return word[0:len(word)-1][::-1] + word[len(word)-1]
    
    # If word has neither a punctuation nor capitalization:
    else:
        return word[::-1]
    
def sentence_reversal(sentence):
    # Calls maps sentence onto reverse function and produces list with strings using list comprehension:
    return [' '.join(map(reverse, sentence))]

def main_func():
    # Takes user input + acts as __main__ function + outputs reverse of strings:
    n = int(input())
    sentences_list = []
    for i in range(0,n):
        sentences_list.append(input().split(' '))
        sentences_list[i] = sentence_reversal(sentences_list[i])
    for sentence in sentences_list:
        print(' '.join(sentence))

main_func()
