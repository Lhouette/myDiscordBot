import discord
import os
import random
import math
import imageio
import time
from PIL import Image, ImageDraw, ImageFont

dirctory = os.path.dirname(__file__)
client = discord.Client()

Game = False
Ready = False
player = []
name = []
turn = -1
playerColor = ["white", "red", "green", "blue", "cyan", "magenta", "yellow", "orange", "purple", "gray", "brown"]
data = []
timer = 0
for i in range(0,9):
    data.append([])
    for j in range(0,9):
        data[i].append([])
        for k in range(0,9):
            data[i][j].append(-1)

def t_pos(commend):
    x = int(ord(commend[0]))-65
    if x < 0 or x > 8:
        x=-1
    y = int(ord(commend[1]))-97
    if y < 0 or y > 8:
        y=-1
    if not commend[2:0].isdigit:
        z=-1
    else:
        z = int(commend[2:])
        if z < 0 or z > 8:
            z=-1
    #print([x,y,z])
    return [x,y,z]

def t_ren(pitch, yaw, x, y, z, origin):
    x_vec = [0,-math.cos(pitch)]
    y_vec = [-math.sin(yaw),math.cos(yaw)*math.sin(pitch)]
    z_vec = [math.cos(yaw),math.sin(yaw)*math.sin(pitch)]
    return (x*x_vec[0]+y*y_vec[0]+z*z_vec[0]+origin[0],x*x_vec[1]+y*y_vec[1]+z*z_vec[1]+origin[1])

def reset():
    global data
    global player
    global turn
    global Game
    global Ready
    global name
    global timer
    Game = False
    Ready = False
    turn = -1
    player = []
    name = []
    data = []
    timer = 0
    for i in range(0,9):
        data.append([])
        for j in range(0,9):
            data[i].append([])
            for k in range(0,9):
                data[i][j].append(-1)

def pos(pox):
    x = 30 + 290*(pox[0]%3) + 260/8*pox[1]
    y = 30 + 290*int(pox[0]/3) + 260/8*pox[2]
    return [x,y]

def drawCircle(x, y, r, draw, color,w):
    draw.ellipse([(x-r/2,y-r/2),(x+r/2,y+r/2)], fill = color,outline = (0,0,0),width = w)
    return 0

def isWin(data, x, y, z, p):
    point = 0
    win = False
    direction = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    #d u r l b f dr ul dl ur db uf df ub rb lf rf lb drb ulf drf ulb dlb urf dlf urb
    #0 1 2 3 4 5 6  7  8  9  10 11 12 13 14 15 16 17 18  19  20  21  22  23  24  25

    if x > 4:
        direction[1] = 4
    else:
        direction[1] = x
    if x < 4:
        direction[0] = 4
    else:
        direction[0] = 8-x
        
    if y > 4:
        direction[3] = 4
    else:
        direction[3] = y
    if y < 4:
        direction[2] = 4
    else:
        direction[2] = 8-y
        
    if z > 4:
        direction[5] = 4
    else:
        direction[5] = z
    if z < 4:
        direction[4] = 4
    else:
        direction[4] = 8-z
        
    direction[6] = min(direction[0], direction[2]) #dr
    direction[7] = min(direction[1], direction[3]) #ul
    direction[8] = min(direction[0], direction[3]) #dl
    direction[9] = min(direction[1], direction[2]) #ur
    direction[10] = min(direction[0], direction[4])#db
    direction[11] = min(direction[1], direction[5])#uf
    direction[12] = min(direction[0], direction[5])#df
    direction[13] = min(direction[1], direction[4])#ub
    direction[14] = min(direction[2], direction[4])#rb
    direction[15] = min(direction[3], direction[5])#lf
    direction[16] = min(direction[2], direction[5])#rf
    direction[17] = min(direction[3], direction[4])#lb

    direction[18] = min(direction[0], direction[2], direction[4])#drb
    direction[19] = min(direction[1], direction[3], direction[5])#ulf
    direction[20] = min(direction[0], direction[2], direction[5])#drf
    direction[21] = min(direction[1], direction[3], direction[4])#ulb
    direction[22] = min(direction[0], direction[3], direction[4])#dlb
    direction[23] = min(direction[1], direction[2], direction[5])#urf
    direction[24] = min(direction[0], direction[3], direction[5])#dlf
    direction[25] = min(direction[1], direction[2], direction[4])#urb

    #print(direction)
    s_vec = [[1,0,0],[0,1,0],[0,0,1],[1,1,0],[1,-1,0],[1,0,1],[1,0,-1],[0,1,1],[0,1,-1],[1,1,1],[1,1,-1],[1,-1,1],[1,-1,-1]]

    for i in range(0,13):
        n = 0
        for j in range(1,direction[2*i]+1):
            if data[x+j*s_vec[i][0]][y+j*s_vec[i][1]][z+j*s_vec[i][2]] == p:
                n += 1
            else:
                break
        for j in range(1,direction[2*i+1]+1):
            if data[x-j*s_vec[i][0]][y-j*s_vec[i][1]][z-j*s_vec[i][2]] == p:
                n += 1
            else:
                break
        if n==3:
            win = True
        #print(str(i)+" : "+str(n))
        point += n
   
    if win:
        return[win, point+1]
    return[False, point+1]

