import os


class Updating:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        try:
            self.previous = self.filename + " copy"
            os.rename(self.filename, self.previous)
        except FileNotFoundError:
            self.previous = None

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            try:
                os.rename(self.filename, self.filename + " error")
            except FileNotFoundError:
                pass
            if self.previous:
                os.rename(self.previous, self.filename)


path = 'index.html'
rename = Updating(path)
print(rename)
