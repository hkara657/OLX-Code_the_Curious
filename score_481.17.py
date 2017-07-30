
# coding: utf-8

# In[1]:


from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"


# In[2]:


import pandas as pd
import numpy as np
import datetime
import os


# In[3]:


ads_data=pd.read_csv('olx_data/ads_data/ads_data.csv')
user_data=pd.read_csv('olx_data/user_data/user_data.csv')
user_msg=pd.read_csv('olx_data/user_messages.csv')
test=pd.read_csv('olx_data/user_messages_test.csv')


# In[4]:


len(pd.unique(ads_data['category_id']))


# In[5]:


test.shape
user_msg.shape
ads_data.shape
user_data.shape


# In[6]:


#no common users in test and user_msg.csv
lst1=set(test['user_id'])
len(lst1)
lst2=set(user_msg['user_id'])
len(lst2)

len(lst1.intersection(lst2))


# In[7]:


test.head(2)
user_msg.head(2)
ads_data.head(2)
user_data.head(2)


# In[8]:


user_data['event_time']=pd.to_datetime(user_data['event_time'])
# user_data['event_time']=pd.to_datetime(str(user_data['event_time'].dt.month)+'-'+str()
user_data['month']=user_data['event_time'].dt.month
user_data['day']=user_data['event_time'].dt.day


# In[9]:


# create ads and category dataframe with ads_id as index
ind=np.array(ads_data['ad_id'])
cat=np.array(ads_data['category_id'])
ads_cat=pd.DataFrame(cat,index=ind,columns=['category_id'])

price=np.array(ads_data['price'])
ads_price=pd.DataFrame(price,index=ind,columns=['price'])

enabled=np.array(ads_data['enabled'])
ads_enabled=pd.DataFrame(enabled,index=ind,columns=['enabled'])


# In[10]:


pd.unique(user_data['origin'])


# In[11]:


cols=['channel','user_lat','user_long']
user_data.drop(cols,axis=1,inplace=True)

mapping = {'view':0 , 'first_message':1}
user_data = user_data.replace({'event':mapping})

mapping = {'browse_search':0,'browse':0 ,'search':0,'notification_center':1, 'home':2, 'push':3, 'drawer':4, 'deeplink':4 }
user_data = user_data.replace({'origin':mapping})

user_data.dtypes


# In[12]:


user_data = user_data.sort_values(by=['month','day','origin','ad_messages','ad_views','ad_impressions'],ascending=[False,False,True,False,False,False])


# In[13]:


ans={}
cat=pd.unique(test['category_id'])
for cid in cat:
    df1=user_data
    catdf = ads_cat.loc[ df1['ad_id'] ]
    df1 = df1[ np.array(catdf==cid) ]  #selecting those adds that have the same category as cid i.e. test instance
#     pricedf = ads_price.loc[ df1['ad_id'] ]
#     df1.shape
    enabledf = ads_enabled.loc[ df1['ad_id'] ]
    df1=df1[np.array(enabledf==1)]
#     df1=df1.sort_values(by=['ad_messages','ad_views','ad_impressions'],ascending=[False,False,False])

    lst=[]
    #to get unique elements in lst
    ids=list(df1['ad_id'])
    for i in np.arange(len(ids)):
        if len(lst)==10:
            break
        if not ids[i] in lst:
            lst.append(ids[i])

    ans[cid]=lst
#     print df1.columns


# In[14]:


from random import shuffle
j=0
result=test[['user_id','category_id']]
res_ads=[]
for i in test.index:
    if j%100==0:
        print j
    j = j+1
    row=test.loc[i]
    uid=row['user_id']
    cid=row['category_id']
#     print 'new',uid,cid
#     user_cat_ads = user_data.loc[ np.logical_and( user_data['user_id']=uid , user_data['']  )    ]
    df1 = user_data.loc[ user_data['user_id']==uid ]
    
    if df1.shape[0]==0:
        res_ads.append(str(ans[cid]))
        continue
        
    catdf = ads_cat.loc[ df1['ad_id'] ]
    df1 = df1[ np.array(catdf==cid) ]  #selecting those adds that have the same category as cid i.e. test instance
    
    enabledf = ads_enabled.loc[ df1['ad_id'] ]
    if df1.shape[0]>0:
        df1=df1[np.array(enabledf==1)]
#     df1=df1.sort_values(by=['ad_messages','ad_views','ad_impressions'],ascending=[False,False,False])
    
    lst=[]
    lst=list(df1['ad_id'][0:10])
    
    if len(lst)<10:
        rem=10-len(lst)
#         rem
#         ans[cid]
        lst.extend(ans[cid][0:rem])
    
#     shuffle(lst)
    res_ads.append(str(lst))
    
#     print 'harshkara'
#     break
    


# In[15]:


from random import shuffle
ls=[1,2,3,4,5]
shuffle(ls)
ls


# In[16]:


result['ads']=res_ads


# In[17]:


result.to_csv("ads_recommendation.csv", index=False)
os.system("spd-say 'task complete'")


# In[18]:


#start time 5:50


# In[19]:


# lst=[1,2,3,4,5]
# lst.extend([7,8,9])
# lst


# In[20]:


# list(df1['ad_id'][0:10])


# In[21]:


# df['e']=df['e']+np.ones(df.shape[0],dtype=int)
# df


# In[22]:


# a=np.array([[1,2,3,4,5],[6,7,8,9,10],[1,4,2,6,7],[3,1,6,9,2],[4,5,6,7,8]])
# df=pd.DataFrame(a,columns=['a','b','c','d','e'])
# df[0:100]
# b=[1,2,3]
# # ind=[0,2,4]
# df=df.loc[df['a']==1]
# df
# df['xyz']=np.array([99,100])
# df


# In[ ]:





# In[ ]:





# In[ ]:





# In[23]:


# tdf=pd.DataFrame(np.array(b),index=ind,columns=['xyz'])
# tdf
# tdf==3
# oop=[7,45]
# tdf.loc[oop]


# In[24]:


# df
# tdf
# tdf.loc[tdf['xyz']==3]


# In[25]:


# df['xyz']=np.array(tdf)
# df


# In[26]:


# df.loc[np.logical_and(df['a']==1, np.mod(df['d'],2)==1)]


# In[27]:


# #ONLY FOR TESTING PURPOSE
# # uid=row['user_id']
# uid=18
# cid=800
# # cid=row['category_id']
# print uid
# print cid
# #     user_cat_ads = user_data.loc[ np.logical_and( user_data['user_id']=uid , user_data['']  )    ]
# df1 = user_data.loc[ user_data['user_id']==uid ]
# df1
# if df1.shape[0]==0:
#     df1=user_data

# catdf = ads_cat.loc[ df1['ad_id'] ]
# print '*******************************'
# catdf
# df1 = df1[ np.array(catdf==cid) ]  #selecting those adds that have the same category as cid i.e. test instance
# pricedf = ads_price.loc[ df1['ad_id'] ]

# df1['price'] = np.array(pricedf)
# df1

