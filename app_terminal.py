import streamlit as st
import os
from joblib import load
import pandas as pd
import sklearn
import numpy as np
import graphs  

SUBURBS = [ "Auckland", "Avondale", "Blockhouse Bay", "Eden Terrace", "Ellerslie", 
        "Epsom", "Freemans Bay", "Glen Innes", "Glendowie", "Grafton", "Greenlane", 
        "Grey Lynn", "Herne Bay", "Hillsborough", "Kingsland", "Kohimarama", 
        "Meadowbank", "Mission Bay", "Morningside", "Mount Albert", "Mount Eden", 
        "Mount Roskill", "Mount Wellington", "New Windsor", "Newmarket", "One Tree Hill", 
        "Onehunga", "Otahuhu", "Parnell", "Point Chevalier", "Point England", 
        "Ponsonby", "Remuera", "Royal Oak", "Saint Heliers", "Saint Johns", 
        "Saint Marys Bay", "Sandringham", "St Heliers", "Stonefields", "Three Kings", 
        "Waiotaiki Bay", "Waterview", "Westmere"
    ]

AREAS = {'Central Auckland': [],
         'Central Auckland East': [],
         'Central Auckland West': [],
         'Eastern Suburbs': [],
         'Franklin/Manukau Rural': [],
         'North Shore': [],
         'Northland': [],
         'Pakuranga/Howick': [],
         'Rodney': [],
         'South Auckland': [],
         'West Auckland': ["Avondale","Ponsonby",],
         }

