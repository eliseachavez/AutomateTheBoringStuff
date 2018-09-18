import datetime
print("""Type in 'import datetime' to bring in the datetime module from the
standard library. Nothing will appear to happen.
Then, type in "print(dir(datetime))" to show all the items
inside the the datetime module that are available for use.""")
print("")
print(dir(datetime))
print("")
print("""The text above are all the imported functions and operations
that you can perform now that the module has been imported.

If you type 'help(datetime.datetime)', you can access the help
functions in Python that allows you to learn about the individual
functions. In this case, the datetime funtion inside the datetime
module.""")
print("")
#help(datetime.datetime)
print("""The text above is all reference materials found after using
the help function on that specific module.""")
print("")
print("""We will start using the datetime module and functions
to begin programming.  Enter the text 'gvr = datetime.date(1956,1,31).

Then, type the command to print the date created.
'print(gvr)'.""")
gvr = datetime.date(1956,1,31)
print("")
print(gvr)
print("")
print("""Each part of the date can be accessed separately.
Type 'print(gvr.year)' , 'print(gvr.month' , 'print(gvr.day)'
to see each of the individual values returned.""")
print("")
print(gvr.year)
print("")
print(gvr.month)
print("")
print(gvr.day)
print("")
print("""Now, we are going to store a date in the variable 'mill'
by typing 'startdate = datetime.date(2000,1,1)'.""")
startdate = datetime.date(2000,1,1)
print("")
print("""Now that we have stored that date, we will use the module
function 'datetime.timedelta' to determine the length of time between
that date and another date.  Since we have already stored another
date 'gvr', we will use.

We will store the new date generated after passing the argument
for the numbers of days (100) into the function as variable
'timepassed'.""")
timepassed = datetime.timedelta(100)
print("")
print(timepassed + startdate)
print("""This date represents the date 100 days after our stored
starting date of 1/1/2000.""")
print("")
print("""Next, we will print a message that has had its format style
defined prior to printing the mesage. Giving the command:
'print(gvr.strftime("%A, %B %d, %Y"))' will give the following output.""")
#Day-name, Month-name Day-#, Year
print("")
print(gvr.strftime("%A, %B %d, %Y"))
print("")
print("""This set of instructions is order and case-sensitive.""")
print("")
print("""Then, type 'message = "GVR was born on {:%A, %B %d, %Y}.".
It will give the following message:""")
print("")
message = "GVR was born on {:%A, %B %d, %Y}."
print(message.format(gvr))
print("")
print("""We will now create a date and a time for a launch sequence
for SpaceX.  We will create two variables to store our created
date and time, and the combinationf of the two:
launch_date, launch_time, and launch_datetime, respectively.

Type in 'launch_date = datetime.date(2017,3,30)'
and
         'launch_time = datetime.time(22,27,0)'
and
     'launch_datetime = datetime.datetime(2017,3,30,22,27,0)'

For the date, the three arguments entered are: year, month, year.
For the time, the three arguments entered are: hours, minutes, seconds.""")
print("")
launch_date = datetime.date(2017,3,30)
launch_time = datetime.time(22,27,0)
launch_datetime = datetime.datetime(2017,3,30,22,27,0)
print("""The variables have been saved. So, now we will print them.
To do that type:
'print(launch_date,launch_time,launch_datetime)'. The comma between
the two variable names  will cause Python to recognize the variables
as being in the same print line with a space separating them.""")
print("")
print(launch_date,launch_time,launch_datetime)
print("")
print("""You can also access invidual elements within the datetime.
If you type 'print(launch_time.hour)', you get the hour element
printed as a integer. The same is true by selecting .minute, or
.second to access those elements.""")
print(launch_time.hour)
print(launch_time.minute)
print(launch_time.second)
print("")
print("""If you want to access the current date and time information,
you can use the datetime module in the datetime class under the
today() method.

Type 'save_the_date = datetime.datetime.today()'.
This will store the current date and time information in the variable
save_the_date.

Type 'print(save_the_date)' to show the captured data.""")
print("")
save_the_date = datetime.datetime.today()
print(save_the_date)
print("")
