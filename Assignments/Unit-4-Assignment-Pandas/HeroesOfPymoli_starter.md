
### Heroes Of Pymoli Data Analysis
* Of the 1163 active players, the vast majority are male (84%). There also exists, a smaller, but notable proportion of female players (14%).

* Our peak age demographic falls between 20-24 (44.8%) with secondary groups falling between 15-19 (18.60%) and 25-29 (13.4%).  
-----

### Note
* Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.


```python
# Dependencies and Setup
import pandas as pd
import numpy as np

# File to Load (Remember to Change These)
file_to_load = "Resources/purchase_data.csv"

# Read Purchasing File and store into Pandas data frame
purchase_data = pd.read_csv(file_to_load)
purchase_data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase ID</th>
      <th>SN</th>
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Lisim78</td>
      <td>20</td>
      <td>Male</td>
      <td>108</td>
      <td>Extraction, Quickblade Of Trembling Hands</td>
      <td>3.53</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Lisovynya38</td>
      <td>40</td>
      <td>Male</td>
      <td>143</td>
      <td>Frenzied Scimitar</td>
      <td>1.56</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Ithergue48</td>
      <td>24</td>
      <td>Male</td>
      <td>92</td>
      <td>Final Critic</td>
      <td>4.88</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Chamassasya86</td>
      <td>24</td>
      <td>Male</td>
      <td>100</td>
      <td>Blindscythe</td>
      <td>3.27</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Iskosia90</td>
      <td>23</td>
      <td>Male</td>
      <td>131</td>
      <td>Fury</td>
      <td>1.44</td>
    </tr>
  </tbody>
</table>
</div>



## Player Count

* Display the total number of players



```python
total_players = len(purchase_data['SN'].unique())

pd.DataFrame({
    'Total Players': [total_players]
})
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Players</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>576</td>
    </tr>
  </tbody>
</table>
</div>



## Purchasing Analysis (Total)

* Run basic calculations to obtain number of unique items, average price, etc.


* Create a summary data frame to hold the results


* Optional: give the displayed data cleaner formatting


* Display the summary data frame



```python

purchas_analysis = pd.DataFrame({
    'Number of Unique Items' : [len(purchase_data['Item ID'].unique())],
    'Average Price' : [
         "${:,.2f}".format(purchase_data['Price'].sum() / len(purchase_data['Item ID']))
    ],
    'Number of Purchases' : [len(purchase_data['Purchase ID'])],
    'Total Revenue' : ["${:,.2f}".format(purchase_data['Price'].sum())]
})

purchas_analysis

purchase_data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase ID</th>
      <th>SN</th>
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Lisim78</td>
      <td>20</td>
      <td>Male</td>
      <td>108</td>
      <td>Extraction, Quickblade Of Trembling Hands</td>
      <td>3.53</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Lisovynya38</td>
      <td>40</td>
      <td>Male</td>
      <td>143</td>
      <td>Frenzied Scimitar</td>
      <td>1.56</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Ithergue48</td>
      <td>24</td>
      <td>Male</td>
      <td>92</td>
      <td>Final Critic</td>
      <td>4.88</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Chamassasya86</td>
      <td>24</td>
      <td>Male</td>
      <td>100</td>
      <td>Blindscythe</td>
      <td>3.27</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Iskosia90</td>
      <td>23</td>
      <td>Male</td>
      <td>131</td>
      <td>Fury</td>
      <td>1.44</td>
    </tr>
  </tbody>
</table>
</div>



## Gender Demographics

* Percentage and Count of Male Players


* Percentage and Count of Female Players


* Percentage and Count of Other / Non-Disclosed





```python

```


```python
new_index = ["Male", "Female", "Other / Non-Disclosed"]
columns = ["","Total Count","Percentage of Players"]

total_count = purchase_data.nunique()["SN"]
male_count = purchase_data[purchase_data["Gender"] == "Male"]["SN"].nunique()
female_count = purchase_data[purchase_data["Gender"] == "Female"]["SN"].nunique()
other_count = purchase_data[purchase_data["Gender"] == "Other / Non-Disclosed"]["SN"].nunique()

gender_df = pd.DataFrame({
    "": new_index, 
    "Percentage of Players": [ 
        (male_count / total_players * 100),
        (female_count / total_players * 100),
        (other_count / total_players * 100)
    ],
    "Total Count": [
        male_count,
        female_count,
        other_count
    ]
})

# gender_df.sort_values(["Total Count"], ascending = False).style.format({"Percentage of Players":"{:.2f}"})
gender_df.style.format({"Percentage of Players":"{:.2f}"})

