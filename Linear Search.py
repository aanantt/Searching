def linear_searching(s,ele):
    for i in s:
        if i==ele:
            return True
    return False
ans=linear_searching([1,7,4,2,0,8],7)
if ans:
    print("Element is in the list")
else:
    print("Element is not present")
