import pandas as pd
import random as rm

list_code_word=[]
list_enc_word=[]
list_error_word=[]
list_error_check=[]

def korel(x):
    return ''.join([format(int(a)+1,'02b') for a in str(x)])

def distort(x):
    b=x[::2]
    cnt=0
    print("b", b)
    for i in range(len(b)):
        if b[i] == b[i+1]:
            return "Є помилка"
        else:
            return "Немає"
for i in range(10):
    code_word=""
    enc_word=""
    error_word=""
    error_check=""

    code_word=str(input("Input a code word: "))
    list_code_word.append(code_word)

    enc_word+=code_word
    """
    for i in range(0, len(enc_word)):
        if (enc_word[i]=="1"):
            enc_word=enc_word[:i].replace("1", "10")+enc_word[i:]
        else:
            enc_word=enc_word[:i].replace("0", "01")+enc_word[i:]
    print("Encrypyted code word: " + enc_word)
    list_enc_word.append(enc_word)
    """
    enc_word=korel(enc_word)
    print("Encrypyted code word: " + enc_word)
    list_enc_word.append(enc_word)

    error_word+=enc_word
    index = rm.randrange(0, len(error_word))
    print(index)
    if rm.randrange(0, 10)<5:
        if error_word[index]=="1":
            error_word=error_word[:index]+"0"+error_word[index+1:]
        else:
            error_word=error_word[:index]+"1"+error_word[index+1:]
    print("Encrypyted code word with mistake: " + error_word)
    list_error_word.append(error_word)

    error_check=distort(error_word)
    print(error_check)
    list_error_check.append(error_check)

table=pd.DataFrame({'Code word from LAB3 |': list_code_word,
                    'Encrypted code words |':list_enc_word,
                    'Encrypted code words with error |': list_error_word,
                    'Error check': list_error_check})
print(table)
