from Controller import Controller


class App:
    def __init__(self):
        self.controller = Controller()
        self.controller.view.main()


if __name__ == '__main__':
    App()

