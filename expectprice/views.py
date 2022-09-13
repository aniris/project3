import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from django.shortcuts import render, redirect
import logging
# %matplotlib inline


# Create your views here.

def calc(request):
    
    if request.method == 'POST':
        
        # logger 외않됨?
        logger = logging.getLogger("mylogger")
        logger.info(request.POST['year'])
        logger.info(request.POST['month'])

        plt.rc("font",family="Malgun Gothic")
        
        mulga = pd.read_csv("C:/Users/scn09/Documents/GitHub/yanderesex/expectprice/mulgasabu.csv", encoding="euc-kr")
        mulga = np.transpose(mulga)

        gap = list(mulga[0])    
        gap.pop(0)
        
        for i in range(len(gap)):
            gap[i] *= 1000
            
        day = [i for i in range(1, 45)]
        
        day_reg = day[30:46]
        day_mo = pd.DataFrame({'a' : day})
        dayreg_mo = pd.DataFrame({'a' : day_reg})

        gap_reg = gap[30:46]
        gap_mo = pd.DataFrame({'a' : gap})
        gapreg_mo = pd.DataFrame({'a' : gap_reg})

        model = LinearRegression()
        search = model.fit(dayreg_mo,gap_reg)

        # print("날짜를 입력해주세요 YYYY/MM")
        try:
            in_year = int(request.POST['year'])
            in_mon = int(request.POST['month'])
            in_day = ((in_year-2019)*12 + in_mon)
            in_day = search.predict([[in_day]])
            plt.rc("font",family="Malgun Gothic")
            mulga = pd.read_csv("C:/Users/scn09/Documents/GitHub/yanderesex/expectprice/mulga.csv", encoding="euc-kr")
            mulga = np.transpose(mulga)
            
            day = list(mulga.index)[1:]
            # day = day[1:]
            
            gap = list(mulga[0])[6:9]
            # gap = gap[6:9]
            
            gap1 = list(mulga[1])[6:9]
            # gap1 = gap1[6:9]
            
            x = pd.DataFrame({'a':gap})
            
            # search2 = model.fit(x.values.reshape(-1,1), gap1)
            search2_gap = model.fit(x.values.reshape(-1,1), gap1).predict([in_day*0.001])
            
            # logger.log("황x올리브", in_year,"년도 예측가격은", search2_gap[0],"입니다.")
            
            return render(request, 'hi.html', {'year' : in_year, 'expected_price' : int(search2_gap[0])})
            
        except:
            # print("응 안돼")
            return render(request, 'hi.html', {'year' : 'error1', 'expected_price' : 'error1'})
    
    else:
        # return render(request, 'hi.html', {'year' : 'error', 'expected_price' : 'error'})
        return render(request, 'hi.html', {'year' : 'this is GET method', 'expected_price' : 'GET method'})