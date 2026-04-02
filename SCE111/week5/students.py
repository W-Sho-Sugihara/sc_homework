import csv

ID_LENGTH = 9

def main():
    students = store_students()
    while True:
        search_id = input("Input search student ID: ").replace("-", "")
        if len(search_id) < ID_LENGTH:
            print("Entered ID is too short.")
        elif len(search_id) > ID_LENGTH:
            print("Entered ID is too long.")
        elif len(search_id) != len(''.join(filter(str.isdigit, search_id))):
            print("Invalid ID. ID cannot include non-integer values")
        else: break
       
    try:
        student_name = students[search_id]
    except KeyError as e:
       print(f"ID not found. {e}")
    else:
       print(f"Student name for ID# {search_id} is {student_name}.")

def store_students():
    with open("students.csv", "rt") as student_file:
       reader = csv.reader(student_file)
       next(reader)
       students = {}

       for id, name in reader:
          students[id] = name
    print(students)
    return students


if __name__ == "__main__":
  main()