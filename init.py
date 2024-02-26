import os
from google.colab import drive
from IPython      import get_ipython

class GDrive:
    def __init__(self):
        self.base_path = '/content/gdrive'
        drive.mount(self.base_path, force_remount=True)

    def cd(self, path):
        self.path = os.path.join(self.base_path, path)
        print(self.base_path)
        print(self.path)

    def imp(self, path):
        ipython = get_ipython()
        ipython.run_line_magic('run', os.path.join(self.path, path).replace(' ', '\ '))
