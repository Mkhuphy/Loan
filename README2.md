# Assignment-1
* IT WAS TOLD TO TO MAKE A SEPARATE FILE, 'NOT' A REPOSITORY SO THERE WOULD BE FILES WHICH WERE USED FOR RECRUITMENT.
### 1.About this project
-----------------------------------
This program uploaded here calculates the minimum number which should be appended at the end of "iitk"( e.g if we append 184519 to "iitk", it becomes "iitk184519")
so that the SHA256 hash function of the resulting string is less than a given value, (which is arbitrary) : "0000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF"
or in other words has at least four zeros at the beginning.

### 2.To run this program
------------
Any online or offline pyhton compiler would suffice the need of executing the program.

### 3.About the code
-----------------
It has a string as a reference which it uses to find the required number which would be appended to "iitk" so that it becomes less than that reference number.
The program converts both, the reference and the changing "iitk" string to the corresponding decimal forms owing to the large computational power of python.<br />
Then it compares the two integers and when the changing "iitk" string becomes less than the reference string, it stops the process and outputs the value of 
the required number to be appended.<br /><br />
Also, the problem could have been solved by string manipulation, but I wanted to implement the hex-to-dec converter to highlight the fact that we are dealing 
with hexadecimal numbers
