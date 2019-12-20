import pandas as pd

def compress(data):
    comp_data = []
    dictionnary = ['']
    word = ''
    i = 0
    for char in data:
        i += 1
        word += char
        if not word in dictionnary:
            dictionnary.append(word)
            comp_data.append([dictionnary.index(word[:-1]), word[-1]])
            word = ''
        elif i == len(data):
            comp_data.append([dictionnary.index(word), ''])
            word = ''
    lapki = []
    for elem in dictionnary:
        k = '"'+elem+'"'
        #print(k)
        lapki.append(k)
    print(pd.Series(lapki))
    for elem in comp_data:
        print(elem)
    print("___________________________________________________________________")
    print(dictionnary)
    numer = list(enumerate(dictionnary))
    print(numer)
    return comp_data



if __name__ == '__main__':
    data = "HolovenHoloven"
    # data = "Well_somebody_told_me_you_had_a_boyfriend_who_looked_like_a_girlfriend_that_I_had_in_February_of_last_year_it_is_not_confidential_I_have_got_potential"
    # data = "fsgfd_erty_cvbn_gkijki_qwerwq_xcvbxn_adsfs_tyhrt_kioko_zxcvz_mgmhjg_hfhbg_kiyuki_uioluiol_zxvczd_trgrtg_tyujtyj_xcvbxvc_nmjghm_lkjend"
    comp_data = compress(data)
    print(comp_data)
