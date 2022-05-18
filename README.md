# About the project

Preparing real data gotten from a tourist agency to predict price of an apartment based on given features. Data was given in multiple csv tables.

csv files: property, property_unit, facilities, prices

## data.py , facility_value.py

In these scripts I analyzed the data to get insight in different values from facility csv. which had 125 unique values.

for example :

                                on
                         no-heating
             deposit-is-obligatory
            final-cleaning-in-price
                          yes-free
             
        card_payment_not_accepted
             int-con-public-areas
          int-con-business-centre
                  entire_property
    after_cancellation_fee_begins



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

DNN modeled in Keras with input layer of 247 nodes which is the number of input features, one hidden dense layer with 128 nodes and relu activation function, and last output layer with one node. I used  Adam optimizer and learning rate of 0,003, metrics used are mean squared error. Batch size is 16 and training has 150 epochs.

mean squared error is 10 %


	pred	test	diff
	71.311707	70.00	-1.311707
	61.472240	59.00	-2.472240
	48.984123	45.00	-3.984123
	68.911026	54.64	-14.271026
	116.381119	110.00	-6.381119

	69.428879	77.00	7.571121
	106.956787	115.00	8.043213
	88.990173	53.00	-35.990173
	51.296207	55.00	3.703793
	74.544083	83.00	8.455917




















