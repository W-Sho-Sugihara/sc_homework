import csv
from os import path

def main():
    products_dict = read_dictionary(path.join(path.dirname(__file__), "products.csv"), 0)

    try:  
        with open(path.join(path.dirname(__file__), "request.csv"), "rt") as f:
            reader = csv.reader(f)
            next(reader)
            print("Requested Items:")
            for product_id, quantity in reader:
                product = products_dict[product_id]
                print(f"{product[1]}: {quantity} @ ${product[2]} each")
    except FileNotFoundError as e:
        print(f"Given file not found: {e}")
    except PermissionError as e:
        print(f"Error accessing file: {e}")

def read_dictionary(file_name, key_column_index):
    results = {}
    try:  
        with open(file_name, "rt") as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                results[row[key_column_index]] = row
    except FileNotFoundError as e:
        print(f"Given file not found: {e}")
    except PermissionError as e:
        print(f"Error accessing file: {e}")
    return results

if __name__ == "__main__":
  main()