# 튜플의 모든 원소를 ​​스캔하기(원소 수를 미리 파악)
x = ('John', 'George', 'Paul', 'Ringo')

for i in range(len(x)):
    print(f'x[{i}] = {x[i]}')


# 튜플의 모든 원소를 ​​enumerate 함수로 스캔하기
y = ('John', 'George', 'Paul', 'Ringo')

for i, name in enumerate(y):
    print(f'x[{i}] = {name}')


# 튜플의 모든 원소를 ​​enumerate 함수로 스캔하기(1부터 카운트)
z = ('John', 'George', 'Paul', 'Ringo')

for i, name in enumerate(z, 1):
    print(f'{i} 번째 = {name}')


# 튜플의 모든 원소를 ​​스캔하기(인덱스 값을 사용하지 않음)
a = ('John', 'George', 'Paul', 'Ringo')

for i in a:
    print(i)