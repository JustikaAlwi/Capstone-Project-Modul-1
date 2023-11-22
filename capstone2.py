# CAPSTONE PROJECT MODUL 1
# Job Connector Data Science Online Learning
# JUSTIKA ALWI

# MENU UTAMA
# [1] Tampilkan Data Pasien Rawat Inap
# [2] Tampilkan Detail Pasien         
# [3] Tambah Data Pasien Rawat Inap
# [4] Update Biaya/Pembayaran/Status Pasien
# [5] Hapus Data Pasien Rawat Inap (Pasien Keluar Bangsal)       
# [0] Keluar

def WelcomeGreeting ():
    print("        Selamat Datang di Rumah Sakit ABC")
    print ("*" * 50)

def Keluar ():
    print ("*" * 50)
    print('Terima Kasih!')
    print('Have a nice day!')
    print ("*" * 50)

# Data Pasien Bangsal Bromelia
data_pasien= [ 
{'NO':1,'Reg ID': 23110001, 'Nama Pasien': 'Devi Sartika', 'Nomor Kamar': 501, 'DPJP':'dr. Rahmi Ayu, Sp.A', 'Total Biaya': 6500000, 'Pembayaran' : 6000000, 'Status': 'Kurang Bayar'},
{'NO':2,'Reg ID': 23110002, 'Nama Pasien': 'Rangga Saputra', 'Nomor Kamar': 502, 'DPJP':'dr. Sheandra, Sp.P', 'Total Biaya': 10500000, 'Pembayaran' : 5000000, 'Status': 'Kurang Bayar'},
{'NO':3,'Reg ID': 23110003, 'Nama Pasien': 'Wahyu TS', 'Nomor Kamar': 503, 'DPJP':'dr. Radya A, Sp.PD', 'Total Biaya': 23000000, 'Pembayaran' : 10000000,'Status': 'Kurang Bayar'},
{'NO':4,'Reg ID': 23110004, 'Nama Pasien': 'Monica Rani', 'Nomor Kamar': 504, 'DPJP':'dr. Ika Wulan, Sp.BS', 'Total Biaya': 15000000, 'Pembayaran' : 12000000,'Status': 'Kurang Bayar'},
{'NO':5,'Reg ID': 23110005, 'Nama Pasien': 'Arief Hidayat', 'Nomor Kamar': 505, 'DPJP':'dr. Putri Y, Sp.N', 'Total Biaya': 8500000, 'Pembayaran' : 8500000,'Status': 'Nihil'},
]

# Fungsi untuk display Tabel Data Pasien (READ)
def Tabel_data_pasien ():
    if len(data_pasien)!= 0:
        print('*'*60)
        print('\t\tDAFTAR PASIEN BANGSAL BROMELIA')
        print('*'*60)
        print('''
        [1] Tampilkan Data Pasien
        [2] Kembali ke Menu Utama
        ''')
        submenu = int(input('Pilih [1]/[2]: '))
        if submenu == 1:
            print('\n')
            print('='*150)
            print(f"|{'NO':^6}|{'Reg ID':^10}|{'Nama Pasien':^25}|{'Nomor Kamar':^15}|{'DPJP':^25}|{'Total Biaya':^20}|{'Pembayaran':^20}|{'Status':^20}|")
            print('='*150)
            for patient in data_pasien:  
                print(f"|{patient['NO']:<6}|{patient['Reg ID']:<10}|{patient['Nama Pasien']:<25}|{patient['Nomor Kamar']:<15}|{patient['DPJP']:<25}|{patient['Total Biaya']:<20}|{patient['Pembayaran']:<20}|{patient['Status']:<20}|")
            print('='*150)
    
            submenu1 = input('Kembali ke Menu Utama? (y/t): ').lower()
            if submenu1 == 'y':
                Menu_Utama ()
            elif submenu1 == 't':
                Tabel_data_pasien()
            else:
                print('Perintah tidak ditemukan!')
                Menu_Utama()
        elif submenu == 2:
            Menu_Utama ()
        else:
            print('Hanya menerima input 1 / 2!')
    elif len(data_pasien)==0:
        print('Tidak Ada Pasien Di Bangsal Bromelia Saat Ini!')

