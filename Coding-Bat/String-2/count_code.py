def count_code(str):
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  sum = 0
  for c in alphabet:
    d = 'co' + c + 'e'
    
    for i in range(len(str) - 1):
      if str[i : i + 4] == d:
        sum += 1
  return sum

