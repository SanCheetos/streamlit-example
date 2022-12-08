import firebase_admin
import streamlit as st
from firebase_admin import credentials
from firebase_admin import db
import json

KEY_FIREBASE = '{ "type": "service_account", "project_id": "streamlit-sst-sum", "private_key_id": "09c970b2b9b4f441c34c346f08934bcfdd622782", "private_key": "-----BEGIN PRIVATE KEY-----\\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCYojNMWLbZ8IeR\\nE99RW0KZxnmHBzeYqb92apR0q+XtxJkODh7hlZuHsKWr7ZXtY2F5UtcM/As/06+4\\nTkrGaIKcugPDc3H1VDxigg3d/ivfu7NZWQhf//YMCZ0f3tBvw2xG6venSVbTadnu\\ncqeFDaZhSk3yiUkgm1v8+R/NZBNHlzUsP0U8Icbl8kFaUaUr0yoyuTOVJeHv4NxX\\nRYdOogTS78uqFaMJbkFr3jvCvvYYdsRxLhDmd+uSxEzVe2Pu0wMntK56PqCVO4Jz\\n0JseMaSeVxXvZO13gI4yg7RF9eL2AnaaKdLKyV8xsWFflTfqRX7e075ZAepPUjzT\\nNn8My0UpAgMBAAECggEADvIQ/liQfQovqB3PR+7c+GRGGZn0EHOMryp0A3Gil9Pg\\nnc71qKam3lRGgK2IuQA6dvAM5TVX36XZhr1J1qA8q96OCEkpXzmimQ29kF93Sdbe\\nErFkX8wXOmoFk+2UMOFsnIwc+Gk2wohSoeXhr+ZchJnLRKS7P6Fe0khNnCXAuol1\\nwKAWhkfqXXPXlNMnZQHaUoSSsRWJkX73VunBHcTkPrxqpbAQvl3wkfFvMNVK3l5V\\nKjUGZW0XbKGa0Wvo7CifqsjUoeQiaVSmC8WqjIGD4lBLvkerPKjCZAE8ylcs/cdX\\n3rX/Xp5ulHQ9l0QqnLXO+L/xtbx5/05jp1RWl+iRpQKBgQDWkBMzthhSMCd4jplu\\ntEYPn3DvkVHN3/WZgvqYdsbIGQHlaVv8uvEAePhG1gGcYzxmZ3CvM6bhci2bBCk8\\nedT0NgMoQj1FoBDJtqNttvR2+bO4FM/FUxCOxdae469KzOpjXVOXsrdoYMIAQ0AA\\nHO1+GISOUKgW7d8fAy/zcAh1NQKBgQC2HFzuRhoGgKCL/jQ/6kMZn4DnlnlYyR5R\\n7GTcprp+sYFqnzO5La4so2RzUDtuuY7rCVLDzlfFu5Rpq8r+omDUQYdC84Jdj+Mw\\neroidLXJoSkLRfyWXLS7AiNc6HILQxm+pLtrfSpmetB7FyL34R0YMv1hNn0zddv0\\nmtv0B/ISpQKBgQCuuPRqD8cOZpg93CGlvLew0S2uaLAs7kuZjsdykIafO34HyxxV\\nWgYXVGsZg/wb1dPBsEpa4bzrqYbpzSGnVa7Mj49SoV4z7Hy/RjMfjPTWTdDD/m6T\\nSWkaWpDDIrYEO4pDECSaS7Z/EQvqGtlrPiNHo7+OBLBcu6gOIRJTMtAwYQKBgC1m\\n5thUy9pBKUWdq8MfkXkK5iVWw4waICAGkqLcQnShpoVBibCqLdldJwcEwrx5MKNy\\nYJsGj6Vxfa/Wr7ZKH1/rsmBDu4W+AMMuZcd/V28cadIwsad/F2PkRZK9NOmP4hRA\\nl6VVwENqbR2zB/nKuuk0lS0uW4p/4MWb8ihl7rktAoGBAMd141NTLlE3KDAiP8AB\\nBNTDfbH1BGoNfq5HoK6kd/y/jz1NncjZPctfPxN729sk2RrmUGsNEOXepbo589r4\\nnxlCQBE3iSevbCx3A4hG+uzp5rxkjHZ6WTD93AjHO4oTEiXkseWUZlSqCJICIMbl\\nyvaH54a+St7zxNuRvl/uzCSx\\n-----END PRIVATE KEY-----\\n", "client_email": "firebase-adminsdk-xerj5@streamlit-sst-sum.iam.gserviceaccount.com", "client_id": "103237298877314924209", "auth_uri": "https://accounts.google.com/o/oauth2/auth", "token_uri": "https://oauth2.googleapis.com/token", "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs", "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-xerj5%40streamlit-sst-sum.iam.gserviceaccount.com" }'
#firebaseConfig = json.dumps(KEY_FIREBASE, ensure_ascii=False)
yo = json.loads(KEY_FIREBASE)
st.write(str(yo == json.loads(st.secrets["KEY_FIREBASE"])))

#Функция должна срабатывать каждый раз, когда нажалась кнопка и пошел процесс основной работы
def FireBase_Push(date, percentSum, textLength, CheckBoxes, timeYandex):
    cred = credentials.Certificate("key.json")
    try:
        firebase_admin.initialize_app(cred)
    except:
        print("Already connected")
    ref = db.reference(path="/Analitics", url="https://streamlit-sst-sum-default-rtdb.firebaseio.com") 
    if (len(CheckBoxes) != 5):
        return "Not this array!"
    else:
        ref.push({
                	"Дата": date,
                    "Процент сокращения": percentSum,
                    "Длина текста": textLength,
                    "Имена": CheckBoxes[0],
                    "Организации": CheckBoxes[1],
                    "Локации": CheckBoxes[2],
                    "Деньги": CheckBoxes[3],
                    "Даты": CheckBoxes[4],
                    "Время работы SpeechKit": timeYandex
                    
                 })
        return "Success"
def FireBase_Get():
    cred = credentials.Certificate(json.loads(st.secrets["KEY_FIREBASE"]))
    try:
        firebase_admin.initialize_app(cred)
    except:
        print("Already connected")
    ref = db.reference(path="/Analitics", url="https://streamlit-sst-sum-default-rtdb.firebaseio.com") 
    return ref.get()
