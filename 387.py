#changes the inputted word into the proper caeser chipher by taking the user inputted change
def CaeserChiper(word, number):
    #punctuation list
    punctuation = ['.',"'",'"',',','!','(',')','^','/','?','+','=',';',':']
    #letters dictionary
    letters = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
    #inverted key:value list
    numbers = {0:'a',1:'b',2:'c',3:'d',4:'e',5:'f',6:'g',7:'h',8:'i',9:'j',10:'k',11:'l',12:'m',13:'n',14:'o',15:'p',16:'q',17:'r',18:'s',19:'t',20:'u',21:'v',22:'w',23:'x',24:'y',25:'z'}

    #changes one letter to its coresponding key
    #only works for lower case
    def Changer(letter, number):
        changer = letters[letter]  #access dictionary, make changer = letters position
        changer = changer + number #take the changer, and add the desired cipher to it

        if changer > 25:    #checks if number larger than letter dict
            changer = changer - 26
        
        letterOutput = numbers[changer] #the outputed letter is accessed through the inverse dictionary and made to be output

        return letterOutput

    #passes one letter at a time to the Changer
    def LetterPasser(word, number):
        chipheredWord = ''
        for i in range(len(word)):
            if word[i] == ' ':  #check if space
                chipheredWord = chipheredWord + ' '
            elif word[i].isupper(): #check if uppercase
                chipheredWord = chipheredWord + (Changer((word[i]).lower(),number)).upper()
            elif word[i] in punctuation:    #check if punctuation
                chipheredWord = chipheredWord + word[i]
            else:
                chipheredWord = chipheredWord + Changer(word[i],number)

        return chipheredWord

    output = LetterPasser(word, number)
    return output

def Main():
    flag1 = False
    flag2 = False

    while(flag1 == False):
        try:
            uInput1 = input("Enter the word to be chiphered: ")
        except:
            print("try again.... not a valid input")
        else:
            flag1 = True

    while(flag2 == False):
        try:
            uInput2 = int(input("Enter the distance to be chiphered: "))

            if uInput2 > 26:
                raise(Exception())
        except:
            print("try again.... not a valid input")
        else:
            flag2 = True


    output = CaeserChiper(uInput1, uInput2)

    print(output)

Main()