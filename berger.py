import math as m
import pandas as pd
import random as rm

list_code_word=[]
list_enc_word=[]
list_error_word=[]
list_error_check=[]

def to_bin(n):
    b = ''

    while n > 0:
        b = str(n % 2) + b
        n = n // 2
    return b

for i in range(10):
    code_word=""
    enc_word=""
    error_word=""
    error_check=""

    code_word=str(input("Input a code word: "))
    list_code_word.append(code_word)

    log = m.log2(len(code_word)+1)
    if log % 1 == 0:
        r = log
    else:
        r = m.ceil(log)
    cnt = 0
    for i in range(len(code_word)):
        if code_word[i] == '1':
            cnt += 1
    num_of_ones = cnt
    if cnt != 0:
        result = ['0'] * (m.floor(m.log2(cnt)) + 1)
        while cnt != 0:
            bit = m.floor(m.log2(cnt))
            result[bit] = '1'
            cnt = cnt - 2 ** bit
        len1 = len(result)
        while r > len1:
            result.append('0')
            len1 += 1
    else:
        result = ['0'] * int(r)

    for i in range(len(result)):
        if result[i] == '0':
            result[i] = '1'
        elif result[i] == '1':
            result[i] = '0'
    res = ''
    result = res.join(result)
    enc_word=code_word + result[::-1]
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

    cnt1=0
    for i in range(len(code_word)):
        if code_word[i]=="1":
            cnt1+=1
    pere=to_bin(cnt1)
    if result[0]=='0':
        result=result[1:]
    if pere==result:
        error_check="Немає"
    else:
        error_check="Є помилка"
    print(error_check)
    list_error_check.append(error_check)
table=pd.DataFrame({'Code word from LAB3 |': list_code_word,
                    'Encrypted code words |':list_enc_word,
                    'Encrypted code words with error |': list_error_word,
                    'Error check': list_error_check})
print(table)
