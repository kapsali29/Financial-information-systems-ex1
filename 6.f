SELECT data.MSgTime, data.MsgDate, data.TradeId, data.TradeAmount, data.TradePrice FROM 
(SELECT max(MsgTime) as max_ts,MsgDate, TradeId FROM data WHERE MsgType LIKE '%8%' GROUP BY MsgDate, TradeId) as T
INNER JOIN data
ON T.max_ts = data.MsgTime and T.MsgDate = data.MsgDate and T.TradeId = data.TradeId