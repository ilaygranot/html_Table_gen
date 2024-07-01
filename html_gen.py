import streamlit as st
import pandas as pd

# Set up the Streamlit app
st.title("HTML Table Generator")
st.write("Upload a CSV file or input data manually to generate an HTML table.")

# Display example CSV input
st.subheader("Example CSV Input")
example_data = {
    "Column1": ["Value1", "Value2", "Value3"],
    "Column2": ["ValueA", "ValueB", "ValueC"],
    "Column3": ["ValueX", "ValueY", "ValueZ"]
}
example_df = pd.DataFrame(example_data)
st.table(example_df)

# File upload
uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

# Manual input
manual_input = st.text_area("Or manually input data (comma-separated values, new line for each row)", "")

# Function to generate HTML from DataFrame
def generate_html(df):
    html_code = """
    <font size="4" face="Helvetica Neue">
    <head>
        <title>Generated Table</title>
        <style>
            caption {
                padding: 20px;
            }
            table, th, td {
                padding: 15px;
                border: 1px solid black; 
                border-collapse: collapse;
                font-family: "Helvetica Neue";
                font-weight: "45";
            }
        </style>
    </head>
    <body>
    <table width="100%">
        <caption>Generated Table</caption>
        <tr>
    """
    # Adding table headers
    for column in df.columns:
        html_code += f"<th>{column}</th>"
    html_code += "</tr>"

    # Adding table rows
    for _, row in df.iterrows():
        html_code += "<tr>"
        for cell in row:
            html_code += f"<td>{cell}</td>"
        html_code += "</tr>"
    html_code += """
        </table>
    </body>
    </html>
    """
    return html_code

# Initialize the DataFrame
df = None

# Process CSV file or manual input
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
elif manual_input:
    data = [row.split(",") for row in manual_input.split("\n") if row]
    if data:
        df = pd.DataFrame(data[1:], columns=data[0])  # Assuming first row as header

# Display data preview and HTML code if DataFrame is not None
if df is not None:
    st.write("Data Preview:")
    st.write(df)
    html_code = generate_html(df)
    st.write("Generated HTML Code:")
    st.code(html_code, language='html')
