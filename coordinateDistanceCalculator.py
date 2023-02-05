import streamlit as st
import math

def haversine_distance(lat1, long1, lat2, long2):
    R = 6371  # earth's radius in kilometers
    
    lat1, long1, lat2, long2 = map(math.radians, [lat1, long1, lat2, long2])
    
    dlat = lat2 - lat1
    dlong = long2 - long1
    
    a = (math.sin(dlat / 2) ** 2) + (math.cos(lat1) * math.cos(lat2) * (math.sin(dlong / 2) ** 2))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    
    return distance

def main():
    st.title("Distance Between Two Coordinates")
    
    lat1 = st.number_input("Enter Latitude 1", step=0.01, value=0.0)
    long1 = st.number_input("Enter Longitude 1", step=0.01, value=0.0)
    lat2 = st.number_input("Enter Latitude 2", step=0.01, value=0.0)
    long2 = st.number_input("Enter Longitude 2", step=0.01, value=0.0)
    
    if st.button("Calculate Distance"):
        result = haversine_distance(lat1, long1, lat2, long2)
        st.write("Distance: ", result, "kilometers")

if __name__ == '__main__':
    main()
