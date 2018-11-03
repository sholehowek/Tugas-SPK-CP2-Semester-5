nama = input("Masukkan Nama Anda = ")
programmer = 0
itadministrator = 0
teknisi = 0
dll = 0
nilai = 0

# file = open('data.txt', 'r+')
# .write

def getKemampuan():
   choice = input("\nHallo " + nama + ", Apakah Kemampuan kamu bagus dibidang Matematika dan Programing ?\n 1.Iya\n 2.Tidak\n Jawaban = ")
   if choice == "1":
      global programmer
      programmer = 1
      getLogika()

   elif choice =="2":
      programmer = 0
      getLogika()

def getLogika():
   choice = input("\nApakah Logika Kamu Bagus ?\n 1.Iya\n 2.Tidak\n Jawaban = ")
   if choice == "1":
      global programmer
      programmer = programmer + 2
      getMinat()

   elif choice == "2":
      programmer = programmer + 1
      getMinat()

def getMinat():
      choice = input("\nSeberapa Berminat Kamu Berkarir Sebagai Programmer ?\n 1.Sangat Berminat\n 2.Biasa\n 3.Tidak Berminat \nJawaban = ")
      if choice == "1":
         global programmer
         programmer = programmer + 2
         karir()

      elif choice == "2":
         programmer = programmer + 1
         karir()

      elif choice == "3":
         programmer = programmer + 0
         karir()



def karir():

   if programmer >=5:
      print("\nSelamat" + nama + ", Kamu Memang Cocok Berkarir Sebagai Seorang Programmer")
   elif programmer == 4 :
      print ("\nKarir yang Cocok untuk" + nama + " Adalah IT Administrator")
   elif programmer ==3 :
      print("\nKarir yang Cocok untuk" + nama + " Adalah Teknisi Komputer")
   elif programmer <=2 :
      print("Mungkin " + nama + " bisa berkarir di Bidang yang lain\n " )

   
      # print(echo <br>)
      # echo <br>
      
# def mengulang():
      # print("Apakah Anda Ingin mengulang ?\n 1. Iya \n 2. Tidak")
         # if choice == "1":
         #    getKemampuan()
         # else:
         #    print(nama)


      


getKemampuan()
# mengulang()
# getLogika()
# getMinat()