import os
import json
import traceback
import win32com.client
from typing import List
from datetime import datetime
from unidecode import unidecode

def send_email(to: str, subject_content: str, body_content: str, attachment: List[str] = None):
    """
    Sends an email using Microsoft Outlook via win32com.

    :param to: The recipient email address.
    :param subject: The subject line of the email.
    :param body: The body of the email.
    :param attachments: Optional. A list of file paths to attachments to include with the email.
    :return: None
    """
    try:
      outlook = win32com.client.Dispatch('Outlook.Application')
      mail = outlook.CreateItem(0)
      mail.To = to
      mail.Subject = subject_content
      mail.Body = body_content
      if attachment:
        mail.Attachments.Add(attachment)
      mail.Send()
    except Exception as err:
      create_log(traceback.format_exc())

def create_log(execption_content: str):
  os.makedirs('logs', exist_ok = True)
  content = {'Error': unidecode(execption_content), 'Occurrence Time': datetime.now().strftime("%d-%m-%Y %H:%M")}
  open(f'logs{os.sep}log_{datetime.now().strftime("%d-%m-%Y %H_%M")}.json', 'w').write(json.dumps(content).replace('\\"', ''))
