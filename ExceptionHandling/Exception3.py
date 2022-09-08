try:
    klu1=open("rajesh1.txt","r+")
    try:
        klu1.write("xyzThis is S17 section CRT class")
    finally:
        klu1.close()
except IOError:
    print("file not found")
else:
    print("the file opened successfully")
    klu1.close()

