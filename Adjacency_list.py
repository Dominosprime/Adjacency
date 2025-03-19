import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class SocialNetwork:
    def __init__(self):
        self.graph = {}
        
    def add_user(self, user):
        if user not in self.graph:
            self.graph[user] = []
            
    def follow(self, user1, user2):
        if user1 in self.graph and user2 in self.graph:  # Fix here
            if user2 not in self.graph[user1]:
                self.graph[user1].append(user2)
    
    def find_mutual_friends(self, user1, user2):
        if user1 not in self.graph or user2 not in self.graph:
            return []
        return list(set(self.graph[user1]) & set(self.graph[user2]))
    
    def bfs(self, start):
        visited = set()
        queue = deque([start])
        
        print("BFS Traversal:")
        while queue:
            node = queue.popleft()
            if node not in visited:
                print(node, end=" ")
                visited.add(node)
                queue.extend(self.graph[node])
        print()
    
    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
            
        if start not in visited:
            print(start, end=" ")
            visited.add(start)
            for neighbor in self.graph[start]:
                self.dfs(neighbor, visited)
        return visited
    
    def visualize_network(self):
        G = nx.DiGraph()
        for user, followers in self.graph.items():
            for follower in followers:
                G.add_edge(user, follower)
                
        plt.figure(figsize=(8,6))  # Increase size
        pos = nx.spring_layout(G, seed=42)  # Improve layout
        nx.draw(G, pos, with_labels=True, node_color="lightblue",
                edge_color="gray", node_size=3000, font_size=12, arrows=True)
        
        plt.show(block=True)  # Keep window open

# Test Code
network = SocialNetwork()

network.add_user("Prince")
network.add_user("Mandeya")  
network.add_user("Samuel")
network.add_user("Kofi") 
    
network.follow("Prince", "Mandeya") 
network.follow("Prince", "Samuel") 
network.follow("Mandeya", "Kofi") 
network.follow("Samuel", "Kofi") 
    
mutual = network.find_mutual_friends("Prince", "Mandeya")
print("Mutual Friends between Prince and Mandeya:", mutual)

network.bfs("Prince")
print("DFS Traversal: ")
network.dfs("Prince")
print()

network.visualize_network()
