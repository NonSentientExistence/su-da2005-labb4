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
