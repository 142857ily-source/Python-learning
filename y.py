
cost_in_Japan= {'figurines':'$150', 'clothes':'$540', 'skin_cares':'$210', 'eatings':'$500', 'hotel':'$770', 'transit':'$110'}
cost_in_Japan['flight ticket']='$1600'
cost_in_China={'tea':'¥1500', 'hotel':'¥800', 'train':'¥1600'}
total_cost=cost_in_China | cost_in_Japan
C = input (f'what do you want to search:')
print (total_cost[C])