print ('===== Selamat datang di Toko Andi Tersenyum, selamat belanja! ====-')
a= int(input ('total belanja: '))
b= a*0.02
c= a*0.05
d= a*0.1
if a >=1000000:
    print ('biaya yang harus dibayar setelah diskon adalah', a - d)
elif a>= 500000:
    print ('biaya yang harus dibayar setelah diskon adalah', a - c)
elif a>= 100000:
    print ('biaya yang harus dibayar setelah diskon adalah', a - b)
elif a< 100000:
    print ('biaya yang harus dibayar setelah diskon adalah', a)
else:
    print ('tidak ada')