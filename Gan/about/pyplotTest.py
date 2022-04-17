import matplotlib.pyplot as plt
from scipy import rand
from torch import randn

#------------------------------------------------------------

# 开
plt.ion()   # something about continuous plotting
# 关
plt.ioff()
# 展示
plt.show()

#------------------------------------------------------------

# plt.cla() 初始化图片
plt.cla()
# plt.show()

#------------------------------------------------------------

# plt.plot(x:横坐标位置, y:纵坐标位置, c:颜色, lw:曲线宽度)
plt.plot([1,2,3], [1,2,3], c='#4AD631', lw=1, label='a')
plt.plot([1,2,3], [2,4,6], c='#74BCFF', lw=2, label='b')
plt.plot([1,2,3], [4,8,12], c='#FF9359', lw=3, label='c')

#------------------------------------------------------------

# plt.text(x:横坐标位置, y:纵坐标位置, fontdict={'size': 10}: 字体尺寸)
plt.text(2, 2, 'a', fontdict={'size': 10})
plt.text(2, 4, 'b', fontdict={'size': 20})
plt.text(2, 8, 'c', fontdict={'size': 40})

#------------------------------------------------------------

# plt.ylim((a, b)) 设置 y 轴的取值范围
plt.ylim((1, 10))

#------------------------------------------------------------

# plt.legend(loc='upper right', fontsize=10); (loc：放置位置， fontsize：字体尺寸)
plt.legend(loc='upper right', fontsize=10) # 'upper left', 'upper right', 'lower left', 'lower right'

#------------------------------------------------------------

# 重新绘制
plt.draw()

#------------------------------------------------------------

# 间隔显示：每隔一段时间，更新一次图画
plt.pause(0.01)

#------------------------------------------------------------

# 将绘制的图像展示出来
plt.show()