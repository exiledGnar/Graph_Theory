import networkx as nx
import matplotlib.pyplot as plt
def is_graph_sequence(sequence):
    sequence = sorted(sequence, reverse=True)  # 将序列按非递增顺序排序
    while sequence:
        if sequence[0] < 0 or sequence[0] >= len(sequence):
            return False
        for i in range(1, sequence[0] + 1):
            sequence[i] -= 1
            if sequence[i] < 0:
                return False
        sequence.pop(0)
        sequence = sorted(sequence, reverse=True)  # 重新排序
    return True

# 从用户输入获取序列
input_sequence = input("请输入序列，以逗号分隔：")
sequence = [int(x) for x in input_sequence.split(",")]

# 判断输入序列是否为图序列
if is_graph_sequence(sequence):
    print("是图序列")
    # 创建一个空的无向图
    G = nx.Graph()
    # 添加顶点
    G.add_nodes_from(range(1, len(sequence) + 1))
    # 添加边
    for i, degree in enumerate(sequence):
        neighbors = [j for j in range(i + 1, len(sequence)) if sequence[j] > 0]
        for _ in range(degree):
            if not neighbors:
                break
            neighbor = neighbors.pop(0)
            G.add_edge(i + 1, neighbor + 1)
            sequence[neighbor] -= 1
    # 绘制图形
    nx.draw(G, with_labels=True)
    plt.show()
else:
    print("不是图序列")
