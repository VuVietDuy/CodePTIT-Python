# Python

## 1. Tổ chức code
- Không cần dấu ; cuối câu lệnh
- Tổ chức mã dựa trên thụt lề
- Không thể sử dụng khoảng trắng một cách tự do ngoài các dòng trống
- Các khối mã được tạo bằng cách thụt lề chứ không phải dấu {}
- Tip: Tab thụt lề sang trái, Shift + Tab thụt lề sang trái
- Định dạnh file .py
- Nên tách định nghĩa của def và Class với các phần trên bằng 2 dòng trống, và các method trong Class cách nhau 1 dòng trống
- Nên nhóm các lệnh import theo thứ tự:
  - Các thư viện tiêu chuẩn như os, sys
  - Các thư viện bên thứ 3
  - Các module/thư viện local
- Nên đặt tên theo quy tắc
  - Class SomeExampleClass
  - def some_example_function
  - CONSTANT_STRING = "STRING"

## Variables
- Python has no command for declaring a variable, a variable is create the moment you first assign a value to it.
- Var do not need to be declared with any particular type, and can even change type after they have been set

## Data Types
Built-in Data Types
- Text Type: `str`
- Numeric Types: `int`, `float`, `complex`
- Sequence Types: `list`, `tuple`, `range`
- Mapping Type: `dict`
- Set Types: `set`, `frozenset`
- Boolean Type:	`bool`
- Binary Types:	`bytes`, `bytearray`, `memoryview`
- None Type:	`NoneType`
