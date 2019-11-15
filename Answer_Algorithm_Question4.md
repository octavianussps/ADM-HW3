## 4. Algorithmic question
You are given a string, s. Let's define a subsequence as the subset of characters that respects the order we find them in s. For instance, a subsequence of "DATAMINING" is "TMNN". Your goal is to define and implement an algorithm that finds the length of the longest possible subsequence that can be read in the same way forward and backwards. For example, given the string "DATAMININGSAPIENZA" the answer should be 7 (dAtamININgsapIenzA).

### Answer: 
The Idea that is referred in this question is of the longest palindromic subsequence. I am defining this algorithm with the dynamic programming approach which is defined as dividing a problem into sub-problems, then solving these sub-problems in a way to store their results in a structure dataset for future query.
First of all understand the problem, let’s suppose the sequence is “anwaralam” and its length is 9 and index 0-8. So,

1.	First part is to identify the subsequences of this sequence, which can be defined as the sub-problem of the main - - problem.
2.	Then second part is to identify their palindromic nature from first and last element of the subsequence and store the result in a data structure, (data structure is defined as a 2 dimensional table DST in our case)
3.	Thirdly to identify the longest Palindromic Subsequence from the data structure of stored result

 DST Data Structure Table: It’s a 2 dimensional table with rows and column equal to the length of the sequence
 
<p align="left">
<img src="https://github.com/anwaralamgithub/ADM2019HW3_Movies_Search_Engine/blob/images/FIG1.jpg" height=430 
</p>
 
#### In: 
```html
s = "anwaralam"
n = len(s)
DST= [[0 for i in range(n)]for i in range (n)]
```
#### OUT :
```html
 [[0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0]]
```

### First and Second Step 
##### Dividing into sub-problem, solving and storing them in a Data structure

I have arranged this step in a manner of increasing order of subsequence length. So first consider subsequence length is 1 that is only one character, so
```html
DST[0][0] = ‘a’ = 1	DST[1][1] = ‘n’ = 1	DST[2][2] = ‘w’ = 1	DST[3][3] = ‘a’ = 1	DST[4][4] = ‘r’ = 1	
DST[5][5] = ‘a’ = 1	DST[6][6] = ‘l’ = 1	DST[7][7] = ‘a’ = 1	DST[8][8] = ‘m’ = 1
```
As its one character so it same character, we were consider TRUE as 1

<p align="left">
<img src="https://github.com/anwaralamgithub/ADM2019HW3_Movies_Search_Engine/blob/images/FIG2.jpg" height=430 
</p>

#### In: 
```html
for i in range (n):
    l[i][i] = 1
```
#### OUT
```html
[[1, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 1, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 1, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 1, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 1, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 1, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 1, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 1]]
```
Now for the length of subsequence (sseq) 2 or more, i.e. (2 <= sseq >= n+1), 

we will generate a loop for this purpose to and check the conditions.

If the two consecutive alphabets are same DST[i] = DST[i+sseq-1] and sseq = 2.

If the alphabets are not same then 2 or else the Maximum between these two results DST[i][j-1] and DST[i+1][j]

So when sseq = 2, i with a loop starting with 0 and j initiate its position at j = i+sseq-1, so
```html
DST[0][1] = "an" = 1	DST[1][2] = "nw" = 1	DST[2][3] = "wa" = 1	DST[3][4] = "ar" = 1	DST[4][5] = "ra" = 1
DST[5][6] = "al" = 1	DST[6][7] = "la" = 1	DST[7][8] = "am" = 1
```
<p align="left">
<img src="https://github.com/anwaralamgithub/ADM2019HW3_Movies_Search_Engine/blob/images/FIG3.jpg" height=430 
</p>

#### IN:
```html
for sseq in range(2, n+1): # loop for the length of subsequence
    for i in range(n-sseq+1):
        j = i+sseq-1
        if (seq[i] == seq[j] and sseq == 2): #conditioning for length 2 subsequences
            DST[i][j] = 2	
        elif seq[i] == seq[j]:
            DST[i][j] = DST[i+1][j-1] + 2
        else:
            DST[i][j] = max(DST[i][j-1], DST[i+1][j])
```
#### OUT:
```html
[[1, 1, 0, 0, 0, 0, 0, 0, 0],
[0, 1, 1, 0, 0, 0, 0, 0, 0],
[0, 0, 1, 1, 0, 0, 0, 0, 0],
[0, 0, 0, 1, 1, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 1, 0, 0, 0],
[0, 0, 0, 0, 0, 1, 1, 0, 0],
[0, 0, 0, 0, 0, 0, 1, 1, 0],
[0, 0, 0, 0, 0, 0, 0, 1, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 1]]
```
Similarly when sseq = 3, starting i with a loop from 0 and j initiate its position at j = i+sseq-1,

