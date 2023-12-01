from PIL import Image, ImageDraw, ImageFont
     
""" Table.png 생성 프로그램 """
img = Image.open("900x900.png")

draw = ImageDraw.Draw(img)
draw.rectangle([(0, 0), (900, 900)], fill=(10, 10, 10))
fnt = ImageFont.truetype("NanumGothic.ttf",280, encoding="UTF-8")
for i in range(0,3):
    for j in range(0,3):
        text = chr(65+i+3*j)
        tw, th = fnt.getsize(text)
        draw.text((160+290*i-tw/2,160+290*j-th/2-30),text,font=fnt,fill = (90,90,90))
        for k in range(0,9):
            draw.line([(30+290*i+260/8*k,30+290*j),(30+290*i+260*k/8,290+290*j)],fill="white")
            draw.line([(30+290*i,30+290*j+260/8*k),(290+290*i,30+290*j+260/8*k)],fill="white")
            
fnt = ImageFont.truetype("NanumGothic.ttf",15, encoding="UTF-8")
for i in range(0,3):
    for k in range(0,9):
        text = chr(97+k)
        tw, th = fnt.getsize(text)
        draw.text((30+260/8*k-tw/2+ 290*i,13-th/2),text,font=fnt,fill="white")
        draw.text((30+260/8*k-tw/2+ 290*i,303-th/2),text,font=fnt,fill="white")
        draw.text((30+260/8*k-tw/2+ 290*i,593-th/2),text,font=fnt,fill="white")
        draw.text((30+260/8*k-tw/2+ 290*i,883-th/2),text,font=fnt,fill="white")

        text = str(k)
        tw, th = fnt.getsize(text)
        draw.text((15-tw/2,30-th/2+ 290*i+260/8*k),text,font=fnt,fill="white")
        draw.text((305-tw/2,30-th/2+ 290*i+260/8*k),text,font=fnt,fill="white")
        draw.text((595-tw/2,30-th/2+ 290*i+260/8*k),text,font=fnt,fill="white")
        draw.text((885-tw/2,30-th/2+ 290*i+260/8*k),text,font=fnt,fill="white")

img.show()
img.save('table.png')

