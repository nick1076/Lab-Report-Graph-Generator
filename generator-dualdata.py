import pandas as pd
import matplotlib.pyplot as plt

# Function to read data from a CSV and create a plot
def plot_lab_data(csv_file, csv2_file, x_column, y_column, plot_title, x_label, y_label):
    # Read the CSV file into a pandas DataFrame
    data = pd.read_csv(csv_file)
    data2 = pd.read_csv(csv2_file)

    # Plot the data
    plt.figure(figsize=(8, 6))  # Set the size of the plot
    plt.plot(data[x_column], data[y_column] * 1000, marker='o', linestyle='-', color='b')
    plt.plot(data2[x_column], data2[y_column]*1000, marker='o', linestyle='-', color='r')

    # Add labels and title
    plt.title(plot_title, fontsize=14)
    plt.xlabel(x_label, fontsize=12)
    plt.ylabel(y_label, fontsize=12)

    # Show grid for better visualization
    plt.grid(True)

    # Show the plot
    plt.tight_layout()  # Adjust layout to fit everything nicely
    plt.show()

# Example usage:
csv_file = 'data.csv'  # Path to your CSV file
csv2_file = 'data.csv'  # Path to your CSV file
x_column = 'CH1 Voltage'  # The column you want on the X-axis
y_column = 'CH1 Current'  # The column you want on the Y-axis
plot_title = 'Voltage vs Time'
x_label = 'Voltage (V)'
y_label = 'Current (mA)'

print("-- Python Lab Report Graph Generator --")
print("")
print("Place your CSV in this programs folder...")
print("")
csv_file = input("Type in your CSV's filename here: ")
print("")
csv2_file = input("Type in your 2nd CSV's filename here: ")
print("")
print("Ok... generating.")
print("")
csv_file+=".csv"
csv2_file+=".csv"

# Call the function to create and display the plot
plot_lab_data(csv_file, csv2_file, x_column, y_column, plot_title, x_label, y_label)
