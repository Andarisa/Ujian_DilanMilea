
# import requests

# url = 'http://raw.githubusercontent.com/LintangWisesa/Ujian_Fundamental_JCDS08/master/data/provinsi.json'
# data1 = requests.get(url)

# hasil1 = data1.json()
# print(hasil1)


# import requests

# url = 'http://raw.githubusercontent.com/LintangWisesa/Ujian_Fundamental_JCDS08/master/data/kodepos.json'
# data2 = requests.get(url)

# hasil2 = data2.json()
# print(hasil2)



# 15341
# 40115

kodepos1 = input('Masukkan Kode Pos 1: ')
kodepos2 = input('Masukkan Kode Pos 2: ')


import requests
apiKey = '9o4F23jAUDB70J9uM8BNjdzNnvulCaUJJgsGBHThVNt1JalwAfU41lCHobjoJtov'
url = f'http://www.zipcodeapi.com/rest/{apiKey}/distance.json/{kodepos1}/{kodepos2}/km'
data = requests.get(url)

hasil = data.json()
jarak = hasil["distance"]
print(f'Kode Pos lokasi Dilan adalah {kodepos1}')
print(f'Kode Pos lokasi Milea adalah {kodepos2}')
print(f'Jarak Dilan & Milea adalah {jarak} km' )