"""
for i in range(1,18):
    draw.line([(300-outlineSize/2, 300-outlineSize/2 + outlineSize/18*i),(300+outlineSize/2, 300-outlineSize/2 + outlineSize/18*i)],fill=(0,0,0))
    draw.line([(300-outlineSize/2 + outlineSize/18*i, 300-outlineSize/2),(300-outlineSize/2 + outlineSize/18*i, 300+outlineSize/2)],fill=(0,0,0))

for i in range(0,3):
    for j in range(0,3):
        draw.ellipse([(300-outlineSize/2+outlineSize/6+outlineSize/3*i-dotSize/2,300-outlineSize/2+outlineSize/6+outlineSize/3*j-dotSize/2),(300-outlineSize/2+outlineSize/6+outlineSize/3*i+dotSize/2,300-outlineSize/2+outlineSize/6+outlineSize/3*j+dotSize/2)], fill=(0,0,0))

fontsize = 15
fnt = ImageFont.truetype("NanumGothic.ttf",fontsize, encoding="UTF-8")

for i in range(0,19):
    text = chr(65+i)
    tw, th = fnt.getsize(text)
    draw.text((75-tw/2 + outlineSize/18*i, 25-int(fnt.size/2)), text, font=fnt, fill="white")
    draw.line([(75+outlineSize/18*i,40),(75+outlineSize/18*i,60)], fill=(255,255,255))
    draw.text((75-tw/2 + outlineSize/18*i, 600-25-int(fnt.size/2)), text, font=fnt, fill="white")
    draw.line([(75+outlineSize/18*i,600-40),(75+outlineSize/18*i,600-60)], fill=(255,255,255))
    text = str(i)
    tw, th = fnt.getsize(text)
    draw.text((25-tw/2 , 75-int(fnt.size/2)+ outlineSize/18*i), text, font=fnt, fill="white")
    draw.line([(40,75+outlineSize/18*i),(60,75+outlineSize/18*i)], fill=(255,255,255))
    draw.text((600-25-tw/2 , 75-int(fnt.size/2)+ outlineSize/18*i), text, font=fnt, fill="white")
    draw.line([(600-40,75+outlineSize/18*i),(600-60,75+outlineSize/18*i)], fill=(255,255,255))

fnt = ImageFont.truetype("NanumGothic.ttf",25, encoding="UTF-8")
draw.text((620,20), "참가자 정보", font=fnt, fill="white")

fnt = ImageFont.truetype("NanumGothic.ttf",20, encoding="UTF-8")
draw.text((630,60), "색상", font=fnt, fill="white")
draw.text((680,60), "이름", font=fnt, fill="white")
draw.text((750,60), "포인트", font=fnt, fill="white")

img.show()
img.save('table.png')

"""
"""
data = [[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]]

def t_pos(commend):
    if len(commend) < 2:
        return [-1,-1]
    x = int(ord(commend[0]))-65
    if x < 0 or x > 18:
        x = -1
    if not commend[1:].isdigit():
        y = -1
    else:
        y = int(commend[1:])
        if y < 0 or y > 18:
            y = -1
    return [x,y]
    

def pos(x):
    return 75 + 450/18*x

def drawCircle(x, y, r, draw, color):
    draw.ellipse([(x-r/2,y-r/2),(x+r/2,y+r/2)], fill = color, outline = (0,0,0), width = 3)
    return 0

def isWin(data, x, y, p):
    direction = [0,0,0,0,0,0,0,0] #u ur r dr d dl l ul
    if y > 5:
        direction[0] = 5
    else:
        direction[0] = y
    if y < 13:
        direction[4] = 5
    else:
        direction[4] = 18-y
    if x > 5:
        direction[6] = 5
    else:
        direction[6] = x
    if x < 13:
        direction[2] = 5
    else:
        direction[2] = 18-x
    direction[1] = min(direction[0], direction[2])
    direction[3] = min(direction[2], direction[4])
    direction[5] = min(direction[4], direction[6])
    direction[7] = min(direction[6], direction[0])
    print(direction)
    n = 0
    for i in range(1,direction[0]+1):
        if data[y-i][x] == p:
            n += 1
        else:
            break
    for i in range(1,direction[4]+1):
        if data[y+i][x] == p:
            n += 1
        else:
            break
    if n == 4:
        return [True, p]
    print(n)
    n = 0
    for i in range(1,direction[1]+1):
        if data[y-i][x+i] == p:
            n += 1
        else:
            break
    for i in range(1,direction[5]+1):
        if data[y+i][x-i] == p:
            n += 1
        else:
            break
    if n == 4:
        return [True, p]
    print(n)
    n = 0
    for i in range(1,direction[2]+1):
        if data[y][x+i] == p:
            n += 1
        else:
            break
    for i in range(1,direction[6]+1):
        if data[y][x-i] == p:
            n += 1
        else:
            break
    if n == 4:
        return [True, p]
    print(n)
    n = 0
    for i in range(1,direction[3]+1):
        if data[y+i][x+i] == p:
            n += 1
        else:
            break
    for i in range(1,direction[7]+1):
        if data[y-i][x-i] == p:
            n += 1
        else:
            break
    if n == 4:
        return [True, p]
    print(n)
    return[False, p]

player = []
playerColor = ["white", "black", "red", "green", "blue", "cyan", "magenta", "yellow", "orange", "purple", "gray", "brown"]

tableImg = Image.open("table.png")
draw = ImageDraw.Draw(tableImg)

for i in range(0,19):
    for j in range(0,19):
        drawCircle(pos(i),pos(j),20,draw,playerColor[(i+j*2)%8])

p=0
while True:
    p = (p+1)%12
    pox = t_pos(input())
    print(pox)
    if pox[0] == -1 or pox[1] == -1:
        continue
    data[pox[1]][pox[0]] = p
#    print(data)
    print(isWin(data, pox[0], pox[1], p))
    drawCircle(pos(pox[0]),pos(pox[1]),20,draw,playerColor[p])
    tableImg.show()
"""
































