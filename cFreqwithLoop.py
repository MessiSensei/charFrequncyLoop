import os
chDic={}
while True:
   
    ch = input("enter your text here :").lower() # lowercase the input so I can read char no matter lower or upper case 
    if ch=='q':
        break
    for i in range(len(ch)): #first populate the char dictionary and assign 0 as value to all the chars 
        chDic[ch[i]] = 0
#print(chDic)

#for all the charachters we have check the dictiory and when you find them add +1 to their values 
    for c in range(len(ch)):
        for x in chDic:
            #print(f'C is : {ch[c]} and x:{x}')
            if (ch[c]==x):
                #print("x is found")
                chDic[x]+=1
    print(f'{chDic}\n')
    os.system("pause")
    os.system('cls')


