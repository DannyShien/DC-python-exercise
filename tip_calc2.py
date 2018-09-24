bill_amount = float(input('Total bill amount? $' ))
service = input('Level of service? ' )
split = float(input('Split how many ways? '))


tip_amount = float(bill_amount)
service_good = tip_amount * .20
service_fair = tip_amount * .15
service_bad = tip_amount * .10




if service == 'good':
  print('Tip amount: $%.2f' % (service_good)) 
  print('Total amount: $%.2f' % (bill_amount + service_good))
  print('Total amount: $%.2f' % ((bill_amount + service_good) / split))
elif service == 'fair':
  print('Tip amount: $%.2f' % (service_fair)) 
  print('Total amount: ', (bill_amount + service_fair  ))
  print('Total amount: $%.2f' % ((bill_amount + service_fair) / split))
elif service == 'bad':
  print('Tip amount: $%.2f' % (service_bad))
  print('Total amount: $%.2f' % (bill_amount + service_bad))
  print('Total amount: $%.2f' % ((bill_amount + service_bad) / split))