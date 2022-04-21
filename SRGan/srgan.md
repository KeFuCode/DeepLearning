# 数据集

# 模型
```python
# 生成器：主要使用 SRResNet，生成高质量超分图像
# input: 低分辨率图像
# 第一部分：特征提取
# conv + Parametric Relu （将低分辨率图像映射到高分辨率图像, 最佳非线性函数之一）
# 第二部分：特征提取
# SRRetNet
    # conv + BN + PRelu + conv + BN + Elementwise Sum
    # ...
    # conv + BN + PRelu + conv + BN + Elementwise Sum
    # conv + BN + Elementwise Sum
# 第三部分：上采样
# conv + pixelShuffler*2 + Relu (上采样)
# conv + pixelShuffler*2 + Relu (上采样)
# conv
# output：×4高分辨率图像
```
```python
# 辨别器
# input: 
# conv + Leaky Relu(0.2)
# conv + BN + Leaky Relu
# 密集层
    # conv + BN + Leaky Relu
    # conv + BN + Leaky Relu
    # conv + BN + Leaky Relu
    # conv + BN + Leaky Relu
    # conv + BN + Leaky Relu
    # conv + BN + Leaky Relu
# Dense(1024)
# Leaky Relu
# Dense(1)
# Sigmoid
```