gender_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Percentage of Players</th>
      <th>Total Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Male</td>
      <td>84.027778</td>
      <td>484</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Female</td>
      <td>14.062500</td>
      <td>81</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Other / Non-Disclosed</td>
      <td>1.909722</td>
      <td>11</td>
    </tr>
  </tbody>
</table>
</div>




## Purchasing Analysis (Gender)

* Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender




* Create a summary data frame to hold the results


* Optional: give the displayed data cleaner formatting


* Display the summary data frame


```python
gender_stats = purchase_data.groupby("Gender")
purchase_count = gender_stats["Purchase ID"].count()
avg_purchase_price = gender_stats["Price"].mean()
avg_purchase_total = gender_stats["Price"].sum()
avg_purchase_per_person = avg_purchase_total / gender_stats.nunique()["SN"]
 
purchas_analysis = pd.DataFrame({"Purchase Count": purchase_count, 
                                 "Average Purchase Price": avg_purchase_price,
                                 "Average Purchase Value":avg_purchase_total,
                                 "Avg Purchase Total per Person": avg_purchase_per_person
                                })

purchas_analysis.index.name = "Gender"

purchas_analysis.style.format({"Average Purchase Value":"${:,.2f}",
                               "Average Purchase Price":"${:,.2f}",
                               "Avg Purchase Total per Person":"${:,.2f}"
                              })
```




<style  type="text/css" >
</style>  
<table id="T_6e0a4aa4_3343_11e9_9ea4_d4258b18bc57" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >Purchase Count</th> 
        <th class="col_heading level0 col1" >Average Purchase Price</th> 
        <th class="col_heading level0 col2" >Average Purchase Value</th> 
        <th class="col_heading level0 col3" >Avg Purchase Total per Person</th> 
    </tr>    <tr> 
        <th class="index_name level0" >Gender</th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_6e0a4aa4_3343_11e9_9ea4_d4258b18bc57level0_row0" class="row_heading level0 row0" >Female</th> 
        <td id="T_6e0a4aa4_3343_11e9_9ea4_d4258b18bc57row0_col0" class="data row0 col0" >113</td> 
        <td id="T_6e0a4aa4_3343_11e9_9ea4_d4258b18bc57row0_col1" class="data row0 col1" >$3.20</td> 
        <td id="T_6e0a4aa4_3343_11e9_9ea4_d4258b18bc57row0_col2" class="data row0 col2" >$361.94</td> 
        <td id="T_6e0a4aa4_3343_11e9_9ea4_d4258b18bc57row0_col3" class="data row0 col3" >$4.47</td> 
    </tr>    <tr> 
        <th id="T_6e0a4aa4_3343_11e9_9ea4_d4258b18bc57level0_row1" class="row_heading level0 row1" >Male</th> 
        <td id="T_6e0a4aa4_3343_11e9_9ea4_d4258b18bc57row1_col0" class="data row1 col0" >652</td> 
        <td id="T_6e0a4aa4_3343_11e9_9ea4_d4258b18bc57row1_col1" class="data row1 col1" >$3.02</td> 
        <td id="T_6e0a4aa4_3343_11e9_9ea4_d4258b18bc57row1_col2" class="data row1 col2" >$1,967.64</td> 
        <td id="T_6e0a4aa4_3343_11e9_9ea4_d4258b18bc57row1_col3" class="data row1 col3" >$4.07</td> 
    </tr>    <tr> 
        <th id="T_6e0a4aa4_3343_11e9_9ea4_d4258b18bc57level0_row2" class="row_heading level0 row2" >Other / Non-Disclosed</th> 
        <td id="T_6e0a4aa4_3343_11e9_9ea4_d4258b18bc57row2_col0" class="data row2 col0" >15</td> 
        <td id="T_6e0a4aa4_3343_11e9_9ea4_d4258b18bc57row2_col1" class="data row2 col1" >$3.35</td> 
        <td id="T_6e0a4aa4_3343_11e9_9ea4_d4258b18bc57row2_col2" class="data row2 col2" >$50.19</td> 
        <td id="T_6e0a4aa4_3343_11e9_9ea4_d4258b18bc57row2_col3" class="data row2 col3" >$4.56</td> 
    </tr></tbody> 
</table> 



## Age Demographics

* Establish bins for ages


* Categorize the existing players using the age bins. Hint: use pd.cut()


* Calculate the numbers and percentages by age group


* Create a summary data frame to hold the results


* Optional: round the percentage column to two decimal points


* Display Age Demographics Table



