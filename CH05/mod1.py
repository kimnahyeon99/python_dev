# 함수 선언 : 네임스페이스 등록 -> 실행된다.
def sum_(a,b):
    return a + b

def safe_sum(a,b):
    if type(a)!=type(b):
        print('타입이 동일하지 않다')
        return None
    else: # 타입 동일 경우
        result = sum(a,b)
        
    return result

# 위 함수들을 테스트 코드
# mod1을 단독 실행할 때는 main 작동한다.
# __name__ : 어떻게 실행한 것인지를 저장
# __name__ = '__main__'이 대입된다.

# mod1이 단독 실행될 때만 테스트 코드 실행되게 하고 싶다.
if __name__ == '__main__':
    print(sum_(1,6))
    print(safe_sum(1,'a'))
    
# import 했을 때는 위 테스트 코드가 실행이 안된다.
