import sys
import csv
import os
import jsonpickle
from label import Label

os.chdir('../')
def process_csv(filename="label_data.csv", outputdir="db"):
    """
    Generates a directory of json files corresponding to the provided
    csv file.
    """
    with open(filename) as csvfile:
        if not csvfile:
            print("File '%s' not found. " % filename)
            sys.exit(1)
        if not os.path.isdir(outputdir):
            print("Directory '%s' not found. " % outputdir)
            sys.exit(1)

        reader = csv.reader(csvfile)
        # Skip the two header rows
        next(reader)
        next(reader)
        for row in reader:
            label = Label(row)
            outfile = open(os.path.join(outputdir, label.name+'.json'), 'w')
            json = jsonpickle.encode(label)
            outfile.write(json)
            outfile.close()
            print(label.name)

# Runs on running this script
# Usage: python3 generateJSON.py [input.csv] [outputDir]
if len(sys.argv) > 2:
    process_csv(sys.argv[1], sys.argv[2])
elif len(sys.argv) > 1:
    process_csv(sys.argv[1])
else:
    process_csv()
