import re
# abcd, book, desk
# ca?e
# care, cafe, case, cave
# caae, cabe, cace, cade, ...

p = re.compile("ca.e")   # 정규식
# p는 패턴을 의미
# . (ca.e) : 하나의 문자를 의미 > care, cafe, case (O) | caffe (X)
# ^ (^de)  : 문자열의 시작 > desk, destination (O) | fade (X)
# $ (se$)  : 문자열의 끝 > case, base (O) | face (X)

m = p.match("case")   
print(m.group())
# ex) m = p.match("caffe")
#     print(m.group())  << 에러가 발생함 (.은 하나의 문자를 의미하는데 f가 두번 들어갔기 때문) 즉, 7행의 정규식과 매칭X

def print_match(m):
    if m:
        print("m.group():", m.group()) # 일치하는 문자열 반환
        print("m.string:", m.string) # 입력받은 문자열
        print("m.start():", m.start()) # 일치하는 문자열의 시작 index
        print("m.end():", m.end()) # 일치하는 문자열의 끝 index
        print("m.span():", m.span()) # 일치하는 문자열의 시작 / 끝 index
    else:
        print("매칭되지 않음")

m = p.match("careless")
print_match(m) 



def print_match(m):
    if m:
        print(m.group())

    else:
        print('매칭이 되지 않음.')    

m = p.match("careless")
print_match(m)        

# m = p.match("careless") # match : 주어진 문자열의 처음부터 일치하는지 확인
# print_match(m)

# m = p.search("good care") # search : 주어진 문자열 중에 일치하는게 있는지 확인
# print_match(m)

# lst = p.findall("good care cafe") # findall : 일치하는 모든 것을 리스트 형태로 반환
# print(lst)

# 1. p = re.compile("원하는 형태")
# 2. m = p.match("비교할 문자열") : 주어진 문자열의 처음부터 일치하는지 확인
# 3. m = p.search("비교할 문자열") : 주어진 문자열 중에 일치하는게 있는지 확인
# 4. lst = p.findall("비교할 문자열") : 일치하는 모든 것을 "리스트" 형태로 반환
