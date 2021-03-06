# Quize) 당신은 Cocoa 서비스를 이용하는 택시 기사님입니다.
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

# 조건1 : 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
# 조건2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.
# (출력문 예제)
# [O] 1번째 손님 (소요시간 : 15분)
# [  ] 2번째 손님 (소요시간 : 50분)
# [O] 3번째 손님 (소요시간 : 5분) 
# ...
# [  ] 50번째 손님 (소요시간 : 16분) 

# 총 탑승 승객 : 2 분

# 출력 결과는 50명의 승객 모두에 대해 출력하되 매칭된 경우 [O] 로, 
# 매칭되지 않은 경우 [  ] 로 하며 해당 승객의 예상 소요 시간 정보도 포함하여 출력합니다.

from random import *

# 마지막 줄에 총 탑승 승객 수를 출력하기 위해서는 승객이 매칭될 때마다 어딘가 값을 저장해야 하므로 
# 코드 위쪽에서 탑승 승객 수 정보를 의미하는 카운트 변수 cnt 를 선언하고 기본값은 0 으로 지정합니다.
cnt = 0   # 총 탑승 승객 수
for customers in range(1,51):
    time = randrange(5,51)   # 시간 정보를 저장하는 time 변수, 5분 ~ 50분 사이의 소요 시간

# time 값을 비교하여 조건2에 제시된 5분 ~ 15분 사이의 승객만 매칭하겠습니다. 
# 조건에 맞으면 매칭을 시키고 매칭 정보를 출력 후 총 탑승 승객 수를 증가시키고, 
# 조건에 맞지 않으면 그냥 매칭 실패 정보만 출력하면 됩니다. 

if 5 <= time <= 15:   # 5분 ~ 15분 사이의 손님의 경우 매칭 성공
   print("[0] {0}번째 손님 (소요시간 : {1}분)" .format(customers, time))   # 성공 정보 출력
   cnt += 1   # 총 탑승 승객 수 증가 처리
else :
    print("[] {0}번째 손님 (소요 시간 : {1}분)" .format(customers, time))   # 실패 정보 출력

print("총 탑승객 : {0}분" .format(cnt))


# [총 정리]
from random import*
cnt = 0
for customers in range(1, 51):
    time = randrange(5, 51)
    if 5 <= time <= 15:
        print("[0] {0}번째 손님 (소요시간 : {1}분)" .format(customers, time))
        cnt += 1
    else:
        print("[] {0}번째 손님 (소요시간 : {1}분)" .format(customers, time))

print("총 탑승객 수 : {0}분" .format(cnt))