# from __future__ import print_function
# import pickle
# import os.path
# from googleapiclient.discovery import build
# from google_auth_oauthlib.flow import InstalledAppFlow
# from google.auth.transport.requests import Request
#
# # If modifying these scopes, delete the file token.pickle.
# SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
#
# def main():
#     """Shows basic usage of the Gmail API.
#     Lists the user's Gmail labels.
#     """
#     creds = None
#     # The file token.pickle stores the user's access and refresh tokens, and is
#     # created automatically when the authorization flow completes for the first
#     # time.
#     if os.path.exists('token.pickle'):
#         with open('token.pickle', 'rb') as token:
#             creds = pickle.load(token)
#     # If there are no (valid) credentials available, let the user log in.
#     if not creds or not creds.valid:
#         if creds and creds.expired and creds.refresh_token:
#             creds.refresh(Request())
#         else:
#             flow = InstalledAppFlow.from_client_secrets_file(
#                 'credentials.json', SCOPES)
#             creds = flow.run_local_server(port=0)
#         # Save the credentials for the next run
#         with open('token.pickle', 'wb') as token:
#             pickle.dump(creds, token)
#
#     service = build('gmail', 'v1', credentials=creds)
#
#     # Call the Gmail API
#     # results = service.users().labels().list(userId='me').execute()
#     # labels = results.get('labels', [])
#     results = service.users().messages().list(userId='me', labelIds = 'INBOX').execute()
#     labels = results.get('messages', [])
#     if not labels:
#         print('No labels found.')
#     else:
#         print('Labels:')
#         for label in labels:
#             print(label['name'])
#
# if __name__ == '__main__':
#     main()
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from tqdm.auto import tqdm
import chech_and_delet as cad
import del as dl

SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'
temp_list = []
def main():

    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('gmail', 'v1', http=creds.authorize(Http()))

    # labelIds = ['label/Rej_mail']

    # Call the Gmail API to fetch INBOX
    results = service.users().messages().list(userId='me', q = "in:Rej_mail" ).execute()
    messages = results.get('messages', [])


    if not messages:
        print("No messages found.")
    else:
        print("Message snippets:")
        for message in messages:
            msg = service.users().messages().get(userId='me', id=message['id']).execute()
            payld = msg['payload']
            headr = payld['headers']
            for rec_m in headr:
                    if rec_m['name'] == 'X-Failed-Recipients':
                        msg_frm = rec_m['value']
                        temp_list.append(msg_frm)
                        print("Added: ", end= '')
                        print(msg_frm, end='\r')



            # print(headr)

if __name__ == '__main__':
    main()
    print(temp_list)
    print(len(temp_list))
    for l in temp_list:
        print("deleting: " + l )
        delr = cad.parser_d(l)
        dl.dell(delr)
