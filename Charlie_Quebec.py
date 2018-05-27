# Dictionary of all ICAO Code Words:
ICAO_dict = {
    'A':'Alpha','B':'Bravo','C':'Charlie','D':'Delta','E':'Echo','F':'Foxtrot','G':'Golf','H':'Hotel',
    'I':'India','J':'Juliet','K':'Kilo','L':'Lima','M':'Mike','N':'November','O':'Oscar','P':'Papa',
    'Q':'Quebec','R':'Romeo','S':'Sierra','T':'Tango','U':'Uniform','V':'Victor','W':'Whiskey','X':'Xray',
    'Y':'Yankee','Z':'Zulu', ' ':' '
}

def find_spaces(text):
    return [index for index,word in enumerate(text) if word == ' ']

# To translate text into ICAO code:
def ICAO_translator(text):
    ICAO_text = []
    text.split(' ')
    for word in text:
        for char in word:
            ICAO_text.append(ICAO_dict[char.upper()]) 
    output = ''
    for count,word in enumerate(ICAO_text):
        if (word != ' ') and (not count + 1 in find_spaces(text)) and (count != len(ICAO_text)-1):
            output += word+'-'
        else:
            output += word
    return output
# To act as __main__ function + takes input of test cases, lines, and text on each line + outputs its ICAO translation:
def main():
    T = int(input())
    output = []
    for i in range(0,T):
        lines = int(input())
        text_list = []
        for i in range(0,lines):
            text_list.append(input())
        for text in text_list:
            output.append(ICAO_translator(text))
        
    for item in output:
        print(item)
main()
