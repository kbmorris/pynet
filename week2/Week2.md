# Videos:

Numbers\
Video https://vimeo.com/244128549\
Length is 9 minutes
 
Files\
Video https://vimeo.com/244127459\
Length is 10 minutes
 
Lists\
Video https://vimeo.com/244257596\
Length is 6 minutes
 
List Slices\
Video https://vimeo.com/244259492\
Length is 4 minutes
 
Lists are Mutable\
Video https://vimeo.com/244287000\
Length is 5 minutes
 
Tuples\
Video https://vimeo.com/244153105\
Length is 3 minutes
 
Using .join()\
​Video https://vimeo.com/245464488\
Length is 3 minutes
 
sys.argv\
Video https://vimeo.com/245464766\
Length is 2 minutes
 
Linters\
Video https://vimeo.com/245102246\
Length is 6 minutes

# Additional Content:

Automate the Boring Stuff with Python (Chapter 4 on Strings)
Up through the section named "Removing Values from Lists with del Statements"

Dive Into Python, Lists

# Exercises:
Reference code for these exercises is posted on GitHub at:
https://github.com/ktbyers/pynet/tree/master/learning_python/lesson2

1. Open the "show_version.txt" file for reading. Use the .read() method to read in the entire file contents to a variable. Print out the file contents to the screen. Also print out the type of the variable (you should have a string at this point).\
 Close the file.\
 Open the file a second time using a Python context manager (with statement). Read in the file contents using the .readlines() method. Print out the file contents to the screen. Also print out the type of the variable (you should have a list at this point).

2. Create a list of five IP addresses.\
 Use the .append() method to add an IP address onto the end of the list. Use the .extend() method to add two more IP addresses to the end of the list.\
 Use list concatenation to add two more IP addresses to the end of the list.\
 Print out the entire list of ip addresses. Print out the first IP address in the list. Print out the last IP address in the list.\
 Using the .pop() method to remove the first IP address in the list and the last IP address in the list.\
 Update the new first IP address in the list to be '2.2.2.2'. Print out the new first IP address in the list.

3. Read in the "show_arp.txt" file using the readlines() method. Use a list slice to remove the header line.\
 Use pretty print to print out the resulting list to the screen, syntax is:\
 from pprint import pprint\
 pprint(some_var)\
 Use the list .sort() method to sort the list based on IP addresses.\
 Create a new list slice that is only the first three ARP entries.\
 Use the .join() method to join these first three ARP entries back together as a single string using the newline character ('\n') as the separator.\
 Write this string containing the three ARP entries out to a file named "arp_entries.txt".

4. Read in the "show_ip_int_brief.txt" file into your program using the .readlines() method.\
 Obtain the list entry associated with the FastEthernet4 interface. You can just hard-code the index at this point since we haven't covered for-loops or regular expressions. Use the string .split() method to obtain both the IP address and the corresponding interface associated with the IP.\
 Create a two element tuple from the result (intf_name, ip_address).\
 Print that tuple to the screen.\
 Use pycodestyle on this script. Get the warnings/errors to zero. You might need to 'pip install pycodestyle' on your computer (you should be able to type this from the shell prompt). Alternatively, you can type 'python -m pip install pycodestyle'.

5. Read the 'show_ip_bgp_summ.txt' file into your program. From this BGP output obtain the first and last lines of the output.\
 From the first line use the string .split() method to obtain the local AS number.\
 From the last line use the string .split() method to obtain the BGP peer IP address.\
 Print both local AS number and the BGP peer IP address to the screen.\