import csv

from locator.models import Trashcan


def csv_import():
    with open('Downtown_Trash_Receptacles.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        cnt = 0
        for row in reader:
            if cnt > 1:
                trashcan = Trashcan()
                coords = row[0].split(",")
                trashcan.longitude = float(coords[0])
                trashcan.latitude = float(coords[1])
                trashcan.save()
            cnt += 1


csv_import()