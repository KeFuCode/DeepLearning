from turtle import pen
import torch
import numpy as np
import torch.nn as nn

#------------------------------------------------------------

# torch.from_numpy()
a = [1, 2, 3]
# print(a)
# [1, 2, 3]

result_1 = np.array([1, 2, 3]) 
# print(result_1)
# [1 2 3]

result_2 = torch.from_numpy(result_1)
# print(result_2)
# tensor([1, 2, 3], dtype=torch.int32)

result_3 = result_2.float()
# print(result_3)
# tensor([1., 2., 3.])

#------------------------------------------------------------

# nn.Linear()
m = nn.Linear(2, 3)
# print(m)
# Linear(in_features=2, out_features=3, bias=True)

input = torch.randn(4, 2)
# print(input)
# tensor([[-1.5239, -0.0888],
#         [ 1.2870, -2.1956],
#         [-1.8883,  0.8138],
#         [ 0.5050,  0.5147]])

input = torch.randn(4, 2, requires_grad=True)
# print(input)
# tensor([[-1.1864,  1.8237],
#         [-0.5870,  0.0888],
#         [-1.4771, -0.7782],
#         [ 0.6174, -0.6089]], requires_grad=True)

result_4 = m(input)
# print(result_4)
# tensor([[-0.6737,  0.3011,  0.3564],
#         [ 0.8522, -0.5135, -0.5570],
#         [-0.9924,  0.3018,  0.7683],
#         [ 0.0198, -0.6410,  0.6874]], grad_fn=<AddmmBackward>)
#------------------------------------------------------------

# nn.Sigmoid()
m = nn.Sigmoid()
# print(m)
# Sigmoid()

input = torch.randn(2)
# print(input)
# tensor([ 2.1226, -1.5139])

output = m(input)
# print(output)
# tensor([0.8931, 0.1804])

#------------------------------------------------------------

# nn.ReLU()
m = nn.ReLU()
# print(m)
# ReLU()

input = torch.randn(2)
# print(input)
# tensor([ 0.5672, -0.9819])

output = m(input)
# print(output)
# tensor([0.5672, 0.0000])

#------------------------------------------------------------

# torch.log()
a = torch.randn(5)
# print(a)
# tensor([-0.8492,  2.1351, -0.3837,  1.8907, -0.0907])

b = torch.log(a)
# print(b)
# tensor([   nan, 0.7585,    nan, 0.6370,    nan])

#------------------------------------------------------------

# torch.mean()
a = torch.randn(1, 3)
# print(a)
# tensor([[ 0.4336, -1.1612, -0.6267]])

_a = torch.randn(3)
# print(_a)
# tensor([-0.1473, -0.8278, -1.0459])

b = torch.mean(a)
# print(b)
# tensor(-0.4515)

y = (0.4336 - 1.1612 - 0.6267) / 3
# print(y)
# -0.45143333333333335

#------------------------------------------------------------

# torch.detach()
a = torch.randn(1, 3)
# print(a)
# tensor([[ 0.1794,  0.4425, -0.7865]])
b = a.detach()
# print(b)
# tensor([[ 0.1794,  0.4425, -0.7865]])

#------------------------------------------------------------

# torch.nn.Sequential
G = nn.Sequential(                      # Generator
    nn.Linear(2, 3),            # random ideas (could from normal distribution)
    nn.ReLU(),
    nn.Linear(3, 4),     # making a painting from these random ideas
)
# print(G)
# Sequential(
#   (0): Linear(in_features=2, out_features=3, bias=True)
#   (1): ReLU()
#   (2): Linear(in_features=3, out_features=4, bias=True)
# )

D = nn.Sequential(                      # Discriminator
    nn.Linear(2, 3),     # receive art work either from the famous artist or a newbie like G
    nn.ReLU(),
    nn.Linear(3, 4),
    nn.Sigmoid(),                       # tell the probability that the art work is made by artist
)
# print(D)
# Sequential(
#   (0): Linear(in_features=2, out_features=3, bias=True)
#   (1): ReLU()
#   (2): Linear(in_features=3, out_features=4, bias=True)
#   (3): Sigmoid()
# )

#------------------------------------------------------------

# torch.nn.Sequential.parameters()
a = D.parameters()
# print(a)
# <generator object Module.parameters at 0x000001A118FB9C80>
b = G.parameters()
# print(b)
# <generator object Module.parameters at 0x000001A118FB9C80>

a = list(D.parameters())
# print(a)
# [Parameter containing:
# tensor([[ 0.3046,  0.5120],
#         [ 0.5427,  0.4600],
#         [ 0.0174, -0.6802]], requires_grad=True), Parameter containing:
# tensor([ 0.0405,  0.2917, -0.6328], requires_grad=True), Parameter containing:
# tensor([[ 0.3055,  0.4615,  0.1208],
#         [-0.0430, -0.4903, -0.0650],
#         [-0.4379, -0.3150, -0.0190],
#         [ 0.1814, -0.1719, -0.4915]], requires_grad=True), Parameter containing:
# tensor([0.4245, 0.2363, 0.0718, 0.3680], requires_grad=True)]
b = list(G.parameters())
# print(b)
# [Parameter containing:
# tensor([[-0.3607,  0.3183],
#         [ 0.4203, -0.2133],
#         [-0.3973,  0.2094]], requires_grad=True), Parameter containing:
# tensor([0.1282, 0.2172, 0.3175], requires_grad=True), Parameter containing:
# tensor([[ 0.3191,  0.3684,  0.2442],
#         [-0.5072, -0.4098, -0.0375],
#         [-0.2992, -0.4428, -0.3903],
#         [-0.0637,  0.3509,  0.1105]], requires_grad=True), Parameter containing:
# tensor([ 0.5584,  0.4543, -0.4590,  0.4794], requires_grad=True)]

#------------------------------------------------------------

# torch.optim.Adam

opt_D = torch.optim.Adam(D.parameters(), lr=0.0001)
# print(opt_D)
# Adam (
# Parameter Group 0
#     amsgrad: False
#     betas: (0.9, 0.999)
#     eps: 1e-08
#     lr: 0.0001
#     weight_decay: 0
# )
opt_G = torch.optim.Adam(G.parameters(), lr=0.0001)
# print(opt_G)
# Adam (
# Parameter Group 0
#     amsgrad: False
#     betas: (0.9, 0.999)
#     eps: 1e-08
#     lr: 0.0001
#     weight_decay: 0
# )

#------------------------------------------------------------

# torch.optim.Adam.zero_grad()
# 梯度初始化
# why? https://stackoverflow.com/questions/48001598/why-do-we-need-to-call-zero-grad-in-pytorch

a = torch.randn(1, 3)
# print(a)
# tensor([[ 0.9703,  2.9971, -0.9806]])
b = torch.optim.Adam([a], lr=0.0001)
# print(b)
# Adam (
# Parameter Group 0
#     amsgrad: False
#     betas: (0.9, 0.999)
#     eps: 1e-08
#     lr: 0.0001
#     weight_decay: 0
# )
c = b.zero_grad()
# print(c)
# None

#------------------------------------------------------------


