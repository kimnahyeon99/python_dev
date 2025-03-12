# 모듈안에 선언된 변수
PI = 3.141592

# 모듈안에 선언된 클래스
class Math:
    def solv(self,r):
        return PI * (r**2)
    
# 모듈안에 선언된 함수
def sum(a,b):
    return a+b

# 테스트
if __name__ == '__main__':
    print(PI)
    a = Math()
    print(a.solv(2))
    print(sum(PI,4.4))