for suburb in SUBURBS:
    if suburb in ["Auckland", "Eden Terrace", "Freemans Bay", "Grafton", "Newmarket", "Parnell", "Ponsonby", "Remuera"]:
        AREAS['Central Auckland'].append(suburb)
    elif suburb in ["Ellerslie", "Greenlane", "One Tree Hill", "Onehunga"]:
        AREAS['Central Auckland East'].append(suburb)
    elif suburb in ["Avondale", "Blockhouse Bay", "Mount Albert", "Mount Roskill", "New Windsor"]:
        AREAS['Central Auckland West'].append(suburb)
    elif suburb in ["Kingsland", "Morningside", "Sandringham", "Waterview"]:
        AREAS['Central Auckland West'].append(suburb)
    elif suburb in ["Epsom", "Greenlane"]:
        AREAS['Central Auckland'].append(suburb)
    elif suburb in ["Freemans Bay", "Herne Bay", "Saint Marys Bay", "St Heliers"]:
        AREAS['Central Auckland'].append(suburb)
    elif suburb in ["Meadowbank", "Mission Bay", "Kohimarama"]:
        AREAS['Central Auckland East'].append(suburb)
    elif suburb in ["Saint Heliers", "Glendowie"]:
        AREAS['Central Auckland East'].append(suburb)
    elif suburb in ["Glen Innes", "Kohimarama", "Meadowbank", "Mission Bay", "Orakei"]:
        AREAS['Central Auckland East'].append(suburb)
    elif suburb in ["Mount Eden", "Three Kings"]:
        AREAS['Central Auckland West'].append(suburb)
    elif suburb in ["Grey Lynn", "Point Chevalier"]:
        AREAS['Central Auckland West'].append(suburb)
    elif suburb in ["Hillsborough", "Lynfield", "Mount Roskill"]:
        AREAS['Central Auckland West'].append(suburb)
    elif suburb in ["Westmere"]:
        AREAS['Central Auckland West'].append(suburb)
    elif suburb in ["Mangere", "Mangere East", "Otahuhu"]:
        AREAS['South Auckland'].append(suburb)
    elif suburb in ["Manurewa", "Manurewa East"]:
        AREAS['South Auckland'].append(suburb)
    elif suburb in ["Pakuranga", "Botany Downs", "Cockle Bay", "Farm Cove", "Half Moon Bay", "Highland Park", "Shelly Park"]:
        AREAS['Pakuranga/Howick'].append(suburb)
    elif suburb in ["East Tamaki", "East Tamaki Heights"]:
        AREAS['Pakuranga/Howick'].append(suburb)
    elif suburb in ["Flat Bush"]:
        AREAS['Pakuranga/Howick'].append(suburb)
    elif suburb in ["Alfriston", "Randwick Park"]:
        AREAS['South Auckland'].append(suburb)
    elif suburb in ["Clendon Park"]:
        AREAS['South Auckland'].append(suburb)
    elif suburb in ["Hill Park", "The Gardens"]:
        AREAS['South Auckland'].append(suburb)
    elif suburb in ["Manukau", "Weymouth"]:
        AREAS['South Auckland'].append(suburb)
    elif suburb in ["Dannemora", "Shelly Park"]:
        AREAS['Pakuranga/Howick'].append(suburb)
    elif suburb in ["Bucklands Beach", "Eastern Beach"]:
        AREAS['Pakuranga/Howick'].append(suburb)
    elif suburb in ["Cockle Bay"]:
        AREAS['Pakuranga/Howick'].append(suburb)
    elif suburb in ["Half Moon Bay"]:
        AREAS['Pakuranga/Howick'].append(suburb)
    elif suburb in ["Howick"]:
        AREAS['Pakuranga/Howick'].append(suburb)
    elif suburb in ["Burswood", "East Tamaki"]:
        AREAS['Pakuranga/Howick'].append(suburb)
    elif suburb in ["Northpark"]:
        AREAS['Pakuranga/Howick'].append(suburb)
    elif suburb in ["Botany Downs"]:
        AREAS['Pakuranga/Howick'].append(suburb)
    elif suburb in ["Huntington Park"]:
        AREAS['Pakuranga/Howick'].append(suburb)
    elif suburb in ["Chapel Downs"]:
        AREAS['Pakuranga/Howick'].append(suburb)
    elif suburb in ["Highland Park"]:
        AREAS['Pakuranga/Howick'].append(suburb)
    elif suburb in ["Dannemora"]:
        AREAS['Pakuranga/Howick'].append(suburb)
    elif suburb in ["Farm Cove"]:
        AREAS['Pakuranga/Howick'].append(suburb)
    elif suburb in ["Mellons Bay"]:
        AREAS['Pakuranga/Howick'].append(suburb)
    elif suburb in ["Shelly Park"]:
        AREAS['Pakuranga/Howick'].append(suburb)
    elif suburb in ["Whitford"]:
        AREAS['Pakuranga/Howick'].append(suburb)
    elif suburb in ["Glen Papatoetoe"]:
        AREAS['South Auckland'].append(suburb)
    elif suburb in ["Opaheke"]:
        AREAS['Franklin/Manukau Rural'].append(suburb)
    elif suburb in ["Papakura"]:
        AREAS['Franklin/Manukau Rural'].append(suburb)
    elif suburb in ["Rosehill"]:
        AREAS['Franklin/Manukau Rural'].append(suburb)
    elif suburb in ["Takanini"]:
        AREAS['Franklin/Manukau Rural'].append(suburb)
    elif suburb in ["Golflands"]:
        AREAS['Franklin/Manukau Rural'].append(suburb)
    elif suburb in ["Conifer Grove"]:
        AREAS['Franklin/Manukau Rural'].append(suburb)
    elif suburb in ["Papatoetoe"]:
        AREAS['South Auckland'].append(suburb)
    elif suburb in ["Hillcrest"]:
        AREAS['North Shore'].append(suburb)
    elif suburb in ["Northcote"]:
        AREAS['North Shore'].append(suburb)
    elif suburb in ["Sunnynook"]:
        AREAS['North Shore'].append(suburb)
    elif suburb in ["Takapuna"]:
        AREAS['North Shore'].append(suburb)
    elif suburb in ["Hauraki"]:
        AREAS['North Shore'].append(suburb)
    elif suburb in ["Milford"]:
        AREAS['North Shore'].append(suburb)
    elif suburb in ["Castor Bay", "Forrest Hill"]:
        AREAS['North Shore'].append(suburb)

for area, suburbs in AREAS.items():
    print(f'{area}: {suburbs}')

model = load('models/RandomForest.joblib')
scaler_features = load('models/scaler_features.joblib')
target_features = load('models/scaler_target.joblib')

