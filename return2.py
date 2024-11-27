from envs.notebook.Tools.demo.mcast import sender


def send_mail(message,recipient,*,sender = "university.help@gmail.com"):
    domains= (".com",".ru",".net")
    if "@" not in sender or not sender.endswith(domains):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return
    if "@" not in recipient or not recipient.endswith(domains):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return
    if recipient==sender:
        print( "Нельзя отправить письмо самому себе!")
        return
    if sender== "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
        return
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")


send_mail("Это сообщение для проверки связи","vasyok1337@gmail.com")
send_mail('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru',sender='urban.info@gmail.com')
send_mail('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_mail('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')