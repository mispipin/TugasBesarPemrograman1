print("Selamat datang di Store Book")
print("1. Novel")
print("2. Komik")
print("3. Biografi")
print("4. Search")

pilihmenu = input("Inputkan nomor yang anda butuhkan: ")

judul =["Hello,Cello","Malioboro at Midnight","Kota Para Pecundang","Rumah untuk Alie","Kata Sandi",
        "Death Note Short Stories","Akasha Record of Ragnarok 06","One Piece 98","Blue Lock 01","Tokyo Revengers 01",
        "Biografi Politik Habibie","Soekarno: Biografi Singkat 1901-1970","Tan Malaka: Biografi Singkat 1897-1949","History Of Madura","Carok Budaya & Hukum",]
pengarang=["Nadia Ristivani","Skysphire","Itakrn","Lenn Liu","Dian Yutyaningsih",
           "Tsugumi Ohba","Shinaya Umemura dan Takumi Fukui","Eiichiro Oda", "Muneyuki Kaneshiro dan Yusuke Nomura","PKen Wakui",
           "Raden Toto Sugiarto","Taufik Adi Susilo","Taufik Adi Susilo","Drs.H.Muhammad Syamsudin","DR.Wahju Prijo Sjatmiko, SH",]
harga=["Rp. 89.100","Rp. 91.000","Rp. 88.000","Rp. 99.000","Rp. 99.000",
       "Rp. 48.000","Rp. 45.000","Rp. 115.000","Rp. 36.000","Rp. 40.000",
       "Rp. 95.000","Rp. 70.000","Rp. 67.500","Rp. 63.000","Rp. 148.000",]
            
if pilihmenu == '1':
    print("Buku Novel yang tersedia :")
    print(f"1. {judul[0]}")
    print(f"2. {judul[1]}")
    print(f"3. {judul[2]}")
    print(f"4. {judul[3]}")
    print(f"5. {judul[4]}")
    
    pilihbuku = input("Inputkan nomor yang anda butuhkan: ")
    if pilihbuku == '1':
        print(f"Buku        : {judul[0]}")
        print(f"Pengarang   : {pengarang[0]}")
        print(f"Harga       : Rp {harga[0]}")

        belibuku = input("Input Y (beli) dan N (kembali): ")
    elif pilihbuku =="2":
        print(f"Buku        : {judul[1]}")
        print(f"Pengarang   : {pengarang[1]}")
        print(f"Harga       : Rp {harga[1]}")

        belibuku = input("Input Y (beli) dan N (kembali): ")
        
    elif pilihbuku =="3":
        print(f"Buku        : {judul[2]}")
        print(f"Pengarang   : {pengarang[2]}")
        print(f"Harga       : Rp {harga[2]}")

        belibuku = input("Input Y (beli) dan N (kembali): ")
        
    elif pilihbuku =="4":
        print(f"Buku        : {judul[3]}")
        print(f"Pengarang   : {pengarang[3]}")
        print(f"Harga       : Rp {harga[3]}")

        belibuku = input("Input Y (beli) dan N (kembali): ")
        
    elif pilihbuku =="5":
        print(f"Buku        : {judul[4]}")
        print(f"Pengarang   : {pengarang[4]}")
        print(f"Harga       : Rp {harga[4]}")

        belibuku = input("Input Y (beli) dan N (kembali): ")
    else:
        print("Masukan inputan dengan benar!")

elif pilihmenu == '2':
    print("Komik yang tersedia")
    print(f"1. {judul[5]}")
    print(f"2. {judul[6]}")
    print(f"3. {judul[7]}")
    print(f"4. {judul[8]}")
    print(f"5. {judul[9]}")
    
    pilihbuku = input("Inputkan nomor yang anda butuhkan: ")
    if pilihbuku == '1':
        print(f"Buku        : {judul[5]}")
        print(f"Pengarang   : {pengarang[5]}")
        print(f"Harga       : Rp {harga[5]}")

        belibuku = input("Input Y (beli) dan N (kembali): ")
    elif pilihbuku =="2":
        print(f"Buku        : {judul[6]}")
        print(f"Pengarang   : {pengarang[6]}")
        print(f"Harga       : Rp {harga[6]}")

        belibuku = input("Input Y (beli) dan N (kembali): ")
        
    elif pilihbuku =="3":
        print(f"Buku        : {judul[7]}")
        print(f"Pengarang   : {pengarang[7]}")
        print(f"Harga       : Rp {harga[7]}")

        belibuku = input("Input Y (beli) dan N (kembali): ")
        
    elif pilihbuku =="4":
        print(f"Buku        : {judul[8]}")
        print(f"Pengarang   : {pengarang[8]}")
        print(f"Harga       : Rp {harga[8]}")

        belibuku = input("Input Y (beli) dan N (kembali): ")
        
    elif pilihbuku =="5":
        print(f"Buku        : {judul[9]}")
        print(f"Pengarang   : {pengarang[9]}")
        print(f"Harga       : Rp {harga[9]}")

        belibuku = input("Input Y (beli) dan N (kembali): ")
    else:
        print("Masukan inputan dengan benar!")
elif pilihmenu == '3':
    print("Buku Biografi yang tersedia")
    print(f"1. {judul[10]}")
    print(f"2. {judul[11]}")
    print(f"3. {judul[12]}")
    print(f"4. {judul[13]}")
    print(f"5. {judul[14]}")
    
    pilihbuku = input("Inputkan nomor yang anda butuhkan: ")
    if pilihbuku == '1':
        print(f"Buku        : {judul[10]}")
        print(f"Pengarang   : {pengarang[10]}")
        print(f"Harga       : Rp {harga[10]}")

        belibuku = input("Input Y (beli) dan N (kembali): ")
    elif pilihbuku =="2":
        print(f"Buku        : {judul[11]}")
        print(f"Pengarang   : {pengarang[11]}")
        print(f"Harga       : Rp {harga[11]}")

        belibuku = input("Input Y (beli) dan N (kembali): ")
        
    elif pilihbuku =="3":
        print(f"Buku        : {judul[12]}")
        print(f"Pengarang   : {pengarang[12]}")
        print(f"Harga       : Rp {harga[12]}")

        belibuku = input("Input Y (beli) dan N (kembali): ")
        
    elif pilihbuku =="4":
        print(f"Buku        : {judul[13]}")
        print(f"Pengarang   : {pengarang[13]}")
        print(f"Harga       : Rp {harga[13]}")

        belibuku = input("Input Y (beli) dan N (kembali): ")
        
    elif pilihbuku =="5":
        print(f"Buku        : {judul[14]}")
        print(f"Pengarang   : {pengarang[14]}")
        print(f"Harga       : Rp {harga[14]}")

        belibuku = input("Input Y (beli) dan N (kembali): ")
    else:
        print("Masukan inputan dengan benar!")
elif pilihmenu == '4':
    print("Pencarian Buku")
    cari_buku = input("Masukkan judul atau pengarang buku yang ingin dicari: ")
    
    hasil_pencarian = []
    for i in range(len(judul)):
        if cari_buku.lower() in judul[i].lower() or cari_buku.lower() in pengarang[i].lower():
            hasil_pencarian.append(i)
    
    if len(hasil_pencarian) > 0:
        print("Hasil Pencarian:")
        for i in hasil_pencarian:
            print(f"{i+1}. {judul[i]} - {pengarang[i]} (Rp {harga[i]})")
            belibuku = input("Input Y (beli) dan N (kembali): ")
    else:
        print("Buku tidak ditemukan")
