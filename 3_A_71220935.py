a= int(input ('Masukkan nilai soal 1: '))
b= int(input ('Masukkan nilai soal 2: '))
c= int(input ('Masukkan nilai soal 3: '))
d= int(input ('Masukkan umur anda: '))
e= int(a*0.05)
f= int(b*0.03)
g= int(c*0.02)
h= ('rata rata nilai anda', a + b + c)
print ('rata-rata nilai anda', a + b + c )
if h>80 and d<25:
    print ('Selamat Anda Lulus')
elif h>90 and d>25:
    print ('Selamat Anda Lulus')
else:
    print ('Coba Lagi Tahun Depan')