class MyFile:

    def __init__(self, file_name, mode):
        self._file_name = file_name
        self._mode = mode
        self.file = open(self._file_name, self._mode)

    def __enter__(self):
        print('*enter*')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('*exit*')
        self.file.close()

with MyFile('abc.txt', 'w') as f:
    f.file.write('12345754')
