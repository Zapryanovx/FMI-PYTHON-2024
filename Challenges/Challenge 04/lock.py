class LockPicker_8MI0600405:

    def __init__(self, lock):
        self.lock = lock

    def unlock(self):
        args = []

        while True:
            try:
                if self.lock.pick(*args):
                    return 'Ало-ало, тук Нощен ястреб. Вътре сме! Край!'
            except TypeError as err:
                if err.position is None:
                    args.extend([None] * (err.expected - len(args)))
                else:
                    args[err.position - 1] = err.expected()
            except ValueError as err:
                args[err.position - 1] = err.expected