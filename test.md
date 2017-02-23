# Тестовое задание Python

1. Дан словарь:
  ```python
  d = {1: 2, 3: 4}
  ```
  Сколько параметров, каких типов и значений передадутся при вызове функций:
  ```python
  func1(d)
  func2(*d)
  func3(**d)
  ```
  
  ответ:
 ```
d = {1: 2, 3: 4}

print
def func1(arg):
	print arg, type(arg)
	print type(arg)

func1(d)

print
def func2(*args):
	print args, type(args)
	for arg in args:
		print type(arg)
    
func2(*d)

print
d = {'1': 2, '3': 4}

def func3(**kwargs):
	print kwargs, type(kwargs)
	for key in kwargs:
		print type(key), kwargs[key]

func3(**d) 
```

2. Значения какого типа будет содержать переменная `y` в следующем коде:
  ```python
  x = {1: 2, 3: 4}
  y = x.items()
  ```
  
  ответ:
  ```
  print type(y)  # python2.7 <type 'list'>
  print(type(y)) # python3.4 <class 'dict_items'>
  ```


3. Что напечатает данная программа:
  ```python
  x = [[]]*3
  x[0].append('a')
  x[1].append('b')
  x[2].append('c')
  x[0] = ['d']
  print x
  ```
  
  ответ:
  ```
  [['d'], ['a', 'b', 'c'], ['a', 'b', 'c']]
  ```


4. Напишите декоратор, который печатает результат выполнения функции.

ответ:
```
def decorator(f):
    def wrapper(*argv):
        print f(*argv)
    return wrapper
    
@decorator
def sum(a,b):
	return a + b

sum(2,3)
```

5. Напишите генератор, который производит чётные натуральные числа.

ответ:
генератор выводит нат.числа от 0 до N, учитвает тот факт что в send может быть послано отриц. или вещ. число

```
def f(N):
    current = 0
    
    while current <= N:
        reset = yield current

        if reset is not None:
            reset = int(reset)
            if reset < 0:
                current = -2


            elif reset % 2 == 0:
                current = reset - 2
                            
            else:
                current = reset - 1
        current += 2
        
g = f(21)

print(next(g))
print(next(g))
print('------')
print(g.send(-5.5))
print(next(g))
for e in g:
    print(e)
```

6. Что напечатает следующая программа? Почему?
  ```python
  funcs = []
  for i in range(5):
      def f():
        print i
      funcs.append(f)

  for f in funcs:
    f()
  ```
    
  ответ:
  ```
  4
  4
  4
  4
  4
  
  список заполнится ссылкой на функцию
  print funcs # [<function f at ...>, <function...>, ...
  print type(funcs[0]) #<type 'function'>
  
  после прохождения цикла i=4 меняться уже не будет, т.к. ф-я определа внутри цикла, а не наоборот
  ```

7. Напишите функцию, которая принимает на вход последовательность строк,
  отбрасывает из списка пустые строки в конце и начале, а в других местах списка
  идущие подряд несколько пустых строк заменяет на одну. Например:
  `["", "abc", "123", "", "x", "", "", "y", "", "" ]` должно превратиться в:
  `["abc", "123", "", "x", "", "y"]`.
    * Оформите её в виде модуля.
    * Сделайте так, чтоб функция могла работать с потенциально бесконечными
      генераторами (и была бы сама генератором, соответственно).
