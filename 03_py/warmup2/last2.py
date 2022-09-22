# https://codingbat.com/prob/p145834

"""
Given a string, return the count of the number of times that a substring length
2 appears in the string and also as the last 2 chars of the string, so "hixxxhi"
yields 1 (we won't count the end substring).
"""

def last2(str):
  if len(str)<2:
    return 0
  count=0
  last = str[len(str)-2:]
  for inc in range(len(str)-2):
    if str[inc:inc+2]==last:
        count+=1
  return count

  # test cases: do not edit
print(last2('hixxhi')) # 1
print(last2('xaxxaxaxx')) # 1
print(last2('axxxaaxx')) # 2
