import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('airport_traffic.csv')

# Removing unnecessary columns
used_columns = [col for col in data.columns if not col in ["AggregationMethod", "Geography", "PercentOfBaseline", "Version", "Centroid"]]
data = data[used_columns]

# Filtering unique data by Airport Name
data_unique = data[~data[["AirportName"]].duplicated()].reset_index(drop=True)

# Pie Chart visualization
def pieChart():
    df_airport = pd.DataFrame(data["AirportName"].value_counts())
    plot_airport = df_airport.plot.pie(y='AirportName', figsize=(8, 8), autopct="%.2f", legend=False)
    plot_airport.set_title("Airport Name Records")
    
    df_country = pd.DataFrame(data["Country"].value_counts())
    plot_country = df_country.plot.pie(y='Country', figsize=(8, 8), autopct="%.2f", legend=False)
    plot_country.set_title("Country Records")
    
    df_state = pd.DataFrame(data["State"].value_counts())
    plot_state = df_state.plot.pie(y='State', figsize=(8, 8), autopct="%.2f", legend=False)
    plot_state.set_title("State Records")
    
    df_city = pd.DataFrame(data["City"].value_counts())
    plot_city = df_city.plot.pie(y='City', figsize=(8, 8), autopct="%.2f", legend=False)
    plot_city.set_title("City Records")

# Bar Chart visualization
def barChart():
    plt.figure(figsize = (10,5))
    plot_airport_count = sns.countplot(data=data, x="AirportName", order = data['AirportName'].value_counts().index)
    plot_airport_count.set_xticklabels(plot_airport_count.get_xticklabels(), rotation=90)
    plot_airport_count.set_title("Airport Records")

    plt.figure(figsize = (10,5))
    plot_country_count = sns.countplot(x = 'Country', data = data, order = data['Country'].value_counts().index)
    plot_country_count.set_xticklabels(plot_country_count.get_xticklabels())
    plot_country_count.set_title("Country Records")

    plt.figure(figsize = (10,5))
    plot_state_count = sns.countplot(x = 'State', data = data, order = data['State'].value_counts().index)
    plot_state_count.set_xticklabels(plot_state_count.get_xticklabels(), rotation=90)
    plot_state_count.set_title("State Records")

    plt.figure(figsize = (10,5))
    plot_city_count = sns.countplot(x = 'City', data = data, order = data['City'].value_counts().index)
    plot_city_count.set_xticklabels(plot_city_count.get_xticklabels(), rotation=90)
    plot_city_count.set_title("City Records")

def main():
    pieChart()
    barChart()

main()
