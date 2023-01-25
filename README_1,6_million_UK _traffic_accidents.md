# 1.6 million UK Traffic Accidents Project

**In this project, answers to four questions were sought based on data collected from traffic accidents in the United Kingdom.
1-How does the change in traffic flow affect the accidents?
2-What increases the accident rates?
3-Can we predict accident rates over time?
4-How did rural and urban areas differ?**

You can access this dataset [by clicking here](https://www.kaggle.com/datasets/daveianhickey/2000-16-traffic-flow-england-scotland-wales?select=ukTrafficAADF.csv).

Firstly, the files separated into three different files according to the years under the "data preparation" section were read and merged.The dataset contains many columns. Among these columns, those whose answer is not suitable for the question sought are not included in the dataframe (column selections differ according to the questions). This process not only simplifies the analysis, but also speeds up the execution of the program.
Then the "null" values in the merged file were cleared. The purpose of this process is to achieve more accurate results.

## How does the change in traffic flow affect the accidents?

Since traffic density is proportional to the number of vehicles, "Number_of_Vehicles" and "Accident_Severity" columns were analyzed to find the answer to this question. First of all, the unique values of the number of vehicles in the dataset were determined. Then, the accident severity for these values was scanned in the data set, collected and averaged. Finally, the accident severity graph corresponding to the number of vehicles was drawn.

![How does the change in traffic flow affect accidents](https://user-images.githubusercontent.com/93272032/214677780-40b74ad8-3fb9-4e96-85ba-444fd3559cdd.png)


## What increases the accident rates?
For the second question, many topics were reviewed and analyzed using a pie chart.
![Figure 2023-01-25 231158](https://user-images.githubusercontent.com/93272032/214682056-7cc0298f-8abe-4c60-8283-3504ee79d41c.png)
![Figure 2023-01-25 231211](https://user-images.githubusercontent.com/93272032/214682066-0fe9efc0-9eb0-4824-966d-088a2871290a.png)
![Figure 2023-01-25 231217](https://user-images.githubusercontent.com/93272032/214682070-3523dac8-3f7a-479e-8ef8-ea90fd6915f4.png)
![Figure 2023-01-25 233718](https://user-images.githubusercontent.com/93272032/214684753-1997e60e-a66f-4ad5-8eb0-c9ca47f5b6eb.png)
![Figure 2023-01-25 233723](https://user-images.githubusercontent.com/93272032/214684765-5cf0f25c-eef1-436a-84b5-2e0c1eabb453.png)  
![Figure 2023-01-25 231244](https://user-images.githubusercontent.com/93272032/214682086-cb463a17-d21a-486f-9f67-fca9fa9b1e96.png)
![Figure 2023-01-25 232453](https://user-images.githubusercontent.com/93272032/214682090-30ff3270-486b-4a6d-8a95-0a80d5e76749.png)

**Based on the graphs, the following can be said:**  
-Contrary to expectations, fewer accidents occur in conditions with difficult road surfaces, while accidents on dry surfaces are more.  

-When the accidents are evaluated according to the weather conditions, it is seen that the most accidents occur in the windless and good weather. In snowy, foggy and similar bad weather conditions, this rate is too low to compete with good weather.  

-When we look at the light situation in which the accidents occur, contrary to expectations, the accidents experienced during the daytime show the majority.  

-When the graph about the pedestrian crossing and physical facilities is examined, it can be said that they cause a very small part of the accidents.  

-It has been observed that there are more accidents in places where the speed limit is low and the number of accidents decreases as the speed increases.  

-When the comments were made according to the days of the accidents, it was observed that it was generally evenly distributed, but the highest rate was seen on Friday.  

-According to the time of the day, it was observed that the accidents were frequent, especially between 12.30-13.00, 15.00-15.30, 17.30-18.00.  

## Can we predict accident rates over time?
Two different columns were used to make this evaluation: Estimation_Method and Estimation method_detailed.  

![Figure 2023-01-25 235255](https://user-images.githubusercontent.com/93272032/214688158-1992424e-3f17-458e-b23f-8dd8f33c68cc.png)
![Figure 2023-01-25 235305](https://user-images.githubusercontent.com/93272032/214688160-a3c56e01-9bae-4832-b1ca-8b0269ba93f8.png)

As can be seen from these graphs, it is possible to predict accidents by supplementing with other information, but it is necessary to automate it.

## How did rural and urban areas differ?
The data under the heading "urban_or rural" in the data set were used to interpret how the accidents changed according to rural urban areas. As we did for the first question, first the accident severity values corresponding to 1:urban and 2:rural were divided into two groups, averaged, and converted to a column chart.


![Figure 2023-01-25 235310](https://user-images.githubusercontent.com/93272032/214688772-e0b40618-5e3e-4f79-ab85-2290affc67e6.png)

From this it is concluded that there are more severe accidents in urban areas than in rural areas.



