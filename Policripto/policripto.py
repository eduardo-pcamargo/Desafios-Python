alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

somando = 1

msg = str(input())
nums = input()

nums = list(nums)
msg = list(msg)

for i in range(len(msg)):
    if(msg[i]=='w'):
        msg[i] = ' '

for j in range(len(nums)):
    if(nums[j] == '+'):
        nums[j] = ' '
        somando = 1
        continue
    else:
        if(nums[j] == '-'):
            nums[j] = ' '
            somando = 0
            continue

    if(somando==1):
        nums[j] = int(nums[j])
    else:
        if(somando==0):
            nums[j] = int(nums[j])*(-1)

while(' ' in nums):
    nums.remove(' ')

for k in range(len(msg)):
    if(msg[k] == ' '):
        nums.insert(k,0)

for m in range(len(msg)):
    if(msg[m]==" "):
        continue
    else:
        indAlf = alfabeto.index(msg[m])
        novoInd = indAlf+nums[m]
        if(novoInd>25):
            novoInd = (novoInd-26)
        else:
            if(novoInd<0):
                novoInd = (26+novoInd)
    msg[m] = alfabeto[novoInd]

msgFinal = ''.join(msg)
print(msgFinal)
