'''
Solution unibrow.py
'''
import pandas as pd
import streamlit as st
import pandaslib as pl

st.title("UniBrow")
st.caption("The Universal data browser")

file = st.file_uploader("Upload a file", type=["csv", "xlsx", "json"])

if file is not None:
    # Determine file extension
    file_extension = file.name.split('.')[-1]

    # Step 2: Load the file based on the extension
    try:
        df = pl.load_file(file, file_extension)
        
        # Step 3: Display column names and let user choose columns to display
        columns = pl.get_column_names(df)
        selected_columns = st.multiselect("Select columns to display", columns, default=columns)
        
        # Filter the DataFrame based on selected columns
        filtered_df = df[selected_columns]
        
        # Step 4: Text filter for specific columns
        filter_enabled = st.checkbox("Enable text filter")
        
        if filter_enabled:
            column_name = st.selectbox("Select column to filter", columns)
            unique_values = pl.get_unique_values(df, column_name)
            selected_value = st.selectbox("Select value to filter by", unique_values)
            
            # Apply the filter
            filtered_df = filtered_df[filtered_df[column_name] == selected_value]
        
        # Step 5: Display the filtered DataFrame
        st.write("Filtered DataFrame:")
        st.dataframe(filtered_df)
        
        # Step 6: Display DataFrame statistics
        st.write("Dataframe Statistics:")
        st.write(filtered_df.describe())
    
    except Exception as e:
        st.error(f"Error: {str(e)}")

