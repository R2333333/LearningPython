dinnerList = ['pA', 'pB', 'pC']

for p in dinnerList:
  print(p + ' please come to dinner')

print(dinnerList[0] + ' can\'t come' )
dinnerList[0] = 'Jack'
for p in dinnerList:
  print(p + ' please come to dinner')

print('found a larger table')
dinnerList.insert(0, 'Josh')
dinnerList.insert(int(len(dinnerList)/2), 'CiCi')
dinnerList.append('Pi')
for p in dinnerList:
  print(p + ' please come to dinner')

print('the new table can\'t come')
while len(dinnerList) > 2:
    print('sorry ' + dinnerList.pop() + 'you can\'t come')
while len(dinnerList) > 0:
    print(dinnerList[0] + ' you can still come')
    del dinnerList[0]
print(dinnerList)
