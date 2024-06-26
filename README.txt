Problem Statement:

•    Provide code that simulates an elevator. You are free to use any language.
•    Upload the completed project to GitHub for discussion during interview.
•    Document all assumptions and any features that weren’t implemented.
•    The result should be an executable, or script, that can be run with the following inputs and generate the following outputs.
                   Inputs: [list of floors to visit] (e.g. elevator start=12 floor=2,9,1,32)
                   Outputs: [total travel time, floors visited in order] (e.g. 560 12,2,9,1,32)
                   Program Constants: Single floor travel time: 10
    

Solution:

Usage:
Run with Python 3.6 and up
>>python elevator.py [-s --start <single floor to start from> [-f --floor <comma-separated list of floors to stop at>] [-o --optimize]


# ASSUMPTIONS: 
# There is only 1 elevator
# Floors must be specified between 1 and 100
# Start floor is provided
# The entire list of floors to visit is provided once and will be visited in order, unless the --optimize flag is set
# The time to travel between two floors is constant
# The number of people being dropped off at each floor is not specified
# The elevator doesn't have any other constraints

# FEATURES not implemented:
# Elevator object maintaining current floor location between script runs
# Elevator prioritizing stopping at closer floors first
# Handling new requests (neither drop offs or pickups) in the middle of execution
# Specifying a preferred direction the elevator should travel in at start of execution
# Specifying the number of people being dropped off at each floor to optimize total wait time for all people inside
