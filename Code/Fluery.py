import networkx as nx
import random
import matplotlib.pyplot as plt

def fleury_algorithm(graph):
    # 复制图以保留原始图
    graph = graph.copy()

    # 检查图中是否存在奇度顶点
    odd_degrees = [node for node, degree in graph.degree() if degree % 2 != 0]

    # 随机选择一个起始顶点
    start_vertex = random.choice(list(graph.nodes))

    # 初始化Eulerian路径，并将起始顶点加入路径中
    eulerian_path = [start_vertex]

    while graph.number_of_edges() > 0:
        current_vertex = eulerian_path[-1]

        # 检查当前顶点是否有未访问的边
        available_edges = [
            edge for edge in graph.edges(current_vertex) if edge not in eulerian_path
        ]

        if len(available_edges) > 0:
            # 如果当前顶点有未访问的边，选择其中一条边
            next_edge = random.choice(available_edges)
            next_vertex = next_edge[1]  # 下一个顶点是边的终点

            # 从图中删除选择的边
            graph.remove_edge(*next_edge)

            # 将下一个顶点加入Eulerian路径中
            eulerian_path.append(next_vertex)
        else:
            # 如果当前顶点没有未访问的边，则需要回溯到前一个顶点
            for i in range(len(eulerian_path) - 1, -1, -1):
                backtrack_vertex = eulerian_path[i]

                # 检查回溯顶点是否有未访问的边
                available_edges = [
                    edge
                    for edge in graph.edges(backtrack_vertex)
                    if edge not in eulerian_path
                ]

                if len(available_edges) > 0:
                    # 如果回溯顶点有未访问的边，选择其中一条边
                    next_edge = random.choice(available_edges)
                    next_vertex = next_edge[1]  # 下一个顶点是边的终点

                    # 从图中删除选择的边
                    graph.remove_edge(*next_edge)

                    # 在回溯顶点之后插入下一个顶点到Eulerian路径中
                    eulerian_path = (
                        eulerian_path[: i + 1] + [next_vertex] + eulerian_path[i + 1 :]
                    )
                    break

    return eulerian_path

# 创建一个图对象
G = nx.Graph()

# 添加节点到图中
G.add_nodes_from([1, 2, 3, 4, 5])

# 添加边到图中
G.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (3, 5), (4, 5)])

# 调用Fleury算法获取Eulerian路径
eulerian_path = fleury_algorithm(G)

# 转换Eulerian路径为边的列表
path_edges = [(eulerian_path[i], eulerian_path[i+1]) for i in range(len(eulerian_path)-1)]

# 绘制原始图和Eulerian路径
plt.figure(figsize=(8, 4))
plt.subplot(121)
nx.draw(G, with_labels=True, node_color='lightblue', node_size=500, font_size=12, width=1.5)
plt.title('Original Graph')

plt.subplot(122)
G_eulerian_path = G.edge_subgraph(path_edges)
nx.draw(G_eulerian_path, with_labels=True, node_color='lightblue', node_size=500, font_size=12, width=1.5)
plt.title('Eulerian Path')

plt.tight_layout()
plt.show()