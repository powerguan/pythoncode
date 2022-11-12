"""
Given a list of  numbers, sort them and output them one per line from smallest to largest.

Input Specification
The first line of the input contains a positive integer  no greater than , the number of numbers to follow.

Each line after will have a single positive integer less than .

Output Specification
Output the numbers in sorted order from smallest to largest, one per line.

Sample Input
Copy
4
4
3
2
1
Sample Output
Copy
1
2
3
4

[解析]
             2,  3,  1
第一轮: 2 =>  1,  3,  2
第二轮: 3 =>  1,  2,  3

"""

numbers = [100, 250, 500,100,600,700]

print("==== print original result ====")
for i in range(0, len(numbers)):
    print(f"{numbers[i]} ", end='')
print()

for i in range(0, len(numbers)-1):
    for k in range(i+1, len(numbers)):
        if (numbers[i] > numbers[k]):
            tmp = numbers[i]
            numbers[i] = numbers[k]
            numbers[k] = tmp
    print(f"**** After No.{i} result ****")
    for n in range(0, len(numbers)):
        print(f"{numbers[n]} ", end='')
    print()


print("==== print sorted result ====")
for i in range(0, len(numbers)):
    print(f"{numbers[i]} ", end='')
print()

