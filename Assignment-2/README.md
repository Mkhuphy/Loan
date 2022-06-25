# Assignment-2
### About this project
-------------------------
In this project, lending and loaning services is applied through a smart contract. A smart contract is something that if once deployed, <\br>
it gets auto-updated whenever a transaction is made.
So here is an owner who initially has 100K Meta-coins. He is said to have aquired all this by taking loans from some parties. Now one by one, the <\br>
parties start taking back their lendings plus the compound interest associated with that amount at a given rate, for a time entered.<\br>

## To run this program
----------------
This code can be easily run on any smart contract platform like 'remix'. Just copy paste in the 'remix' page and hiit deploy and thus the contract would<\br>
be running.
[Maybe due to my ignorance (or maybe due to insufficient time provided) the functions may not work propely as the project has some flaws that needs to<\br>
be weeded out.

### About the code
----------------
1. getCompoundInterest : allows anyone to use it to calculate the amount of interest for given values of P, R, T (in years).<\br>
   Aolidity does not have a good support for floats though, so enter the rate as a whole number (like if the rate is 83%, enter 83). <\br>
   We are looking for an iterative implementation to calculate the Compound Interest, which is compounded annually.<\br>
   This is an inefficient method though.<\br><\br>
   
2. reqLoan: anyone should be able to use it to request the Owner to settle his loan. The P, R, T entered is used to calculate the dues,
   and is added to a mapping. It should emit the Request event.

3. getOwnerBalance: anyone can use it to get the amount of MetaCoins owned by the owner. use of MetaCoin contract's getBalance is made to implement
   this, to create a taste of inheritance!

4. viewDues : only the owner can access this to view the amount of loan he owes to the input address, which is stored in the loans mapping.
   Modifier has been used.

5. settleDues: only the owner can use this to settle the amount of loan he owes to the input address, use MetaCoin's sendCoin function to settle 
   these dues, with appropriate checks for the return values from sendCoin. Also remember to set the amount owed to 0 or whatever remains if 
   sendCoin runs succesfully!
   
   ### To demonstrate how it works
   -------------------
   ```mermaid
   flowchart TD
        B[2K MC-1]--P--R--T-->A[100K MC-A]---->B[Loan paid-1]
        A[100K MC-A]--\-ci-->E[97K - CI:1]
        C[3K MC-1]--P--R--T-->E[97K MC-A]---->C[Loan paid-2]
        A[97K MC-A]--\-ci-->F[92K - CI:2]
        D[45K MC-3]--P--R--T-->F[92K MC-A]---->D[Loan paid-3]
        A[92K MC-A]--\-ci-->G[43K - CI:3]
   ```
   * MC stands for metacoins
   
   
   
   
   
   
   
