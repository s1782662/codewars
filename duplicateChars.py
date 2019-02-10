from collections import Counter

str = '(( @'
d = Counter(str.lower())
res_str = ''
for s in str:
    if s in d:
        res_str += ')' if d[s] > 1 else '('
    else:
        res_str += ')'

print(res_str)



'''

Another solution


str='recede'

'(' if str.count(s) == 1 else ')' for s in str

'''
