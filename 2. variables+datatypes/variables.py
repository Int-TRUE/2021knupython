# 홍길동씨 개인정보
name = "홍길동"
age = 25
height = 184.6
print(type(name)) # 자료형 확인
print(type(age))
print(type(height))

# 변수 이름 짓는 규칙
# 1. 영문자(대, 소문자 구분), 숫자, 언더바 한글 사용 가능
# Age, age, age3, Age_3, ag3e, 나이, 나이3,...

# 2. 첫 자리에는 숫자를 사용할 수 없다.
# 3age, 5_age,...

# 3. 파이썬에서 자체적으로 사용하고 있는 단어(예약어)는 사용할 수 없다.
#True, if, while...


# Convention : 협업할때 편리하도록 정해놓은 관습 느낌, 파이썬 PEP-8
# 1. 한 단어로 된 변수는 소문자로 적는다.
# age, good, name

# 2. 두 단어 이상의 변수는 언더바로 구분한다
# my_name, my_friend_name

# 3. 예약어와 충돌하는 경우에는 언더바를 붙인다
# if_, time_

# 4. 상수의 경우 대문자와 언더바를 혼용하여 쓴다
# TOTAL, PI, MAX_NUM, AVG