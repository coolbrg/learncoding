# Write a program to ask a question and measure the time taken.
# Ask 5 questions and calculate total time take and score out of 5

import time

QNS = [
    "What is 10 + 17 ? ",
    "What is 90 / 5 ? ",
    "10 + 2/2 - 5 = ? ",
    "8*9 - 5*2 = ? ",
    "75/15 + 30*5 = ? "
]

ANS = [
    27,
    18,
    6,
    62,
    155
]

total_time = 0
correct_answers = 0

for i, qns in enumerate(QNS):
    start = time.time()
    ans = input(qns)
    end = time.time()
    diff = end - start

    total_time += diff

    if int(ans) == ANS[i]:
        print("Correct! That took %.2f seconds." % diff)
        correct_answers += 1
    else:
        print("That's not corrent.")

score = correct_answers/len(QNS) * 100
print("Correctness percentage: {}.".format(score))
print("Total Time: {:.2f} seconds.".format(total_time))
