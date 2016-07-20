---
author:
- lvzejun 201528013229115
title: Assignment 2
...

Money robbing
=============

A robber planning to rob houses along a street. Each house has a certain
amount of money stashed, the only constraint stopping you from robbing
each of them is that adjacent houses have security system connected and
it will automatically contact the police if two adjacent houses were
broken into on the same night.\
1.Given a list of non-negative integers representing the amount of money
of each house, determine the maximum amount of money you can rob tonight
without alerting the police.\
\
2. What if all houses are arranged in a circle?

Optimal subproblems And DP equation
-----------------------------------

### Question1

Denote the optimal solution value as rob\_max(i) which means the max
money can be robbed when consider the $i^{th}$ house,and m stand for the
count of money of each house.Suppose we start the house index from
0,then:\
(1)If there exists only 1 house,rob\_max(0) = $m_0$;\
(2)If there exists 2 houses,chose the max one.max{$m_0$,$m_1$}.\
(3)If there exists more than 2 houses,we can summarizing two cases:\
$$

rob\_max(i-2)+ m\_i&\
rob\_max(i-1) &

$$Optimal sub-structure property:\\$$ rob\_max(i) =

m\_0 &\
max{m\_0,m\_1} &\
max{rob\_max(i-2)+m\_i,rob\_max(i-1)}&

$$\subsubsection{Question2-All houses in a circle}
If all houses are arrange in a circle,it means that the robber can't rob the first and last house in the sametime,either the first one or the last one.So we can divide the problem into two subquestions,(1)find max of 1 to last-1,(2)find max of 2-last,then find max.
\subsection{Proof}
%We define rob\_max(i) to be max money.Suppose there exists another rob_max'(i) 
The algoritm evaluates the recurrence rob\_max(i),Note that since we evaluate rob\_max(i) as i increases from 1 to n,all values for subproblems referenced by the recurrence for rob\_max(i) have already been computed.At the end,our algorithmlreturns the maximum value in the rmax array.
\subsection{Code}

\begin{algorithm}[H]
\caption{Money robbing} \label{Dynamic Programming}
\begin{lstlisting}[]

#include <iostream>
#include <cstdio>
#include <cstdlib>

using namespace std;

int max(int a,int b)
{
    return a>b ? a:b;
}

int rob_max(int a[],int n) //n stand for the size of array
{
    int rmax[n];
    if(n==1) return a[0];
    else if(n==2) return max(a[0],a[1]);
    else
    {
        rmax[0] = a[0];
        rmax[1] = max(a[0],a[1]);
        for(int i=2;i<n;i++)
        {
            rmax[i] = max(rmax[i-2]+a[i],rmax[i-1]);
        }
    }
    return rmax[n-1];
}

int main()
{
    //test cases;
    int a[5] = {1,3,4,2,1};
    int b[4] = {50,1,1,50};
    int c[8] = {10,13,23,17,6,11,18,16};
    cout<<rob_max(a,5)<<endl;
    cout<<rob_max(b,4)<<endl;
    cout<<rob_max(c,8)<<endl;

    //If all houses are in a circle
    cout<<max(rob_max(&c[1],7),rob_max(c,7))<<endl;
    return 0;
}
\end{lstlisting}
\end{algorithm}
\subsection{Complexity of Algorithm}
Analysis function rob\_max,there exist only one for loop,from 2 to n,so time complexity is O(n).And we use one array rmax[n] to store the optimal result for every step,
so the space complexity is O(n)
%=================================================================================================== %

\section{Minimum path sum}
Find the minimum path sum of a triangle from top to bottom. Each step you may move to adjacent numbers on the row below.
For example, given the following triangle:

\centerline{2}
\centerline{3 4}
\centerline{6 5 7}
\centerline{4 1 8 3}

The minimum path sum from top to bottom is 11 ( i.e., 2 + 3 + 5 + 1 = 11).
\subsection{Optimal subproblems And DP equation}
If we use two-dimensional array a[n][n] to store the input triangl,and layer i will have i nodes.Denote the optimal solution value as minsum[i][j],which means the minimum sum when reach the current node.The node a[i][j] can come from a[i-1][j-1] and a[i-1][j],and a[i][0] can only from a[i-1][0],a[i][i-1] can only come from a[i-1][i-1].\\
So,we can define the optimal sub-structure property:\\$$
minpath\[i\]\[j\] =

minsum\[i-1\]\[j\]+a\[i\]\[j\] &\
minsum\[i-1\]\[j-1\]+a\[i\]\[j\] &\
min(minsum\[i-1\]\[j-1\],minsum\[i-1\]\[j\])+a\[i\]\[j\] &

$$

Proof
-----

The algoritm evaluates the recurrence minsum\[i\]\[j\],Note that since
we evaluate minsum\[i\]\[j\] as i increases from 1 to n and j increase
from i to n,all values for subproblems referenced by the recurrence for
minsum\[i\]\[j\] have already been computed.And every time we chose the
minimum one.At the end,our algorithmlreturns the minimum value in the
minsum array.Suppose there exists another minsum’\[i\]\[j\],there must
be more mininum minsum\[i-1\]\[j-1\] or minsum\[i-1\]\[j\],which confict
with our define.

Code
----

