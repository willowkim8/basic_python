import sys
# input보다 readline이 시간이 더 짧다.
N = int(sys.stdin.readline())

stack = list()

for i in range(N):
    cmd = sys.stdin.readline().split() 

    if cmd[0] == "push":
        stack.append(int(cmd[1]))

    elif cmd[0] == "pop":
        if not stack:
            print('-1')
        else:
            print(stack[-1])
            stack.pop()

    elif cmd[0] == "size":
        print(len(stack))

    elif cmd[0] == "empty":
        if not stack:
            print(1)
        else:
            print(0)

    elif cmd[0] == "top":
        if not stack:
            print(-1)
        else:
            print(stack[-1])