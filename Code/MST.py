import matplotlib.pyplot as plt

# 定义边的类
class Edge:
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight

# 定义图的类
class Graph:
    def __init__(self, vertices):
        self.V = vertices  # 图的顶点数
        self.edges = []    # 存储边的列表

    # 添加边到图中
    def add_edge(self, src, dest, weight):
        edge = Edge(src, dest, weight)
        self.edges.append(edge)

    # 查找顶点的根节点
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    # 合并两个集合
    def union(self, parent, rank, x, y):
        x_root = self.find(parent, x)
        y_root = self.find(parent, y)
        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        else:
            parent[y_root] = x_root
            rank[x_root] += 1

    # 执行 Kruskal 算法，生成最小生成树
    def kruskal(self):
        result = []  # 存储最小生成树的边
        i = 0
        e = 0
        self.edges = sorted(self.edges, key=lambda edge: edge.weight)  # 按权重对边进行排序

        parent = []
        rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while e < self.V - 1:
            edge = self.edges[i]
            i += 1

            x = self.find(parent, edge.src)
            y = self.find(parent, edge.dest)

            if x != y:
                e += 1
                result.append(edge)
                self.union(parent, rank, x, y)

        return result

    # 绘制图形
    def draw_graph(self):
        plt.figure(figsize=(8, 4))

        # 绘制原始图的边
        for edge in self.edges:
            x1, y1 = self.vertices[edge.src]
            x2, y2 = self.vertices[edge.dest]
            plt.plot([x1, x2], [y1, y2], 'k-', linewidth=1, alpha=0.5)

        # 绘制最小生成树的边
        mst_edges = self.kruskal()
        for edge in mst_edges:
            x1, y1 = self.vertices[edge.src]
            x2, y2 = self.vertices[edge.dest]
            plt.plot([x1, x2], [y1, y2], 'b-', linewidth=2)

        # 绘制顶点
        for vertex, (x, y) in self.vertices.items():
            plt.plot(x, y, 'ro', markersize=8)

        plt.title("Original Graph and Minimum Spanning Tree")
        plt.axis('off')
        plt.show()

# 创建一个图的实例
g = Graph(8)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(1, 4, 8)
g.add_edge(2, 5, 12)
g.add_edge(3, 5, 7)
g.add_edge(3, 6, 9)
g.add_edge(4, 6, 11)
g.add_edge(5, 7, 14)
g.add_edge(6, 7, 3)

# 设置顶点坐标（可根据需要自行调整）
g.vertices = {
    0: (0, 0),
    1: (1, 1),
    2: (2, 0),
    3: (1, -1),
    4: (3, 2),
    5: (4, 0),
    6: (3, -2),
    7: (5, 1)
}

# 绘制图形
g.draw_graph()