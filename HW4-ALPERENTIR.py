import os
import pandas as pd

fileName = os.getcwd() + "\Plaza Coffee.csv"
df = pd.read_csv(fileName, sep=';')

groupData= df.groupby(["Company","Order","Payment"],as_index=False).sum()

compName = groupData["Company"].unique()

for cN in range(0,len(compName)):
    cent = []
    for row in range(0, groupData.shape[0]):
        if groupData.iat[row,3] == 1:
            ct = " person has bought "
        else:
            ct = " people have bought "
            
        if groupData.iat[row,0] == compName[cN]:
            temp= (str(groupData.iat[row,3]) + ct + groupData.iat[row,1] + " and paid in " + groupData.iat[row,2])
            cent.append(temp)

    cCent = ", ".join(cent)
    lastWords = "From " + compName[cN] + ", " + cCent +"."
    print(lastWords)
    