def predict_price(data):

    prediction_data = {
        "Suburb": 0,
        "Bedroom": 0,
        "Bathroom": 0,
        "Garage": 0,
        "Furniture": 0,
        "Type_Apartment": 0,
        "Type_House": 0,
        "Type_Studio": 0,
        "Type_Townhouse": 0,
        "Type_Unit": 0,
    }

    # create and array populate the type with iether 0 or 1
    property_type = ["Apartment", "House", "Studio", "Townhouse", "Unit"]
    col_name = ["Type_Apartment","Type_House","Type_Studio","Type_Townhouse","Type_Unit"]

    property_type_bin = [0,0,0,0,0]
    for i in range(len(property_type)):
        if data['property_type'] == property_type[i]:
            property_type_bin[i] = 1
        prediction_data[col_name[i]] = property_type_bin[i]

    #find suburb index, matches to how we encode suburbs in the model.
    for i in range(len(SUBURBS)):
        if data['suburb'] == SUBURBS[i]:
            prediction_data['Suburb'] = i

    prediction_data['Bedroom'] = data['num_bedrooms']
    prediction_data['Bathroom'] = data['num_bathrooms']
    prediction_data['Garage'] = data['num_garage_spaces']
    prediction_data['Furniture'] = data['is_furnished']
    
    #normalize the input data using the scaler from training
    prediction_data = pd.DataFrame(prediction_data, index=[0])
    normalized_data_array = scaler_features.transform(prediction_data)
    normalized_data = pd.DataFrame(normalized_data_array, columns=prediction_data.columns)
    
    # make prediction ond un-normalize the data
    prediction = model.predict(normalized_data)
    prediction = prediction.reshape(-1, 1)
    prediction = target_features.inverse_transform(prediction)
    prediction = prediction.flatten()
    
    return prediction[0]

def get_stats(suburb, beds):
    avgsale = 0
    avgrent = 0

    df = pd.read_csv("data/area_data.csv")

    avg_sale_df = df[df['Focus Area'].str.contains('average_sale_price')]
    avg_rent_df = df[df['Focus Area'].str.contains('average_weekly_rent')]

    for index, row in avg_sale_df.iterrows():
        area = row['Focus Area'].replace("_average_sale_price", "") 
        if suburb in AREAS[area]:
            avgsale = row[str(beds)]

    for index, row in avg_rent_df.iterrows():
        area = row['Focus Area'].replace("_average_weekly_rent", "") 
        if suburb in AREAS[area]:
            avgrent = row[str(beds)]


    return [avgsale, avgrent]


def main():
    st.title("Rent Price Predictor App")
    st.write("### View Suburb stats")

    plot_data = st.selectbox('Select metric', ["",'Average sale price', 'Average weekly rent'])
    graph_type = st.selectbox('Graph type', ['line', 'bar'])

    # function to diplay some usefull statistics
    if st.button('See Suburb stats'):
        graphs.display_graphs_page(plot_data, graph_type)

    st.write("### Property Details")
    # Select suburb from the list
    suburb = st.selectbox("Select the suburb:", [""] + SUBURBS)

    # Select property type
    property_type = st.selectbox("Select property type:", ["", "House", "Townhouse", "Unit", "Apartment","Studio", "Unknown"])

    # Number of rooms
    # num_rooms = st.slider("How many rooms?", 1, 10)

    # Number of bedrooms
    num_bedrooms = st.slider("How many bedrooms?", 1, 10)
    num_bathrooms = st.slider("How many bathrooms?", 1, 10)

    # Number of garage spaces
    num_garage_spaces = st.slider("How many garage spaces?", 0, 10)

    # Furnishing details
    is_furnished = st.radio("Is the property furnished?", ["Yes", "No"])
    is_furnished_binary = 1 if is_furnished == "Yes" else 0

    # Property price
    price_str = st.text_input("Enter the price:")
    try:
        price = float(price_str)
    except ValueError:
        st.write("Please enter a valid number.")
        price = None

    predicted_price = 0
    if st.button("Predict") and price:
        data = {
            "suburb": suburb,
            "property_type": property_type,
            # "num_rooms": num_rooms,
            "num_bedrooms": num_bedrooms,
            "num_bathrooms": num_bathrooms,
            "num_garage_spaces": num_garage_spaces,
            "is_furnished": is_furnished_binary
        }
        
    
        predicted_price = predict_price(data)
        st.write(f"Predicted Price: ${predicted_price:.2f}")
        
        
        if price > predicted_price:
            st.write("The property is priced higher than the predicted price.")
        elif abs(price - predicted_price) <= 70:  # we can change
            st.write("The property is priced close to the predicted price.")
        else:
            st.write("The property is priced lower than the predicted price.")

        #diplay some general stats
        stats = get_stats(data['suburb'], data['num_bedrooms'])
        print(stats)
        st.write(f"Avegerage sale price in this area: {stats[0]}")
        st.write(f"Avegerage weekly rent in this area: {stats[1]}")

        #data to display some graph

    
    if st.button("Restart"):
        os.system('killall streamlit')
        os.system('streamlit run your_app_name.py')

if __name__ == "__main__":
    main()

