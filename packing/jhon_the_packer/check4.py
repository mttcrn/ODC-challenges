
def check(param):
  v6 = pow(param, 5.0) * 0.5166666688
  v7 = v6 - pow(param, 4.0) * 8.125000037
  v8 = pow(param, 3.0) * 45.83333358 + v7
  return v8 - pow(param, 2.0) * 109.8750007 + param * 99.65000093 + 83.99999968

for i in range(6):
  print(chr(round(check(i+1))))
