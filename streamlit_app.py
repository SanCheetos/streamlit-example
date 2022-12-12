from FireBase import FireBase_Get
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import time
import json

def getAnalitics():
    cleanData = FireBase_Get()
    df = pd.DataFrame({
        "Дата": [],
        "Процент сокращения": [],
        "Длина текста": [],
        "Имена": [],
        "Организации": [],
        "Локации": [],
        "Деньги": [],
        "Даты": [],
        "Время работы SpeechKit": []
        })
    
    
    arrayData = cleanData.items()
    for elem in arrayData:
        df = df.append(elem[1], ignore_index=True)
    df["Имена"].astype(int)
    df["Организации"].astype(int)
    df["Без выделений"] = sum((df["Имена"] == 0) & 
                              (df["Организации"] == 0) & 
                              (df["Локации"] == 0) & 
                              (df["Деньги"] == 0) & 
                              (df["Даты"] == 0))
    
    fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, ncols=1, figsize=(9, 19))
    
    #Гистограмма для чекбоксов (одна, по y  доля использований, по x все чекбоксы)
    ax1.bar(['Имена','Организации', 'Локации', 'Деньги', 'Даты', 'Без выделений'], height=[(sum(df["Имена"] == 1)/len(df)) * 100, 
                                   (sum(df["Организации"] == 1)/len(df)) * 100, 
                                   (sum(df["Локации"] == 1)/len(df)) * 100,
                                   (sum(df["Деньги"] == 1)/len(df)) * 100,
                                   (sum(df["Даты"] == 1)/len(df)) * 100,
                                   (sum(df["Без выделений"] == 1)/len(df)) * 100])
    ax1.set_ylabel("Процент от общего использования")
    ax1.set_title('Использование выделений в тексте')
    
    ax2.hist(data=df, x ="Длина текста", bins=15)
    ax2.set_title('Количество обрабонного текста по его длине')
    ax2.set_xlabel("Длина текста")
    ax2.set_ylabel("Количество обработок по этой длине")
    
    ax3.hist(data=df, x ="Процент сокращения", bins= 10)
    ax3.set_title('Количество обрабонного текста по проценту сокращения')
    ax3.set_xlabel("Процент сокращения")
    ax3.set_ylabel("Количество обработок по этому проценту")
    st.write(fig)
    
    #Средняя длина текста - просто вывод
    #Гистограмма по длине текста с разбросом в 100-200 символов (по количеству использований)
    st.write("Среднее значение обработанной длины текста: " + str(df["Длина текста"].mean()))
    #Аналогично с процентом сокращения
    st.write("Средний процент сокращения: " + str(df["Процент сокращения"].mean()))
'''
 plt.bar([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000], width=10, height=
            [sum(df["Процент сокращения"] < 11),
             sum((df["Процент сокращения"] > 10) & (df["Процент сокращения"] < 21)),
             sum((df["Процент сокращения"] > 20) & (df["Процент сокращения"] < 31)),
             sum((df["Процент сокращения"] > 30) & (df["Процент сокращения"] < 41)),
             sum((df["Процент сокращения"] > 40) & (df["Процент сокращения"] < 51)),
             sum((df["Процент сокращения"] > 50) & (df["Процент сокращения"] < 61)),
             sum((df["Процент сокращения"] > 60) & (df["Процент сокращения"] < 71)),
             sum((df["Процент сокращения"] > 70) & (df["Процент сокращения"] < 81)),
             sum((df["Процент сокращения"] > 80) & (df["Процент сокращения"] < 91)),
             sum(df["Процент сокращения"] > 90)])
    plt.xticks([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000], ["0-10", "11-20", "21-30", "31-40", "41-50", "51-60", "61-70", "71-80", "81-90", "91-100"])
'''
    
