def hello_GAYmers():
    print('#=====================#')
    print('#   здорова ГЕЙмеры   #')
    print('#     это игра в      #')
    print('#!!!КРЕСТИКИ НОЛИКИ!!!#')
    print('#       начнем?       #')
    print('#=====================#')

def BUY_BUY():
    print('#====================#')
    print('#  веселая игра была #')
    print('#     еще увидимся   #')
    print('#====================#')

hello_GAYmers()

maps=[1,2,3,4,5,6,7,8,9]

victory=[[0,1,2],[3,4,5],[6,7,8],
         [0,3,6],[1,4,7],[2,5,8],
         [0,4,8],[2,4,6]]

def game_map():
    print(maps[0], end=' ')
    print(maps[1], end=' ')
    print(maps[2])
    print(maps[3], end=' ')
    print(maps[4], end=' ')
    print(maps[5])
    print(maps[6], end=' ')
    print(maps[7], end=' ')
    print(maps[8])

def step_in_maps(step,symbol):
    ind=maps.index(step)
    maps[ind]=symbol

def final_result():
    win=''
    for i in victory:
        if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
            win = "X"
        elif maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
            win = "O"
    return win

g_over=False
p1=True

while g_over==False:
    game_map()
    if p1==True:
        symbol="X"
        step=int(input('Геймер №1, ходи: '))
    else:
        symbol="O"
        step=int(input('Геймер №2, ходи: '))
    step_in_maps(step,symbol)
    win=final_result()
    if win!='':
        g_over=True
    else:
        g_over=False
        p1=not(p1)

map()
print('WINNER IS:', win)
BUY_BUY()



