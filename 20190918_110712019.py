#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 2-1 使用 Python 做計算

#工讀金採時薪制，每小時 120 元。小美每週工讀 8 小時，持續 16 週，工讀金總額多少元？

print(120*8*16)


# In[2]:


# 練習 2-1-1
#工讀金採時薪制，每小時 130元。小華每日各工讀 8 小時，持續一年，工讀金總額多少元？
print(130*8*365)


# In[ ]:


# 練習 2-1-2
# 嘗試其他數字計算


# In[4]:


# 2-2 認識變數
#工讀金採時薪制，金額會隨法規而變動，不同人的工讀總時間會不同，同一人每月工讀時間會有所不同...
"""2019年8月新規定新聞，https://www.cna.com.tw/news/firstnews/201908145004.aspx"""

x=120       #變數名稱x，以等號賦予整數值120
print(x)    #輸出函數print()，輸出在螢幕上


# In[ ]:


x=140
print(x)


# In[3]:


#小美的工讀金總額
x=158          
y=x*8*16     
print(y)       


# In[ ]:


#練習 2-2-1
#小華的工讀金總額


# In[5]:


# 年度收入、支出與結餘金額(數學符號的變數)
x=158
y=x*30*8
a=6000
b=a*12
s=y-b
print(y)
print(b)
print(s)


# In[6]:


# 年度收入、支出與結餘金額(字面意義的變數)

hourly_wage=158                  
annaul_salary=hourly_wage*30*8      
monthly_fee=6000                    
annaul_fee=monthly_fee*12 
savings=annaul_salary-annaul_fee 

print(annaul_salary)
print(annaul_fee)
print(savings)


# In[11]:


#練習 2-2-2 (改寫成字面意義的變數)
#優惠存款問題：本金 100000 元，優存年利率 2%，按日複利計算利息，1 年後的本利和為多少？
Principal=10000
Annual_rate=0.02
t=1
Accumulated_amount=Principal*(1+Annual_rate/365)**(t*365)
print(Accumulated_amount)


# In[ ]:


# 2-3 程式的意義
#計算程序化：可重複開啟執行，免去重複編寫的麻煩
#數值可變化：可因應變數調整，適用不同數值情形


# In[8]:


# 2-4 程式的註解
'''年度費用收入、支出與結餘'''
hourly_wage=158                     #每小時工讀薪水
annaul_salary=hourly_wage*30*8      #每年工讀總額
monthly_fee=6000                    #每月生活支出
annaul_fee=monthly_fee*12           #每年生活總支出
savings=annaul_salary-annaul_fee    #每年結餘
print(annaul_salary)
print(annaul_fee)
print(savings)


# In[12]:


#練習 2-4-1 (字面意義、加註並存成 *.py 檔)
#優惠存款問題：本金 1000000 元，優存年利率 2%，按日複利計算利息，1 年後的本利和為多少？

Principal=10000                                           #本金 1000000 元
Annual_rate=0.02                                          #優存年利率 2%
t=1                                                       #1 年
Accumulated_amount=Principal*(1+Annual_rate/365)**(t*365) #本利和
print(Accumulated_amount)                                 


# In[16]:


#練習 2-4-2 (字面意義、加註並存成 *.py 檔)
#高利貸問題：借款 60000 元，月息一分(1%)，按日複利計算利息，3年後的本利和為多少？
Principal=60000                                           #本金 60000 元
Monthly_rate=0.01                                         #月息一分(1%)
t=3                                                       #3年
Accumulated_amount=Principal*(1+Monthly_rate/30)**(t*365) #本利和
print(Accumulated_amount)                                 


# In[ ]:


# 2-5 變數宣告方式
# Python的變數給值後就可使用，不同於其他語言，需先宣告此變數名稱與類型後，才可以賦予值及使用


# In[ ]:


# 2-6 變數的命名方式
#字首必須是英文字母、中文字或底線_，不過，中文字不建議使用，底線為特殊用途
#變數名稱只能是英文字母、數字、中文字及底線組成
#大小寫的英文字母是被看成不同的
#系統有內建的保留字和函數，不建議使用

""" Python 3.x 有33 個保留字，中文請參考https://www.itread01.com/content/1548367586.html"""
""" Python 3.x 內建函數，原文請參考https://docs.python.org/3.5/library/functions.html"""


# In[ ]:


# 範例 2-6-1