#Время работы SpeechKit в зависимости от длины текста (График, где x - длина текста, а y Время работы speechkit),
fig, ax = plt.subplots()
#ax.hist(data=df, x="Длина текста", y)
ax.plot("Длина текста", "Время работы SpeechKit", data=df)
fig
KEY_FIREBASE = '{ "type": "service_account", "project_id": "streamlit-sst-sum", "private_key_id": "09c970b2b9b4f441c34c346f08934bcfdd622782", "private_key": "-----BEGIN PRIVATE KEY-----\\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCYojNMWLbZ8IeR\\nE99RW0KZxnmHBzeYqb92apR0q+XtxJkODh7hlZuHsKWr7ZXtY2F5UtcM/As/06+4\\nTkrGaIKcugPDc3H1VDxigg3d/ivfu7NZWQhf//YMCZ0f3tBvw2xG6venSVbTadnu\\ncqeFDaZhSk3yiUkgm1v8+R/NZBNHlzUsP0U8Icbl8kFaUaUr0yoyuTOVJeHv4NxX\\nRYdOogTS78uqFaMJbkFr3jvCvvYYdsRxLhDmd+uSxEzVe2Pu0wMntK56PqCVO4Jz\\n0JseMaSeVxXvZO13gI4yg7RF9eL2AnaaKdLKyV8xsWFflTfqRX7e075ZAepPUjzT\\nNn8My0UpAgMBAAECggEADvIQ/liQfQovqB3PR+7c+GRGGZn0EHOMryp0A3Gil9Pg\\nnc71qKam3lRGgK2IuQA6dvAM5TVX36XZhr1J1qA8q96OCEkpXzmimQ29kF93Sdbe\\nErFkX8wXOmoFk+2UMOFsnIwc+Gk2wohSoeXhr+ZchJnLRKS7P6Fe0khNnCXAuol1\\nwKAWhkfqXXPXlNMnZQHaUoSSsRWJkX73VunBHcTkPrxqpbAQvl3wkfFvMNVK3l5V\\nKjUGZW0XbKGa0Wvo7CifqsjUoeQiaVSmC8WqjIGD4lBLvkerPKjCZAE8ylcs/cdX\\n3rX/Xp5ulHQ9l0QqnLXO+L/xtbx5/05jp1RWl+iRpQKBgQDWkBMzthhSMCd4jplu\\ntEYPn3DvkVHN3/WZgvqYdsbIGQHlaVv8uvEAePhG1gGcYzxmZ3CvM6bhci2bBCk8\\nedT0NgMoQj1FoBDJtqNttvR2+bO4FM/FUxCOxdae469KzOpjXVOXsrdoYMIAQ0AA\\nHO1+GISOUKgW7d8fAy/zcAh1NQKBgQC2HFzuRhoGgKCL/jQ/6kMZn4DnlnlYyR5R\\n7GTcprp+sYFqnzO5La4so2RzUDtuuY7rCVLDzlfFu5Rpq8r+omDUQYdC84Jdj+Mw\\neroidLXJoSkLRfyWXLS7AiNc6HILQxm+pLtrfSpmetB7FyL34R0YMv1hNn0zddv0\\nmtv0B/ISpQKBgQCuuPRqD8cOZpg93CGlvLew0S2uaLAs7kuZjsdykIafO34HyxxV\\nWgYXVGsZg/wb1dPBsEpa4bzrqYbpzSGnVa7Mj49SoV4z7Hy/RjMfjPTWTdDD/m6T\\nSWkaWpDDIrYEO4pDECSaS7Z/EQvqGtlrPiNHo7+OBLBcu6gOIRJTMtAwYQKBgC1m\\n5thUy9pBKUWdq8MfkXkK5iVWw4waICAGkqLcQnShpoVBibCqLdldJwcEwrx5MKNy\\nYJsGj6Vxfa/Wr7ZKH1/rsmBDu4W+AMMuZcd/V28cadIwsad/F2PkRZK9NOmP4hRA\\nl6VVwENqbR2zB/nKuuk0lS0uW4p/4MWb8ihl7rktAoGBAMd141NTLlE3KDAiP8AB\\nBNTDfbH1BGoNfq5HoK6kd/y/jz1NncjZPctfPxN729sk2RrmUGsNEOXepbo589r4\\nnxlCQBE3iSevbCx3A4hG+uzp5rxkjHZ6WTD93AjHO4oTEiXkseWUZlSqCJICIMbl\\nyvaH54a+St7zxNuRvl/uzCSx\\n-----END PRIVATE KEY-----\\n", "client_email": "firebase-adminsdk-xerj5@streamlit-sst-sum.iam.gserviceaccount.com", "client_id": "103237298877314924209", "auth_uri": "https://accounts.google.com/o/oauth2/auth", "token_uri": "https://oauth2.googleapis.com/token", "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs", "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-xerj5%40streamlit-sst-sum.iam.gserviceaccount.com" }'
#firebaseConfig = json.dumps(KEY_FIREBASE, ensure_ascii=False)
yo = json.loads(KEY_FIREBASE)
st.write(yo)
st.write(json.loads(st.secrets["KEY_FIREBASE"]))
getAnalitics()