\[H\]

    #include <iostream>
    #include <cstdio>
    #include <cstdlib>
    #include <climits>
    using namespace std;

    int a[4][4];
    int minsum[4][4];
    int n;

    int min(int a,int b)
    {
        return a<b ? a:b;
    }

    int minpath()
    {
        int m=INT_MAX; 
        minsum[0][0]=a[0][0];
        for(int i=1;i<n;i++)
            for(int j=0;j<=i;j++)
            {
                if(j==0) minsum[i][j] = minsum[i-1][j]+a[i][j];
                else if(j==i) minsum[i][j] = minsum[i-1][j-1]+a[i][j];
                else
                    minsum[i][j] = min(minsum[i-1][j],minsum[i-1][j-1]) + a[i][j];
            }
        for(int k=0;k<n;k++)
            m = min(m,minsum[n-1][k]);
        return m;
    }

    int main()
    {
        //test case
        n=4;
        a[0][0]=2;
        a[1][0]=3;a[1][1]=4;
        a[2][0]=6;a[2][1]=5;a[2][2]=7;
        a[3][0]=4;a[3][1]=1;a[3][2]=8;a[3][3]=3;

        cout<<minpath()<<endl;
    }

Complexity of Algorithm
-----------------------

Analysis function minpath(),we travelsal every node once.So the time
complexity is O($n^2$).we use two-dimensional array to store every
optimal sub-problems.So the space complexity is O($n^2$)

Decoding
========

A message containing letters from A-Z is being encoded to numbers using
the following mapping:\

A: 1

B: 2

...

Z: 26

\
\
Given an encoded message containing digits, determine the total number
of ways to decode it. For example, given encoded message “12”, it could
be decoded as “AB” (1 2) or “L” (12). The number of ways decoding “12”
is 2.

Optimal subproblems And DP equation
-----------------------------------

By Observing the encode,we can find that,when decoding,Only two
neighboring characters can combian.And character ’0’ can’t be divided
alone.So we should judge whether the character can be divide
alone,whether can combian with front character.Denote the optimal
solution value as count\[n\] which means the most solutions of
decoding.\
So,we can define the optimal sub-structure property:\
$$count[i] = \begin{cases}
    count[i-1] & \text{can divide} \\
    0 & \text{can't divide} \\
    count[i]+count[i-2] & \text{can combian} \\
    \end{cases}$$

Proof
-----

The algoritm evaluates the recurrence count\[i\],Note that since we
evaluate count\[i\] as i increases from 1 to n,all values for
subproblems referenced by the recurrence for count\[i\] have already
been computed.At the end,our algorithmlreturns the count of solutions in
the count\[n\] array.

Code
----

\[H\]

    #include <iostream>
    #include <cstdio>
    #include <cstdlib>
    #include <cstring>
    using namespace std;

    bool cancom(char a,char b)
    {
        if(a=='1') return true;
        else if(a=='2' && b<='6') return true;
        else
            return false;
    }
    int numdecode(char *s)
    {
        int len = strlen(s);
        int count[len+1];

        count[0]=1;
        count[1]=1;

        if(len==0) return 0;
        if(s[0]=='0') return 0;
        if(len==1) return 1;
        for(int i=2;i<=len;i++)
        {
            //cannot divide
            if(s[i-1]=='0')
                count[i]=0;
            else
                count[i]=count[i-1];
            if(cancom(s[i-2],s[i-1]))
            {   
                cout<<"here"<<endl;
                count[i]+=count[i-2];
            }
            if(count[i]==0) return 0;
        }
        return count[len];
    }

    int main()
    {
        char s[100];
        while(~scanf("%s",s))
        {
            cout<<numdecode(s)<<endl;
        }
        return 0;
    }

Complexity of Algorithm
-----------------------

Analysis function numdecode(),we only use one for loop tocalculate the
solutions of decode,so the time complexity is O(n).And we use
one-dimensional array to store the optimal sub-problem solutions,so the
space complexity is O(n).

Maximum profit of transactions
==============================

Say you have an array for which the i-th element is the price of a given
stock on day i. Design an algorithm and implement it to find the maximum
profit. You may complete at most two transactions. Note: You may not
engage in multiple transactions at the same time (ie,you must sell the
stock before you buy again).

Optimal subproblems And DP equation
-----------------------------------

For this problem,we can consider more simple problem.Suppose we can
complete only one transaction.we denote p1\[n\] to store maximum
profit,define mmin to maintain the minimum stock for every day i.max1
maintain the max profit for current day.Define stock\[n\] for input.

So,we can define the optimal sub-structure property:\

p1\[i\] = max(max1,stock\[i\]-mmin)

Now talk about this problem,we can complete at most two transactions.If
we complete two transactions,the max profit must come from day 1 to k
and day k+1 to n.So we need to calculate max profit from day k to n(k
can be 1 to n).It’s similar to calculate max profit for day 1 to n,just
from day n to 1 to calcute.We use p2\[n\] to store it.P\[i\] means the
max profit for day i to n.And we calculate the max vaule of p1\[k\] and
p2\[k+1\].

Code
----

\[H\]

    int maxprofit(int* p, int size) {

       int max1 = 0; int mmin=INT_MAX; int p1[size];
        for(int i=0;i<size;i++)
        {
            if(p[i] < mmin) mmin = p[i];
            int c = p[i]-mmin;
            if(c>max1) max1=c;
            p1[i]=max1;
        }

        int max2=0; int mmax=INT_MIN; int p2[size];
        for(int i=size-1;i>=0;i--)
        {
            if(p[i] > mmax) mmax=p[i];
            int c=mmax-p[i];
            if(c>max2) max2=c;
            p2[i]=max2;
        }

       int max_result = 0;
       for(int k=0;k<size-2;k++)
       {
           int sum = p1[k]+p2[k+1];
           if(sum>max_result)
               max_result= sum;
       }
       return max_result > max1 ? max_result: max1;
    }

    int main()
    {
        int a[4]={1,5,1,5,6};
        cout<<maxprofit(a,5)<<endl;
    }

Complexity of Algorithm
-----------------------

Analysis function maxprofit(),we use three for loop independent.So time
complexity is O(n).And use p1 and p2 to store the max profit,the space
complexit is O(n).
