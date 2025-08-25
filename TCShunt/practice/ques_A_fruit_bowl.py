import math

# Function to calculate Euclidean distance
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Cross product helper for convex hull
def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

# Convex Hull using Monotone Chain
def convex_hull(points):
    points = sorted(set(points))  # Remove duplicates and sort
    if len(points) <= 1:
        return points

    # Build lower hull
    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    # Build upper hull
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    # Concatenate lower and upper hull, removing last point of each (duplicate)
    return lower[:-1] + upper[:-1]

if __name__ == "__main__":
    n = int(input().strip())
    points = []
    for _ in range(n):
        x, y = map(int, input().split())
        points.append((x, y))

    hull = convex_hull(points)

    # Calculate perimeter
    perimeter = 0
    for i in range(len(hull)):
        perimeter += distance(hull[i], hull[(i + 1) % len(hull)])

    print(round(perimeter))
