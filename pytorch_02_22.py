# -*- coding: utf-8 -*-
"""pytorch_02_22.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gEGV3ti5j6rChXb8FKxzJO1x1WIo5yyu

# Pytorch 기본
"""

import torch
torch.__version__

"""pytorch 사용 전에 torch에 import를 해 준다.
.__version__ 으로 해당 버젼을 확인할 수 있다.
"""

x = torch.empty(4,2)
print(x)

"""torch.empty(행,렬)을 통해 초기값이 없는 값의 텐서객체를 만들 수 있다.
초기화가 되지 않았기에 메모리를 잡긴 잡되, 기존에 해당 메모리에 있던 값이 딸려나와서 값이 들어있는 것처럼 출력된다.
"""

x = torch.randn(3,3)
print(x)

"""torch.randn(행,렬)을 통해 랜덤값이 할당된 텐서객체를 만들 수 있다."""

x = torch.zeros(3,3,dtype=torch.int)
print(x)

"""torch.zeros 를 통해 0으로 이뤄진 텐서 객체를 만들 수 있고, ',dtype=torch.데이터타입' 으로 데이터 타입 변환도 가능하다."""

x = torch.randn(2,2)
x = x.new_ones(4,4)
print(x)

"""텐서.new_ones(행,렬)로 ones행렬을 만들 수 있음. new는 특정 값을 다시 할당하겠다는 의미로 쓰임."""

x = torch.tensor([10,20,30,40,-40,5.5])
print(x)

"""torch.tensor() 를 통해 특정 값을 텐서형으로 바꿀 수 있다."""

x = torch.randn(2,2)
print(x)
x = torch.randn_like(x,dtype=torch.float)
print(x)

"""기존 x의 틀(2x2)를 유지하며 랜덤한 float값이 x에 들어감을 확인할 수 있음."""

print(x.size())

"""텐서.size()를 통해 해당 텐서의 크기를 알 수 있다.

텐서간의 연산을 하는 방법은 여러가지가 있다.

1.텐서1 + 텐서2  
2.torch.add(텐서1,텐서2)  
3.torch.add(텐서1,텐서2,out=제공텐서)  
   ㄴ 텐서 연산 결과를 인자로 제공  
4.텐서2.add_(텐서1)  
   ㄴ 결과가 텐서2+=텐서1 과 같음. in-place방식이라 함
"""

x = torch.randn(2,2)
y = torch.randn(2,2)
z = torch.empty(2,2)
print(x+y)
print(torch.add(x,y))
torch.add(x,y,out=z)
print(z)
y.add_(x)
print(y)

"""그 외의 연산은 다음과 같다.   
  
뺄셈 : - : torch.sub  
요소 별 곱셈 : * : torch.mul  
나눗셈 : / : torch.div  
내적(행렬 곱) : torch.mm (연산자 없음)

"""

x = torch.tensor([[3,3],[2,2]])
y = torch.tensor([[2,2],[1,1]])
z = torch.empty(2,2)
print(x-y)
print(torch.sub(x,y))
torch.sub(x,y,out=z)
print(z)
x = x.sub_(y)
print(x)

x = torch.tensor([[5,5],[3,3]])
y = torch.tensor([[2,2],[4,4]])
z = torch.empty(2,2)
print(x*y)
print(torch.mul(x,y))
torch.mul(x,y,out=z)
print(z)
x = x.mul_(y)
print(x)

x = torch.tensor([[10,20],[50,10]])
y = torch.tensor([[5,4],[10,5]])
z = torch.empty(2,2)
print(x/y)
print(torch.div(x,y))
torch.div(x,y,out=z)
print(z)
x = x.div(y)
print(x)

x = torch.randn(2,2)
y = torch.randn(2,2)
print(torch.mm(x,y))