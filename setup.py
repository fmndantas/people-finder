import setuptools
from pathlib import Path
import sys

with open("README.md", 'r') as f:
    long_description = f.read()

_PACK_BASE_DIR_ = Path(__file__)

if sys.platform in ('win32', 'win64'):
    sys.path.append(Path.joinpath(_PACK_BASE_DIR_, '/bin'))

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
    install_requires=['numpy>=1.11', 'selenium', 'tqdm', 'python-telegram-bot', 'astropy', 'pyautoit'],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
    ),
)
