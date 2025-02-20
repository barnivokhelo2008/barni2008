konyvek = []

def konyv_hozzaadasa(cím, szerzo):
    konyv = {'cím': cím, 'szerzo': szerzo}
    konyvek.append(konyv)
    print(f"könyv hozzáadva: {cím} by {szerzo}")

def konyv_torlese(cím):
    global konyvek
    konyvek = [konyv for konyv in konyvek if konyv['title'] != cím]
    print(f"könyv törölve: {cím}")

def konyvek_listazasa():
    if not konyvek:
        print("nincs könyv a listában.")
    else:
        print("A könyvtárban található könyvek:")
        for konyv in konyvek:
            print(f"cím: {konyv['cím']}, szerzo: {konyv['szerzo']}")

def konyv_keresese(cím):
    konyvek_keresese = [konyv for konyv in konyvek if cím.lower() in konyv['cím'].lower()]
    if konyvek_keresese:
        print("keresett könyvek:")
        for book in konyvek_keresese:
            print(f"cím: {book['cím']}, szerzo: {book['szerzo']}")
    else:
        print("nem található könyv ilyen címmel.")


def show_menu():
    while True:
        print("\nkönyvtárkezelő Program")
        print("1. könyv hozzáadása")
        print("2. könyv törlése")
        print("3. könyvek listázása")
        print("4. könyv keresése")
        print("5. kilépés")
        choice = input("válassz egy lehetőséget: ")

        if choice == '1':
            cím = input("Add meg a könyv címét: ")
            szerzo = input("Add meg a könyv szerzőjét: ")
            konyv_hozzaadasa(cím, szerzo)
        elif choice == '2':
            cím = input("Add meg a törölni kívánt könyv címét: ")
            konyv_torlese(cím)
        elif choice == '3':
            konyvek_listazasa()
        elif choice == '4':
            cím = input("Add meg a keresett könyv címét: ")
            konyv_keresese(cím)
        elif choice == '5':
            print("kilépés a programból...")
            break
        else:
            print("érvénytelen választás! Kérlek próbáld újra.")

if __name__ == "__main__":
    show_menu()
    