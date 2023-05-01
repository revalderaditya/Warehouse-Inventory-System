#Stock awal
inventory = {
    "tehpucukjkt": {'Warehouse': 'jakarta',
        'Category': 'FMCG',
        'Rack Location': 'J1',
        'Product Name': 'teh pucuk',
        'Quantity (pcs)' : 1000},
    "indomiejkt": {'Warehouse': 'jakarta',
        'Category': 'FMCG',
        'Rack Location': 'J1',
        'Product Name': 'indomie',
        'Quantity (pcs)' : 500},
    "ayamjkt": {'Warehouse': 'jakarta',
        'Category': 'FRESH',
        'Rack Location': 'JF1',
        'Product Name': 'ayam potong',
        'Quantity (pcs)' : 10},
    "waferbdg": {'Warehouse': 'bandung',
        'Category': 'FMCG',
        'Rack Location': 'B1',
        'Product Name': 'wafer tango',
        'Quantity (pcs)' : 750},
    "spritebdg": {'Warehouse': 'bandung',
        'Category': 'FMCG',
        'Rack Location': 'B1',
        'Product Name': 'sprite 500ml',
        'Quantity (pcs)' : 800},
    "telorbdg": {'Warehouse': 'bandung',
        'Category': 'FRESH',
        'Rack Location': 'BF1',
        'Product Name': 'telor ayam',
        'Quantity (pcs)' : 100}
}

#Functions part

def menu_awal():
    print ('Berikut Ini List Barang yang Tersedia\n')
    print ('Warehouse\t|Category\t| Rack Location\t| Product Name\t| Quantity (pcs)')
    print ('=======================================================================')
    for i in inventory.keys():
         print(f'{inventory[i]["Warehouse"]}\t\t| {inventory[i]["Category"]}\t\t| {inventory[i]["Rack Location"]}\t\t|{inventory[i]["Product Name"]}\t| {int(inventory[i]["Quantity (pcs)"])}')

def showwarehouse():
    wh= input('Masukan nama warehouse yang mau ditampilkan: ')
    print ('Warehouse\t|Category\t| Rack Location\t| Product Name\t| Quantity (pcs)')
    print ('=======================================================================')
    for i in inventory.keys():
        if wh.lower() in inventory[i]["Warehouse"]:
            print('{}\t\t|{}\t\t|{}\t\t|{}\t|{}'.format(inventory[i]["Warehouse"],inventory[i]["Category"],inventory[i]["Rack Location"],inventory[i]["Product Name"],inventory[i]["Quantity (pcs)"]))
        else:
            continue


def showcat():
    category=input('''
    Pilihan category yang tersedia

    1. FMCG
    2. FRESH

    Masukan pilihan category yang ingin ditampilkan: 
    ''')

    if category=='1':
        print ('Warehouse\t|Category\t| Rack Location\t| Product Name\t| Quantity (pcs)')
        print ('=======================================================================')
        for i in inventory.keys():
            if 'FMCG' in inventory[i]["Category"]:
                print("{}\t\t|{}\t\t|{}\t\t|{}\t|{}".format(inventory[i]["Warehouse"],inventory[i]["Category"],inventory[i]["Rack Location"],inventory[i]["Product Name"],inventory[i]["Quantity (pcs)"]))
            else:
                continue

    elif category=='2':
        print ('Warehouse\t|Category\t| Rack Location\t| Product Name\t| Quantity (pcs)')
        print ('=======================================================================')
        for i in inventory.keys():
            if 'FRESH' in inventory[i]["Category"]:
                print("{}\t\t|{}\t\t|{}\t\t|{}\t|{}".format(inventory[i]["Warehouse"],inventory[i]["Category"],inventory[i]["Rack Location"],inventory[i]["Product Name"],inventory[i]["Quantity (pcs)"]))
            else:
                continue
    else:
        print('MASUKAN PILIHAN YANG BENAR!')


def showrack():
    rack=input('Masukan lokasi rack yang diinginkan: ')
    print ('Warehouse\t|Category\t| Rack Location\t| Product Name\t| Quantity (pcs)')
    print ('=======================================================================')
    for i in inventory.keys():
        if rack.upper() in inventory[i]["Rack Location"]:
            print('{}\t\t|{}\t\t|{}\t\t|{}\t|{}'.format(inventory[i]["Warehouse"],inventory[i]["Category"],inventory[i]["Rack Location"],inventory[i]["Product Name"],inventory[i]["Quantity (pcs)"]))
        else:
            continue


def tambahstockbaru():
    category_list1 = ['FMCG']
    category_list2 = ['FRESH']
    newkeys = input('Masukan Unique Keys baru : ')
    if newkeys.lower() not in inventory.keys():
        newwh = input('Masukan lokasi warehouse: ')
        newcat = input('Masukan category: ')
        if newcat.upper() in category_list1:
            newrack = input('Masukan lokasi rack product: ')
            newname = input('Masukan nama product: ')
            newqty = int(input('Masukan quantity (pcs) barang: '))
            inventory[newkeys] = {"Warehouse": newwh.lower(), "Category": newcat.upper(), "Rack Location": newrack.upper(), "Product Name": newname.lower(), "Quantity (pcs)": newqty}
        elif newcat.upper() in category_list2:
            newrack = input('Masukan lokasi rack product: ')
            newname = input('Masukan nama product: ')
            newqty = int(input('Masukan quantity (pcs) barang: '))
            inventory[newkeys] = {"Warehouse": newwh.lower(), "Category": newcat.upper(), "Rack Location": newrack.upper(), "Product Name": newname.lower(), "Quantity (pcs)": newqty}
        else:
            print('CATEGORY TERSEBUT TIDAK ADA')
    else:
        print('UNIQUE KEYS TERSEBUT SUDAH ADA HARAP MASUKAN UNIQUE KEYS YANG BERBEDA!')


