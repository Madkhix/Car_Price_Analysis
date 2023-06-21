import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sehirler=["Adana", "Adıyaman", "Afyon", "Ağrı", "Amasya", "Ankara", "Antalya", "Artvin", "Aydın", "Balıkesir", "Bilecik", "Bingöl", "Bitlis", "Bolu", "Burdur", "Bursa", "Çanakkale", "Çankırı", "Çorum", "Denizli", "Diyarbakır", "Edirne", "Elazığ", "Erzincan", "Erzurum", "Eskişehir", "Gaziantep", "Giresun", "Gümüşhane", "Hakkari", "Hatay", "Isparta", "İçel (Mersin)", "İstanbul", "İzmir", "Kars", "Kastamonu", "Kayseri", "Kırklareli", "Kırşehir", "Kocaeli", "Konya", "Kütahya", "Malatya", "Manisa", "Kahramanmaraş", "Mardin", "Muğla", "Muş", "Nevşehir", "Niğde", "Ordu", "Rize", "Sakarya", "Samsun", "Siirt", "Sinop", "Sivas", "Tekirdağ", "Tokat", "Trabzon", "Tunceli", "Şanlıurfa", "Uşak", "Van", "Yozgat", "Zonguldak", "Aksaray", "Bayburt", "Karaman", "Kırıkkale", "Batman", "Şırnak", "Bartın", "Ardahan", "Iğdır", "Yalova", "Karabük", "Kilis", "Osmaniye", "Düzce"]

#Data reading
df = pd.read_excel("E:/Users//Spyder Python/output_araCliojoy.xlsx")
#Choosing Location
a = df['Lokasyon']
b = df['Fiyat']
c = df['Yıl']
#Convert to list
li = a.tolist()
d = c.tolist()
#new list
res = []
#Only choose cities
for i in range(1000):
    sr = li[i]
    res.append(sr.split('/', 1)[0])
#print(max(res,key=res.count))

#Max city min price
x = []
y = []
z = []
q = []
for i in range(1000):
    if('İstanbul' == res[i]):
        x.append(b[i])
#print(min(x))
#Min price 
for i in range(1000):
    if(min(b) == b[i]):
        print(res[i])
        print(min(b))

#max year
#print(max(d,key=d.count))

#year 2017 min and max
for i in range(1000):
    if(2017 == d[i]):
        y.append(b[i])
#print(min(y))
#print(max(y))
s = []
#find year 2017 min price is which city
for i in range(1000):
    if(2017 == d[i] and 389.999 == b[i]):
        z.append(res[i])
#print(z)

for j in range(81):
    for i in range(1000):
        if(2017 == d[i] and res[i] == sehirler[j]):
            q.append(b[i])
            s.append(res[i])
lst1 =list(zip(s,q))

def common_member(a, b):
    result = [i for i in a if i in b]
    return result
a = common_member(s,sehirler)
my_dict = {i:a.count(i) for i in a}

temp = []

for x in s:
    if x not in temp:
        temp.append(x)

ints_list = temp
#print (my_dict)

averages = {}
counts = {}
for name, value in lst1:
    if name in averages:
        averages[name] += value
        counts[name] += 1
    else:
        averages[name] = value
        counts[name] = 1
        
writer = averages
for name in writer:
    writer[name] = writer[name]/float(counts[name]) 

#tüm değerler tek çatı altında
dictionary = {k: [q[i] for i in [j for j, x in enumerate(s) if x == k]] for k in set(s)}

for i in ints_list:
    print(min(dictionary[i]))
    print(max(dictionary[i]))
dfD = pd.DataFrame.from_dict(dictionary, orient='index')
dfD = dfD.transpose()

dfD.to_excel("output_city_mean_dict.xlsx", index=False)

dfS = pd.DataFrame(data=writer, index = [1])

#convert into excel
dfS.to_excel("output_city_mean23.xlsx", index=False)
cities = ['Adana', 'Ankara', 'Antalya', 'Aydın', 'Bursa', 'Çankırı', 'Denizli', 'Diyarbakır', 'Eskişehir', 'Gaziantep', 'Hatay', 'İstanbul', 'İzmir', 'Kayseri', 'Kırklareli', 'Kırşehir', 'Kocaeli', 'Konya', 'Manisa', 'Kahramanmaraş', 'Mardin', 'Muğla', 'Ordu', 'Sakarya', 'Samsun', 'Sivas', 'Tekirdağ', 'Tokat', 'Trabzon', 'Van', 'Yozgat', 'Zonguldak', 'Aksaray', 'Batman', 'Düzce']
def heatmap():
    sns.set(rc={"figure.figsize":(40,10)})

    g = sns.heatmap(dfS, cmap="Blues", annot=True, fmt='g')
    g.get_figure().savefig("heatmap.png")

def boxplot_plt():
    plt.rcParams["figure.figsize"] = [20, 20]
    plt.rcParams["figure.autolayout"] = True
    ax = dfD[['Adana', 'Ankara', 'Antalya', 'Aydın', 'Bursa', 'Çankırı', 'Denizli', 'Diyarbakır', 'Eskişehir', 'Gaziantep', 'Hatay', 'İstanbul', 'İzmir', 'Kayseri', 'Kırklareli', 'Kırşehir', 'Kocaeli', 'Konya', 'Manisa', 'Kahramanmaraş', 'Mardin', 'Muğla', 'Ordu', 'Sakarya', 'Samsun', 'Sivas', 'Tekirdağ', 'Tokat', 'Trabzon', 'Van', 'Yozgat', 'Zonguldak', 'Aksaray', 'Batman', 'Düzce']].plot(kind='box', title='boxplot')
    plt.show() 
    
