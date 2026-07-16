import json
from produk import Produk

class ManagerProduk:
    def __init__(self):
        self.daftar_produk = []
        self.load_data()

    def load_data(self):
        try:
            with open("produk.json", "r", encoding="utf-8") as file:
                data = json.load(file)

            for item in data:
                produk = Produk(
                    item["id_produk"],
                    item["nama"],
                    item["harga"],
                    item["stok"]
                )

                self.daftar_produk.append(produk)
        
        except (FileNotFoundError, json.JSONDecodeError):
            self.daftar_produk = []
    
    def simpan_data(self):
        data = []

        for p in self.daftar_produk:
            data.append({
                "id_produk" : p.id_produk,
                "nama" : p.nama,
                "harga" : p.harga,
                "stok" : p.stok
            })

        with open("produk.json","w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def buat_id_baru(self):
        id_terbesar = 0

        for p in self.daftar_produk:
            if p.id_produk > id_terbesar:
                id_terbesar = p.id_produk
        return id_terbesar + 1

        if not self.daftar_produk:
            return 1

    def tambah_produk(self, produk):
        self.daftar_produk.append(produk)
        self.simpan_data()
        print("Produk berhasil ditambahkan")

    def tambah(self):
        id_baru = self.buat_id_baru()
        nama = input("Nama : ")
        
        while True:
            try:
                harga = int(input("Harga : "))
                break
            except ValueError:
                print("Input harus angka!")

        while True:
            try:
                stok = int(input("Stok : "))
                break
            except ValueError:
                print("Input harus angka!")

        produk = Produk(id_baru, nama, harga, stok)

        self.tambah_produk(produk)

    def lihat(self):
        print("\n===== DAFTAR Produk =====")
        
        if not self.daftar_produk:
            print("Produk belum ada")
            return
        for p in self.daftar_produk:
            print(f"ID    :", p.id_produk)
            print(f"Nama  :", p.nama)
            print(f"Harga :", p.harga)
            print(f"Stok  :", p.stok)
            print("-" * 30)
        print(f"\nJumlah produk : {len(self.daftar_produk)}")

    def cari_produk(self, id_produk):
        for p in self.daftar_produk:
            if p.id_produk == id_produk:
                return p
        return None
    
    def cari(self):
        id_produk = int(input("Masukkan ID Produk :"))

        p = self.cari_produk(id_produk)

        if p:
            print("Produk ditemukan")
            print("ID    :", p.id_produk)
            print("Nama  :", p.nama)
            print("Harga :", p.harga)
            print("Stok  :", p.stok)
        else:
            print("Data tidak ditemukan")

    def edit(self):
        id_produk_lama = int(input("Masukkan ID yang akan diubah :"))

        p = self.cari_produk(id_produk_lama)

        if p:
            nama_baru = input("Masukkan Nama Baru :")

            while True:
                try:
                    harga_baru = int(input("Masukkan Harga Baru :"))
                    break
                except ValueError:
                    print("Input harus angka")

            while True:
                try:
                    stok_baru = int(input("Masukkan Stok Baru :"))
                    break
                except ValueError:
                    print("Input harus angka")
        
            p.nama = nama_baru
            p.harga = harga_baru
            p.stok = stok_baru
            self.simpan_data()
            print("Produk berhasil diubah")
        else:
            print("Produk tidak ada")

    def hapus(self):
        while True:
            try:
                id_produk = int(input("Masukkan ID yang ingin dihapus :"))
                break
            except ValueError:
                print("Input Harus angka")

        produk = self.cari_produk(id_produk)

        if produk:
            self.daftar_produk.remove(produk)
            self.simpan_data()
            print("Produk berhasil dihapus")
        else:
            print("Produk tidak ada")

    def menu(self): 
        print("===== MENU =====")
        print("1. Lihat Produk")
        print("2. Tambah Produk")
        print("3. Transaksi")
        print("4. Ceckout")
        print("5. Lihat Riwayat Transaksi")
        print("6. Edit Produk")
        print("7. Hapus Produk")
        print("8. cari Produk")
        print("9. Keluar")