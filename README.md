# fate

Calculate important changes in your life by your birth year.

Usage:

    fate.py birth_year
    
Arguments:

    birth_year -- Your birth year.
  
Returns:
  + Your Master Number.
  + Your life milestone years.

## Numerology background
Your birth year can tell a lot of things about you, your personality, and even determine your fate. The sum of your birth year digits tells your Master Number, which is usually associated with life path, challenges, etc. This number also can be used to calculate the milestone years (the years you will have significant changes in your life).

Remember, **it's just a game!** 

## The algorithm
 + Take your year of birth and summarize its digits until you got a one-digit number. This number is your **Master Number**.
  *For example: if you were born in 1983, summarize 1 + 9 + 8 + 3 (21), and then sumarize 2 + 1 (3). Your Master Number is 3 in this case.*
 + Add your Master Number to your birth year, and you will get the first year in which you had changes in your life.
  *If you were born in 1983, add your master number to 1983 (1983 + 3 = 1986) 1986*
 + Now take this year, and calculate it's Master Number, and add it to this year.
 + Repeat the previous step as many times as you want.
 
In this program, I've added an upper limit of 80 years, which is a reachable and common human lifespan. On the next versions, I will add an option to change this limit to an arbitrary value, but it makes no sense to the algorithm.

## History
First I wrote the implementation of this program in PHP back in 2010, and hosted on a free service. Since the service has been discontinued, I've rewritten the whole program in Python, and moved to Github. My intention is to save it for myself, but if you like it, or want to develop, your contributions are welcome.

## Licence
Public domain. Everything is permitted.
