# [Do it! 실습 2C-2] 리스트의 모든 원소를 ​​enumerate 함수로 스캔하기
x = ['John', 'George', 'Paul', 'Ringo']

for i, name in enumerate(x):
    print(f'x[{i}] = {name}')


# [Do it! 실습 2C-2] 리스트의 모든 원소를 ​​enumerate 함수로 스캔하기
y = ['John', 'George', 'Paul', 'Ringo']

for i, name in enumerate(y):
    print(f'x[{i}] = {name}')


# [Do it! 실습 2C-3] 리스트의 모든 요소를 ​​enumerate 함수로 스캔(1부터 카운트)
z = ['John', 'George', 'Paul', 'Ringo']

for i, name in enumerate(z, 1):
    print(f'{i}번째 = {name}')


# [Do it! 실습 2C-4] 리스트의 모든 원소를 ​​스캔하기(인덱스 값을 사용하지 않음)
a = ['John', 'George', 'Paul', 'Ringo']

for i in a:
    print(i)