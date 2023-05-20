import time
start_time = time.time()  # Record the starting time
N = int(input())
points = []
for i in range(N):
        x, y = map(int, input().split())
        points.append([x, y])
print(points)

end_time = time.time()  # Record the ending time
runtime = end_time - start_time  # Calculate the runtime
print("Runtime:", runtime, "seconds")