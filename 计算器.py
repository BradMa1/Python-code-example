# 輸出标题
print("简易计算器")

# 通过用户输入获取运算的第一个数
num1 = int(input("输入第一个数字: "))
# 通过用户输入获取运算的第二个数
# 默认是字符串需要用int把字符转换为数组
num2 = int(input("输入第二个数字: "))

# 提示用户输入运算符
print("输入运算：+相加；-相减；*相乘；/相除")

# 获取用户输入的运算符号
choice = input("输入你的选择(+ - * /):")

# 如果是 +
if choice == '+':
   print(num1,"+",num2,"=", num1+num2)
# 如果是 -
elif choice == '-':
   print(num1,"-",num2,"=", num1-num2)
# 如果是 *
elif choice == '*':
   print(num1,"×",num2,"=", num1*num2)
# 如果是 /
elif choice == '/':
   print(num1,"÷",num2,"=", num1/num2)
# 其他輸入都是無效的
else:
   print("無效输入")