# Fungsi untuk display Tabel Data Pasien dengan input tertentu (READ)
def Tampilan_detail_pasien ():
    if len(data_pasien)!= 0:
        print('*'*60)
        print('\tDetail Pasien Rawat Inap Bangsal Bromelia')
        print('*'*60)
        print('''
            [1] Tampilkan Detail Data Pasien
            [2] Kembali ke Menu Utama
            ''')
        submenu2 = int(input('Pilih [1]/[2]: '))
        if submenu2 == 1:
            while True:
                regID = int(input('Masukkan Reg ID Pasien (23xxxxxx): '))
                reg_Id_pasien = []
                for i in range(len(data_pasien)):
                    reg_Id_pasien.append(data_pasien[i]['Reg ID'])

                if regID in reg_Id_pasien:
                    print('\t\t\t\t\t\tDetail Pasien Bangsal Bromelia Reg ID {}'.format(regID))
                    print('='*150)
                    print(f"|{'NO':^6}|{'Reg ID':^10}|{'Nama Pasien':^25}|{'Nomor Kamar':^15}|{'DPJP':^25}|{'Total Biaya':^20}|{'Pembayaran':^20}|{'Status':^20}|")
                    print('='*150)
                    print(f"|{data_pasien[reg_Id_pasien.index(regID)]['NO']:<6}|{regID:<10}|{data_pasien[reg_Id_pasien.index(regID)]['Nama Pasien']:<25}|{data_pasien[reg_Id_pasien.index(regID)]['Nomor Kamar']:<15}|{data_pasien[reg_Id_pasien.index(regID)]['DPJP']:<25}|{data_pasien[reg_Id_pasien.index(regID)]['Total Biaya']:<20}|{data_pasien[reg_Id_pasien.index(regID)]['Pembayaran']:<20}|{data_pasien[reg_Id_pasien.index(regID)]['Status']:<20}|")
                    print('='*150)
                else:
                    print('Registrasi Pasien {} Tidak Ditemukan. Silahkan Coba Lagi!'.format(regID))
                    continue
        
                submenu1 = input('Kembali ke Menu Utama? (y/t): ').lower()
                if submenu1 == 'y':
                    Menu_Utama ()
                elif submenu1 == 't':
                    continue
                else:
                    print('Perintah tidak ditemukan!')    
        elif submenu2 == 2:
            Menu_Utama ()
        else:
            print('Hanya menerima input 1 / 2!')         
    elif len(data_pasien)==0:
        print('Tidak Ada Pasien Di Bangsal Bromelia Saat Ini!')

# Fungsi Tambah data Pasien (CREATE)
def Tambahan_data_pasien ():
    print('*'*60)
    print('\t\tTambah Data Pasien Rawat Inap')
    print('*'*60)
    print('''
          
    [1] Tambah Data Pasien
    [2] Kembali ke Menu Utama
          
    ''')
    submenu3 = int(input('Pilih [1]/[2]: '))
    print('*'*60)
    if submenu3 == 1:
        while True:
            # nomor untuk data pasien baru
            maxNo = max(patient['NO'] for patient in data_pasien)
            NoBaru = maxNo + 1
        
            # Reg ID untuk pasien baru
            max_RegID = max(patient['Reg ID'] for patient in data_pasien)
            RegID_Baru = max_RegID + 1
        
            # Input Nama Pasien Baru
            NamaPasienBaru = input('Masukkan Nama Pasien: ')
        
            # Input Nomor Kamar untuk Pasien Baru
            for key in ['Reg ID', 'Nama Pasien', 'Nomor Kamar', 'DPJP', 'Total Biaya','Pembayaran', 'Status']:
                if key == 'Nomor Kamar':
                    while True:
                        NoKamarBaru = (input('Masukkan Nomor Kamar: '))
                        if not any(patient[key] == int(NoKamarBaru) for patient in data_pasien):
                            break
                        else:
                            print("Kamar {} sudah terisi. Silahkan pilih kamar lain!".format(NoKamarBaru))             
                            continue    
                        
    
    
            # Input Nama Dokter
            DPJP = input('Masukkan Nama Dokter: ')

            # Input Total Biaya Berjalan
            TotalBiaya = input('Masukkan Total Biaya: ')

            # Input Pembayaran Pasien
            UangMuka = input('Masukkan Pembayaran: ')

            # Status Pasien
            StatusPulang = input('Masukkan Status Pasien (Kurang Bayar/Lebih Bayar/Nihil): ')

            data_pasien_baru = {'NO': NoBaru, 'Reg ID': RegID_Baru, 'Nama Pasien' : str(NamaPasienBaru), 'Nomor Kamar' : NoKamarBaru, 'DPJP': DPJP, 'Total Biaya': TotalBiaya, 'Pembayaran': UangMuka, 'Status': StatusPulang }
            data_pasien.append(data_pasien_baru)
            data_baru = print(input('Tampilkan Data Pasien Terbaru?(y/t):').lower())
            if data_baru == 'y':
                Tabel_data_pasien () 
            elif data_baru == 't':
                Menu_Utama ()
            else:
                print("Hanya menerima input 'y' atau 't'!")
                Menu_Utama()
    elif submenu3 == 2:
        Menu_Utama ()
    else:
        print('Hanya menerima input 1 / 2!')
    
