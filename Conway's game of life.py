import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 棋盘大小
N = 100

# 随机生成初始状态
# 0 = 死细胞
# 1 = 活细胞
grid = np.random.choice([0, 1], size=(N, N), p=[0.8, 0.2])

def update(frame):
    global grid
    # 计算每个格子周围 8 个邻居中有多少活细胞
    neighbors = (
        np.roll(grid, 1, axis=0)
        + np.roll(grid, -1, axis=0)
        + np.roll(grid, 1, axis=1)
        + np.roll(grid, -1, axis=1)
        + np.roll(np.roll(grid, 1, axis=0), 1, axis=1)
        + np.roll(np.roll(grid, 1, axis=0), -1, axis=1)
        + np.roll(np.roll(grid, -1, axis=0), 1, axis=1)
        + np.roll(np.roll(grid, -1, axis=0), -1, axis=1)
    )
    # 康威生命游戏规则：
    # 1. 活细胞周围有 2 或 3 个活细胞 -> 继续活
    # 2. 死细胞周围恰好有 3 个活细胞 -> 复活
    # 3. 其他情况 -> 死亡
    grid = (
        ((grid == 1) & ((neighbors == 2) | (neighbors == 3)))
        | ((grid == 0) & (neighbors == 3))
    ).astype(int)
    image.set_data(grid)
    return [image]
# 创建图像
fig, ax = plt.subplots()
image = ax.imshow(grid, cmap="binary")
ax.set_title("Conway's Game of Life")
ax.set_xticks([])
ax.set_yticks([])
# 每 100 毫秒更新一次
animation = FuncAnimation(
    fig,
    update,
    interval=100,
    blit=True
)
plt.show()