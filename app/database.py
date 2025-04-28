import mysql.connector

# Database connection setup
def get_db_connection():
    connection = mysql.connector.connect(
        host="localhost",          # Replace with your MySQL host if running on another server
        user="root",               # Replace with your MySQL username
        password="your_password",  # Replace with your MySQL password
        database="certificate_generator"
    )
    return connection

# Create a function to save participant details
def save_participant(name, email, event):
    connection = get_db_connection()
    cursor = connection.cursor()

    # Insert participant data
    query = '''
        INSERT INTO participants (name, email, event)
        VALUES (%s, %s, %s)
    '''
    cursor.execute(query, (name, email, event))
    connection.commit()
    connection.close()

# Create a function to retrieve all participants
def get_all_participants():
    connection = get_db_connection()
    cursor = connection.cursor()

    # Fetch all participants
    query = 'SELECT * FROM participants'
    cursor.execute(query)
    rows = cursor.fetchall()
    connection.close()

    return rows

import csv

def export_to_csv(file_path):
    participants = get_all_participants()  # Fetch all participants

    # Write data to a CSV file
    with open(file_path, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['ID', 'Name', 'Email', 'Event', 'Generated At'])  # Header row
        csvwriter.writerows(participants)  # Data rows
        
        
def import_from_csv(file_path):
    connection = get_db_connection()
    cursor = connection.cursor()

    # Read data from a CSV file
    with open(file_path, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)  # Skip the header row
        for row in csvreader:
            query = '''
                INSERT INTO participants (id, name, email, event, generated_at)
                VALUES (%s, %s, %s, %s, %s)
            '''
            cursor.execute(query, row)

    connection.commit()
    connection.close()
    