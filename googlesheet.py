import os.path
from googleapiclient.discovery import build
from google.oauth2 import service_account


SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SERVICE_ACCOUNT_FILE = os.path.join(BASE_DIR, 'credentials.json')  # You must create credentials.json in your account

credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1EobMhDZ4MAeqLu1Te6PGczbwELz_E8HMxS_KndWFyC4'
SAMPLE_RANGE_NAME_TYPES = 'Ответы на форму!H2:H'
SAMPLE_RANGE_NAME_CONTACTS = 'Ответы на форму!L2:L'
service = build('sheets', 'v4', credentials=credentials)

sheet = service.spreadsheets()
result_types = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME_TYPES).execute()
result_contacts = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME_CONTACTS).execute()



def get_users_list(result_types, result_contacts):
    pre_contacts_list = []
    pre_types_list = []
    for key, value in result_contacts.items():
        pre_contacts_list.append(value)
    pre_contacts_list = pre_contacts_list[2:][0]

    contacts_list= []
    for item in pre_contacts_list:
        contacts_list.append(''.join(item))

    for key, value in result_types.items():
        pre_types_list.append(value)
    pre_types_list = pre_types_list[2:][0]

    types_list= []
    for item in pre_types_list:
        types_list.append(''.join(item))
    users_list = dict(zip(types_list, contacts_list))
    return users_list


USERS_DICT = get_users_list(result_types, result_contacts)