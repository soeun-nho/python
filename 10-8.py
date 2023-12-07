import csv

with open("output.csv", "w", newline="") as ourf:
    writer = csv.writer(ourf)
    datas='hello,python'
    writer.writerow(datas)