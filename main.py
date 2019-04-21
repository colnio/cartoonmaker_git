import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random

def write_msg(user_id, message):
    vk.method('messages.send', {
        'user_id': user_id,
        'message': message,
        'random_id': random.randint(1, 9999)
    })

vk = vk_api.VkApi(token = "6e6e50ff9bb646bbbc7cf03d0a7fa7a21d22714ee7d0b2eae5ad9b69840d9ab9dbfc2bb6530773fb2d7be")
longpoll = VkLongPoll(vk)

random.seed(version=2)
Greeting = ["Привет", "привет", "Здравствуй", "Хай", "Приветствую", "Доброго времени суток"]
Parting = ["Пока", "пока", "Бывай", "Удачи", "До скорого", "До свидвания"]

# Основной цикл
for event in longpoll.listen():

    # Если пришло новое сообщение
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            try:
        # Если оно имеет метку для меня( то есть бота)

                # Сообщение от пользователя
                print(event.attachments.items())
                if(list(event.attachments.items()) == []):
                    print("TextMessage")
                elif event.attachments['attach1_type'] == 'sticker':
                    print("Sticker")
                elif event.attachments['attach1_type'] == 'doc':
                    if  ('attach1_kind' in event.attachments):
                        print(event.attachments['attach1_kind'])
            except KeyError:
                write_msg(event.user_id, "Что ты мне кинул?")
            #else: print(event.attachments['attach1_kind'] if event.attachments['attach1_type'] == 'doc' else 'doc')
            request = event.text
                # Каменная логика ответа
                #write_msg(event.user_id,"И тебе " + request)
            if request in Greeting:
                write_msg(event.user_id, random.choice(Greeting))
            elif request in Parting:
                write_msg(event.user_id, random.choice(Parting))
            elif request == "Gif+MP3":
                write_msg(event.user_id, "Видео")

            else:
                write_msg(event.user_id, "Я не понимаю, что Вы хотели мне сказать...\nЕсли хочешь получить классный видеоролик, то отправь мне выбранную GIF и голосовое, а остальное я сделаю сам")