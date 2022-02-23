# 슬라이싱
# 파이썬에서는 슬라이싱이라는 것을 이용해서 데이터를 원하는 만큼 잘라서 가져올 수가 있습니다.
# n 번째 인덱스에 있는 문자 (또는 데이터) 하나만을 가져올 수가 있습니다. 이 때 사용되는 것이 바로 대괄호입니다.
# 문자열을 포함한 어떤 인덱스 값이 일반적으로 우리가 생각하는 것처럼 1 이 아닌 0 부터 시작합니다. 그래서 성별을 나타내는 1이란 값의 위치는 8이 아닌 7이 되는 것이다.
# 변수명[:인덱스] → 처음부터 인덱스 직전까지 슬라이싱
# 변수명[인덱스:] → 인덱스부터 끝까지 슬라이싱
# 변수명[:] → 처음부터 끝까지 슬라이싱

jumin = "000324-4459311"

print("성별 : " + jumin[7])
print("연 : " + jumin[0:2]) # 0 ~ 2 직전까지
print("월 : " + jumin[2:4]) # 2 ~ 4 직전까지
print("일 : " + jumin[4:6]) # 4 ~ 6 직전까지

print("생년월일 : " + jumin[:6]) # 처음부터 6직전까지
print("뒤 7자리 :" + jumin[7:]) # 7부터 끝까지
print("주민등록번호 :" + jumin[:]) # 처음부터 끝까지

# 처음이 아닌 뒤에서부터 슬라이싱을 할 필요도 있는데, 이럴 때는 음수를 이용하면 됩니다.
# 맨 처음의 인덱스는 [0] 이지만 맨 뒤의 인덱스는 [-1] 이라는 점 주의해주세요.

print("뒤 7자리 (뒤에서부터 계산) :" + jumin[-7:]) # 맨 뒤에서 7번째부터 끝까지