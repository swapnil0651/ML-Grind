import subprocess
import pandas as pd

# Run the 'top' command with the specified flags
result = subprocess.run(['top', '-b', '-n', '1'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Split the output by newlines
lines = result.stdout.splitlines()

# Find the line where the header starts (e.g., line that contains 'PID', 'USER', etc.)
header_line_index = None
for i, line in enumerate(lines):
    if "PID" in line and "USER" in line:  # Header usually contains 'PID' and 'USER'
        header_line_index = i
        break

if header_line_index is None:
    print("Header not found.")
else:
    # Get the header line and extract headers
    header_line = lines[header_line_index]
    headers = header_line.split()

    # Initialize a list to hold all process data
    data = []

    # Loop through the remaining lines starting from the header line to get values for each process
    for line in lines[header_line_index + 1:]:
        columns = line.split()
        if len(columns) == len(headers):  # Ensure the line has the same number of columns as headers
            data.append(columns)

    # Create a DataFrame using pandas
    df = pd.DataFrame(data, columns=headers)

    # Save the DataFrame to a CSV file
    df.to_csv('top_output.csv', index=False)

    print("CSV file 'top_output.csv' created successfully!")
