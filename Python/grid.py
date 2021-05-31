import requests
import json

res = requests.get('http://localhost:1234').content.decode("utf8")
data = json.loads(res)

grid = data['maze']
for i in range(800 // 40):
    grid[0][i] = 1
    grid[1][i] = 1

grid[0][-1] = 1
grid[0][-2] = 0
grid[1][-1] = 0
grid[1][-2] = 0
