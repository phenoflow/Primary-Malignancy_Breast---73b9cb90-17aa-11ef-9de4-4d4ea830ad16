# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"40359.0","system":"readv2"},{"code":"62871.0","system":"readv2"},{"code":"105488.0","system":"readv2"},{"code":"42542.0","system":"readv2"},{"code":"48809.0","system":"readv2"},{"code":"95323.0","system":"readv2"},{"code":"18694.0","system":"readv2"},{"code":"58131.0","system":"readv2"},{"code":"21833.0","system":"readv2"},{"code":"67884.0","system":"readv2"},{"code":"12499.0","system":"readv2"},{"code":"67701.0","system":"readv2"},{"code":"60803.0","system":"readv2"},{"code":"23399.0","system":"readv2"},{"code":"39760.0","system":"readv2"},{"code":"68480.0","system":"readv2"},{"code":"348.0","system":"readv2"},{"code":"95057.0","system":"readv2"},{"code":"3968.0","system":"readv2"},{"code":"59831.0","system":"readv2"},{"code":"12300.0","system":"readv2"},{"code":"19423.0","system":"readv2"},{"code":"54494.0","system":"readv2"},{"code":"8351.0","system":"readv2"},{"code":"30189.0","system":"readv2"},{"code":"42070.0","system":"readv2"},{"code":"29826.0","system":"readv2"},{"code":"31546.0","system":"readv2"},{"code":"26853.0","system":"readv2"},{"code":"64686.0","system":"readv2"},{"code":"56715.0","system":"readv2"},{"code":"3969.0","system":"readv2"},{"code":"38475.0","system":"readv2"},{"code":"20685.0","system":"readv2"},{"code":"12480.0","system":"readv2"},{"code":"10387.0","system":"readv2"},{"code":"45222.0","system":"readv2"},{"code":"7833.0","system":"readv2"},{"code":"54202.0","system":"readv2"},{"code":"102593.0","system":"readv2"},{"code":"49148.0","system":"readv2"},{"code":"23380.0","system":"readv2"},{"code":"53803.0","system":"readv2"},{"code":"9470.0","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('primary-malignancy_breast-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["breast---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["breast---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["breast---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
