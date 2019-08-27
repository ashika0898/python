Python 3.7.3 (default, Apr  3 2019, 05:39:12) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> a="Hii Ashika"
>>> a
'Hii Ashika'
>>> b=how r u
SyntaxError: invalid syntax
>>> b="how are you"
>>> b
'how are you'
>>> a+b
'Hii Ashikahow are you'
>>> a*2
'Hii AshikaHii Ashika'
>>> a*b
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    a*b
TypeError: can't multiply sequence by non-int of type 'str'
>>> b*2
'how are youhow are you'
>>> len(a)
10
>>> len(b)
11
>>> len(a+b)
21
>>> a(0:4)
SyntaxError: invalid syntax
>>> a(4:10)
SyntaxError: invalid syntax
>>> a[0:4]
'Hii '
>>> a[4:10]
'Ashika'
>>> b[3:11]
' are you'
>>> b[1:5]
'ow a'
>>> a+b[0:10]
'Hii Ashikahow are yo'
>>> a+b[10:21]
'Hii Ashikau'
>>> a.upper
<built-in method upper of str object at 0x7f4991fe72b0>
>>> a.upper()
'HII ASHIKA'
>>> a.lower()
'hii ashika'
>>> b.upper()
'HOW ARE YOU'
>>> b.lower()
'how are you'
>>> a+b.upper()
'Hii AshikaHOW ARE YOU'
>>> a+b.lower()
'Hii Ashikahow are you'
>>> a.capitalize()
'Hii ashika'
>>> a.title()
'Hii Ashika'
>>> c+a+b
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    c+a+b
NameError: name 'c' is not defined
>>> c=a+b
>>> c
'Hii Ashikahow are you'
>>> c.capitalize()
'Hii ashikahow are you'
>>> c.title()
'Hii Ashikahow Are You'
>>> append a()
SyntaxError: invalid syntax
>>> a.replace[Hii,hello]
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    a.replace[Hii,hello]
NameError: name 'Hii' is not defined
>>> del a
>>> a
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> c
'Hii Ashikahow are you'
>>> a.sort()
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    a.sort()
NameError: name 'a' is not defined
>>> b.sort()
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    b.sort()
AttributeError: 'str' object has no attribute 'sort'
>>> a="Hii Ashika"
>>> a
'Hii Ashika'
>>> b
'how are you'
>>> c
'Hii Ashikahow are you'
>>> a.remove("Hii")
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    a.remove("Hii")
AttributeError: 'str' object has no attribute 'remove'
>>> a.remove[Hii]
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    a.remove[Hii]
AttributeError: 'str' object has no attribute 'remove'
>>> a.insert(Ashika,"R")
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    a.insert(Ashika,"R")
AttributeError: 'str' object has no attribute 'insert'
>>> a.pop()
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    a.pop()
AttributeError: 'str' object has no attribute 'pop'
>>> 
