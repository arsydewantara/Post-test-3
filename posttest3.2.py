import time

while True:
    try:
        angka = int(input("Masukkan nilai: "))
        a = 1
        b = 1
        while a <= angka:
            print (b)
            b += 1
            if b == 10:
                b -= 9
            a += 1
        break
    except ValueError:
        print("Nilai yang anda masukkan tidak valid")
        time.sleep(2.0)
