import pandas as pd
import streamlit as st

import streamlit as st

def main():
    st.title("Rent Price Predictor App")

    prediction_type = st.selectbox("Please choose your prediction type:", ["", "Room", "House"])

    if prediction_type == "Room":
        data = room_questions()
        if st.button('Predict for Room'):
            
            # result = your_model.predict(data)
            st.write(f"Predicted Rent Price for Room: ...")  

    elif prediction_type == "House":
        data = house_questions()
        if st.button('Predict for House'):
            
            # result = your_model.predict(data)
            st.write(f"Predicted Rent Price for House: ...") 

def room_questions():
    st.subheader("Questions for Room")

    is_suite = st.radio("Is it a suite?", ["Yes", "No"])
    if is_suite == "No":
        bathroom_share_count = st.slider("With how many people do you share the bathroom?", 1, 10)

    has_built_in_wardrobe = st.radio("Has built-in wardrobe?", ["Yes", "No"])
    if has_built_in_wardrobe == "No":
        has_movable_wardrobe = st.radio("Has movable wardrobe?", ["Yes", "No"])

    has_bed = st.radio("Has bed?", ["Yes", "No"])

    room_size = st.slider("What's the room size (in square meters)?", 5.0, 50.0)

    num_people_in_house = st.slider("How many people live in the house?", 1, 10)
    house_size = st.slider("What's the size of the house (in square meters)?", 20.0, 250.0)

    amenities = st.multiselect("What amenities does the house have?", 
                               ["Pool", "Dryer", "Washing Machine", "Dishwasher"])

    neighborhood = st.text_input("Which neighborhood is the room located?")

    nearby_places = st.multiselect("Which of these places are less than 1.5km away?",
                                   ["Supermarket", "Pharmacy", "Gym", "School", "Motorway"])

    
    data = {
        "is_suite": is_suite,
        "bathroom_share_count": bathroom_share_count if is_suite == "No" else None,
        "has_built_in_wardrobe": has_built_in_wardrobe,
        "has_movable_wardrobe": has_movable_wardrobe if has_built_in_wardrobe == "No" else None,
        "has_bed": has_bed,
        "room_size": room_size,
        "num_people_in_house": num_people_in_house,
        "house_size": house_size,
        "amenities": amenities,
        "neighborhood": neighborhood,
        "nearby_places": nearby_places
    }

    return data

def house_questions():
    st.subheader("Questions for House")

    num_rooms = st.slider("How many rooms does the house have?", 1, 10)
    
    num_bathrooms = st.slider("How many bathrooms does the house have?", 1, 5)

    has_garage = st.radio("Has a garage?", ["Yes", "No"])
    if has_garage == "Yes":
        garage_size = st.slider("Size of the garage (in square meters)?", 10.0, 100.0)

    house_size = st.slider("What's the house size (in square meters)?", 20.0, 500.0)

    garden_size = st.slider("What's the garden size (in square meters)?", 0.0, 500.0)

    amenities = st.multiselect("What amenities does the house have?", 
                               ["Pool", "Dryer", "Washing Machine", "Dishwasher", "Air Conditioning", "Fireplace"])

    neighborhood = st.text_input("Which neighborhood is the house located?")

    nearby_places = st.multiselect("Which of these places are less than 1.5km away?",
                                   ["Supermarket", "Pharmacy", "Gym", "School", "Motorway"])

    data = {
        "num_rooms": num_rooms,
        "num_bathrooms": num_bathrooms,
        "has_garage": has_garage,
        "garage_size": garage_size if has_garage == "Yes" else None,
        "house_size": house_size,
        "garden_size": garden_size,
        "amenities": amenities,
        "neighborhood": neighborhood,
        "nearby_places": nearby_places
    }

    return data


if __name__ == "__main__":
    main()
