with open("textfiles/dream.txt", "r") as my_file:
    content_list = my_file.readlines() #문자열들이 list 항목으로
    print(type(content_list))
    print(content_list)

    for line in content_list:
        print(line.replace('\n', ''))

with open("textfiles/dream1.txt", "r") as myfile:
    while 1:
        line = myfile.readline()
        if not line:
            break
        print(line.replace("\n", ""))

with open("textfiles/dream1.txt", "r") as myfile:
    contents=myfile.read()
    
    word_list = contents.split()
    line_list = contents.split("\n")

    word_frq={}
    for w in word_list:
        if w in word_frq.keys():
            word_frq[w]+=1
        else:
            word_frq[w]=0
    print(word_frq)
    for k,v in word_frq.items():
        print(k, "===", v)

print("총 글자의 수", len(contents))
print("총 단어의 수", len(word_list))
print("총 줄의 수", len(line_list))
