if __name__ == '__main__':
    myLisr= []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        myLisr.append([score, name])

    myLisr.sort()
    first = [i for i in myLisr if i[0] != myLisr[0][0]]
    sec = [j for j in first if j[0] == first[0][0]]
    
    sec.sort(key = lambda x: x[1])
    for i in range(len(sec)):
        print(sec[i][1])