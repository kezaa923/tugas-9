data_panen = {
    "lokasi1": {
        "nama_lokasi": "Kebun A",
        "hasil_panen": {"padi": 1200, "jagung": 800, "kedelai": 500},
    },
    "lokasi2": {
        "nama_lokasi": "Kebun B",
        "hasil_panen": {"padi": 1500, "jagung": 900, "kedelai": 450},
    },
    "lokasi3": {
        "nama_lokasi": "Kebun C",
        "hasil_panen": {"padi": 1100, "jagung": 750, "kedelai": 600},
    },
    "lokasi4": {
        "nama_lokasi": "Kebun D",
        "hasil_panen": {"padi": 1300, "jagung": 850, "kedelai": 550},
    },
    "lokasi5": {
        "nama_lokasi": "Kebun E",
        "hasil_panen": {"padi": 1400, "jagung": 950, "kedelai": 480},
    },
}
def harvest_list(data):
    """Fungsi untuk melihat hasil panen dengan struktur kode yang berbeda"""
    
    print(" ======== Nomor 1 ===========")
    for key, value in data.items():
        nama = value["nama_lokasi"]
        hasil = value["hasil_panen"]
        print(f"Lokasi nguli {nama}")
        print("Hasil panen")
        print(f"Jagung: {hasil['jagung']}")
        print(f"Padi: {hasil['padi']}")
        print(f"Kedelai: {hasil['kedelai']}\n")
    
    print("\n ======== Nomor 2 ===========")
    lokasi2 = data.get("lokasi2", {})
    if lokasi2:
        nama = lokasi2["nama_lokasi"]
        jagung = lokasi2["hasil_panen"]["jagung"]
        print(f"Lokasi {nama}")
        print("Hasil panen")
        print(f"Jagung: {jagung}\n")
    
    print("\n ======== Nomor 3 ===========")
    lokasi3 = data.get("lokasi3", {})
    if lokasi3:
        nama = lokasi3["nama_lokasi"]
        print(f"Nama Lokasi dari lokasi3 adalah {nama}\n")
    
    print(" ======== Nomor 4 ===========")
    total_padi = sum(value["hasil_panen"]["padi"] for value in data.values())
    total_kedelai = sum(value["hasil_panen"]["kedelai"] for value in data.values())
    print(f"Hasil panen Padi : {total_padi} , Kedelai : {total_kedelai}")
    
    print("\n ======== Nomor 5 ===========")
    lokasi_dict = {
        value["nama_lokasi"]: value["hasil_panen"] for value in data.values()
    }
    for nama, hasil in lokasi_dict.items():
        print(f"Lokasi {nama}")
        print(f"Padi: {hasil['padi']}")
        print(f"Kedelai: {hasil['kedelai']}")
        print(f"Jagung: {hasil['jagung']}\n")
    
    print("\n\n\n ======== Nomor 6 ===========")
    for nama, hasil in lokasi_dict.items():
        if hasil["padi"] > 1300 or hasil["jagung"] > 800:
            print(f"Lokasi {nama} memerlukan perhatian khusus")
        else:
            print(f"Lokasi {nama} dalam kondisi baik")

harvest_list(data_panen)
print(1)

