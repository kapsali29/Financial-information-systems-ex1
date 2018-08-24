#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
import cymysql
import csv
import numpy as np
##Connection with Mysql Database
conn = cymysql.connect(host='127.0.0.1', user='root', passwd='', db='exercise2', charset='utf8')
cur = conn.cursor()

## 6.a What is the total number number of messages 
sql6a = """SELECT COUNT(id) FROM data"""
cur.execute(sql6a)
total_messages = cur.fetchone()[0]
print(total_messages)

###6.b How many heartbeat messages on average are transmitting per day
sql6b = """SELECT MsgDate, COUNT(MsgType) FROM data WHERE MsgType LIKE '%0%' GROUP BY MsgDate"""
cur.execute(sql6b)
grouped_zeros = cur.fetchall()
print(grouped_zeros)

total_zero_messages = 0
for item in grouped_zeros:
    total_zero_messages = total_zero_messages + item[1]
print(total_zero_messages)
average_zero_messages = np.round(total_zero_messages/len(grouped_zeros))
print(average_zero_messages)

##6.c How many new orders are incoming per days?
sql6c = """SELECT MsgDate, Count(MsgType) FROM data WHERE MsgType LIKE '%D%' AND Outcome LIKE '%0%' GROUP BY MsgDate"""
cur.execute(sql6c)
new_orders_per_day = cur.fetchall()
print(new_orders_per_day)

#PYTHON-BASED APPROACH
##6.d Which mothly period was the period with the most incoming orders and which with the less
new_orders_per_day = [list(elem) for elem in new_orders_per_day]
for item in new_orders_per_day:
    item[0] = item[0].replace(' ', '')[:-4].upper()
print(new_orders_per_day)
new_orders = dict()
for item in new_orders_per_day:
    if item[0] not in new_orders.keys():
        new_orders[item[0]] = item[1]
    else:
        new_orders[item[0]] +=item[1]
print(new_orders)
del new_orders['"CURRE']

maximum_incoming_orders = max(new_orders, key=new_orders.get)  # Just use 'min' instead of 'max' for minimum.
print(maximum_incoming_orders, new_orders[maximum_incoming_orders])

minimum_incoming_orders = min(new_orders, key=new_orders.get)  # Just use 'min' instead of 'max' for minimum.
print(minimum_incoming_orders, new_orders[minimum_incoming_orders])

##6.e What is the average number of trades, MsgType=8, that are traded every day
sqle = """SELECT MsgDate, Count(MsgType) FROM data WHERE MsgType LIKE '%8%' GROUP BY MsgDate"""
cur.execute(sqle)
trades = cur.fetchall()
print(trades)

total_trade_messages = 0
for item in trades:
    total_trade_messages = total_trade_messages + item[1]
print(total_trade_messages)
average_trades = np.round(total_trade_messages/len(trades))
print(average_trades)
