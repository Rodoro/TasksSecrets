# ctfcup{d0TnEtPlusjAv4_is_l0ve}

from pyDes import *

key = ''
k1 = 'some_phrase_i_dont_know_'
k2 = 'be_the_coolest_guy_ever_'
for i in range(24):
    key += chr(ord(k1[i]) ^ ord(k2[i]))

des3 = triple_des(key, CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)

check = b'\x8d\x83\xeb;%\x8c\xd2\x82>\x94/\xe6\t\x87\xa9\xbb\xd7\nHBs\xe0\xdf\xbb\xf0\xc7\xf7\xb8\xa0\xcc\x821'
print(des3.decrypt(check).decode())
