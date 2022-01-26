# Challenge Summary
<!-- Description of the challenge -->
1. Write a function called validate brackets
   Arguments: string
   Return: boolean
    representing whether or not the brackets in the string are balanced

There are 3 types of brackets:
Round Brackets : ()
Square Brackets : []
Curly Brackets : {}

## Whiteboard Process
<!-- Embedded whiteboard image -->

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
Big 0 time :(1)
      space : (n)

## Solution
<!-- Show how to run your code, and examples of it in action -->

Defined a Validating bracket class, that accept string input as parameter. Have an empty stack and a dictionary with keyy value pair which are the two sets of bracket, cury or parenthesis. created a for loop that goes through the string paremeter. if input str is in the dictionary it get aphended to the empty list. if it is not in the list, it get poped or/and if the len for the stack is 0 we return false. At the end of the function, if the stack is empty we return true, if not we return false.
