import csv

def classify_statements(input_file):
    while True:
        user_id = input("Please enter your user ID or type 'EXIT' to quit: ").strip()

        # User quit the program.
        if user_id.upper() == 'EXIT':
            print('Closing the program...')
            return

        # Read the input csv file.
        with open(input_file, mode='r', encoding='utf-8', newline='') as file:
            reader = csv.reader(file)
            headers = next(reader)
            rows = [row for row in reader]

        # Determine if the user id has already existed.
        user_column_header = f'user_{user_id}'
        if user_column_header in headers:
            print(f"User {user_id} has already made an attempt!")
            continue
        else:
            headers.append(user_column_header)
            break

    user_responses = []

    for row in rows:
        # Extract the first two columns for file_name and statement
        file_name, statement = row[:2]
        print("------------------------------------------------")
        print(f"File Name: {file_name}\nStatement: {statement}")
        response = input("Is this an environmental statement? (0: No, 1: Yes, 2: Uncertain): ").strip()
        # In case user didn't read the prompt 🤦‍♂️
        while response not in ['0', '1', '2']:
            print("[WARNING] Invalid input. Please ONLY choose from '0', '1', or '2'.")
            response = input("Classify the statement (0: Not Environment, 1: Environment, 2: Uncertain): ").strip()
        user_responses.append(response)

    for i, row in enumerate(rows):
        while len(row) < len(headers):
            row.append('')
        col = headers.index(user_column_header)
        row[col] = user_responses[i]

    # Write the user response to the csv file
    with open(input_file, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(rows)

    print("------------------The End------------------")
    print("---------------Thank you!------------------")

# Test
input_csv = 'annotation_01.csv'

classify_statements(input_csv)