```python
age_bins = [0, 9.90, 14.90, 19.90, 24.90, 29.90, 34.90, 39.90, 99999]
group_names = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]

purchase_data["Age Group"] = pd.cut(purchase_data["Age"],age_bins, labels=group_names)
purchase_data

age_grouped = purchase_data.groupby("Age Group")
age_count = age_grouped['SN'].nunique()
percentage_by_age = (age_count / total_players) * 100


age_demographics = pd.DataFrame({"Total Count": age_count, "Percentage of Players": percentage_by_age})
age_demographics.index.name = None
age_demographics.style.format({"Percentage of Players":"{:,.2f}"})

age_demographics
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Count</th>
      <th>Percentage of Players</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;10</th>
      <td>17</td>
      <td>2.951389</td>
    </tr>
    <tr>
      <th>10-14</th>
      <td>22</td>
      <td>3.819444</td>
    </tr>
    <tr>
      <th>15-19</th>
      <td>107</td>
      <td>18.576389</td>
    </tr>
    <tr>
      <th>20-24</th>
      <td>258</td>
      <td>44.791667</td>
    </tr>
    <tr>
      <th>25-29</th>
      <td>77</td>
      <td>13.368056</td>
    </tr>
    <tr>
      <th>30-34</th>
      <td>52</td>
      <td>9.027778</td>
    </tr>
    <tr>
      <th>35-39</th>
      <td>31</td>
      <td>5.381944</td>
    </tr>
    <tr>
      <th>40+</th>
      <td>12</td>
      <td>2.083333</td>
    </tr>
  </tbody>
</table>
</div>



## Purchasing Analysis (Age)

* Bin the purchase_data data frame by age


* Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below


* Create a summary data frame to hold the results


* Optional: give the displayed data cleaner formatting


* Display the summary data frame


```python
age_bins = [0, 9.90, 14.90, 19.90, 24.90, 29.90, 34.90, 39.90, 99999]
group_names = ["10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]

purchase_data["Age Group"] = pd.cut(purchase_data["Age"],age_bins, labels=group_names)

age_grouped = purchase_data.groupby("Age Group")
age_count = age_grouped['SN'].nunique()
percentage_by_age = (age_count / total_players) * 100


age_demographics = pd.DataFrame({
    "Purchase Count": percentage_by_age, 
    "Average Purchase Price": age_count,
    "Total Purchase Value": age_count,
    "Avg Total Purchase per Person": age_count
})

age_demographics.index.name = None
age_demographics.style.format({"Percentage of Players":"{:,.2f}"})

age_demographics
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
      <th>Avg Total Purchase per Person</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>10</th>
      <td>2.951389</td>
      <td>17</td>
      <td>17</td>
      <td>17</td>
    </tr>
    <tr>
      <th>10-14</th>
      <td>3.819444</td>
      <td>22</td>
      <td>22</td>
      <td>22</td>
    </tr>
    <tr>
      <th>15-19</th>
      <td>18.576389</td>
      <td>107</td>
      <td>107</td>
      <td>107</td>
    </tr>
    <tr>
      <th>20-24</th>
      <td>44.791667</td>
      <td>258</td>
      <td>258</td>
      <td>258</td>
    </tr>
    <tr>
      <th>25-29</th>
      <td>13.368056</td>
      <td>77</td>
      <td>77</td>
      <td>77</td>
    </tr>
    <tr>
      <th>30-34</th>
      <td>9.027778</td>
      <td>52</td>
      <td>52</td>
      <td>52</td>
    </tr>
    <tr>
      <th>35-39</th>
      <td>5.381944</td>
      <td>31</td>
      <td>31</td>
      <td>31</td>
    </tr>
    <tr>
      <th>40+</th>
      <td>2.083333</td>
      <td>12</td>
      <td>12</td>
      <td>12</td>
    </tr>
  </tbody>
</table>
</div>



## Top Spenders

* Run basic calculations to obtain the results in the table below


* Create a summary data frame to hold the results


* Sort the total purchase value column in descending order


* Optional: give the displayed data cleaner formatting


* Display a preview of the summary data frame




```python

```

## Most Popular Items

* Retrieve the Item ID, Item Name, and Item Price columns


* Group by Item ID and Item Name. Perform calculations to obtain purchase count, item price, and total purchase value


* Create a summary data frame to hold the results


* Sort the purchase count column in descending order


* Optional: give the displayed data cleaner formatting


* Display a preview of the summary data frame




```python

```

## Most Profitable Items

* Sort the above table by total purchase value in descending order


* Optional: give the displayed data cleaner formatting


* Display a preview of the data frame




```python

```
