import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random
#import  change_voice_script
# import url_download


def write_msg(user_id, message):
    vk.method('messages.send', {
        'user_id': user_id,
        'message': message,
        'random_id': random.randint(1, 9999)
    })

def write_vc(user_id, message):
    vk.method('messages.send', {
        'user_id': user_id,
        'random_id': random.randint(1, 9999),
        'attachment': "doc" + message
    })

def write_photo(user_id, message):
    vk.method('messages.send', {
        'user_id': user_id,
        'random_id': random.randint(1, 9999),
        'message': "photo" + message,
        'attachment': "doc" + message
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
        msg_type = 'None' # будем хранить тип сообщения
        if event.to_me:
            try:
        # Если оно имеет метку для меня( то есть бота)

                # Сообщение от пользователя
                print(event.attachments.items())
                if(list(event.attachments.items()) == []):
                    msg_type = "TextMessage"
                elif event.attachments['attach1_type'] == 'sticker':
                    msg_type = "Sticker"
                elif event.attachments['attach1_type'] == 'photo':
                    msg_type = "Photo"
                elif event.attachments['attach1_type'] == 'doc':
                    if  ('attach1_kind' in event.attachments):
                        msg_type = event.attachments['attach1_kind']
                    else:
                        msg_type = "GIF"
                print("type = " + msg_type)
            except KeyError:
                write_msg(event.user_id, "Что ты мне кинул?")
            if msg_type == "TextMessage":
                request = event.text
                if request in Greeting:
                    write_msg(event.user_id, random.choice(Greeting))
                elif request in Parting:
                    write_msg(event.user_id, random.choice(Parting))
                elif request == "Gif+MP3":
                    write_msg(event.user_id, "Видео")
                else:
                    write_msg(event.user_id, "Я не понимаю, что Вы хотели мне сказать...\nЕсли хочешь получить классный видеоролик, то отправь мне выбранную GIF и голосовое, а остальное я сделаю сам\nGIF можно взять здесь\nhttps://gifer.com/ru/gifs/%D0%BF%D0%B8%D0%BA%D0%B0%D1%87%D1%83")
            elif msg_type == "audiomsg":
                write_msg(event.user_id, "Я тебя услышал")
                #print(vk_api.message.getById())
                # urlv = event.attachments["attach1"]
                # write_vc(event.user_id, urlv)
            elif msg_type == "GIF":
                write_msg(event.user_id, "Отличная GIF")
            elif msg_type == "Photo":
                write_msg(event.user_id, "Хорошая фотография, но  мне бы GIF...")
                urlp = event.attachments["attach1"]
                write_photo(event.user_id, urlp)
            elif msg_type == "Sticker":
                write_msg(event.user_id, "Стикеры это классно, но пока я не умею с ними работать...")
            else:
                write_msg(event.user_id, "Это не GIF")


