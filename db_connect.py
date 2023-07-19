import psycopg2
import csv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# PostgreSQL database connection settings (replace placeholders with actual connection details)
db_settings = {
    "dbname": "your_db_name",
    "user": "your_db_user",
    "password": "your_db_password",
    "host": "your_db_host",
    "port": "your_db_port"
}

# Function to fetch table data from PostgreSQL and export to a CSV file
def export_table_to_csv(table_name, file_path):
    try:
        # Connect to the PostgreSQL database
        connection = psycopg2.connect(**db_settings)

        # Create a cursor to execute SQL queries
        cursor = connection.cursor()

        # Fetch data from the table
        cursor.execute(f"SELECT * FROM {table_name}")
        data = cursor.fetchall()

        # Export data to a CSV file
        with open(file_path, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow([desc[0] for desc in cursor.description])  # Write header row
            csv_writer.writerows(data)  # Write data rows

        # Close the cursor and database connection
        cursor.close()
        connection.close()
        
        print(f"Data exported to {file_path} successfully.")
    except Exception as e:
        print(f"Error: {e}")

# Function to send an email with the CSV file attached
def send_email_with_attachment(file_path, recipient_email, sender_email, sender_password, subject, body):
    try:
        # Set up the email message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject

        # Attach the CSV file
        attachment = open(file_path, 'rb')
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= " + file_path.split('/')[-1])
        msg.attach(part)

        # Add email body
        msg.attach(MIMEText(body, 'plain'))

        # Set up the SMTP server and send the email
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
        server.quit()

        print("Email sent successfully.")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    table_name = "your_table_name"  # Replace with the name of your table
    csv_file_path = "output.csv"    # Replace with the desired CSV file path

    export_table_to_csv(table_name, csv_file_path)

    recipient_email = "recipient@example.com"  # Replace with the recipient's email address
    sender_email = "sender@gmail.com"         # Replace with your email address
    sender_password = "your_email_password"   # Replace with your email password
    subject = "CSV File from PostgreSQL Database"
    body = "Please find the attached CSV file containing data from the PostgreSQL database."

    send_email_with_attachment(csv_file_path, recipient_email, sender_email, sender_password, subject, body)