# Fungsi Update Data Pasien (UPDATE)
def Update_data_pasien (): 
    if len(data_pasien)!= 0:
        while True:
            print('\n')
            print('\tUpdate Biaya/Pembayaran/Status Pasien')
            print('*'*60)
            print('''
              
            [1] Update Total Biaya Pasien
            [2] Update Pembayaran Pasien
            [3] Kembali ke Menu Utama
              
            ''')
            submenu4 = int(input('Pilih [1]/[2]/[3]: '))
            if submenu4 == 1:
                while True:
                    regID4 = int(input('Masukkan Reg ID Pasien (23xxxxxx): '))
                    reg_Id_pasien = []
                    for i in range(len(data_pasien)):
                        reg_Id_pasien.append(data_pasien[i]['Reg ID'])

                    if regID4 in reg_Id_pasien:
                        Update_data_pasien = data_pasien[reg_Id_pasien.index(regID4)]
                        print('='*150)
                        print(f"|{'NO':^6}|{'Reg ID':^10}|{'Nama Pasien':^25}|{'Nomor Kamar':^15}|{'DPJP':^25}|{'Total Biaya':^20}|{'Pembayaran':^20}|{'Status':^20}|")
                        print('='*150)
                        print(f"|{data_pasien[reg_Id_pasien.index(regID4)]['NO']:<6}|{regID4:<10}|{data_pasien[reg_Id_pasien.index(regID4)]['Nama Pasien']:<25}|{data_pasien[reg_Id_pasien.index(regID4)]['Nomor Kamar']:<15}|{data_pasien[reg_Id_pasien.index(regID4)]['DPJP']:<25}|{data_pasien[reg_Id_pasien.index(regID4)]['Total Biaya']:<20}|{data_pasien[reg_Id_pasien.index(regID4)]['Pembayaran']:<20}|{data_pasien[reg_Id_pasien.index(regID4)]['Status']:<20}|")
                        print('='*150)
                        
                        Total_Biaya_Update = int(input('Masukkan Tambahan Biaya: '))
                        Update_data_pasien['Total Biaya'] = Total_Biaya_Update + (data_pasien[reg_Id_pasien.index(regID4)]['Total Biaya'])
                        
                        #Auto Update Status Pasien
                        if Update_data_pasien ['Total Biaya'] == Update_data_pasien ['Pembayaran']:
                            Update_data_pasien ['Status'] = 'Nihil'
                        elif Update_data_pasien['Total Biaya'] < Update_data_pasien ['Pembayaran']:
                            Update_data_pasien ['Status'] = 'Kurang Bayar'
                        else:
                            Update_data_pasien ['Status'] = 'Lebih Bayar'
                        print('''
                    [1] Tampilkan Data Pasien
                    [2] Kembali ke Menu Utama
                        ''')
                        display_updated_data = int(input("Pilih 1/2:"))
                        if display_updated_data == 1:
                            print('='*150)
                            print(f"|{'NO':^6}|{'Reg ID':^10}|{'Nama Pasien':^25}|{'Nomor Kamar':^15}|{'DPJP':^25}|{'Total Biaya':^20}|{'Pembayaran':^20}|{'Status':^20}|")
                            print('='*150)
                            print(f"|{Update_data_pasien['NO']:<6}|{regID4:<10}|{Update_data_pasien['Nama Pasien']:<25}|{Update_data_pasien['Nomor Kamar']:<15}|{Update_data_pasien['DPJP']:<25}|{Update_data_pasien['Total Biaya']:<20}|{Update_data_pasien['Pembayaran']:<20}|{Update_data_pasien['Status']:<20}|")
                            print('='*150)
                            submenu5 = input('Kembali ke Menu Utama? (y/t): ').lower()
                            if submenu5 == 'y':
                                Menu_Utama ()
                            elif submenu5 == 't':
                                break
                            else:
                                print('Perintah tidak ditemukan!')
                                Menu_Utama()
                        elif display_updated_data ==2:
                            Menu_Utama()
                        else:
                            print('Hanya Menerima Input 1/2: ')
                            break
                    else:
                        print('Reg ID Pasien {} tidak ditemukan. Silahkan Coba Lagi!'.format(regID4))
                        continue

            elif submenu4 == 2:
                while True:
                    regID4 = int(input('Masukkan Reg ID Pasien (23xxxxxx): '))
                    reg_Id_pasien = []
                    for i in range(len(data_pasien)):
                        reg_Id_pasien.append(data_pasien[i]['Reg ID'])

                    if regID4 in reg_Id_pasien:
                        Update_data_pasien = data_pasien[reg_Id_pasien.index(regID4)]
                        print('='*150)
                        print(f"|{'NO':^6}|{'Reg ID':^10}|{'Nama Pasien':^25}|{'Nomor Kamar':^15}|{'DPJP':^25}|{'Total Biaya':^20}|{'Pembayaran':^20}|{'Status':^20}|")
                        print('='*150)
                        print(f"|{data_pasien[reg_Id_pasien.index(regID4)]['NO']:<6}|{regID4:<10}|{data_pasien[reg_Id_pasien.index(regID4)]['Nama Pasien']:<25}|{data_pasien[reg_Id_pasien.index(regID4)]['Nomor Kamar']:<15}|{data_pasien[reg_Id_pasien.index(regID4)]['DPJP']:<25}|{data_pasien[reg_Id_pasien.index(regID4)]['Total Biaya']:<20}|{data_pasien[reg_Id_pasien.index(regID4)]['Pembayaran']:<20}|{data_pasien[reg_Id_pasien.index(regID4)]['Status']:<20}|")
                        print('='*150)
                        Total_Pembayaran_Update = int(input('Masukkan Tambahan Pembayaran Pasien: '))
                        print('\n')
                        Update_data_pasien['Pembayaran'] = Total_Pembayaran_Update + (data_pasien[reg_Id_pasien.index(regID4)]['Pembayaran'])
                        
                        #Auto Update Status Pasien
                        if Update_data_pasien['Total Biaya'] == Update_data_pasien ['Pembayaran']:
                            Update_data_pasien ['Status'] = 'Nihil'
                        elif Update_data_pasien['Total Biaya'] > Update_data_pasien ['Pembayaran']:
                            Update_data_pasien ['Status'] = 'Kurang Bayar'
                        elif Update_data_pasien['Total Biaya'] < Update_data_pasien ['Pembayaran']:
                            Update_data_pasien ['Status'] = 'Lebih Bayar'
                        print('''
                            [1] Tampilkan Data Pasien
                            [2] Kembali ke Menu Utama
                        ''')
                        display_updated_data = int(input("Pilih 1/2:"))
                        if display_updated_data == 1:
                            print('='*150)
                            print(f"|{'NO':^6}|{'Reg ID':^10}|{'Nama Pasien':^25}|{'Nomor Kamar':^15}|{'DPJP':^25}|{'Total Biaya':^20}|{'Pembayaran':^20}|{'Status':^20}|")
                            print('='*150)
                            print(f"|{Update_data_pasien['NO']:<6}|{regID4:<10}|{Update_data_pasien['Nama Pasien']:<25}|{Update_data_pasien['Nomor Kamar']:<15}|{Update_data_pasien['DPJP']:<25}|{Update_data_pasien['Total Biaya']:<20}|{Update_data_pasien['Pembayaran']:<20}|{Update_data_pasien['Status']:<20}|")
                            print('='*150)
                            submenu5 = input('Kembali ke Menu Utama? (y/t): ').lower()
                            if submenu5 == 'y':
                                Menu_Utama ()
                            elif submenu5 == 't':
                                break
                            else:
                                print('Perintah tidak ditemukan!')
                                Menu_Utama()
                        elif display_updated_data ==2:
                            Menu_Utama()
                        else:
                            print('Hanya Menerima Input 1/2: ')
                            break
                    else:
                        print('Reg ID Pasien {} tidak ditemukan. Silahkan Coba Lagi!'.format(regID4))
                        continue
            elif submenu4 == 3:
                Menu_Utama()
            else:
                print('Hanya menerima input 1/2/3!')
    elif len(data_pasien) ==0:
        print('Tidak Ada Pasien Di Bangsal Bromelia Saat Ini!')