def boxplot_sns():    
    sns.boxplot(y=dfD["Adana"]) 

import geopandas

def geo():
    countires = geopandas.read_file("countries.geojson")
    countires[countires["ADMIN"]=="Turkey"].plot()
    turkey_geo = geopandas.read_file(r'TUR_adm/TUR_adm1.shp')
    print(turkey_geo.head(10))
    turkey_geo.plot()
    turkey_geo.plot(figsize=(18,18),edgecolor ="k",facecolor="none")
    turkey_geo.plot(figsize=(18,18),edgecolor ="red",facecolor="orange")
    
    data = pd.read_excel("output_city.xlsx")
    
    for i in turkey_geo["NAME_1"].iteritems():
        print(i)
    for j in data["city"].iteritems():
        print(j)
    turkey_geo.replace("K. Maras","Kahramanmaraş",inplace=True)
    turkey_geo.replace('Çankiri', 'Çankırı',inplace=True)
    turkey_geo.replace('Adiyaman', 'Adıyaman',inplace=True)
    turkey_geo.replace('Agri', 'Ağrı',inplace=True)
    turkey_geo.replace('Aydin', 'Aydın',inplace=True)
    turkey_geo.replace('Balikesir', 'Balıkesir',inplace=True)
    turkey_geo.replace('Diyarbakir', 'Diyarbakır',inplace=True)
    turkey_geo.replace('Eskisehir', 'Eskişehir',inplace=True)
    turkey_geo.replace('Gümüshane', 'Gümüşhane',inplace=True)
    turkey_geo.replace('Istanbul', 'İstanbul',inplace=True)
    turkey_geo.replace('Izmir', 'İzmir',inplace=True)
    turkey_geo.replace('Kinkkale', 'Kırıkkale',inplace=True)
    turkey_geo.replace('Kirklareli', 'Kırklareli',inplace=True)
    turkey_geo.replace('Kirsehir', 'Kırşehir',inplace=True)
    turkey_geo.replace('Mugla', 'Muğla',inplace=True)
    turkey_geo.replace('Mus', 'Muş',inplace=True)
    turkey_geo.replace('Nevsehir', 'Nevşehir',inplace=True)
    turkey_geo.replace('Sanliurfa', 'Şanlıurfa',inplace=True)
    turkey_geo.replace('Sirnak', 'Şırnak',inplace=True)
    turkey_geo.replace('Tekirdag', 'Tekirdağ',inplace=True)
    turkey_geo.replace('Usak', 'Uşak',inplace=True)
    turkey_geo.replace('Zinguldak', 'Zonguldak',inplace=True)
    turkey_geo.replace('Afyon', 'Afyonkarahisar',inplace=True)
    turkey_geo.replace('Nigde', 'Niğde',inplace=True)
    for i in turkey_geo["NAME_1"].iteritems():
        print(i)
        
    turkey_geo.rename(columns = {'NAME_1':'İl'},inplace = True)
    data.rename(columns = {"city":"İl"},inplace= True)
    
    print(turkey_geo.head(5))
    
    print(data.head(5))
    
    harita_data = turkey_geo.merge(data,on="İl")
    print(harita_data)  
    harita_data.plot(figsize=(18,18))
    harita_data.plot(column="price",cmap="Reds",figsize=(15,18))
    
    harita_data_points = harita_data.copy()
    harita_data_points["center"] = harita_data_points["geometry"].centroid
    harita_data_points.set_geometry("center", inplace = True)
    print(harita_data_points)
    
    import adjustText as aT
    
    ax = harita_data.plot(figsize = (20, 12), column = "price",cmap="Spectral",edgecolor ="k", legend=True)
    texts = []

    for x, y, label in zip(harita_data_points.center.x, harita_data_points.center.y, harita_data_points["İl"]):
        texts.append(plt.text(x, y, label, fontsize = 8)) #illerin ve karşılık gelen enlem ve boylam ortalamalarını içeren veri seti oluşturuyoruz 

    aT.adjust_text(texts, force_points=0.3, force_text=5, expand_points=(1,1), expand_text=(1,1), 
               arrowprops=dict(arrowstyle="-", color='grey', lw=0.5)) #il isimlerini haritaya ekliyoruz. 

    ax.set_title("Türkiye İkinci El Araba Ortalama Fiyat",size = 20)
    ax.set_axis_off() #eksenleri kaldırıyoruz
import bar_chart_race as bcr

def barchart():
    data = pd.read_excel("output_city.xlsx")
    print(data.head())
    data = data[['city', 'price']]
    df = data.pivot_table(values = 'price',index = ['city'], columns = 'city')
    print(df.head())
    df.fillna(0, inplace=True)
    df.sort_values(list(df.columns),inplace=True)
    df = df.sort_index()
    print(df.head())
    df.iloc[:, 0:-1] = df.iloc[:, 0:-1].cumsum()
    print(df.head())
    top_prem_clubs = set()

    for index, row in df.iterrows():
        top_prem_clubs |= set(row[row > 0].sort_values(ascending=False).head(35).index)

    df = df[top_prem_clubs]
    print(df.head())
    bcr.bar_chart_race(df = df, 
                   n_bars = 35, 
                   sort='desc',
                   title='Şehirlere göre ortalama araç fiyatı',
                   filename = 'plt_shb_Bar.gif')


geo()





    
    