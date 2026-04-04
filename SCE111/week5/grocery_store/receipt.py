import csv
from os import path

PRICE_INDEX = 2
PRODUCT_NAME_INDEX = 1

def main():
    products_dict = read_dictionary(path.join(path.dirname(__file__), "products.csv"), 0)
    subtotal = 0.0
    item_count = 0

    try:  
        with open(path.join(path.dirname(__file__), "request.csv"), "rt") as f:
            reader = csv.reader(f)
            next(reader)

            print("Valley Grocers")
            for product_id, quantity in reader:
                product = products_dict[product_id]
                subtotal += int(quantity) * float(product[PRICE_INDEX])
                item_count += int(quantity)
                print(f"{product[PRODUCT_NAME_INDEX]}: {quantity} @ ${product[PRICE_INDEX]} each")
            print(f"Subtotal: ${subtotal: .2f}")
            print(f"Tax: ${subtotal * .06: .2f}")
            print(f"Total: ${subtotal * 1.06: .2f}")
            print("Thank you for shopping with us today!")
    except FileNotFoundError as e:
        print(f"Given file not found: {e}")
    except PermissionError as e:
        print(f"Error accessing file: {e}")
    except KeyError as e:
        print(f"Product ID not found in products.csv: {e}")

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