# Fungsi Hapus Data Pasien (DELETE)
def proses_pasien_keluar_bangsal ():
    if len(data_pasien)!= 0:
        while True:
            hapus_RegID_pasien = int(input('Masukkan Reg ID Pasien untuk Proses Keluar Bangsal (23xxxxxx): '))
            reg_Id_pasien5 = []
            for i in range(len(data_pasien)):
                reg_Id_pasien5.append(data_pasien[i]['Reg ID'])
            if hapus_RegID_pasien in reg_Id_pasien5:
                print('='*150)
                print(f"|{'NO':^6}|{'Reg ID':^10}|{'Nama Pasien':^25}|{'Nomor Kamar':^15}|{'DPJP':^25}|{'Total Biaya':^20}|{'Pembayaran':^20}|{'Status':^20}|")
                print('='*150)
                print(f"|{data_pasien[reg_Id_pasien5.index(hapus_RegID_pasien)]['NO']:<6}|{hapus_RegID_pasien:<10}|{data_pasien[reg_Id_pasien5.index(hapus_RegID_pasien)]['Nama Pasien']:<25}|{data_pasien[reg_Id_pasien5.index(hapus_RegID_pasien)]['Nomor Kamar']:<15}|{data_pasien[reg_Id_pasien5.index(hapus_RegID_pasien)]['DPJP']:<25}|{data_pasien[reg_Id_pasien5.index(hapus_RegID_pasien)]['Total Biaya']:<20}|{data_pasien[reg_Id_pasien5.index(hapus_RegID_pasien)]['Pembayaran']:<20}|{data_pasien[reg_Id_pasien5.index(hapus_RegID_pasien)]['Status']:<20}|")
                print('='*150)
                
                print('Proses Keluar Bangsal Akan Dilakukan')
                print('''
                            [1] Hapus Data Pasien dari Bangsal
                            [2] Kembali ke Menu Utama
                        ''')
                Hapus_data_pasien = int(input("Pilih 1/2:"))
                if Hapus_data_pasien == 1:
                    del data_pasien[reg_Id_pasien5.index(hapus_RegID_pasien)]
                    Tabel_data_pasien()
                elif Hapus_data_pasien ==2:
                    Menu_Utama()
                else:
                    print('Hanya menerima input 1/2/3!')
                    break
            else:
                print('Reg ID Pasien {} tidak ditemukan. Silahkan Coba Lagi!'.format(hapus_RegID_pasien))
                continue
    elif len(data_pasien) ==0:
        print('Tidak Ada Pasien Di Bangsal Bromelia Saat Ini!')

# Fungsi Menu Utama
def Menu_Utama ():
    while True:
        print('''
    ====================================
                BROMELIA WARD
    ====================================

    [1] Tampilkan Data Pasien Rawat Inap
    [2] Tampilkan Detail Pasien         
    [3] Tambah Data Pasien Rawat Inap
    [4] Update Biaya/Pembayaran/Status Pasien
    [5] Hapus Data Pasien Rawat Inap (Pasien Pulang)
   
          
    [0] Keluar
              ''')    
        pilihMenu = int(input('Pilih Menu:'))
        if pilihMenu == 1:
            Tabel_data_pasien()
        elif pilihMenu == 2:
            Tampilan_detail_pasien ()
        elif pilihMenu == 3:
            print ('Tambah Data Pasien Rawat Inap')
            print('*'*60)
            Tambahan_data_pasien()
        elif pilihMenu == 4:
            Update_data_pasien ()
        elif pilihMenu == 5:
            proses_pasien_keluar_bangsal ()
            Tabel_data_pasien ()
        elif pilihMenu == 0:
            Keluar ()
            break
        else:
            print('Menu tidak ditemukan! Silahkan coba Lagi')
        continue
            
WelcomeGreeting ()
Menu_Utama()