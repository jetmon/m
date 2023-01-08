import csv

with open("D:\LABX\CE.csv") as f:
    csv_file_reader = csv.reader(f)
    data = list(csv_file_reader)
    print(csv_file_reader)
    
    s = data[1][:-1]
    g =[["?" for i in range(len(s))]for j in range(len(s))]
    
    for i in data:
        if i[-1] == "YES":
            for j in range(len(s)):
                if i[j] != s[j]:
                    s[j] = "?"
                    g[j][j] = "?"
        elif i[-1] == "NO":
            for  j in range(len(s)):
                if i[j] != s[j]:
                    g[j][j] = s[j]
                else:
                    g[j][j] = "?"
        print(f"{data.index(i)+1},{s},{g}")
    gh=[]
    for i in g:
        for j in i:
            if j != "?":
                gh.append(i)
                break
    
    print(f"gh = {gh}\n s={s}")