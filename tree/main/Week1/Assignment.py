# Week 1- Activity2: Sum of Even Numbers
# Write a Python program to calculate the sum of all positive even numbers between 1 and a given number n (inclusive). 
# Share your GitHub link here when you have done.
 
# Rewrite the program using a while loop.
# Also modify it to find the sum of positive odd numbers instead. Print all even numbers as well as the total sum.
 
def sumOfEvenNumbers():
    number = input("input value(PLEASE PUT POSITIVE INTENGER NUMBER)")
    n = int(number)
    if n < 1:
        return "Please input a number larger than 1"
    else:
        result = 0
        num = 1
        while num < n + 1:
            if num % 2 == 0:
                result += num
            num += 1
        # for num in range(1, n + 1):
        #     if num % 2 == 0:
        #         result += num
        return result


if __name__ == "__main__":
    answer = sumOfEvenNumbers()
    print("\n Final result:", answer)
