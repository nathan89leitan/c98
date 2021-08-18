import shutil

def swapFileData():
    file1 = input("write first file name___  ")
    file2 = input("write second file name___  ")


    with open(file1, 'r') as file1r:
     data1 = file1r.read()

    with open(file2, 'r') as file2r:
      data2 = file2r.read()

    with open(file1, 'w') as a:
     a.write(data2)

    with open(file2, 'w') as b:
     b.write(data1)
print("Hello")
print("This is a program made to swap files on your computer")
print("It only works with text files")
swapFileData()
print("The first file you chose is now in the seconds place and vice versa")