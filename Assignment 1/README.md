# Assignment-1
* IT WAS TOLD TO TO MAKE A SEPARATE FOLDER, 'NOT' A REPOSITORY SO THERE WOULD BE FILES WHICH WERE USED FOR RECRUITMENT.
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
It has a string as a reference which it uses to find the required number which would be appended to "iitk" so that it becomes less than that reference number.<br />
The problem is solved using string manipulation, i.e. by checking the number of zeros required at the front. The no. of zeros is taken as input.
### To demonstrate the power of this hashing
Execution time and the required value are as follows:

|Number of zeros (input) |Execution time(s) |Number to be appended  |
|---|---|---|
|0 |0 |0 |
|1 |0 |15 |
|2 |0 |338 |
|3 |0 |4514 |
|4 |0 |184519 |
|5 |2 |1217060 |
|6 |56 |25617258 |
|7 |102 |46903559 |

* The rate if increase of execution time with number of zeros is clearly very high.
* The time is calculated by running the program on google colaboratory.
