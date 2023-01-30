import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#  DATA PREPARATION

df1 = pd.read_csv('2015.csv') #csv file reading. The "read_..." command changes for different files. eg read_excel, read_json, read_html...
df2 = pd.read_csv('2016.csv')
df3 = pd.read_csv('2017.csv')
df4 = pd.read_csv('2018.csv')
df5 = pd.read_csv('2019.csv')

# Which countries or regions are in overall happiness?
# 2015

values15=df1["Happiness Score"].nlargest(n=10)
labels15=df1["Country"].head(10)

sns.barplot(y=labels15,x=values15).set(title="Top 10 happiest countries in 2015")
plt.show()


# 2016

values16=df2["Happiness Score"].nlargest(n=10)
labels16=df2["Country"].head(10)

sns.barplot(y=labels16,x=values16).set(title="Top 10 happiest countries in 2016")
plt.show()

# 2017

values17=df3["Happiness.Score"].nlargest(n=10)
labels17=df3["Country"].head(10)

sns.barplot(y=labels17,x=values17).set(title="Top 10 happiest countries in 2017")
plt.show()

# 2018

values18=df4["Score"].nlargest(n=10)
labels18=df4["Country or region"].head(10)

sns.barplot(y=labels18,x=values18).set(title="Top 10 happiest countries in 2018")
plt.show()

# 2019

values19=df5["Score"].nlargest(n=10)
labels19=df5["Country or region"].head(10)

sns.barplot(y=labels19,x=values19).set(title="Top 10 happiest countries in 2019")
plt.show()

# Which countries or regions rank highest in each of the six factors that contribute to happiness?
# How did the country rankings or scores change between the 2015-2016 and 2016-2017 reports for the top 10 countries?
# 6 factors: economic production, social support, life expectancy, freedom, absence of corruption, and generosity

# Economic Production

ep15=float(df1["Economy (GDP per Capita)"].nlargest(n=1))
df_1=df1.to_numpy()
ep15_country=df_1[27,0]+(" 2015")


ep16=float(df2["Economy (GDP per Capita)"].nlargest(n=1))
df_2=df2.to_numpy()
ep16_country=df_2[35,0]+(" 2016")


ep17=float(df3["Economy..GDP.per.Capita."].nlargest(n=1))
df_3=df3.to_numpy()
ep17_country=df_3[34,0]+(" 2017")


ep18=float(df4["GDP per capita"].nlargest(n=1))
df_4=df4.to_numpy()
ep18_country=df_4[19,1]+(" 2018")


ep19=float(df5["GDP per capita"].nlargest(n=1))
df_5=df5.to_numpy()
ep19_country=df_5[19,1]+(" 2019")

xep_axis=(ep15_country,ep16_country,ep17_country,ep18_country,ep19_country)
yep_axis=(ep15,ep16,ep17,ep18,ep19)
plt.barh(xep_axis,yep_axis)
plt.title("Countries ranked first in happiness due to economic factor by years")
plt.show()

# Family

fa15=float(df1["Family"].nlargest(n=1))
fa15_country=df_1[1,0]+(" 2015")


fa16=float(df2["Family"].nlargest(n=1))
fa16_country=df_2[2,0]+(" 2016")


fa17=float(df3["Family"].nlargest(n=1))
fa17_country=df_3[2,0]+(" 2017")


fa18=float(df4["Social support"].nlargest(n=1))
fa18_country=df_4[3,1]+(" 2018")


fa19=float(df5["Social support"].nlargest(n=1))
fa19_country=df_5[3,1]+(" 2019")

xfa_axis=(fa15_country,fa16_country,fa17_country,fa18_country,fa19_country)
yfa_axis=(fa15,fa16,fa17,fa18,fa19)
plt.barh(xfa_axis,yfa_axis)
plt.title("Countries ranked first in happiness due to social support by years")
plt.show()


# Life expectancy

le15=float(df1["Health (Life Expectancy)"].nlargest(n=1))
le15_country=df_1[23,0]+(" 2015")


le16=float(df2["Health (Life Expectancy)"].nlargest(n=1))
le16_country=df_2[74,0]+(" 016")


le17=float(df3["Health..Life.Expectancy."].nlargest(n=1))
le17_country=df_3[25,0]+(" 2017")


le18=float(df4["Healthy life expectancy"].nlargest(n=1))
le18_country=df_4[75,1]+(" 2018")


le19=float(df5["Healthy life expectancy"].nlargest(n=1))
le19_country=df_5[33,1]+(" 2019")

xle_axis=(le15_country,le16_country,le17_country,le18_country,le19_country)
yle_axis=(le15,le16,le17,le18,le19)
plt.barh(xle_axis,yle_axis)
plt.title("Countries ranked first in happiness due to life expectancy by years")
plt.show()

# Freedom

f15=float(df1["Freedom"].nlargest(n=1))
f15_country=df_1[3,0]+(" 2015")


f16=float(df2["Freedom"].nlargest(n=1))
f16_country=df_2[48,0]+(" 2016")


f17=float(df3["Freedom"].nlargest(n=1))
f17_country=df_3[46,0]+(" 2017")


f18=float(df4["Freedom to make life choices"].nlargest(n=1))
f18_country=df_4[43,1]+(" 2018")


