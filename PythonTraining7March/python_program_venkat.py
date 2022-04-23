import sys
if len(sys.argv) > 1:
    input_value = int(sys.argv[1])
else:
    input_value = None
if input_value is None or input_value >9:
    num = 9
else:
    num = input_value

for i in range(1, num+1):
    for j in range(1, i+1):
        print(j, end='')
    for k in range(j, 1, -1):
        print(k-1, end='')
    print("\n")