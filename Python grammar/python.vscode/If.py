# if
# 조건에 따라 동작이 달라지는 것, 이것을 프로그래밍에서 "분기"라고 함.
# 코드에서 분기는 if 를 사용하며 기본적인 형식은 이렇습니다.
# 값을 비교하기 위해서는 = 을 2번 써야한다.
# if 조건문의 끝에는 콜론(:) 이 붙습니다. 
# if 위치를 기준으로 공백(스페이스) 4칸씩 들여쓰기를 해야 합니다. 
# if 조건:
    # 실행 명령문

# weather 변수에는 "비"라는 값이 들어가있고, if 를 통해서 변수의 값이 "비"인지를 확인하여 맞다면 "우산을 챙기세요" 라는 값을 출력합니다.
Weather = "비"

if Weather == "비":
   print("우산을 챙기세요.")


# if 는 처음 딱 1번만 사용할 수 있지만 elif 는 필요한 만큼 여러 번 사용할 수 있습니다.
# elif 도 if 와 마찬가지로 끝에 콜론(:) 을 붙이고 실행 명령문들은 모두 들여쓰기를 해주어야 합니다.
# if 조건1:
    # 실행 명령문1
# elif 조건2:
    # 실행 명령문2
# elif 조건3:
    # 실행 명령문3

Weather = "미세먼지"

if Weather == "비":
   print("우산을 챙기세요.")

elif Weather == "미세먼지":
     print("마스크를 챙기세요.")

# 비도 안오고 미세먼지도 없을 때 뭔가를 출력해보겠습니다. 
# if 와 elif 들의 모든 조건에 해당하지 않을 때 어떤 명령을 실행하기 위해서는 else 를 사용합니다.
Weather = "맑음"

if Weather == "비":
   print("우산을 챙기세요.")

elif Weather == "미세먼지":
     print("마스크를 챙기세요.")

else:
     print("준비물이 필요없어요.")     


# input() 은 프로그램 실행 시점에 사용자로부터 어떤 값을 입력받는 용도로 사용합니다.   
# 사용자가 값을 입력하고 엔터를 치면 그 값은 항상 "문자열" 형태로 변수에 저장이 됩니다.  
Weather = input("오늘 날씨는 어때요?")
if Weather == "비":
   print("우산을 챙기세요.")
elif Weather == "미세먼지":
     print("마스크를 챙기세요.")
else:
     print("준비물이 필요없어요.")


# 우산은 꼭 비가 올 때만 챙겨야하는 준비물은 아닌 것 같네요. 
# 눈이 많이 오는 날에도 우산을 챙길 필요가 있겠지요? 그럴 때는 if 조건을 이렇게 변경하면 됩니다.
Weather = input("오늘 날씨는 어때요?")
if Weather == "비" or Weather == "눈":
   print("우산을 챙기세요.")
elif Weather == "미세먼지":
     print("마스크를 챙기세요.")
else:
    print("준비물이 필요없어요.")


# 기온(temp)을 입력받아서 조건에 따른 처리
# 사용자로부터 정수 형태의 기온을 받는다고 가정
# input() 은 항상 문자열로 인식한다고 했으니 정수형으로 변환하기 위해 int()로 input()을 감싸줌.
temp = int(input("기온은 어때요.?"))
if 30 <= temp:  # 30 도 이상
    print("너무 더워요. 나가지 마세요.")
elif 10 <= temp and temp < 30:  # 10도 이상 30도 미만
     print("괜찮은 날씨에요.") 
elif 0 <= temp and temp < 10:   # 0도 이상 10도 미만, # elif 0 <= temp < 10:
     print("외투를 챙기세요.")
else:   # 그 외의 모든 경우 (0도 미만이면)
    print("너무 추워요. 나가지 마세요")