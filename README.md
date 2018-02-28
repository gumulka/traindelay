# Train delay

A simple program to check when the next train is coming and if is has any delay

## Adjust to own needs
1. Go to https://reiseauskunft.bahn.de and put in your start and destination train
station using auto complete.
2. After that, inspect the website to see what exactly
are the values for the fields with the source and destination train station.
3. Copy these magic numbers (Some obscure long string, containing the name, the ID
of the train station and something else I did not understand) into the source
code.
4. Done


## Timeslot
The programs checks by default the next trains. If you want to have anything
else, the fields and values should look like this:

- REQ0JourneyTime
  - 15:00
- REQ0JourneyDate
  - Mo, 29.01.18

Change it according to your needs.

Have fun
