def send_email(message, recipient,sender = "university.help@gmail.com"):
    c=0
    pochta="@" in recipient
    if pochta==True:
        c=c+1
    pochta = "@" in sender
    if pochta == True:
        c = c + 1
    if c <= 1:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return
    elif recipient==sender:
        print("Нельзя отправить письмо самому себе!")
        return
    elif "university.help@gmail.com" == sender:
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}")
        return
    k=0
    okonch_ = ".ru" in recipient
    if okonch_ > 0:
        k=k+1
    okonch_ =".com" in recipient
    if okonch_ > 0:
        k = k + 1
    okonch_ = ".net" in recipient
    if okonch_ > 0:
        k = k + 1
    okonch_ = "s.ru" in sender
    if okonch_ > 0:
        k = k + 1
        print("s.ru")
    okonch_ = ".com" in sender
    if okonch_ > 0:
        k = k + 1
    okonch_ = ".net" in sender
    if okonch_ > 0:
        k = k + 1
    if k>1:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")
        return
    else:print(f"Невозможно отправить письмо  с адреса {sender} на адрес {recipient}.")

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru',
           sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru',
           sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru',
          sender='urban.teacher@mail.ru')

