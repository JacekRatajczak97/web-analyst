


import pandas as pd
import matplotlib.pyplot as plt


internet_users = pd.read_csv('/kaggle/input/internet-users/Final.csv')





# Number of internet users in 2020

top_10_countries = (internet_users[internet_users['Year']==2020]
                 .loc[:, ["Entity", "Code", "Year", "No. of Internet Users"]]
                 .sort_values("No. of Internet Users", ascending=False)
                 .loc[(internet_users["Entity"] != "World") & (internet_users["Code"] != "Region")]
                 .head(10))


fig, ax = plt.subplots(figsize=(16, 6))
plt.bar(top_10_countries['Entity'], top_10_countries['No. of Internet Users'])
plt.title('Number of internet users in 2020')
plt.xlabel('Countries')
plt.ylabel('Number of internet users (in millions)')
for i, v in enumerate(top_10_countries['No. of Internet Users']):
    plt.text(i, v+0.5, str(round(v/1000000, 1)) + 'M', ha='center')
plt.show()





# Internet Users %
top10_countries_users = (internet_users[internet_users["Year"] == 2020]
                        .loc[:, ["Entity", "Internet Users(%)","No. of Internet Users"]]
                        .sort_values("Internet Users(%)", ascending=False)
                        .head(10))

fia, ax = plt.subplots(figsize=(16,6))
plt.bar(top10_countries_users["Entity"], top10_countries_users["Internet Users(%)"])
plt.title('Internet Users % in 2020')
plt.xlabel('Country')
plt.ylabel('% of population')
for i, v in enumerate(top10_countries_users["Internet Users(%)"]):
    plt.text(i, v+0.5, str(round(v,2)) + "%", ha="center")





# All about the country
def country_analysis(country):
    my_country = internet_users[internet_users["Entity"] == country]
    
    fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(8,6))
    
    fig.suptitle("Internet Usage in " + country)
    
    #Cellular Subscription
    axs[0,0].plot(my_country['Year'], my_country["Cellular Subscription"])
    axs[0,0].set_title("Cellular Subscription in")
    axs[0,0].grid(True, linestyle="--", alpha=0.4)
    
    #Internet Users(%)
    axs[0,1].plot(my_country['Year'], my_country["Internet Users(%)"])
    axs[0,1].set_title("Internet Users (%)")
    axs[0,1].grid(True, linestyle="--", alpha=0.4)
    
    #No. of Internet Users
    axs[1,0].plot(my_country['Year'], my_country["No. of Internet Users"])
    axs[1,0].set_title("No. of Internet Users (mln)")
    axs[1,0].grid(True, linestyle="--", alpha=0.4)
    
    #Broadband Subscription
    axs[1,1].plot(my_country['Year'], my_country["Broadband Subscription"])
    axs[1,1].set_title("Broadband Subscription")
    axs[1,1].grid(True, linestyle="--", alpha=0.4)
    
    
    fig.subplots_adjust(hspace=0.5)
    
country_analysis("Poland")






