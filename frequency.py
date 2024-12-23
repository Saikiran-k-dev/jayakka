def freq(str):
    dict={}
    for i in str:
        print(i)
        keys=dict.keys()
        # print(keys)
        if i in keys:
            dict[i]+=1
        else:
            dict[i]=1
    return dict

userInput = input()
print(freq(userInput))
