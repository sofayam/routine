A generator for daily routines
==============================

Operation
---------

Run the *main.py* routine with your python interpreter (not included), to create a csv file.

To generate a new routine, edit the main.py file and change the Habits array, and the call to the 
Diary constructor. 


Internals
---------
The routine is generated through the definition of Habits which lead to activity when the habit fires.

For each day, each habit which has been defined is evaluated in order of definition.

Each habit which fires for a given day is assumed to allocate a block of time directly following 
the previous habit. The only exception is when the *insert* parameter is used, see below.

Parameters for **Habit** constructor:

Mandatory 

* days: days on which the habit may fire
* dest: the destination where the habit is pursued
* dur: duration of activity

Optional

* prob: probability (in percent) with which the habit will fire
* start: this starts the habit at a given time if there has been no preceding activity that day
* insert: start the habit at the given time and return to the immediately previous destination after the given duration

Parameters for **Diary** constructor

* name: this defines the name of the generated csv file 
* length: the number of days generated
* startloc: the name of the starting location used every morning
* wake: start time for activities every morning

see *main.py* for examples of use