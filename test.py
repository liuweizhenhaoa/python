print('Hello World!')
msg = "1111111"
print(msg)

#!/usr/bin/python3
 
# 第一个注释
print ("Hello, Python!") # 第二个注释

'''
第三注释
第四注释
'''

if 1>0:
    print("true")
else:
    print("false")


str = "11111111" +\
    "2222222222222222222222"+\
        "33333333333"
print(str)

total = ['item_one', 'item_two', 'item_three',
        'item_four', 'item_five']

word = '字符串'
sentence = "这是一个句子。"
paragraph = """这是一个段落，
可以由多行组成"""
print(word)
print(sentence)
print(total)
print(paragraph)


str='Runoob'
 
print(str)                 # 输出字符串
print(str[0:-1])           # 输出第一个到倒数第二个的所有字符
print(str[0])              # 输出字符串第一个字符
print(str[2:5])            # 输出从第三个开始到第五个的字符
print(str[2:])             # 输出从第三个开始后的所有字符
print(str * 2)             # 输出字符串两次
print(str + '你好')        # 连接字符串
 
print('------------------------------')
 
print('hello\nrunoob')      # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义


input("\n\n按下 enter 键后退出。")


import sys; x = 'runoob'; sys.stdout.write(x + '\n')

# print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=""：
x="a"
y="b"
# 换行输出
print( x )
print( y )
 
print('---------')
# 不换行输出
print( x, end=" " )
print( y, end=" " )
print()