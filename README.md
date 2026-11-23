# pairwise-ragdoll-joint-chain

## 领域

游戏、图形与多媒体

## 主题

布娃娃关节链

## 说明

帧率无关求解、骨骼回收与碰撞组。

初始状态下 `gameplay/ragdoll_joint_chain.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
