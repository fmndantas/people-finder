# people-finder
Tools for finding and storing profile pics of whatsapp contacts in large scale.

## Installation
### From pypi

    $ pip install peoplefinder

### From source (current version 1.0b1)

    $ git clone https://github.com/fmndantas/people-finder.git
    $ cd people-finder
    $ python setup.py install

## Usage

A graphical interface will be implemented in future updates, but, for now, the usage is *inline*. We've set up the number's format to our
country, Brazil (+55 XX XXXX-XXXX). A example of use is

    $ peoplefinder -n 10 -d 84

where the 10 refers to number of loops in search, and 84 refers to the local area code of the phone numbers.
