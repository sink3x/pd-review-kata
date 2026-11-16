"""Сообщение студенту после записи."""


def confirmation(name, slot, room):
    text = "Здравствуйте, " + name + "! Вы записаны на " + slot + ", аудитория " + room
    if room == None:
        text = "Здравствуйте, " + name + "! Вы записаны на " + slot
    return text


def send_confirmation(name, slot, room, chat_id):
    text = confirmation(name, slot, room)
    try:
        send_message(chat_id, text)
    except:
        pass
    return True