so when first and the last alphabets is same then the result is DST[i+1][j-1] + 2, that makes 3 in below 2 cases


```html	
DST[0][2] = "anw" = 1	DST[1][3] = "nwa" = 1	DST[2][4] = "war" = 1	DST[3][5] = "ara" = 3
DST[4][6] = "ral" = 1	DST[5][7] = "ala" = 3	DST[6][8] = "lam" = 1

```
<p align="left">
<img src="https://github.com/anwaralamgithub/ADM2019HW3_Movies_Search_Engine/blob/images/FIG4.jpg" height=430 
</p>
 
#### IN:
```html
elif seq[i] == seq[j]:
    DST[i][j] = DST[i+1][j-1] + 2
else:
    DST[i][j] = max(DST[i][j-1], DST[i+1][j]) 
```
#### OUT:

```html
[[1, 1, 1, 0, 0, 0, 0, 0, 0], 
[0, 1, 1, 1, 0, 0, 0, 0, 0], 
[0, 0, 1, 1, 1, 0, 0, 0, 0], 
[0, 0, 0, 1, 1, 3, 0, 0, 0], 
[0, 0, 0, 0, 1, 1, 1, 0, 0], 
[0, 0, 0, 0, 0, 1, 1, 3, 0], 
[0, 0, 0, 0, 0, 0, 1, 1, 1], 
[0, 0, 0, 0, 0, 0, 0, 1, 1], 
[0, 0, 0, 0, 0, 0, 0, 0, 1]] 
```
Moving forward with increasing length of subsequence (sseq) and verifying the above condition, we come across the below Data structure

<p align="left">
<img src="https://github.com/anwaralamgithub/ADM2019HW3_Movies_Search_Engine/blob/images/FIG5.jpg" height=430 
</p>

________________________________________________________________________________________________________________________
<p align="left">
<img src="https://github.com/anwaralamgithub/ADM2019HW3_Movies_Search_Engine/blob/images/FIG6.jpg" height=430 
</p>

#### IN: 
#### Creating a table of rows and column equal to len of string s 
```html
s = "anwaralam" 
n = len(s) 
DST= [[0 for i in range(n)]for i in range (n)] 
``` 
##### For all values where length of sub sequence is 1 
```html
for i in range (n):     
    DST[i][i] = 1 
```
##### For all values where length of subsequence is more than 1 # We make a loop for the lengths of sub-sequence   
```html
for sseq in range(2, n+1):
    for i in range(n-sseq+1):
        j = i+sseq-1 
        if (s[i] == s[j] and sseq == 2): #conditioning for length 2 subsequences 
            DST[i][j] = 2         
        elif s[i] == s[j]:             
            DST[i][j] = DST[i+1][j-1] + 2         
        else:
            DST[i][j] = max(DST[i][j-1], DST[i+1][j]) 
     Print (DST) 
```
#### OUT: 
```html
[[1, 1, 1, 3, 3, 3, 3, 5, 5], 
[0, 1, 1, 1, 1, 3, 3, 3, 3], 
[0, 0, 1, 1, 1, 3, 3, 3, 3], 
[0, 0, 0, 1, 1, 3, 3, 3, 3], 
[0, 0, 0, 0, 1, 1, 1, 3, 3], 
[0, 0, 0, 0, 0, 1, 1, 3, 3], 
[0, 0, 0, 0, 0, 0, 1, 1, 1], 
[0, 0, 0, 0, 0, 0, 0, 1, 1], 
[0, 0, 0, 0, 0, 0, 0, 0, 1]] 
``` 
#### IN: 
print("The Longest Palindromic sub Sequence is ", DST[0][n-1])  
 
 
#### OUT: 
 
The Longest Palindromic sub Sequence is 5 
