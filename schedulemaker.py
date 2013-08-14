import csv
with open ('/Users/brynhughes/Google Drive/python/2013mwfschedule.csv','rb') as csvfile:
    reader = csv.reader(csvfile, dialect='excel')
    for row in reader:
        print ', '.join(row)