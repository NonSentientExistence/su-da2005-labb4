import matplotlib.pyplot as plt
import math

# Uppgift 1: Förbättringar i strukturen
# Refaktorerar om från en enda stor main funktion till flera mindre funktioner med tydligt syfte och "ansvarsområde" (Inläsning från CSV, beräkningar, utskrift)
# Beräkningsfunktionen skriver ej ut data utan returnerar bara resultatet när den anropas.

def format_csv_line(line):
    """
    Formats a CSV line to a single str for display in warning message
    
    Takes raw line from CSV as input

    Returns a single string of the values with a single space between values
    """

    return ' '.join(field.strip() for field in line.strip().split(','))

def read_csv(filename):
    """
    Reads data from CSV
    
    Takes a string as parameter which should be the file name
    Opens the vile and converts raw csv data to a dict
    
    Returns a dict with batch as key and list with values
    
    This function will return a FileNotFoundError if unable to open the file
    FileNotFoundError will be caught in main()
    """


    data = {}
    with open(filename, 'r') as file:
        for line in file:
            if not line.strip():
                continue
            try:
                batch, x, y, value = line.split(',')
                point = (float(x), float(y), float(value))
            except ValueError:
                print(f"Warning: wrong input format for entry: {format_csv_line(line)}")
                continue
            batch = batch.strip()
            if batch not in data:
                data[batch] = []
            data[batch].append(point)
    return data


def check_is_within_unit_circle(x, y):
    """ 
    Check if a point is within the unit circle
    Takes x and y value as parameters
    Returns bool, True if value is withtin unit circle, False if not.
    Requirement for within unit circle, x**2 + y**2 <= 1
    """

    return x**2 + y**2 <= 1
    

def calc_batch_average(data):
    """
    Calculate the avarage of input measurments within the unit circle

    Parameters required are a list with (x, y, value)

    Returns a float for each point that is within the unit circle (check_is_within_unit_circle is True)
    """

    total = 0
    count = 0
    for x, y, value in data:
        if check_is_within_unit_circle(x,y):
            total += value
            count += 1
    if count == 0:
        return None
    average = total / count
    return average

def calc_all_averages(data):
    """
    Calculate the average per bath in a dataset

    Takes dict as input parameter with batch ID as key and list of (x, y, value) as values
    
    Returns dict with batch ID mapped to average value 
    """

    averages = {}
    for batch, measurements in data.items():
        averages[batch] = calc_batch_average(measurements)
    return averages

def print_batch_averages(averages):

    """
    Print the batch averages to user

    Takes a dict as parameter and prints each batch nr and average value for that batch

    """

    for batch, average in averages.items():
        if average is None:
            print(f"Warning: Batch {batch} has no measurements inside the unit circle.")

    print("Batch\t | Average")
    
    for batch, average in sorted(averages.items()):
        if average is None: 
            continue
        print(batch, "\t | ", average)

def plot_data(data, output_filename):

    """
    Plots all measurements on top of the unit circle and saves and output_filename + .pdf-

    All measurements will be plotted, even if outside the unit circle. Each batch has a unique color code
    and each point will be labled with its value. 

    Takes dict as parameter and name of the output PDF. 
    Required input dict is the dict from read_csv before average calculations. 
    Passing None to the func will only draw the circle, for testing purposes. 
    """
    # Calculate 150 coordinates to draw the circle
    angles = [ n/150 * 2 * math.pi for n in range(151) ]
    x_coords = [ math.cos(a) for a in angles ]
    y_coords = [ math.sin(a) for a in angles ]
    # Draw the circle
    plt.plot(x_coords,y_coords)
    
    if data is not None:
        for measurements in data.values():
            batch_x = [x for x, y, value in measurements]
            batch_y = [y for x, y, value in measurements]
            # Calls plt.plot once per batch. plotlib will pick a color from deafult cycle automatically
            plotted_points = plt.plot(batch_x, batch_y, 'o')
            batch_color = plotted_points[0].get_color()
            for x, y, value in measurements:
                plt.annotate(str(value), (x, y), color=batch_color)

    plt.savefig(output_filename + ".pdf")

def main():
    """
    Run the program: Ask for filename, analyze data in file and print the results to user
    """
    filename = input("Which CSV would you like to analyze?\n")
    try: 
        data = read_csv(filename)
    except FileNotFoundError:
        print(f"File {filename} could not be found")
        return
    averages = calc_all_averages(data)
    print_batch_averages(averages)

    output_filename = filename.rsplit( ".", 1 )[ 0 ]
    plot_data(data, output_filename)
    print(f"A plot of the data can be found in {output_filename}.pdf.")

# Run program if executed directly. If this file gets imported, main will not execute
if __name__ == '__main__':
    main()