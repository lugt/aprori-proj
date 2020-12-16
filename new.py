from efficient_apriori import apriori
import csv

if __name__ == "__main__":
    # transactions = [('eggs', 'bacon', 'soup'),
    #                 ('eggs', 'bacon', 'apple'),
    #                 ('soup', 'bacon', 'banana')]

    transactions = []
    with open('utf8.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        curid = "0"
        cur_list = []
        for row in spamreader:
            # print(', '.join(row))
            # print(row)
            if (row[0] == curid):
                cur_list.append(row[1])
                continue
            else:
                if len(cur_list) >= 2:
                    cur_tuple = tuple(cur_list)
                    transactions.append(cur_tuple)
                cur_list = [row[1]]
                curid = row[0]

transactions = transactions[1:100]

itemsets, rules = apriori(transactions, min_support=0.03, min_confidence=0.01)

# Print out every rule with 2 items on the left hand side,
# 1 item on the right hand side, sorted by lift
rules_rhs = filter(lambda rule: len(rule.lhs) == 2 and len(rule.rhs) == 1, rules)
for rule in sorted(rules_rhs, key=lambda rule: rule.lift):
  print(rule)  # Prints the rule and its confidence, support, lift, ...

