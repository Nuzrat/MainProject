

import math

def tsp_nearest_neighbor(cities, start):
    """
    Solves the TSP problem with a specified starting point using the Nearest Neighbor algorithm.
    """
    unvisited_cities = set(cities)
    unvisited_cities.remove(start)
    current_city = start
    route = [start]
    total_distance = 0
    while unvisited_cities:
        nearest_neighbor = min(unvisited_cities, key=lambda city: distance_between(current_city, city))
        route.append(nearest_neighbor)
        unvisited_cities.remove(nearest_neighbor)
        total_distance += distance_between(current_city, nearest_neighbor)
        current_city = nearest_neighbor
    total_distance += distance_between(current_city, start)
    route.append(start)
    return route, total_distance

def distance_between(city1, city2):
    """
    Returns the Euclidean distance between two cities.
    """
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# # Example usage:
# cities = [(3, 0), (5, 2), (2, 2), (5, 3)]
# start_city = (2, 2)
# shortest_route, shortest_distance = tsp_nearest_neighbor(cities, start_city)
# print("Shortest route starting from", start_city, ":", shortest_route)
# print("Shortest distance:", shortest_distance)
