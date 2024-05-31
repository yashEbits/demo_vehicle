import streamlit as st
import pandas as pd
import os

# Load the CSV file
file_path = 'number_plates.csv'  # Use relative path
df = pd.read_csv(file_path)

# Base directory where the images are stored
base_dir = 'run_20240531_123010'  # Current directory

# Define a function to construct image paths
def get_image_path(base_dir, id, img_type='frame'):
    return os.path.join(base_dir, f'{img_type}_{id}.jpg')

# Define a function to display data with images
def display_data_with_images(data):
    for index, row in data.iterrows():
        vehicle_image_path = get_image_path(base_dir, row['id'], 'frame')
        plate_image_path = get_image_path(base_dir, row['id'], 'plate')

        cols = st.columns(5)

        cols[0].write(f"Timestamp: {row['timestamp']}")
        cols[1].write(f"Number Plate: {row['number_plate']}")
        cols[3].image(vehicle_image_path, caption="Vehicle Image")
        cols[2].image(plate_image_path, caption="Plate Image")

# Streamlit app main function
def main():
    st.title("Number Plates Data")
    st.write("Below is the data from the CSV file with images:")

    display_data_with_images(df)

if __name__ == "__main__":
    main()
