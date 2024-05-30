def create_adjacency_matrix():
    num_vertices = int(input("Enter the number of vertices: "))

 
    adjacency_matrix = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]

   
    num_edges = int(input("Enter the number of edges: "))
    print("Enter the edges in the format: vertex1 vertex2")

    for _ in range(num_edges):
        u, v = map(int, input().split())
        adjacency_matrix[u][v] = 1
        adjacency_matrix[v][u] = 1
#undirected graph
    return adjacency_matrix

# Main function
if __name__ == "__main__":
    adj_matrix = create_adjacency_matrix()
    print("The adjacency matrix is:")
    print(adj_matrix)