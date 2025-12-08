import time
import math
MAX_NEIGHBORS = 4
INPUT = "input.txt"
start_time = time.perf_counter()
points_distance = []

def find_closest(id, matrix):
    (x, y, z) = matrix[id]
    for r in range(id, len(matrix)):
        if r == id:
            continue
        dist = abs(matrix[r][0] - x)**2 + abs(matrix[r][1] - y)**2 + abs(matrix[r][2] - z)**2
        points_distance.append((id, r, dist))
        



try:
    with open(INPUT, 'r') as file:
        coords = []
        total = 0
        for line in file:
            coords.append(list(map(lambda x: int(x), line.strip().split(','))))
        
        closest_points = [None] * len(coords)

        for i in range(len(coords)):
            find_closest(i, coords)

        closest_points = sorted(points_distance, key=lambda x: x[2])

        clusters = []
        main_cluster = set()
        main_cluster.add(closest_points[0][0])
        main_cluster.add(closest_points[0][1])

        for p in range(len(closest_points)):
            (a, b, d) = closest_points[p]
            add_to_main = False
            current_cluster = None
            if a in main_cluster or b in main_cluster:
                add_to_main = True

            for cluster in clusters:
                if a in cluster or b in cluster:
                    if add_to_main:
                        main_cluster.update(cluster)
                        clusters.remove(cluster)
                        continue
                    if current_cluster is not None:
                        current_cluster.update(cluster)
                        clusters.remove(cluster)
                        continue
                    current_cluster = cluster
                    current_cluster.add(a)
                    current_cluster.add(b)
                    clusters.remove(cluster)
                    continue
            if current_cluster is None:
                current_cluster = set()
                current_cluster.add(a)
                current_cluster.add(b)
                if add_to_main:
                    main_cluster.update(current_cluster)
        
            
            clusters.append(current_cluster)
            if len(main_cluster) == len(coords):
                print("All points clustered : " + str(coords[a][0] * coords[b][0]))
                break
        

    end_time = time.perf_counter()
    print(f"Execution time: {(end_time - start_time) * 1000} milliseconds")
            
except Exception as e:
    print(f"An error occurred: {e}")