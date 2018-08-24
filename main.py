#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import pandas as pd
import re
tp=[]
with open('FIS_FIX_txt.txt', encoding='utf8') as csvfile:
    reader = csv.reader(csvfile,delimiter='|')
    outlist = []
    rownum=0
    for row in reader:
        r_trade_id = '0'
        r_trade_amount = '0'
        r_trade_price = '0'
        for field in row:
            if field[0:3] == '35=':
                r_msgtype = field[3]
            elif field[0:3] == '11=':
                r_trade_id = field[3:]
            elif field[0:3] == '14=':
                r_trade_amount = field[3:]
            elif field[0:3] == '44=':
                r_trade_price = field[3:]
        lastfield = row[-1]
        spl=lastfield.split()
        r_outboul= spl[0]
        r_date=spl[1]
        r_time = spl[2]
        outrow = [str(r_msgtype),str(r_outboul),str(r_date),str(r_time),str(r_trade_id),str(r_trade_amount),str(r_trade_price)]
        outlist.append(outrow)
        rownum = rownum+1
        if rownum%100000==0:
            print(rownum)
    csvfile.close();


with open('FIS_FIX_txt_OUT.csv','w', encoding="utf8") as csvfile:
    writer = csv.writer(csvfile,quoting=csv.QUOTE_ALL)
    mrow=[];
    writer.writerow(['MsgType','Outcome','MsgDate', 'MsgTime', 'TradeId', 'TradeAmount', 'TradePrice'])
    for i in outlist:
        if any(row):
            writer.writerow(i)
csvfile.close()
with open('FIS_FIX_txt_OUT.csv') as input, open('out2.csv', 'w') as output:
    non_blank = (line for line in input if line.strip())
    output.writelines(non_blank)
output.close()
