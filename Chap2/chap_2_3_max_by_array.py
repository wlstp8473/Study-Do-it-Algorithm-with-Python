# [Do it! 실습 2-2] 시퀀스 원소의 최댓값 출력하기

# Any: 어떤 자료형이든 허용한다는 의미 (max_of()의 매개변수의 자료형)
# Sequence: 리스트나 튜플처럼 원소가 순서대로 나열된 자료형 (max_of()의 반환값 자료형)
from typing import Any, Sequence

def max_of(a: Sequence) -> Any:
    """시퀀스 a에 저장된 원소 중 최댓값을 반환한다."""

    maximum = a[0] # 첫 번째 원소를 임시 최댓값으로 설정해, 최댓값을 구하면 n-1만큼 비교

    # 첫 번째 원소는 이미 maximum에 저장했으므로 인덱스 1부터 시작한다.
    for i in range(1, len(a)):

        if a[i] > maximum:
            maximum = a[i]

    # 모든 원소의 비교가 끝나면 최댓값을 반환한다.
    return maximum


# 이 파일을 직접 실행했을 때만 아래 코드를 실행한다, 다른 모듈에서 참조시에는 실행 X. (모듈 객체 __name__를 사용)
if __name__ == '__main__':
    print('배열의 최댓값을 구합니다.')

    num = int(input('원소 수를 입력하세요: '))

    # 원소가 num개인 리스트를 만드는데, 아직 값을 입력받지 않았으므로 모든 원소를 None으로 초기화한다.
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]를 입력하세요: '))

    print(f'최댓값은 {max_of(x)}입니다.')
