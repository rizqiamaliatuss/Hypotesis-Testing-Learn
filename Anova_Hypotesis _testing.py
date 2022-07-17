import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as st


mc = pd.read_csv('marketing_campaign.csv', sep='\t') # read data (from kaggle)
mc2 = mc.iloc[:, 0:10] # only show columns ke 1 - 10

mc2_graduated = mc2[mc2['Education'] == 'Graduation']
mc2_phd = mc2[mc2['Education'] == 'PhD']
mc2_master = mc2[mc2['Education'] == 'Master']
mc2_basic = mc2[mc2['Education'] == 'Basic']
mc2_2ncycle = mc2[mc2['Education'] == '2n Cycle']

mc2_graduated = mc2_graduated[mc2_graduated['Income'].isnull() == False]
mc2_phd = mc2_phd[mc2_phd['Income'].isnull() == False]
mc2_master = mc2_master[mc2_master['Income'].isnull() == False]
mc2_basic = mc2_basic[mc2_basic['Income'].isnull() == False]
mc2_2ncycle = mc2_2ncycle[mc2_2ncycle['Income'].isnull() == False]

anova_test = st.f_oneway(mc2_graduated['Income'],
                         mc2_phd['Income'],
                         mc2_master['Income'],
                         mc2_basic['Income'],
                         mc2_2ncycle['Income'])

if anova_test.pvalue>0.05:
    print('in every Level Education gets the same Income')
else:
    print('Level Education in the marketing campaign data varies across an average of Income significantly')