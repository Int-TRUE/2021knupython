# 기본 문자열
s2 = 'Hello, Haedal!'
print(s2)
S2 = "Hello, Haedal!"
print(S2)
s6 = '''Hello, Haedal!'''
print(s6)
S6 = """Hello, Haedal!"""
print(S6)

# 이스케이프 코드 (enter)
# \n, \t, \\, \', \"
longtext1 = """Hello, Haedal!
My name is Haedal Programming."""
print(longtext1)

longtext2 = 'Hello, Haedal!\nMy name is Haedal Programming.'
print(longtext2)

# String Interpolation
a = 123
new_q = f'{a}'
print(new_q) # 123 출력

# 문자열 옛날 방식
print(f'%s %s' % ('one', 'two')) # 문자열만 가능

# pyformat
print('{} {}'. format('one', 'two')) # 자료형 상관x

# f-string
a, b = 'one', 'two'
print(f'{a} {b}')
print(f'{b} {a}')

# example
name = "해달"
eng_name = "Haedal"
print("안녕하세요. {1}입니다. My name is {0}".format(eng_name, name))
print(f'안녕하세요. {name}입니다.')

# 문자열 인덱싱
a = "Hello Haedal!"
print(a[1]) # e

# 문자열 슬라이싱
a = 'Hello, Haedal!'
print(a[4:9])

# 문자열의 길이를 구하는 len()
print(len(a))

# 문자열의 최대, 최소를 구하는 max(), min()
# 아스키코드 -> 
a = '312'
b = 'bac'
print(min(a))
print(max(a))
print(min(b))
print(max(b))
print(a+b)
print(min(a+b)) # a+ b = '312bac'
print(max(a+b))

# 소문자, 대문자로 변환해주는 lower(), upper()
a = 'This is an Apple'
print(a.upper())
print(a.lower())

# 문자열을 구분자에 따라 나누는 split()
a = "안녕, 나는, 해달이야"
print(a.split(sep=','))
b = "안녕, 나는 해달이야"
print(b.split()) # 띄어쓰기가 구분자

# 여러개의 문자열 사이에 구분자를 넣어주는 join()
mylist = ['안녕', '나는', '해달']
mystring = '_'.join(mylist)
print(mystring) # 안녕_나는_해달