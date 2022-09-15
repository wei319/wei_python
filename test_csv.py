import csv
with open('test.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["ID", "sex", "age"])
    writer.writerow([111, "male", 20])
    writer.writerow([222, "female", 30])