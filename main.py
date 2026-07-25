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
    
    # Reads data from CSV
    # 
    # Takes a string as parameter which should be the file name
    # Opens the vile and converts raw csv data to a dict
    #
    # Returns a dict with batch as key and list with values
    #
    # This function will return a FileNotFoundError if unable to open the file
    # FileNotFoundError will be caught in main()


    data = {}
    with open(filename, 'r') as file:
        for line in file:
            try:
                batch, x, y, value = line.split(',')
                batch = batch.strip()
            except ValueError:
                print(f"Warning: wrong input format for entry: {format_csv_line(line)}")
                continue
            if batch not in data: 
                data[batch] = []
            data[batch].append((float(x), float(y), float(value)))
    return data


def check_is_within_unit_circle(x, y):
    """ 
    Check if a point is within the unit circle
    Takes x and y value as parameters
    Returns bool, True if value is withtin unit circle, False if not.
    Requirement for within unit circle, x**2 + y**2 <= 1
    """

    if x**2 + y**2 <= 1:
        return True
    else:
        return False
    

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
    average = total / count
    return average

def calc_all_averages(data):
    """
    Calculate the average per bath in a dataset

    Takes dict as input parameter with batch ID as key and list of (x, y, value) as values
    
    Returns dict with batch ID mapped to average value 
    """

    averages = {}
    for batch, data in data.items():
        averages[batch] = calc_batch_average(data)
    return averages

def print_batch_averages(averages):

    """
    Print the batch averages to user

    Takes a dict as parameter and prints each batch nr and average value for that batch

    """

    print("Batch\t | Average")
    
    for batch, average in averages.items():
        print(batch, "\t | ", average)

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

# Run program if executed directly. If this file gets imported, main will not execute
if __name__ == '__main__':
    main()