def updatestockbarang():
    category_list1 = ['FMCG']
    category_list2 = ['FRESH']
    keysupdate= input('Masukan unique keys yang mau di update: ')
    if keysupdate.lower() in inventory.keys():
        WH_update= input('Masukan lokasi warehouse: ')
        catupdate= input('Masukan jenis product: ')
        if catupdate.upper() in category_list1:
            rackupdate = input('Masukan lokasi rack product: ')
            nameupdate= input('Masukan nama product: ')
            qtyupdate= int(input('Masukan quantity (pcs) barang: '))
            inventory[keysupdate]= {"Warehouse": WH_update.lower(), "Category": catupdate.upper(), "Rack Location": rackupdate.upper(), "Product Name": nameupdate.lower(), "Quantity (pcs)": qtyupdate}
        elif catupdate.upper() in category_list2:
            rackupdate = input('Masukan lokasi rack product: ')
            nameupdate= input('Masukan nama product: ')
            qtyupdate= int(input('Masukan quantity (pcs) barang: '))
            inventory[keysupdate]= {"Warehouse": WH_update.lower(), "Category": catupdate.upper(), "Rack Location": rackupdate.upper(), "Product Name": nameupdate.lower(), "Quantity (pcs)": qtyupdate}
        else:
            print('CATEGORY TERSEBUT TIDAK ADA')
    else:
        print('UNIQUE KEYS YANG DIINGINKAN TIDAK ADA HARAP MASUKAN UNIQUE KEYS YANG BENAR!')


def barangkeluar():
    keyskeluar= input('Masukan keys yang mau keluar: ')
    if keyskeluar.lower() in inventory.keys():
        qtykeluar= int(input('Masukan jumlah barang yang keluar: '))
        if qtykeluar < inventory[keyskeluar]['Quantity (pcs)']:
            inventory[keyskeluar]['Quantity (pcs)'] = inventory[keyskeluar]['Quantity (pcs)']-qtykeluar
            print(f'Barang yang dikeluarkan sebanyak {qtykeluar}')
        elif qtykeluar == inventory[keyskeluar]['Quantity (pcs)']:
            inventory[keyskeluar]['Quantity (pcs)'] = inventory[keyskeluar]['Quantity (pcs)']-qtykeluar
            print(f'''Barang yang dikeluarkan sebanyak {qtykeluar} 
            STOCK SUDAH HABIS SEGERA RESTOCK!''')
        elif qtykeluar > inventory[keyskeluar]['Quantity (pcs)']:
            print('JUMLAH STOCK YANG TERSEDIA TIDAK CUKUP')    
        else:
            print('MASUKAN JUMLAH STOCK YANG BENAR')
    else:   
        print('UNIQUE KEYS YANG DIINGINKAN TIDAK ADA HARAP MASUKAN UNIQUE KEYS YANG BENAR!')

def sortstock():
    sort_stock = sorted(inventory.items(), key=lambda x: x[1]['Quantity (pcs)'])
    print ('Warehouse\t|Category\t| Rack Location\t| Product Name\t| Quantity (pcs)')
    print ('=======================================================================')
    for key, value in sort_stock:
        print(f"{value['Warehouse']}\t\t|{value['Category']}\t\t|{value['Rack Location']}\t\t|{value['Product Name']}\t|{value['Quantity (pcs)']}")
    

def delete():
    keysdelete= input('Masukan keys yang ingin di hapus: ')
    if keysdelete.lower() in inventory.keys():
        del inventory[keysdelete]
    else:
        print('UNIQUE KEYS YANG INGIN DIHAPUS TIDAK ADA')

#Menu

while True :
    menu = input(
        '''
        Selamat Datang Di Gudang Revalde

        List Menu
        1. Menampilkan Stock yang Ada
        2. Menambah Barang
        3. Menghapus Barang
        4. Mengeluarkan Barang
        5. Cek Stock
        6. Exit Program

        Masukan Menu Yang Anda Inginkan : '''
    )

    if menu=='1':
        extramenu= input(
            '''
            Ingin menapilkan 
            1. Semua stock di inventory
            2. Semua stock berdasarkan warehouse
            3. Semua stock berdasarkan category
            4. Semua stock berdasarkan lokasi rack
            5. Kembali ke menu awal
            6. Exit
            
            Pilih menu yang anda inginkan: '''
        )

        if extramenu=='1':
            menu_awal()
        elif extramenu=='2':
            showwarehouse()
        elif extramenu=='3':
            showcat()
        elif extramenu=='4':
            showrack()
        elif extramenu=='5':
            continue
        elif extramenu=='6':
            print('TERIMA KASIH')
            break
        else:
            print('MASUKAN MENU YANG BENAR')

    elif menu=='2':
        menu2= input('''
        1. Menambahkan Stock Baru
        2. Merubah Barang yang Sudah ada
        3. Kembali ke menu awal
        4. Exit
        Pilih menu yang diinginkan: '''
                            )           
        if menu2=='1':
            tambahstockbaru()
        elif menu2=='2':
            updatestockbarang()
        elif menu2=='3':
            continue
        elif menu2=='4':
            print('TERIMA KASIH')
            break
        else:
            print('Masukan pilihan menu yang benar')
    
    elif menu=='3':
        delete()

    elif menu=='4':
        barangkeluar()

    elif menu=='5':
        sortstock()

    elif menu == '6' :
        print('TERIMA KASIH!')
        break

    else : 
        print ('Masukan Menu Yang Benar!!!')