문자변수 = """
         띄어쓰기 하고 싶을 때,
         가독성 높이고 싶을 때...
"""
num = 10 #숫자를 값으로 가지는 변수 num
count = 100

# print(num + count, 문자변수)

list = ['사과' , '배']
# 데이터타입 확인
# print(type(list))
# 사칙연산자 * 곱하기는 복사 기능이 있음 
# print("HI" * 3)
# 첫 대문자 주의 할 것(사실확인인 경우일 시에만 해당)
a = True
b = False
#print(type(a))

#print( 10 > 1 )

#삼항식
age = 20
# 값1 if 조건식 else 값2 
#print("성인" if age <= 19 else "미성년자")

# tab문법
num = 10
if num > 5: 
    print("5보다 크다")
    print("나는 if식에 귀속되어있음")
print("나는 위의 if식과 상관없음")

score = 80

#if score >= 60:
    #print("합격")
#else:
    #print("불합격")

score = 75

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print(score,"점이라서 C이군요") #75점이라서 C군요
else:
    print("F")
