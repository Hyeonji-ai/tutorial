from queue import Queue
import pandas as pd
from pandas.api.types import is_numeric_dtype
data = pd.read_csv()

#데이터를 사용하기 위해서는 맵핑해야함 그때 필요한 식
for n in range(len(data.loc[0])):
    data_type = is_numeric_dtype(data.loc[0][n])
    if data_type == True:#숫자형이면 그냥 넘어가기
        n+=1
    else:
        for i in range(len(data.loc[0])):
            que = Queue()
            que.put('Var'+str(i))
            i+=1
        Var = que.get()
        Var=data.columns[n]
        list1=[]
        for i in range(len(data[data.columns[n]])):
            a=data[data.columns[n]][i]
            if a in list1:
                pass
            else:
                list1.append(a)
        list2=list1.copy()
        count=0
        for i in range(len(list2)):
            list2[i] = count
            count+=1
        data_dic={}
        for q,z in zip(list1,list2):
            data_dic[q]=int(z)
        data[Var] = data[Var].map(data_dic)
        n+=1
        print(data_dic)

print(data.head(5))


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
