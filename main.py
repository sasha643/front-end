import streamlit as st
import requests

# Streamlit app title
st.title("Scraping API Frontend")

# Button to trigger API call
if st.button("Fetch Reviews"):
        with st.spinner("Fetching data from API..."):
            try:
                # API endpoint
                api_endpoint = f"https://scraping-298313983231.asia-south1.run.app/api/reviews?url=https://2717recovery.com/products/recovery-cream"

                # Make GET request to the backend API
                response = requests.get(api_endpoint)

                # Check the response status
                if response.status_code == 200:
                    data = response.json()  # Parse JSON response
                    st.success("Data fetched successfully!")

                    # Display the data as JSON
                    st.subheader("Response Data:")
                    st.json(data)
                else:
                    st.error(f"Error {response.status_code}: {response.text}")
            except Exception as e:
                st.error(f"An error occurred: {e}")
