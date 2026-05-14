import csv

input_file = "Geonode-proxies.txt"     # Input file
output_file = "proxies.txt"  # Output file name

with open(input_file, "r", encoding="utf-8") as infile, \
     open(output_file, "w", encoding="utf-8") as outfile:

    reader = csv.reader(infile)

    for row in reader:
        if len(row) >= 9:
            ip = row[0]
            port = row[7]
            proxy_type = row[8].lower()

            outfile.write(f"{ip}:{port}\n")

print("Done! Proxies saved to", output_file)