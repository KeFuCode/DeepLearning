# DeepLearning Note
## Gan
使用 pytorch 实现 Gan demo。  
**实现思路**  
Generator 是新手画家, Discriminator 是新手鉴赏家, 你是高级鉴赏家。  
你将著名画家的作品和新手画家的作品都给新手鉴赏家评定, 并告诉新手鉴赏家哪些是新手画家画的, 哪些是著名画家画的。  
新手鉴赏家就慢慢学习怎么区分新手画家和著名画家的画, 但是新手画家和新手鉴赏家是好朋友, 新手鉴赏家会告诉新手画家要怎么样画得更像著名画家, 新手画家就能将自己的突然来的灵感 (random noise) 画得更像著名画家。  
**参考链接**  
1.https://youtu.be/EPAIUW_A4sU  
2.https://mofanpy.com/tutorials/machine-learning/torch/GAN/

