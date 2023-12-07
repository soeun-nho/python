try:
    with open("textfiles/dream1.txt", "r") as my_file:
        contents = my_file.read() #통채로
        print(type(contents))
        print(contents)
except:
    print("파일 not found")