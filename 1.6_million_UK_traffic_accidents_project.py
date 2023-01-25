import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#  DATA PREPARATION

df1 = pd.read_csv('traffic_data.csv') #csv file reading. The "read_..." command changes for different files. eg read_excel, read_json, read_html...
df2 = pd.read_csv('traffic_data2.csv')
df3 = pd.read_csv('traffic_data3.csv')

df=pd.concat([df1,df2,df3])

data = df.drop(['Accident_Index', 'Location_Easting_OSGR', 'Location_Northing_OSGR','Longitude',
       'Latitude', 'Police_Force','Date','Local_Authority_(District)','Local_Authority_(Highway)',
       '1st_Road_Class', '1st_Road_Number', 'Speed_limit','Junction_Detail', 'Junction_Control', '2nd_Road_Class',
       '2nd_Road_Number', 'Pedestrian_Crossing-Human_Control', 'Pedestrian_Crossing-Physical_Facilities', 
       'Special_Conditions_at_Site', 'Carriageway_Hazards','Did_Police_Officer_Attend_Scene_of_Accident',
       'LSOA_of_Accident_Location'], axis=1)


# Here the data is updated without nulls. 

data.isna().sum()
data.dropna(inplace=True)

# How does the change in traffic flow affect accidents?

q1_data=data.to_numpy()
summation=np.zeros(80)

t=0
for k in range(70):
    s=0.0
    for i in range(1501957):
        if(q1_data[i,1]==k):
            s+=q1_data[i,0]
    summation[t]=s
    t+=1
   
summ=summation[summation!=0]  #here where columns with a value of zero are dropped

x=data["Number_of_Vehicles"].value_counts()
y=x.sort_index()
yy=y.to_numpy()

graph_y_axis=summ/yy

graph_x_axis=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,28,29,32,34,67])    

plt.bar(graph_x_axis,graph_y_axis)


""" We need to use different columns for almost every question. For this reason, it would be more correct to open a new page for each question.
Question 2 and 4 an be solve in one program"""

# What increases accident rates?     
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#  DATA PREPARATION

df1 = pd.read_csv('traffic_data.csv') #csv file reading. The "read_..." command changes for different files. eg read_excel, read_json, read_html...
df2 = pd.read_csv('traffic_data2.csv')
df3 = pd.read_csv('traffic_data3.csv')

df=pd.concat([df1,df2,df3])

data = df.drop(['Accident_Index', 'Location_Easting_OSGR', 'Location_Northing_OSGR','Longitude',
       'Latitude','Date','Local_Authority_(District)','Local_Authority_(Highway)',"Junction_Detail",
       '1st_Road_Number', 'Junction_Control','2nd_Road_Number','Special_Conditions_at_Site', 'Carriageway_Hazards','Did_Police_Officer_Attend_Scene_of_Accident',
       'LSOA_of_Accident_Location'], axis=1)


# Here the data is updated without nulls. 

data.isna().sum()
data.dropna(inplace=True)

road_cond_array=data["Road_Surface_Conditions"].unique() #burada isimlerini aldık
road_cond=data["Road_Surface_Conditions"].value_counts().values
plt.pie(road_cond ,labels=road_cond_array,radius=2,startangle=35,textprops={"size":"medium"},explode=(0.02,0.02,0.02,0.02,0.7),autopct='%1.1f%%')
plt.legend()
plt.title("Accident percentages by\n road surface conditions")
plt.show()

weather_cond_array=data["Weather_Conditions"].unique()
weather_cond=data["Weather_Conditions"].value_counts().values
plt.pie(weather_cond,labels=weather_cond_array,radius=2,startangle=25,textprops={"size":"medium"},autopct='%1.1f%%',explode=(0.02,0.02,0.02,0.02,0.02,0.5,0.7,1,1.5))
plt.title("Accident percentages by weather conditions")
plt.show()


