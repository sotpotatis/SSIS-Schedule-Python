# SSIS-Schedule-Python
Easy-to-use library for Python for getting the schedule for the school Stockholm Science and Innovation School.

### Please note

This libary is currently a work-in-progress and it is not available through PyPi just yet. With that said though, there is only pretty much the addition a few metadata entries and a main checkup of the code left. So, feel free to use it!

### Usage example

This does not illustrate all metadata available - docs coming very soon!

```python
"""SSIS_schedule library example usage file"""
from ssis_schedule.Schedule import Schedule #Import the schedule library
sc = Schedule("Domino") #Create a new schedule object and pass who we want to get the schedule from
entries = sc.get_schedule() #Get the schedule
for entry in entries: #Loop through entries
    #Pretty-print metadata below
    #(print strings are in Swedish)
    print(entry.subject)
    print("Startar ", entry.starts_at_raw, ". Slutar ", entry.ends_at_raw)
    print("Deltagande lärare: ", ",".join(entry.participating_teachers))
    print("Deltagande klass(er): ", ",".join(entry.participating_classes))
    print("Rum: ", ",".join(entry.room))

```
