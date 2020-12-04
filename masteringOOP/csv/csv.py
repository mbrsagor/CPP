import gzip
import csv

path = 'subset.csv'

with open("subset.csv", "w") as target:
    wtr = csv.writer(target)
    with gzip.open(path) as source:
        line_iter = (b.decode() for b in source)
        match_iter = (format_1_pat.match(line) for line in line_iter)
        wtr.writerows((m.groups() for m in match_iter if m is not None) )
