

def file_write():
    text = str(input("Write something in side a file :"))
    with open("text.txt","a") as f:
        f.write(text+"\n")
def  file_read():
    with open('text.txt') as f:
        # Read Full content
        print(f"Read Full content {f.name}")
        text = f.read()
        print(text)




if __name__ == '__main__':
    print("....File Input/Output...")
    file_write()
    file_read()
