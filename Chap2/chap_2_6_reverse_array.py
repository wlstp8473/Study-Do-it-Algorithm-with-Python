# [Do it! 실습 2-6] 뮤터블 시퀀스 원소를 역순으로 배치하기

# MutableSequence: 리스트처럼 원소를 변경할 수 있는 시퀀스 자료형을 의미한다.
from typing import MutableSequence


def reverse_array(a: MutableSequence) -> None:
    """변경 가능한 시퀀스 a의 원소 순서를 반대로 뒤집는다."""

    n = len(a)

    # 배열의 앞쪽 절반만 반복한다.
    # 한 번 교환할 때 앞쪽 원소와 뒤쪽 원소가 함께 바뀌므로 전체 길이의 절반만 반복하면 모든 원소가 역순으로 배치된다.
    for i in range(n // 2):

        # 앞에서 i번째 원소와 뒤에서 i번째 원소를 서로 교환한다.
        # a[i]         : 앞에서 i번째 원소
        # a[n - i - 1] : 뒤에서 i번째 원소
        a[i], a[n - i - 1] = a[n - i - 1], a[i]


# 이 파일을 다른 파일에서 import할 때는 실행하지 않고,직접 실행했을 때만 아래 코드를 실행한다.
if __name__ == '__main__':
    print('배열 원소를 역순으로 배치합니다.')

    nx = int(input('원소 수를 입력하세요: '))

    # 원소가 nx개인 리스트를 만드는데, 아직 원소의 값이 정해지지 않았으므로 None으로 초기화한다.
    x = [None] * nx

    for i in range(nx):
        x[i] = int(input(f'x[{i}]: '))

    # 리스트는 뮤터블 객체이므로 함수 안에서 변경한 결과가 함수 밖의 리스트 x에도 그대로 반영된다.
    reverse_array(x)

    print('배열 원소를 역순으로 배치했습니다.')

    for i in range(nx):
        print(f'x[{i}] = {x[i]}')