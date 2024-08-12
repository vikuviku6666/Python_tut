# from typing import TextIO
# from typing import Any
# from copy import deepcopy
# from dataclasses import astuple, dataclass, asdict, field
# import attr
# import time
# import unittest
# import pytest
# import asyncio
# import inspect
# from pprint import pprint
# import multiprocessing as mp
# from time_stuff import get_time, timestamp, kill_time
# import os


# numbers = [1, 2, 3, 3, 4, 5, 55]
# largest_number = numbers[1]

# for number in numbers:
#     largest_number = number if number > largest_number else largest_number

# print(largest_number)


# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# print(matrix[2][2])


# numbers.extend([2, 5, 6, 100, 300])
# numbers.pop()

# print(numbers)
# print(numbers.index(2))
# print("number_count:", numbers.count(3))

# print(50 in numbers)


# names = ["vin", "vin", "ami", "ami", "kun", "lun"]
# new_list = []
# for name in names:
#     if name not in new_list:
#         new_list.append(name)
# print(new_list)


# tuples_names = (3, 5, 6, 7, 7)

# print(tuples_names.count(7))


# coordinates = (1, 2, 3)
# coordinates1 = [1, 2, 3]

# x, y, z = coordinates
# x1, y1, z1 = coordinates1


# print("tuple unpacking", x, y, z)
# print("list unpacking", x1, y1, z1)


# # Dictionary

# customer = {"name": "Vinay", "age": 38, "is_verified": True}

# print(customer["age"])
# customer["hobbies"] = ["running", "Jogging", "Horse-riding"]
# print(customer)

# # convert input phone number into output strings in numbers

# phone_number = input("Enter your phone number: ")
# num = {
#     "0": "zero",
#     "1": "one",
#     "2": "two",
#     "3": "three",
#     "4": "four",
#     "5": "five",
#     "6": "six",
#     "7": "seven",
#     "8": "eight",
#     "9": "nine",
# }

# output = ""

# for number in phone_number:
#     output += num.get(number, "!") + " "

# print(output)

# file: TextIO = open('notes.txt')
# try:
#     content: str = file.read()
#     print(content)
# finally:
#     file.close()

# if some thing goes wrong the file closes automatically and the right
# way to open file and read the contents of the file
# with open(file='notes.txt') as file:
#     content: str = file.read()
# print(content)

# number: int = 20
# project_name: str = "vinay"

# print(type(number) is type(project_name))
# print(type(number) is not type(project_name))
# print(isinstance(number, str))
# print(isinstance(project_name, str))


# class Animal:
#     pass


# class Cat(Animal):
#     pass


# print(isinstance(Cat(), Animal))
# print(isinstance(Animal(), Cat))  # Don't compare like this

# letters: str = 'ABCDEFGH'

# for i, letter in enumerate(letters, start=1):
#     print(f'{i} : {letter}')

# a: list[int] = [1, 2, 3]
# b: list[int] = a
# # Here the list is referencing to the a list and just coping
# # the address of a

# print(f"{id(a)=}")
# print(f"{id(b)=}")

# a.append(111)
# b.append(222)

# print(f"{a=}")
# print(f"{b=}")


# a: list[Any] = [1, ['A', 'B'], 3]
# a1: list[Any] = [1, ['A', 'B'], 3]
# b: list[Any] = a.copy()  # shallo copy
# b1: list[Any] = deepcopy(a)  # deep copy

# b[1][0] = 'CHANGED'  # It will change the original list a
# b1[1][0] = 'CHANGED'  # It will not change the original list a

# print(f'{a=}')
# print(f'{b=}')
# print(f'{a1=}')
# print(f'{b1=}')

# caring about the type of exception we get
# when some thing goes wrong in the code


# def read_file(path: str) -> str | None:
#     try:
#         with open(file=path, mode="r") as file:
#             print(file.read())
#     except FileNotFoundError:
#         print(f'"{path}" not found, please try with a different file path')
#     except Exception as e:
#         print(f"New error encountered: {repr(e)}")


