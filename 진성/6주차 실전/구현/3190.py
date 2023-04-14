from collections import deque

class Board:
    # maps used for direction and next position computation
    dmap = {"u" : {"L" : "l", "D" : "r"},
            "l" : {"L" : "d", "D" : "u"},
            "r" : {"L" : "u", "D" : "d"},
            "d" : {"L" : "r", "D" : "l"},
            }
    
    vmap = {"u" : (-1, 0),
            "l" : (0, -1),
            "r" : (0, 1),
            "d" : (1, 0)
            }

    def __init__(self, N):
        self.n = N
        self.board = [[0] * N for _ in range(N)]
        self.snake = deque([(0, 0)]) # head = deque[-1], tail = deque[0]
        self.cur_time = 0
        self.end = False
        self.look = "r"
    
    def set_apple(self, data):
        r, c = data
        self.board[r-1][c-1] = 1

    def next_pos(self, head):
        x, y = head
        dx, dy = self.vmap[self.look]
        return (x + dx, y + dy)

    def command(self, cmd):
        till_time, direction = cmd
        till_time = int(till_time)
        for time in range(self.cur_time + 1, till_time + 1):
            if not self.end:
                self.cur_time = time
                # head next
                next = self.next_pos(self.snake[-1])
                r, c = next
                # if in board and not biting self
                if 0 <= r < self.n and 0 <= c < self.n and next not in self.snake:
                    # if apple:
                    if self.board[r][c]:
                        self.board[r][c] = 0
                        self.snake.append(next)
                    else:
                        self.snake.popleft()
                        self.snake.append(next)
                else:
                    self.end = True
            else:
                continue
        self.look = self.dmap[self.look][direction]


def solve():
    N = int(input())
    K = int(input())
    board = Board(N)

    for _ in range(K):
        board.set_apple(tuple(map(int, input().split())))

    L = int(input())
    for _ in range(L):
        board.command(input().split())
    
    if not board.end:
        # if not finished yet, do it till the end
        board.command(["10100", "D"])
    
    print(board.cur_time)

solve()