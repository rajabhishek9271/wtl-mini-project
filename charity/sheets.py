import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("charity/creds.json", scope)

client = gspread.authorize(creds)

sheet = client.openall()[0]


def Volunteer(name, email, gender, contact, occupation, city, zipcode, reason):
    my_sheet = sheet.worksheets()[0]
    # sheet = client.open("Travancore").sheet2
    data = my_sheet.get_all_records()
    insertRow = [name, email, gender, contact, occupation, city, zipcode, reason]
    my_sheet.insert_row(insertRow, len(data)+2)
