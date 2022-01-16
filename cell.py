class Cell:
    def __init__(self):
        self._status = 'Dead'
        # "?????????" ???????? ??????

    def is_alive(self):
        return self._status == 'Alive'

    def set_dead(self):
        self._status = 'Dead'

    def set_alive(self):
        self._status = 'Alive'

    def print_me(self):
        if self.is_alive():
            return 'O'
        return '.'
