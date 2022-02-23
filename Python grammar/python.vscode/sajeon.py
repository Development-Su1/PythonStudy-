# 사전(Dictionary)

# 사전은 중괄호로 둘러싸서 정의할 수 있으며, key 와 value 는 콜론(:) 으로 구분짓습니다. 
# 2개 이상의 데이터는 리스트와 마찬가지로 콤마(,)로 구분하시면 됩니다.
# { key1 : value1, key2 : value2, ... } > key 들은 중복값을 허용하지 않는 유일한 값으로 설정함.

# 예제) 멤버들이 목욕탕에 가서 각자 사물함 열쇠(key) 를 받고 사물함을 이용하는 것
# 사전 형태의 사물함인 cabinet 을 정의
# 유재석씨에게는 3번 사물함 열쇠를, 김태호씨에게는 100번 사물함 열쇠를 주도록 하겠습니다.
cabinet = {3 : "유재석", 100 : "김태호"}

# 각 사물함이 누구 것인지를 확인해볼까요? 
# 이 때는 대괄호 속에 key 값을 넣음으로써 key 에 해당하는 value 를 가져올 수 있습니다.
print(cabinet[3]) # 유재석 -> key 3 에 해당하는 value
print(cabinet[100]) # 김태호 -> key 100 에 해당하는 value

# 대괄호가 아닌 .get() 을 이용하는 방법도 있음.
print(cabinet.get(3))
print(cabinet.get(100))

# 대괄호[]를 이용해서 만약 정의되지 않은 key 를 전달하면 에러가 발생하고 프로그램이 바로 종료됨.
print(cabinet[5])
print("hi") # hi 출력 안됨.

#  get()은 에러가 발생하지는 않고 None 을 반환해주고, 프로그램은 계속 실행됨.
print(cabinet.get(5))
print("hi") # hi 출력됨.

# 5번 사물함은 아직 사용되고 있지 않으니 사람 이름 대신 "사용 가능" 이라는 기본값을 설정할 수가 있음.
# 만약 나중에 누군가 5번 열쇠를 받게 되면 그 사람의 이름이 출력되겠지만, 그 전에는 "사용 가능" 으로 나오게 됨.
print(cabinet.get(5, "사용가능"))

# 사물함이 사용중인지는 in 을 통해서 확인할 수 있음.
# key 값이 사전 자료형에 정의되어 있는지 여부를 알아보는 것임.
print(3 in cabinet) # True
print(5 in cabinet) # False

# key 는 정수형이 아닌 문자열도 가능
cabinet = {"A-3" : "유재석", "B-100" : "김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])


# 새손님
# 시간이 지난 후, 만약 유재석씨가 목욕을 마치고 집에 가려는데 
# 김종국씨가 목욕탕에 와서 유재석씨가 쓰던 "A-3" 사물함 열쇠를 받으면 어떻게 될까요?
# 이제 "A-3" 사물함은 김종국씨가 사용하게 되겠지요. 이 때는 대괄호를 이용해서 새로운 값을 업데이트 할 수 있습니다. 
# 조세호씨도 함께 왔다고 가정해볼까요? 
# 조세호씨는 아직 아무도 쓰지 않았던 "C-20" 사물함 열쇠를 받습니다.
# 김종국씨 때와 업데이트와 마찬가지로 대괄호를 이용하여 값을 설정하게 되지만, 
# 이 때는 업데이트가 아니라 새로운 key, value 를 추가하는 동작이 됩니다.
print(cabinet)   # cabinet = {"A-3" : "유재석", "B-100" : "김태호"}
cabinet["A-3"] = "김종국"    # key 에 해당하는 값이 있는 경우 업데이트
cabinet["C-30"] = "조세호"   # key 에 해당하는 값이 없는 경우 신규 추가
print(cabinet)

# 간 손님
# 김종국씨가 목욕을 마치고 사물함 열쇠를 반납해보도록 하겠습니다.
# 사전 자료형에서는 del 을 이용하여 key 값에 해당하는 key, value 데이터를 삭제할 수 있습니다.
del cabinet["A-3"]
print(cabinet)

# key 들만 출력
# 사장님은 사용중인 사물함이 어떤 게 있는지 확인하고 싶어합니다. 
# 이 때는 .keys() 를 이용하여 사전 내의 모든 key 들을 확인할 수 있습니다.
print(cabinet .keys())  # dict_keys(['B-100', 'C-30'])

# values 들만 출력
# 손님들은 누가 있는지 볼까요? 
# values() 를 통해 사전 내의 모든 value 들을 확인할 수 있습니다.
print(cabinet .values())  # dict_values(['김태호', '조세호'])

# key, values 쌍으로 출력
# 어떤 사물함을 어떤 손님이 쓰는지를 확인하려면 둘을 동시에 봐야겠네요.
# items() 를 이용하면 key, value 쌍으로 데이터를 확인할 수 있습니다.
print(cabinet .items())  # dict_items([('B-100', '김태호'), ('C-30', '조세호')])

# 목욕탕 폐장
# 이제 손님들에게 목욕탕 종료 안내를 하고 손님들이 가신 뒤에 문을 닫습니다.
# clear() 를 통해서 사전 내의 모든 데이터를 삭제해볼게요
cabinet.clear()
print(cabinet)  # {}