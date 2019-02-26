# people-finder
Tools for finding and storing profile pics of whatsapp contacts in large scale.

## Installation
### From pypi

    $ pip install peoplefinder

### From source (current version 1.0b1)

    $ git clone https://github.com/fmndantas/people-finder.git
    $ cd people-finder
    $ python setup.py install

### Telegram API token

If you plan to use `peopleuploader` functionalities, make sure your environment
variable PEOPLE_API_TOKEN points to our bot.

## Usage

A graphical interface will be implemented in future updates, but, for now, the usage is *inline*. We've set up the number's format to our
country, Brazil (+55 XX XXXX-XXXX). A example of use is

    $ peoplefinder -n 10 -d 84 -r

where the 10 refers to number of loops in search, 84 refers to the local area code of the phone numbers and
the -r flag indicates random number generation

Alternatively one can create a list of numbers in a file named 
input.txt in the same directory and omit this flag.

### Uploading to telegram @peoplefinder

    $ peopleuploader [-s <savedir>] [-c]
    
This will upload all pictures inside savedir. 
The optional flag -c will clear the files simultaneously.
