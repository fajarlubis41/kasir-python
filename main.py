from manager import ManagerProduk
from produk import Produk
from transaksi import Transaksi

manager_produk = ManagerProduk()
manager_transaksi = Transaksi()

jalan = True

while jalan:
    manager_produk.menu()

    pilihan = input("Pilih menu : ")

    if pilihan == "1":
        manager_produk.lihat()

    elif pilihan == "2":
        manager_produk.tambah()

    elif pilihan == "3":
        id_produk = int(input("ID Produk: "))
        jumlah = int(input("Jumlah: "))

        produk = manager_produk.cari_produk(id_produk)

        if produk:
            manager_transaksi.tambah_ke_keranjang(produk, jumlah)
            manager_transaksi.lihat_keranjang()
            total = manager_transaksi.hitung_total()
            print("Total :", total)
        else:
            print("Produk tidak ditemukan")
        
    elif pilihan == "4":
        manager_transaksi.checkout(manager_produk)

    elif pilihan == "5":
        manager_transaksi.lihat_riwayat()

    elif pilihan == "6":
        manager_produk.edit()

    elif pilihan == "7":
        manager_produk.hapus()

    elif pilihan == "8":
        manager_produk.cari()
        
    elif pilihan == "9":
        print("Terimakasih")
        jalan = False