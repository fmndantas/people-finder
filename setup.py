import setuptools
from setuptools.command.install import install
from setuptools.command.develop import develop
from peoplefinder.common import make_dirs

class CustomInstall(install):
	def run(self):
		install.run(self)		
		print('Running custom install...')		
		make_dirs()
		
class CustomDevelop(develop):
	def run(self):		
		develop.run(self)		
		print('Running custom install in develop mode...')
		make_dirs()

with open("README.md", 'r') as f:
    long_description = f.read()

setuptools.setup(
    name="peoplefinder",
    version="1.0b2",
    author="Eduardo Nunes & Fernando Dantas",
    license="MIT",
    description="Tools for finding and storing profile pics of whatsapp contacts in large scale.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fmndantas/people-finder",
    packages=setuptools.find_packages(),
    scripts=["bin/peoplefinder", "bin/peopleuploader", "bin/peoplechatter"],
    install_requires=['numpy>=1.11', 'selenium', 'tqdm', 'python-telegram-bot', 'astropy', 'pyautoit', 'pytest', 'xlrd'],
	cmdclass={
		'install': CustomInstall,
		'develop': CustomDevelop,
	},    
	classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix, Windows",
    ),
)
