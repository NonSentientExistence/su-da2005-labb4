# Uppgift 1: Förbättringar i strukturen
# Refaktorerar om från en enda stor main funktion till tre mindre funktioner med tydligt syfta och "ansvarsområde" (Inläsning från CSV, beräkningar, utskrift)
# Beräkningsfunktionen skriver ej ut data utan returnerar bara resultatet.

def read_csv(filename):
    
    # Read data from CSV
    # Returns a dict with batch as key and list with values

    data = {}
    with open(filename, 'r') as file:
        for line in file:
            batch, x, y, value = line.split(',')
            batch = batch.strip()

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

def print_batch_averages(data):

    """
    Print the batch averages to user

    Takes a dict as parameter and prints each batch nr and average value for that batch

    """

    print("Batch\t | Average")
    
    for batch, average in average.items():
        print(batch, "\t | ", average)

def main():
    """
    Run the program: Ask for filename, analyze data in file and print the results to user
    """
    filename = input("Which CSV would you like to analyze?")
    data = read_csv(filename)
    averages = 