from datetime import datetime
import json
class Transaksi:

    def __init__(self):
        self.keranjang = []
        self.riwayat = []
        self.load_data()

    def load_data(self):
        try:
            with open("transaksi.json", "r", encoding="utf-8") as file:
                data = json.load(file)

            self.riwayat = data
        
        except (FileNotFoundError, json.JSONDecodeError):
            self.riwayat = []
    
    def simpan_data(self):
        with open("transaksi.json", "w", encoding="utf-8") as file:
            json.dump(self.riwayat, file, indent=4, ensure_ascii=False)

    def simpan_transaksi(self, total, uang, kembalian):
        tanggal = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        items = []

        for item in self.keranjang:
            items.append({
                "id_produk": item["produk"].id_produk,
                "nama": item["produk"].nama,
                "harga": item["produk"].harga,
                "jumlah": item["jumlah"],
                "subtotal": item["produk"].harga * item["jumlah"]
            })

        id_transaksi = self.buat_id_transaksi_baru()

        transaksi = {
            "id_transaksi": id_transaksi,
            "tanggal" : tanggal,
            "items": items,
            "total": total,
            "bayar": uang,
            "kembalian": kembalian
        }

        self.riwayat.append(transaksi)
        self.simpan_data()

    def lihat_riwayat(self):
        if not self.riwayat:
            print("Belum ada transaksi")
            return

        for transaksi in self.riwayat:

            print("=" * 45)
            print("ID Transaksi :", transaksi["id_transaksi"])
            print("Tanggal      :", transaksi["tanggal"])
            print("=" * 45)
            
            for item in transaksi["items"]:
                print("- Nama     :", item["nama"])
                print("  Harga    :", item["harga"])
                print("  Jumlah   :", item["jumlah"])
                print("  Subtotal :", item["subtotal"])
                print()

            print("=" * 45)
            print("Total      :", transaksi["total"])
            print("Bayar      :", transaksi["bayar"])
            print("Kembalian  :", transaksi["kembalian"])
            print("=" * 45)    

    def tambah_ke_keranjang(self, produk, jumlah):

        if jumlah > produk.stok:
            print("Stok tidak cukup")
            return

        item = {
            "produk": produk,
            "jumlah": jumlah
        }

        self.keranjang.append(item)

    def hitung_total(self):
        total = 0

        for item in self.keranjang:
            subtotal = item["produk"].harga * item["jumlah"]
            total = total + subtotal
        return total

    def lihat_keranjang(self):
        print("\n===== KERANJANG =====")
        if not self.keranjang:
            print("Keranjang kosong")
            return
        
        for item in self.keranjang:
            print("ID      :", item["produk"].id_produk)
            print("Nama    :", item["produk"].nama)
            print("Harga   :", item["produk"].harga)
            print("Jumlah  :", item["jumlah"])
            print("Subtotal:", item["produk"].harga * item["jumlah"])
            print("-" * 30)
        print(f"\nTotal Item : {len(self.keranjang)}")

    def checkout(self, manager_produk):
        if not self.keranjang:
            print("Keranjang kosong")
            return
        total = self.hitung_total()

        print("\n===== CHECKOUT =====")
        print("Total Belanja :", total)

        while True:
            try:
                uang = int(input("Masukkan Uang : "))
                break
            except ValueError:
                print("Input harus angka!")

        if uang < total:
            print("Uang tidak cukup")
            return
        
        kembalian = uang - total

        print("Kembalian :", kembalian)

        for item in self.keranjang:
            item["produk"].stok -= item["jumlah"]

        manager_produk.simpan_data()

        self.simpan_transaksi(total, uang, kembalian)

        self.keranjang.clear()

        print("Transaksi berhasil!")
        
    def buat_id_transaksi_baru(self):
        if not self.riwayat:
            return "TRX0001"

        id_terbesar = 0

        for t in self.riwayat:
            angka = int(t["id_transaksi"][3:])

            if angka > id_terbesar:
                id_terbesar = angka

        return f"TRX{id_terbesar + 1:04d}"
            