illegal_names=[sum'1, 3y, s&2, and]

legal_name=[Sum, _fpga, x11, 小計]


# In[ ]:


# 範例 2-6-2
SUM=1
Sum=10
sum=100

print(Sum)


# In[ ]:


# 練習 2-6-1：合法與不合法變數個舉一例，賦予值並輸出檢視


# In[ ]:


# 2-7 基本數值運算
# 2-7-1 四則運算

# 範例 2-7-1-1
x=5
y=x+1-2*3/4
print(y)


# In[ ]:


# 範例 2-7-1-2
a=9
b=2
c=3a-2b
print(c)


# In[ ]:


# 練習 2-7-1-1：給定一些變數的值，並利用四則運算產生另一個變數值，並輸出檢視


# In[5]:


# 2-7 基本數值運算
# 2-7-2 整數除法
# 範例 2-7-2-1

x=30
y=7
z1=x/y         #基本除法，商數(以小數表示)
z2=x//y        #整數除法，商數(整數運算，表示商數部分)
z3=x%y         #整數除法，餘數(整數運算，表示餘數部分)

print(z1)
print(z2)
print(z3)


# In[ ]:


# 練習 2-7-2-1：給定一些變數的值，並利用四則運算與整數除法產生另一個變數值，並輸出檢視


# In[ ]:


# 2-7 基本數值運算
# 2-7-3 次方
# 範例 2-7-3-1：多項式的表示

x=-1
y=2*x**3-4*x**2+5*x-9

print(y)


# In[ ]:


# 練習 2-7-3-1：給定一個變數值，並利用其產生一個多項式變數值，並輸出檢視


# In[ ]:


# 2-7 基本數值運算
# 2-7-4 運算次序
  #括號
  #次方
  #除、乘、整數除之商、整數除之餘(同時出現由左至右)
  #加、減(同時出現由左至右)

# 範例 2-7-4-1：多項式的表示

a=-1
b=2
c=4
d=a*b//c**3%2


print(d)


# In[ ]:


# 練習 2-7-4-1：給定一些變數值，並利用各種運算產生另一個變數值，並輸出檢視


# In[ ]:


# 2-8 指派運算子：變數的原有值會依特定運算而賦予新值的表示方式

# 範例 2-8-1：(累加形式)
a=5
a+=3    #相當於 a=a+3
print(a)


# In[ ]:


# 範例 2-8-2：(累減形式)
b=5
b-=3    #相當於 b=b-3
print(b)


# In[ ]:


# 範例 2-8-3：(累乘形式)
c=5
c*=3    #相當於 c=c*3
print(b)


# In[ ]:


# 範例 2-8-4：(累除形式)
d=5
d/=3    #相當於 d=d/3
print(d)


# In[ ]:


# 範例 2-8-5：(累次方形式)
e=1.18
e**=2    #相當於 e=e**2
print(e)


# In[ ]:


# 練習 2-8-1：(舉例呈現整數除法求商的累除形式)


# In[ ]:


# 練習 2-8-2：(舉例呈現整數除法求餘的累除形式)


# In[ ]:


# 2-9 多重給定變數

# 範例 2-9-1：錯誤
a=5, b=3, c=1
e=a*2+b*3+c*4
print(e)


# In[ ]:


# 範例 2-9-2：正確
a,b,c=5,3,1
e=a*2+b*3+c*4
print(e)


# In[ ]:


# 範例 2-9-3
a=b=c=5
e=a*2+b*3+c*4
print(e)


# In[ ]:


# 範例 2-9-4：數值交換
a,b,c=5,3,1
print(a,b,c)
a,b,c=c,a,b
print(a,b,c)
e=a*2+b*3+c*4
print(e)


# In[6]:


# 範例 2-9-4：整數除法的函數 divmod()
a,b=32,5
print(a//b)
print(a%b)
print(divmod(a,b))


# In[ ]:


# 練習 2-9-1：(同時給定三個變數，再利用此三變數同時給定另三個變數)，輸出並檢視


# In[8]:


# 2-10 刪除變數

# 範例 2-10-1：
a,b,c=1,3,5
d=2*a+3*b+4*c
print(d)

del a
print(d)
del d
print(d)


# In[ ]:


# 2-11 多行合併與斷行
# 範例 2-11-1：多行以分號合併，但破壞結構，非常不建議使用
a,b,c=1,3,5;d=2*a+3*b+4*c;print(d)


# In[ ]:


# 範例 2-11-2：以反斜線\或小括號斷行，但沒必要也不要做
a,b,c=1,3,5
d=2*a+  3*b+  4*c
print(d)
e=(4*a+
   3*b+
   2*c)
print(e)