f19=float(df5["Freedom to make life choices"].nlargest(n=1))
f19_country=df_5[40,1]+(" 2019")

xf_axis=(f15_country,f16_country,f17_country,f18_country,f19_country)
yf_axis=(f15,f16,f17,f18,f19)
plt.barh(xf_axis,yf_axis)
plt.title("Countries ranked first in happiness due to Freedom by years")
plt.show()


# Absence of corruption

a15=float(df1["Trust (Government Corruption)"].nlargest(n=1))
a15_country=df_1[153,0]+(" 2015")


a16=float(df2["Trust (Government Corruption)"].nlargest(n=1))
a16_country=df_2[151,0]+(" 2016")


a17=float(df3["Trust..Government.Corruption."].nlargest(n=1))
a17_country=df_3[25,0]+(" 2017")


a18=float(df4["Perceptions of corruption"].nlargest(n=1))
a18_country=df_4[33,1]+(" 2018")


a19=float(df5["Perceptions of corruption"].nlargest(n=1))
a19_country=df_5[33,1]+(" 2019")

xa_axis=(a15_country,a16_country,a17_country,a18_country,a19_country)
ya_axis=(a15,a16,a17,a18,a19)
plt.barh(xa_axis,ya_axis)
plt.title("Countries ranked first in happiness due to corruption by years")
plt.show()


# Generosity

g15=float(df1["Generosity"].nlargest(n=1))
g15_country=df_1[128,0]+(" 2015")


g16=float(df2["Generosity"].nlargest(n=1))
g16_country=df_2[118,0]+(" 2016")


g17=float(df3["Generosity"].nlargest(n=1))
g17_country=df_3[113,0]+(" 2017")


g18=float(df4["Generosity"].nlargest(n=1))
g18_country=df_4[129,1]+(" 2018")


g19=float(df5["Generosity"].nlargest(n=1))
g19_country=df_5[130,1]+(" 2019")

xg_axis=(g15_country,g16_country,g17_country,g18_country,g19_country)
yg_axis=(g15,g16,g17,g18,g19)
plt.barh(xg_axis,yg_axis)
plt.title("Countries ranked first in happiness due to Generosity by years")
plt.show()


#Has any country experienced a significant increase or decrease in happiness?

co_15_h=df1["Country"].head(20).to_numpy()
co_15_t=df1["Country"].tail(20).to_numpy()

co_16_h=df2["Country"].head(20).to_numpy()
co_16_t=df2["Country"].tail(20).to_numpy()

co_17_h=df3["Country"].head(20).to_numpy()
co_17_t=df3["Country"].tail(20).to_numpy()

co_18_h=df4["Country or region"].head(20).to_numpy()
co_18_t=df4["Country or region"].tail(20).to_numpy()

co_19_h=df5["Country or region"].head(20).to_numpy()
co_19_t=df5["Country or region"].tail(20).to_numpy()


for i in range(1,20):
    if(co_15_t[i] in co_16_h):
        print("Country"+co_15_t[i]+" was located in the bottom 20 of the list last year, while in 2016, it entered the top 20.")
    else:
        print("No country has experienced a good rise.")

for i in range(1,20):
    if(co_16_t[i] in co_17_h):
        print("Country"+co_16_t[i]+" was located in the bottom 20 of the list last year, while in 2016, it entered the top 20.")
    else:
        print("No country has experienced a good rise.")


for i in range(1,20):
    if(co_17_t[i] in co_18_h):
        print("Country"+co_17_t[i]+" was located in the bottom 20 of the list last year, while in 2016, it entered the top 20.")
    else:
        print("No country has experienced a good rise.")


for i in range(1,20):
    if(co_18_t[i] in co_19_h):
        print("Country"+co_18_t[i]+" was located in the bottom 20 of the list last year, while in 2016, it entered the top 20.")
    else:
        print("No country has experienced a good rise.")

for i in range(1,20):
    if(co_15_t[i] in co_19_h):
        print("Country"+co_15_t[i]+" was located in the bottom 20 of the list last year, while in 2016, it entered the top 20.")
    else:
        print("No country has experienced a good rise.")


for i in range(1,20):
    if(co_15_h[i] in co_16_t):
        print("Country"+co_15_h[i]+" was located in the top 20 of the list last year, while in 2016, it entered the bottom 20.")
    else:
        print("No country has experienced a important decline.")

for i in range(1,20):
    if(co_16_h[i] in co_17_t):
        print("Country"+co_16_h[i]+" was located in the top 20 of the list last year, while in 2016, it entered the bottom 20.")
    else:
        print("No country has experienced a important decline.")


for i in range(1,20):
    if(co_17_h[i] in co_18_t):
        print("Country"+co_17_h[i]+" was located in the top 20 of the list last year, while in 2016, it entered the bottom 20.")
    else:
        print("No country has experienced a important decline.")


for i in range(1,20):
    if(co_18_h[i] in co_19_t):
        print("Country"+co_18_h[i]+" was located in the top 20 of the list last year, while in 2016, it entered the bottom 20.")
    else:
        print("No country has experienced a important decline.")

for i in range(1,20):
    if(co_15_h[i] in co_19_t):
        print("Country"+co_15_h[i]+" was located in the top 20 of the list last year, while in 2016, it entered the bottom 20.")
    else:
        print("No country has experienced a important decline.")