ligth_cond_array=data["Light_Conditions"].unique()
ligth_cond=data["Light_Conditions"].value_counts().values
plt.pie(ligth_cond,labels=ligth_cond_array,radius=2,startangle=25,textprops={"size":"medium"},autopct='%1.1f%%',explode=(0.02,0.02,0.02,0.7,1))
plt.title("Accident percentages by ligth conditions")
plt.show()

pedestrian_cond_array=data["Pedestrian_Crossing-Physical_Facilities"].unique()
pedestrian_cond=data["Pedestrian_Crossing-Physical_Facilities"].value_counts().values
plt.pie(pedestrian_cond,labels=pedestrian_cond_array,radius=2,startangle=25,textprops={"size":"medium"},autopct='%1.1f%%',explode=(0.02,0.02,0.02,0.02,0.02,1))
plt.title("Accident percentages by ligth conditions")
plt.show()


speed_cond_array=data["Speed_limit"].unique()
speed_cond=data["Speed_limit"].value_counts().values
plt.pie(speed_cond,labels=speed_cond_array,radius=2,startangle=25,textprops={"size":"medium"},autopct='%1.1f%%',explode=(0.02,0.02,0.02,0.02,0.02,0.1,1,1.5))
plt.title("Accident percentages by ligth conditions")
plt.show()

day_array=data["Day_of_Week"].unique()
day=data["Day_of_Week"].value_counts().values
plt.pie(day,labels=day_array,radius=2,startangle=25,textprops={"size":"medium"},autopct='%1.1f%%',explode=(0.02,0.02,0.02,0.02,0.02,0.02,0.02))
plt.title("Accident percentages by days")
plt.show()


time = data["Time"].value_counts() 

time_df = pd.DataFrame(time, index=data["Time"])
time_df.columns =['Number of Accidents']
time_heat = time_df.groupby('Time').min()

plt.figure(figsize = (20,9),facecolor='grey')
ax = sns.heatmap(time_heat,cmap="YlGnBu") 
plt.yticks(rotation =0)
plt.show()

# Can we predict accident rates over time?
df4=pd.read_csv('traffic.csv')

df_4=df4.drop(['AADFYear', 'CP','Region', 'LocalAuthority', 'Road', 'RoadCategory', 'Easting',
       'Northing', 'StartJunction', 'EndJunction', 'LinkLength_km',
       'LinkLength_miles', 'PedalCycles', 'Motorcycles', 'CarsTaxis',
       'BusesCoaches', 'LightGoodsVehicles', 'V2AxleRigidHGV',
       'V3AxleRigidHGV', 'V4or5AxleRigidHGV', 'V3or4AxleArticHGV',
       'V5AxleArticHGV', 'V6orMoreAxleArticHGV', 'AllHGVs', 'AllMotorVehicles',
       'Lat', 'Lon'],axis=1)

df_4.isna().sum()
df_4.dropna(inplace=True)

estimation_array=df_4["Estimation_method"].unique()
estimation=df_4["Estimation_method"].value_counts().values
plt.pie(estimation,labels=estimation_array,radius=2,startangle=25,textprops={"size":"medium"},autopct='%1.1f%%',explode=(0.02,0.02))
plt.title("Estimation method of predicted accidents")
plt.show()


estimation_method_array=df_4["Estimation_method_detailed"].unique()
estimation_method=df_4["Estimation_method_detailed"].value_counts().values
plt.pie(estimation_method,labels=estimation_method_array,radius=2,startangle=25,textprops={"size":"medium"},autopct='%1.1f%%',explode=(0.02,0.02,0.02,0.02,0.02))
plt.title("The way predictions are made")
plt.show()


# How did rural and urban areas differ?

q4_data=data.to_numpy()

def average(x):
    s=0.0
    for i in range(1501918):
        if(q4_data[i,15]==x):
            s+=q4_data[i,1]
    sf=s/1501918
    return sf
        
urban=average(1)
rural=average(2)
y_axis=np.array([urban,rural])
x_axis=np.array(["urban","rural"])
plt.bar(x_axis,y_axis)
plt.title("Average of accident severity of urban and rural areas")
plt.show()




