from tabulate import tabulate
range_value = -1
while range_value < 0:
    range_value=int(input("Podaj zakres liczb dla których wykonać mnożenie \n"))
    if range_value <0:
        print ("Zakres liczb nie może być wartością ujemną. \n")

def generate_multi_table(n):  # Initialize the empty table

    table = [["-"] + [str(i) for i in range(n + 1)]] #headers
    for i in range(n + 1):
        row = [str(i)]
        for j in range(n + 1):
            row.append(str(i * j))
        table.append(row)

    return table

# Generate the table
multi_table = generate_multi_table(range_value)

# Display
print(tabulate(multi_table, headers="firstrow", tablefmt="grid"))
