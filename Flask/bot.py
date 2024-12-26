import requests
import telebot
from gigachat import GigaChat
from gigachat.models import Chat, Messages, MessagesRole, access_token

bot = telebot.TeleBot('6824920579:AAG3RFCHGkJ8b50B5_8HkFdsMtYUMNHCvwM')

payload = Chat(
    messages=[
        Messages(
            role=MessagesRole.SYSTEM,
            content="ты - бот-шутник, который любит подшучивать над собеседник"
        )
    ],
    temperature=0.7,
    max_tokens=100,
)


def pythonChat():
    payload = Chat(
        messages=[
            Messages(
                role=MessagesRole.SYSTEM,
                content="Ты смешной бот-шутник, который который любит подкалывать собеседника."
            )
        ],
        temperature=0.7,
        max_tokens=100,
    )

    # Используйте токен, полученный в личном кабинете из поля Авторизационные данные
    with GigaChat(
            credentials='MjlhYTdmYzktOWIwNC00OGE4LThkNzItNTBjMTBmNzc0YjY2OmQ1MWY1NmE2LTFhNTQtNDlmNC1hYTQwLTcwMTYxMTZiMDVhMg==',
            verify_ssl_certs=False) as giga:
        while True:
            user_input = input("User: ")
            payload.messages.append(Messages(role=MessagesRole.USER, content=user_input))
            response = giga.chat(payload)
            payload.messages.append(response.choices[0].message)
            print("Bot: ", response.choices[0].message.content)


def getMessagefromBot(message):
    with GigaChat(
            credentials='MjlhYTdmYzktOWIwNC00OGE4LThkNzItNTBjMTBmNzc0YjY2OmQ1MWY1NmE2LTFhNTQtNDlmNC1hYTQwLTcwMTYxMTZiMDVhMg==',
            verify_ssl_certs=False) as giga:
        user_input = message
        payload.messages.append(Messages(role=MessagesRole.USER, content=user_input))
        response = giga.chat(payload)
        payload.messages.append(response.choices[0].message)
        return response.choices[0].message.content

# pythonChat()