#if语句的测试
__author__ = 'weijie'
number = 23
guess = int(input('Enter an integer : '))
if guess == number:
    print('Congratulations, you guessed it.') # 新块开始处
    print('(but you do not win any prizes!)') # 新块结束处
elif guess < number:
    print('No, it is a little higher than that') # 另一个块
    # 你可以在一个块里做任何你想做的。。。
else:
    print('No, it is a little lower than that')
    # 只有guess > number 才会执行到此处
print('Done')