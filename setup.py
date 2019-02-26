import setuptools

with open("README.md", 'r') as f:
    long_description = f.read()

setuptools.setup(
    name="peoplefinder",
    version="1.0b1",
    author="Eduardo Nunes & Fernando Dantas",
    license="MIT",
    description="Tools for finding and storing profile pics of whatsapp contacts in large scale.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fmndantas/people-finder",
    packages=setuptools.find_packages(),
    scripts=["bin/peoplefinder", "bin/peopleuploader"],
    install_requires=['numpy>=1.11', 'selenium', 'tqdm', 'python-telegram-bot', 'astropy'],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
    ),
)
