# 飞机大战
# pip install pynput

from pynput.keyboard import Key,Listener,KeyCode

background = [[0, 0, 0],
               [0, "x", 0],
               [0, 0, 0]]
# print(background[0])
# print(background[1])
# print(background[2])

def on_press(key):

    if key == KeyCode.from_char('w'):
        for i in 0,1,2:
            for j in 0,1,2:
                if background[i][j] == "x" and i > 0:
                    background[i][j] = "0"
                    background[i-1][j] = "x"

    elif key == KeyCode.from_char('s'):
        for i in 2, 1, 0:
            for j in 0, 1, 2:
                if background[i][j] == "x" and i < 2:
                    background[i][j] = "0"
                    background[i + 1][j] = "x"

    elif key == KeyCode.from_char('a'):
        for i in 0, 1, 2:
            for j in 0, 1, 2:
                if background[i][j] == "x" and j > 0:
                    background[i][j] = "0"
                    background[i][j - 1] = "x"
                    break

    elif key == KeyCode.from_char('d'):
        for i in 0, 1, 2:
            for j in 0, 1, 2:
                if background[i][j] == "x" and j > 0:
                    background[i][j] = "0"
                    background[i][j + 1] = "x"
                    break

    print()
    print(background[0])
    print(background[1])
    print(background[2])

with Listener(on_press=on_press) as listener:
    listener.join()
