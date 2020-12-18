"""EXAMPLE.PY
ssis_schedule example usage file"""
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
