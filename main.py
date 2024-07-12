from data import DataLoader

# Let's use this to get the static data
data_loader = DataLoader()
edges = data_loader.get_island_graph()

print(edges)
