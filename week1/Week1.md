# Videos:

Introduction\
Video https://vimeo.com/243034300\
Length is 7 minutes

Why Learn Programming?\
Video https://vimeo.com/243905715\
Length is 1 minute

Why Python?\
Video https://vimeo.com/243909371\
Length is 3 minutes

Python2 versus Python3\
Video https://vimeo.com/243912631\
Length is 2 minutes

Characteristics of Python\
Video https://vimeo.com/243918300\
Length is 5 minutes

The Python Interpreter Shell\
Video https://vimeo.com/242411259\
Length is 9 minutes

IPython\
Video https://vimeo.com/242460561\
Length is 4 minutes

Printing to stdout and Reading from stdin\
Video https://vimeo.com/243028886\
Length is 6 minutes

Dir, Help, and Variables​\
Video https://vimeo.com/243480156\
Length is 10 minutes

Python Strings (Part 1)\
Video https://vimeo.com/243481392\
Length is 6 minutes

Python Strings (Part 2)\
Video https://vimeo.com/243482081\
Length is 8 minutes
 

Python Strings (Part 3)\
Video https://vimeo.com/243482871\
Length is 10 minutes
 
Python String Formatting (Part 1)\
Video https://vimeo.com/243936489\
Length is 12 minutes
 
Python String Formatting (Part 2)\
Video https://vimeo.com/243956669\
Length is 4 minutes

# Additional Content:

Google Python Course on Strings

Automate the Boring Stuff with Python (Chapter 6 on Strings)     
*Read up through the section on .join() and .split() string methods.

Python naming conventions:

a. For variable names, function names, object names, and module names use lower case separated by underscore, for example:

```
my_router
find_set_of_devices
convert_id_string_to_list
```

b. For class names, capitalize the first letter of each word.  Do not use any underscores.  For example:

```
ManyToManyField
ClientHistory
UserProfile
```
c. For constants, use all upper case; use underscores for word separation.
```
PI = 3.14
EMAIL_MODE
EMAIL_FROM_ADDRESS
``` 

# Exercises

Reference code for these exercises is posted on GitHub at:
https://github.com/ktbyers/pynet/tree/master/learning_python/lesson1

1. Create a Python script that has three variables: ip_addr1, ip_addr2, ip_addr3 (representing three corresponding IP addresses). Print these three variables to standard output using a single print statement.\
 Make your print statement compatible with both Python2 and Python3.\
 If you are using either Linux or MacOS make your program executable by adding a shebang line and by changing the files permissions (i.e. chmod 755 exercise1.py).\

2. Prompt a user to enter in an IP address from standard input. Read the IP address in and break it up into its octets. Print out the octets in decimal, binary, and hex.\
 Your program output should look like the following:\
​ $ python exercise2.py\
 Please enter an IP address: 80.98.100.240\
 Four columns, fifteen characters wide, a header column, data centered in the column.
```
    Octet1         Octet2         Octet3         Octet4     
------------------------------------------------------------
      80             98             100            240      
   0b1010000      0b1100010      0b1100100     0b11110000   
     0x50           0x62           0x64           0xf0      
------------------------------------------------------------
```

3. Create three different variables the first variable should use all lower case characters with underscore ( _ ) as the word separator. The second variable should use all upper case characters with underscore as the word separator. The third variable should use numbers, letters, and underscore, but still be a valid variable Python variable name.\
 Make all three variables be strings that refer to IPv6 addresses.\
 Use the from future technique so that any string literals in Python2 are unicode.\
 compare if variable1 equals variable2\
 compare if variable1 is not equal to variable3

4. Create a show_version variable that contains the following
```
 show_version = "*0        CISCO881-SEC-K9       FTX0000038X    " 
```
 Remove all leading and trailing whitespace from the string.\
 Split the string and extract the model and serial_number from it.\
 Check if 'Cisco' is contained in the model string (ignore capitalization).\
 Check if '881' is in the model string.\
 Print out both the serial number and the model.



5. You have the following three variables from the arp table of a router:

```
mac1 = "Internet  10.220.88.29           94   5254.abbe.5b7b  ARPA   FastEthernet4"
mac2 = "Internet  10.220.88.30            3   5254.ab71.e119  ARPA   FastEthernet4"
mac3 = "Internet  10.220.88.32          231   5254.abc7.26aa  ARPA   FastEthernet4"
```

Process these ARP entries and print out a table of "IP ADDR" to "MAC ADDRESS" mappings. The output should look like following:

```
             IP ADDR          MAC ADDRESS
-------------------- --------------------
        10.220.88.29       5254.abbe.5b7b
        10.220.88.30       5254.ab71.e119
        10.220.88.32       5254.abc7.26aa
```

Two columns, 20 characters wide, data right aligned, a header column.