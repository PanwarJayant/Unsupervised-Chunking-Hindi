output_file =  open("avgchunks.txt", 'r', encoding="utf8")
gold_standard =  open("gold_standard.txt", 'r', encoding="utf8")

output = list()
gold = list()

for output_line in output_file:
    if output_line in ['\n', '\r\n']:
        continue
    _, phrase = output_line.split()
    output.append(phrase)

for gold_line in gold_standard:
    if gold_line in ['\n', '\r\n']:
        continue
    _, phrase = gold_line.split()
    gold.append(phrase)

count = 0
total_NP_count = 0
NP_count = 0

for i in range(len(gold)):

    if "NP" in gold[i]:
        total_NP_count += 1
        if output[i]=="NP":
            NP_count += 1

    if output[i] == "NP":
        if "NP" in gold[i]:
            count += 1
    elif output[i] == "VP":
        if "VGF" in gold[i] or "VGNN" in gold[i]:
            count += 1
    elif output[i] == "OTHER":
        if "NP" not in gold[i] and "VGF" not in gold[i] and "VGNN" not in gold[i] and "BLK" not in gold[i]:
            count += 1
    elif output[i] == "BLK":
        if "BLK" in gold[i]:
            count += 1

print("Overall Accuracy:", (count*100)/len(gold))
print("Noun Phrase Accuracy:", (NP_count*100)/total_NP_count)
