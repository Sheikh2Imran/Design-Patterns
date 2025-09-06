class Notifier:
    def send(self, message):
        pass


class EmailNotifier(Notifier):
    def send(self, message):
        print("Sending email ", message)


class NotifierDecorator(Notifier):
    def __init__(self, notifier: Notifier):
        self._notifier = notifier

    def send(self, message):
        self._notifier.send(message)


class SMSDecorator(NotifierDecorator):
    def send(self, message):
        super().send(message)
        print("Sending sms: ", message)
    

class SlackDecorator(NotifierDecorator):
    def send(self, message):
        super().send(message)
        print("Sending slack message: ", message)
    

notifier = SlackDecorator(SMSDecorator(EmailNotifier()))
notifier.send("Server down !!")
