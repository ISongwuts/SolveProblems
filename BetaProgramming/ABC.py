def main():
    nums_arr = list(map(int, input().split())).sort()
    s:str = input()
    ans:list = []
    
    """for index in range(3):
        if s[index] == 'A':
            ans.append(nums_arr[0])
        elif s[index] == 'B':
            ans.append(nums_arr[1])
        elif s[index] == 'C':
            ans.append(nums_arr[2])
    """        
    for i in nums_arr:
        print(i)
        
if __name__ == '__main__':
    main()
    