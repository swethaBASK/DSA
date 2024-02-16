# peek element
a=[6,13,7,-5,4,3,19]
for i in range(len(a)):
    if a[i]>=a[i+1] and a[i]>=a[i-1]:
        print(a[i])
        break 
print( " the peek element is ",a[i])
