# About the project

Preparing real data gotten from a tourist agency to predict price of an apartment based on given features. Data was given in multiple csv tables.

csv files: property, property_unit, facilities, prices

## data.py , facility_value.py

In these scripts I analyzed the data to get insight in different values from facility csv. which had 125 unique values.

for example :

0                                 on
1                         no-heating
2              deposit-is-obligatory
3            final-cleaning-in-price
4                           yes-free
                   ...              
120        card_payment_not_accepted
121             int-con-public-areas
122          int-con-business-centre
123                  entire_property
124    after_cancellation_fee_begins
Length: 125, dtype: object


Each value was given a numeric value.


on                               1

no-heating                      -1

deposit-is-obligatory           -1

final-cleaning-in-price          1

yes-free                         1

                                ..
                                
card_payment_not_accepted       -1

int-con-public-areas             1

int-con-business-centre          1

entire_property                  1

after_cancellation_fee_begins    0


## p_units_analysis.py

Here I had to connect and analyse price relative to units, drop unactive units so we can analyse only relevant data

## unit_columns.py, unit_distance.py

In these scripts I added values from facility csv to units. Distance script retrieves float values from facility csv which were not edited as string values from former case.


id_property	id	category	area	floor	beds_basic	beds_additional	garden	twin_bed	unit_wardrobe_closet	...	mosquito_net	paying_amex	paying_master	paying_visa																					


## eda2.py, eda_cjenik.py

Exploratory data analysis on facilities and prices of apartments.

## model2.py

DNN modeled in Keras with input layer of 12




















