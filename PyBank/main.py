#import Resources
import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath) as csvfile:
    bank_data = csv.reader(csvfile, delimiter=",")
    next(bank_data)

    #print(bank_data)
    last_pl = 0.0
    net_pl = 0.0
    tot_rec = 0
    max_inc = 0.0
    inc_date = ''
    max_dec = 0.0
    dec_date = ''
    sum_delta = 0.0
    avg_delta = 0.0
    rec1test = True
    rec1 = 0.0

    for row in bank_data:

        pl = float(row[1])

        if rec1test == True:
            rec1 = pl
            rec1test = False

        tot_rec = tot_rec + 1

        net_pl = net_pl + pl

        if pl > max_inc:
            max_inc = pl
            inc_date = row[0]
        elif pl < max_dec:
            max_dec = pl
            dec_date = row[0]
        
        sum_delta = sum_delta + (pl - last_pl)

        last_pl = pl
    
    avg_delta = (sum_delta - rec1) / (tot_rec - 1)

    print(f'Total Months: {tot_rec}')
    print(f"Total P/L: " "${:,.2f}".format(net_pl))
    print(f"Average  Change: " "${:,.2f}".format(avg_delta))
    print(f"Greatest Increase in Profits in {inc_date}: " "${:,.2f}".format(max_inc))
    print(f"Greatest Decrease in Profits in {dec_date}: " "${:,.2f}".format(max_dec))

    with open("Output.txt", "w") as text_file:
        print(f'Total Months: {tot_rec}', file=text_file)
        print(f"Total P/L: " "${:,.2f}".format(net_pl), file=text_file)
        print(f"Average  Change: " "${:,.2f}".format(avg_delta), file=text_file)
        print(f"Greatest Increase in Profits in {inc_date}: " "${:,.2f}".format(max_inc), file=text_file)
        print(f"Greatest Decrease in Profits in {dec_date}: " "${:,.2f}".format(max_dec), file=text_file)