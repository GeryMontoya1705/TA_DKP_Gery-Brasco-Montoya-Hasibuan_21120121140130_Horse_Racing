pilihan = 0
data = 0
count = 0
size = -1
stack = []
while count == 0:
    print("---Ini Stack---")
    print("1. PUSH Item")
    print("2. POP Item")
    print("3. Lihat Daftar Data")
    print("4. Lihat Data Teratas")
    print("5. Keluar")
    pilihan = int(input("Masukkan Pilihan : "))
    count +=1
    if pilihan == 1:
        data = int(input("Data yang ditambahkan : "))
        stack.append(data)
        count = 0
        size+=1
        print ("")
    if pilihan == 2:
        stack.pop()
        count = 0
        size-=1
        print ("")
    if pilihan == 3:
        print(stack)
        count = 0
        print ("")
    if pilihan == 4:
        print(stack[size])
        count = 0
        print ("")
    if pilihan == 5:
        quit()