import heapq
import networkx as nx
import matplotlib.pyplot as plt

def dijkstra(graph, source, target):
    distances = {node: float('inf') for node in graph}
    distances[source] = 0
    previous = {node: None for node in graph}

    # 使用堆来选择距离最小的节点
    heap = [(0, source)]

    while heap:
        current_distance, current_node = heapq.heappop(heap)

        # 如果当前节点已经处理过，跳过
        if current_distance > distances[current_node]:
            continue

        if current_node not in graph:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # 如果找到更短的路径，更新距离并将邻居节点加入堆
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(heap, (distance, neighbor))

    # 构造从源节点到目标节点的最短路径
    path = []
    current_node = target
    while current_node is not None:
        path.insert(0, current_node)
        current_node = previous[current_node]

    return distances[target], path

# 从用户输入获取图
graph = {}
num_edges = int(input("请输入边的数量："))

for _ in range(num_edges):
    edge = input("请输入边（格式：起点 终点 权重）：").split()
    start, end, weight = edge[0], edge[1], int(edge[2])

    if start not in graph:
        graph[start] = {}
    if end not in graph:
        graph[end] = {}

    graph[start][end] = weight

# 从用户输入获取源节点和目标节点
source_node = input("请输入源节点：")
target_node = input("请输入目标节点：")

# 运行Dijkstra算法
distance, path = dijkstra(graph, source_node, target_node)

# 输出最短距离和路径选择
print(f"从节点 {source_node} 到节点 {target_node} 的最短距离为 {distance}，路径选择为 {path}")

# 创建图形对象
G = nx.DiGraph()

# 添加边
for start, neighbors in graph.items():
    for end, weight in neighbors.items():
        G.add_edge(start, end, weight=weight)

# 绘制图形
pos = nx.spring_layout(G)
nx.draw_networkx(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=12, font_weight='bold', arrows=True)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# 绘制最短路径
edge_colors = ['red' if (u, v) in zip(path, path[1:]) else 'gray' for u, v, _ in G.edges(data='weight')]
nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color=edge_colors, arrows=True)

# 显示图形
plt.title("Shortest Path")
plt.axis('off')
plt.show()