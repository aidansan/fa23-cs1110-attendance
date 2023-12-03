from glob import glob
import csv
from collections import Counter

def compute_grade(days_attended, total_days):
    return min(days_attended/(.8 * total_days), 1)

total_days = 0
attendance_counter = Counter()

for filename in glob('google-sheets/fa23-attendance-sheets/*.csv'):
    if not 'Empty.csv' in filename:
        print(filename)
        with open(filename) as infile:
            total_days += 1
            reader = csv.DictReader(infile, delimiter=',', quotechar='|')
            for row in reader:
                computing_id = row['computing id']
                computing_id = row['computing id']
                here = row['Here'].strip().lower()
                if here == 'p':
                    attendance_counter[computing_id] += 1
                elif here == '':
                    pass
                else:
                    raise Exception('Incorrect value')
                # print(row)

for computing_id, days_attended in attendance_counter.items():
    print(computing_id, compute_grade(days_attended, total_days))