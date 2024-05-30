from collections import deque

def create_adjacency_list():
   
    num_vertices = int(input("Enter the number of vertices: "))

 
    adjacency_list = [[] for _ in range(num_vertices)]

   
    num_edges = int(input("Enter the number of edges: "))
    print("Enter the edges in the format: vertex1 vertex2")

    for _ in range(num_edges):
        u, v = map(int, input().split())
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)

    return adjacency_list

def bfs(graph, start_vertex):
    visited = [False] * len(graph)
    queue = deque([start_vertex])
    visited[start_vertex] = True

    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")

        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True


def print_adjacency_list(adj_list):
    for i in range(len(adj_list)):
        print(f"{i}: {adj_list[i]}")

# Main function
if __name__ == "__main__":
    adj_list = create_adjacency_list()
    print("The adjacency list is:")
    print_adjacency_list(adj_list)
   
    start_vertex = int(input("Enter the starting vertex for BFS: "))
    print("BFS traversal starting from vertex", start_vertex, ":")
    bfs(adj_list, start_vertex)