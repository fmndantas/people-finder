# people-finder
Stalker tool for antissocial nerds.

The main purpose of this project is give access kind of stalker tool based upon on WhatsApp Web.

## Usage

A graphical interface will be implemented in future updates, but, for now, the usage is *inline*. I've set up the number's format to my
country, Brazil (+55 XX X XXXX-XXXX). A example of use is

```
python MainLast.py 10 0 84
```

where the 10 reffers to number of loops in search, 0 means False to send the images and respective numbers to Telegram (this feature 
needs some improvements) and 84 reffers to the DDD (ID for cell phones here) of the phone numbers.

## Chromedriver, etc

The "Chromedriver.exe" makes the connection between Python and the Google Chrome **if** the user have the Google Chrome browser installed 
and intents to use it to execute the algorithm.

If the user intents to use another browser, he should download the driver for his respective browser and make sure that the driver is in the
same folder than the py functions.
