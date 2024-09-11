m= 0
for i in range(5):
  num = int(input(f"Digite o {i+1} número: "))
  if num > m:
    m = num
print(f"O maior número informado foi: {m}")