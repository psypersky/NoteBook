import datetime
from contextlib import contextmanager

# A basic Context Manager

class SessionLogger:
    file_name = None
    file = None

    def __init__(self, file_name):
        print('Creating Session Logger')
        self.file_name = file_name

    def __enter__(self):
        print('Context Manager Created')
        self.file = open(self.file_name, 'a')
        now = datetime.datetime.now()
        self.file.write(f'\n\n=== Session Start: ${str(now)} ===')
        return self.log
        # open file and save file object

    def log(self, text):
        print('Logging text')
        self.file.write('\n' + text)
        # log text to file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Exit Context Manager')
        now = datetime.datetime.now()
        self.file.write(f'\n=== Session End: ${str(now)} ===')
        self.file.close()


with SessionLogger('./log.txt') as log:
    log('Hello Words')
    log('foo != bar')

print('end of example 1')

# A context manager created with @contextmanager decorator
@contextmanager
def session_logger(file_name):

    file = open(file_name, 'a')
    now = datetime.datetime.now()
    file.write(f'\n\n=== Session Start: ${str(now)} ===')

    def log(text):
      file.write(f'\n{text}')

    try:
        yield log
    except:
        # TODO: write error log
        pass
    finally:
        now = datetime.datetime.now()
        file.write(f'\n=== Session End: ${str(now)} ===')
        file.close()

with session_logger('./log.txt') as log:
    log('Hello word @contextmanager')
    log('foo != bar @contextmanager')

print('end of example 2')