# read_file('notes.txt')

# Avoid bad variables names like below

# q: int = 10
# t: str = 'Welcome!'

# # make more descriptive which help other developers to recognise the variable
# # easily
# question: int = 10
# intro_text: str = 'Welcome!'


# @dataclass(frozen=True, order=True)
# class ManualComment:
#     id: int
#     text: str


# def main():
#     comment = ManualComment(1, "I Just scbscribed!")

#     # pprint(inspect.getmembers(ManualComment, inspect.isfunction))

#     print(comment)
#     print(astuple(comment))
#     print(asdict(comment))


# if __name__ == "__main__":
#     main()
# class Language:
#     def __init__(self, name: str, duration: int):
#         self.name = name
#         self.duration = duration

#     def course_started(self):
#         print(self.name, "course is started!")

#     def course_ended(self):
#         print(self.name, "course is ended!")

#     def course_description(self):
#         print(f"{self.name} runs {self.duration} weeks")


# def main():
#     swedish_language = Language("Swedish", 60)
#     swedish_language.course_started()
#     swedish_language.course_ended()
#     swedish_language.course_description()


# if __name__ == "__main__":
#     main()


# class Animal:
#     def __init__(self, name, weight) -> None:
#         self._name = name
#         self._weight = weight

#     @property
#     def weight(self):
#         print(f"{self._weight} is the weight of the {self._name}!")
#         return self._weight

#     @weight.setter
#     def weight(self, value):
#         print(f"{self._weight} is now {value} kg!")
#         self._weight = value

#     @property
#     def name(self):
#         print(f"{self._name} is being accessed!")
#         return self._name

#     @name.setter
#     def name(self, value):
#         print(f"{self._name} is now {value}!")
#         self._name = value


# if __name__ == "__main__":
#     tiger: Animal = Animal("Tiger", 500)
#     tiger.name = "Lion"
#     tiger.weight = 600
#     print(tiger.name)
#     print(tiger.weight)


# class Car:
#     def __init__(self, model, color) -> None:
#         self.model = model
#         self.color = color

#     def __str__(self):
#         return f"{self.model} ({self.color})"

#     def __repr__(self) -> str:
#         return f"Car(model={self.model}, color={self.color})"

#     def __eq__(self, value: object) -> bool:
#         return self.__dict__ == value.__dict__

#     def drive(self):
#         print(f"{self.model} is now driving.")


# if __name__ == "__main__":
#     car = Car("BMW", "Blue")
#     car1 = Car("BMW", "Blue")
#     print(car)
#     print(car.__repr__())
#     print(car == car1)


# Function
# def hello():
#     print("Hello")


# hello()


# class Lamp:
#     def __init__(self, name, model) -> None:
#         self.name = name
#         self.__model = model

#     def description(self):
#         print(self.name, self.__model)


# lamp = Lamp("Lamp", 1010)
# lamp.description()
# print(lamp.__model)

# start_time = time.perf_counter()
# j = 0
# for i in range(10**9):
#     j += 1

# print('Hello')
# time.sleep(1)

# end_time = time.perf_counter()

# print('Total time: ', end_time-start_time, 'seconds', j)


# def add_two_numbers_lol(a, b):
#     return a + b


# class TestGroup:
#     def test_one_plus_one_is_two(self):
#         a, b = 1, 2
#         actual = add_two_numbers_lol(a, b)
#         expected = 3

#         assert actual == expected


# async def fetch_data(data):
#     print("Fetching data...")
#     await asyncio.sleep(5)
#     return {"data": data}


# async def counter():
#     for i in range(10):
#         await asyncio.sleep(0.1)
#         print(i)


# async def main():
#     task1 = asyncio.create_task(fetch_data(1))
#     task2 = asyncio.create_task(counter())

#     data = await task1
#     print(data)
#     await task2


# asyncio.run(main())
