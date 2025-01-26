import time

import numpy as np
import streamlit as st

# Display the Streamlit version
st.write("streamlit version = {}".format(st.__version__))

# Initialize the progress bar and status text in the sidebar
progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()

# Generate initial random data for the chart
last_rows = np.random.randn(1, 1)
chart = st.line_chart(last_rows)

# Update the chart with new data in a loop
for i in range(1, 101):
    # Generate new random data
    new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
    # Update the status text and progress bar
    status_text.text("%i%% Complete" % i)
    progress_bar.progress(i)
    # Add new data to the chart
    chart.add_rows(new_rows)
    last_rows = new_rows
    
    # Pause for a short time before the next update
    time.sleep(0.500)
    
# Clear the progress bar after completion
progress_bar.empty()

# Add a button to re-run the script
st.button('Re-run')











