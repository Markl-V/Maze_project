# лабиринт в граф

def maze_list(path_to_maze):

    with open(path_to_maze, "r", encoding="utf-8") as file:
        l = file.read().splitlines()

    h = len(l)
    w = len(l[0])
    t = h * w
    arr = [[] for _ in range(t)]
    d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for i in range(h):
        for j in range(w):
            c = l[i][j]
            if c != '█':

                if c == 'S':
                    s = i * w + j
                elif c == 'F':
                    f = i * w + j

                irn = i * w + j
                for di, dj in d:
                    qi, qj = i + di, j + dj
                    if 0 <= qi < h and 0 <= qj < w:
                        n = l[qi][qj]
                        if n != '█':
                            arr[irn].append(qi * w + qj)

    return (arr, s, f, h, w)

# решение

# бфс

class Queue():

    def __init__(self):
        self.queue = []

    def enqueue(self, x):
        self.queue.append(x)
        return self.queue

    def dequeue(self):
        if self.queue == []:
            return None
        else:
            p = []
            for i in range(1, len(self.queue)):
                p.append(self.queue[i])
            first = self.queue[0]
            self.queue = p
            return first

    def is_empty(self):
        return self.queue == []


def path(arr, s, f):

    n = len(arr)
    parent = [-1] * n
    visited = [False] * n
    Q = Queue()
    Q.enqueue(s)
    visited[s] = True

    while not Q.is_empty():
        u = Q.dequeue()
        if u == f:
            break
        for v in arr[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                Q.enqueue(v)

    path = []
    c = f
    while c != -1:
        path.append(c)
        c = parent[c]
    return path[::-1]

# рисование пути

def list_maze_path(arr, h, w, s, f, path, path_to_solutions):

    maze = [['█' for _ in range(w)] for _ in range(h)]
    t = h * w

    for x in range(t):
        if arr[x]:
            i = x//w
            j = x%w
            if x == s:
                maze[i][j] = 'S'
            elif x == f:
                maze[i][j] = 'F'
            else:
                maze[i][j] = '·'

    p = len(path)

    for y in range(1, p-1):
        i = path[y]//w
        j = path[y]%w
        if i - 1 == path[y+1]//w:
            maze[i][j] = '↑'
        elif i + 1 == path[y+1]//w:
            maze[i][j] = '↓'
        elif j + 1 == path[y+1]%w:
            maze[i][j] = '→'
        elif j - 1 == path[y+1]%w:
            maze[i][j] = '←'

    m = open(path_to_solutions, 'w', encoding="utf-8")
    s = ''

    for o in range(h):
        for p in range(w):
            s+=maze[o][p]
        s+='\n'
    m.write(s[:-1])

    m.close()