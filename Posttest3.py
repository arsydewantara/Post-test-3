print("List kue yang ada: \n1.Kue Keju Rp.6000 \n2.Kue Coklat Rp.3500")
print(" ")

def diskon10():
    harga_kuekeju = 6000
    harga_total = total_kuekeju * harga_kuekeju
    diskon = harga_total * 10/100
    bayar = harga_total - diskon
    print("Harga total Kue yang anda beli adalah Rp.",bayar)

def diskon15():
    harga_kuekeju = 6000
    harga_total = total_kuekeju * harga_kuekeju
    diskon = harga_total * 15/100
    bayar = harga_total - diskon
    print("Harga total kue yang anda beli adalah Rp.",bayar)

def harga_biasa():
    harga_kuekeju = 6000
    bayar = total_kuekeju * harga_kuekeju
    print(" ")
    print("Harga total kue yang anda beli adalah Rp.",bayar)

def diskon7():
    harga_kuecoklat = 3500
    harga_total = total_kuecoklat * harga_kuecoklat
    diskon = harga_total * 7/100
    bayar = harga_total - diskon
    print(" ")
    print("Harga total kue yang anda beli adalah Rp.",bayar)

def harga_biasacoklat():
    harga_kuecoklat = 3500
    bayar = total_kuecoklat * harga_kuecoklat
    print(" ")
    print("Harga total kue yang anda beli adalah Rp,",bayar)

def diskon12():
    harga_kuecoklat = 3500
    harga_total = total_kuecoklat * harga_kuecoklat
    diskon = harga_total * 12/100
    bayar = harga_total - diskon
    print(" ")
    print("Harga total kue yang anda beli adalah Rp.",bayar)

jenis_kue = input("Pilih jenis Kue yang ingin anda beli:")
if jenis_kue == "kue keju":
    total_kuekeju = int (input("Masukkan Jumlah kue keju yang ingin anda beli: "))

    if (total_kuekeju >=4) and (total_kuekeju <=15):
        print(" ")
        print("Selamat anda mendapatkan diskon sebesar 10%")
        diskon10()
    elif (total_kuekeju >=16) and (total_kuekeju <=25):
        print(" ")
        print("Selamat anda mendapatkan diskon sebesar 15%")
        diskon15()
    elif total_kuekeju <4:
        harga_biasa()
    elif total_kuekeju >25:
        print("Maaf jumlah kue keju yang diproduksi adalah sebanyak 25 per hari")

elif jenis_kue == "kue coklat":
    total_kuecoklat= int(input("Masukkan jumlah kue coklat yang ingin anda beli: "))

    if (total_kuecoklat >=5) and (total_kuecoklat <=20):
        print(" ")
        print("Selamat anda mendapatkan diskon 7%")
        diskon7()
    elif (total_kuecoklat >=21) and (total_kuecoklat <=35):
        print(" ")
        print("Selamat anda mendapatkan diskon 12%")
        diskon12
    elif total_kuecoklat <5:
        print(" ")
        harga_biasacoklat()
    elif total_kuecoklat >35:
        print(" ")
        print("Maaf jumlah kue coklat yang diproduksi adalah sebanyak 35 per hari")
else:
    print(" ")
    print("Maaf Kue yang anda pilih belum tersedia")