@client.event
async def on_ready():
    print("디스코드 봇 로그인이 완료되었습니다.")
    print("디스코드봇 이름:" + client.user.name)
    print("디스코드봇 ID:" + str(client.user.id))
    print("디스코드봇 버전:" + str(discord.__version__))
    print('------')
    await client.change_presence(status=discord.Status.online, activity=discord.Game("삼차원 사목 매니저를"))
    #await client.get_channel(909978535215661116).send("황성준 접속중!")

@client.event
async def on_message(message):
    Author = message.author
    Content = message.content
    ch = client.get_channel(909978535215661116)
    global data
    global player
    global turn
    global Game
    global Ready
    global name
    global playerColor
    global timer
    if Author == client.user: #자기 메세지는 무시
        return
    if Content[0] == '!':
        Content = Content[1:]
        Message = Content.split()
        if len(Message) == 0:
            await ch.send("게임준비 --> !준비\n게임시작 --> !시작")
        elif not Game and not Ready:
            if Message[0] == "준비":
                Ready = True
                await ch.send("참가하려면 !참가를 입력해주세요.")
            elif Message[0] == "시작":
                await ch.send("시작하기 전에 !준비 해야 합니다.")
        elif not Game and Ready:
            if Message[0] == "참가":
                if Author.id in player:
                    await ch.send("이미 참가했습니다.")
                else:
                    player.append(Author.id)
                    name.append(Author.display_name)
                    await ch.send(name[-1]+"님이 참가했습니다.")
            elif Message[0] == "시작":
                if len(player) < 2:
                    await ch.send("최소 두 명 이상 참가해야 합니다.")
                else:
                    await ch.send("총 "+str(len(player))+"명이 참가했습니다.")
                    text = "순서는 "+name[0]
                    for i in range(1, len(name)):
                        text += " --> "+name[i]
                    text += " 입니다."
                    timer = time.time()
                    await ch.send(text)
                    await ch.send("삼차원 사목을 시작합니다.")
                    random.shuffle(playerColor)
                    table = Image.open("table.png")
                    table.save("tableSequence.png")
                    await ch.send(file=discord.File("tableSequence.png"))
                    Game = True
                    turn = 0
            elif Message[0] == "참가취소":
                p = player.index(Author.id)
                player.pop(p)
                await ch.send(name.pop(p)+"님이 참가를 취소했습니다.")
            elif Message[0] == "준비취소":
                player = []
                name = []
                Ready = False
                await ch.send("준비가 취소되었습니다.")
            elif Message[0] == "챰가" and Author.id == 785385532493529109:
                await ch.send("챰가가 아니라 참가란다~!")
            else:
                await ch.send("!참가\t\t:: 게임에 참가합니다.\n!참가취소\t:: 참가를 취소합니다.\n!준비취소\t:: 준비를 취소합니다.")
        elif Game and Ready:
            if Message[0] == "put":
                if len(Message[1:]) < 1:
                    await ch.send("명령 형식 : !put [대문자+소문자+숫자]\n명령 예시 : !put Ac7")
                elif not(Author.id in player):
                    await ch.send("개입할 수 없습니다. (참가하지 않았습니다.)")
                elif Author.id != player[turn]:
                    await ch.send("차례를 기다리세요.")
                else:
                    p = player.index(Author.id)
                    pox = t_pos(Message[1])
                    if pox[0] == -1 or pox[1] == -1 or pox[2] == -1:
                        await ch.send("명령 형식 : !put [대문자+소문자+숫자]\n명령 예시 : !put Ac7")
                    elif data[pox[0]][pox[1]][pox[2]] != -1:
                        await ch.send("그 위치엔 놓을 수 없습니다.")
                    else:
                        data[pox[0]][pox[1]][pox[2]] = p
                        table = Image.open("tableSequence.png")
                        draw = ImageDraw.Draw(table)
                        w = isWin(data, pox[0], pox[1], pox[2], p)
                        drawCircle(pos(pox)[0],pos(pox)[1],20,draw,playerColor[p],0)
                        table.save("tableSequence.png")
                        turn += 1
                        if turn == len(player):
                            turn = 0
                        await ch.send(file=discord.File("tableSequence.png"))
                        if w[0]:
                            await ch.send(Author.display_name+"가 우승하였습니다.")
                            await ch.send("게임을 종료합니다.")  ##========
                            reset()
                        else:
                            await ch.send(name[turn]+"님의 차례입니다.")
            elif Message[0] == "compulsion":
                dt = time.time()-timer
                if len(Message[1:]) < 1:
                    await ch.send("명령 형식 : !compulsion [대문자+소문자+숫자]")
                elif not(Author.id in player):
                    await ch.send("참가하지 않은 사람은 사용할 수 없습니다.")
                elif dt < 600:
                    await ch.send("저번 순서 이후로 10분이 지나지 않았습니다. 지난 시간 : "+str(int(dt//60))+"분 "+str(int(dt%60))+"초")
                else:
                    p = turn
                    pox = t_pos(Message[1])
                    await ch.send(name[p]+"님이 10분동안 가만히 있었습니다. "+name[player.index(Author.id)]+"님이 대신 놓습니다.")
                    if pox[0] == -1 or pox[1] == -1 or pox[2] == -1:
                        await ch.send("명령 형식 : !put [대문자+소문자+숫자]\n명령 예시 : !put Ac7")
                    elif data[pox[0]][pox[1]][pox[2]] != -1:
                        await ch.send("그 위치엔 놓을 수 없습니다.")
                    else:
                        data[pox[0]][pox[1]][pox[2]] = p
                        table = Image.open("tableSequence.png")
                        draw = ImageDraw.Draw(table)
                        w = isWin(data, pox[0], pox[1], pox[2], p)
                        drawCircle(pos(pox)[0],pos(pox)[1],20,draw,playerColor[p],0)
                        table.save("tableSequence.png")
                        turn += 1
                        timer = time.time()
                        if turn == len(player):
                            turn = 0
                        await ch.send(file=discord.File("tableSequence.png"))
                        if w[0]:
                            await ch.send(Author.display_name+"님이 우승하였습니다.")
                            await ch.send("게임을 종료합니다.")  ##========
                            reset()
                        else:
                            await ch.send(name[turn]+"님의 차례입니다.")
            elif Message[0] == "3Dview":
                await ch.send("이미지를 준비중입니다. 10초 정도 소요됩니다.")
                start = time.time()
                img = Image.open("900x900.png")
                draw = ImageDraw.Draw(img)
                for frame in range(0,61):
                    fnt = ImageFont.truetype("NanumGothic.ttf",20, encoding="UTF-8")
                    pitch = (30)*math.pi/180
                    yaw = (45-45*math.cos(frame/60*math.pi))*math.pi/180
                    origin = [450,450]
                    draw.rectangle([(0,0),(900,900)], fill = (54,57,63))
                    draw.polygon([t_ren(pitch, yaw, -250, -250, -250, origin),t_ren(pitch, yaw, 250, -250, -250, origin),t_ren(pitch, yaw, 250, 250, -250, origin),t_ren(pitch, yaw, -250, 250, -250, origin)], fill=(50,50,50)) #xy plane
                    draw.polygon([t_ren(pitch, yaw, -250, -250, -250, origin),t_ren(pitch, yaw, 250, -250, -250, origin),t_ren(pitch, yaw, 250, -250, 250, origin),t_ren(pitch, yaw, -250, -250, 250, origin)], fill=(50,50,50)) #zx plane
                    draw.polygon([t_ren(pitch, yaw, -250, -250, -250, origin),t_ren(pitch, yaw, -250, 250, -250, origin),t_ren(pitch, yaw, -250, 250, 250, origin),t_ren(pitch, yaw, -250, -250, 250, origin)], fill=(50,50,50)) #yz plane
                    draw.line([t_ren(pitch, yaw, -250, -250, -250, origin),t_ren(pitch, yaw, 275, -250, -250, origin)], fill="white", width=5) #x axis
                    draw.line([t_ren(pitch, yaw, -250, -250, -250, origin),t_ren(pitch, yaw, -250, 275, -250, origin)], fill="white", width=5) #y axis
                    draw.line([t_ren(pitch, yaw, -250, -250, -250, origin),t_ren(pitch, yaw, -250, -250, 275, origin)], fill="white", width=5) #z axis
                    for t in range(0,9):
                        draw.line([t_ren(pitch, yaw, -250, -200+50*t, -250, origin),t_ren(pitch, yaw, 250, -200+50*t, -250, origin)], fill=(150,150,150), width=1)
                        draw.line([t_ren(pitch, yaw, -250, -250, -200+50*t, origin),t_ren(pitch, yaw, 250, -250, -200+50*t, origin)], fill=(150,150,150), width=1)
                        draw.line([t_ren(pitch, yaw, -200+50*t, -250, -250, origin),t_ren(pitch, yaw, -200+50*t, 250, -250, origin)], fill=(150,150,150), width=1)
                        draw.line([t_ren(pitch, yaw, -250, -250, -200+50*t, origin),t_ren(pitch, yaw, -250, 250, -200+50*t, origin)], fill=(150,150,150), width=1)
                        draw.line([t_ren(pitch, yaw, -200+50*t, -250, -250, origin),t_ren(pitch, yaw, -200+50*t, -250, 250, origin)], fill=(150,150,150), width=1)
                        draw.line([t_ren(pitch, yaw, -250, -200+50*t, -250, origin),t_ren(pitch, yaw, -250, -200+50*t, 250, origin)], fill=(150,150,150), width=1)
                        draw.text(t_ren(pitch, yaw, 220-50*t, -250, 275, origin),chr(65+t),font=fnt,fill="white")
                        draw.text(t_ren(pitch, yaw, -250, 200-50*t, 275, origin),str(8-t),font=fnt,fill="white")
                        draw.text(t_ren(pitch, yaw, -250, 275, 200-50*t, origin),chr(105-t),font=fnt,fill="white")
                    for i in range(0,9):
                        for j in range(0,9):
                            for k in range(0,9):
                                if data[8-i][j][k] != -1:
                                    cord = t_ren(pitch, yaw, -200+50*i, -200+50*k, -200+50*j, origin)
                                    drawCircle(cord[0], cord[1], 40, draw, playerColor[data[8-i][j][k]],2)
                    img.save('3dsequences/3dseq'+str(frame)+'.png')
                sequences = []
                speed = {'duration': 1/30}
                for i in range(0,60):
                    sequences.append(imageio.imread('3dsequences/3dseq'+str(i)+'.png'))
                for i in range(0,60):
                    sequences.append(imageio.imread('3dsequences/3dseq'+str(60-i)+'.png'))
                imageio.mimsave('3dview.gif',sequences,**speed)
                await ch.send(file=discord.File("3dview.gif"))
                await ch.send("gif를 완성했습니다. 실행 시간: "+str(time.time() - start)+"초")

                    
                    
        

client.run('') #토큰
