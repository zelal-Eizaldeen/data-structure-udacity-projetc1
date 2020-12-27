import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    listText = list(texts[0])
    print(f"First record of texts, {listText[0]} texts {listText[1]} at time {listText[2]}")

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    listCalls = list(calls.pop())
    print(f"Last record of calls,  {listCalls[0]} calls {listCalls[1]} at time {listCalls[2]} lasting {listCalls[3]}")



