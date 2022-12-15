


sign = lambda x : -1 if x < 0 else 1

def st2path(st):
    st = [s.strip() for s in st.split("->")]
    last = tuple(map(int,st[0].split(",")))
    path = {last}
    for s in st[1:]:
        (x,y) = tuple(map(int,s.split(",")))
        (xx,yy) = last
        dx, dy = x - xx , y - yy
        if (dx==0):
            path.update([(x,yy+i*sign(dy)) for i in range(1,abs(dy))])
        if (dy==0):
            path.update([(xx+i*sign(dx),y) for i in range(1,abs(dx))])
        path.add((x,y))
        last = (x,y)
    return list(path)

rocks = set()
with open("input.txt","r") as f:
    lines = f.readlines()
    for line in lines:
        rocks.update(list(st2path(line)))


#rocks.update(st2path("498,4 -> 498,6 -> 496,6"))
#rocks.update(st2path("503,4 -> 502,4 -> 502,9 -> 494,9"))

down = lambda x : (x[0],x[1]+1)
left = lambda x : (x[0]-1,x[1])
right = lambda x : (x[0]+1,x[1])
down_left = lambda x : left(down(x))
down_right = lambda x : right(down(x))
y_max = max([i[1] for i in rocks])
not_in_floor = lambda x : x[1] < y_max+2

def sand_pouring(start):
    if (down(start) not in rocks)  and (not_in_floor(down(start))):
        return sand_pouring(down(start))
    elif (down_left(start) not in rocks) and (not_in_floor(down_left(start))):
        return sand_pouring(down_left(start))
    elif (down_right(start) not in rocks) and (not_in_floor(down_right(start))):
        return sand_pouring(down_right(start))
    else:
        return start

counts = 0
while True:
    new = sand_pouring((500,0))
    if new in rocks:
        break
    counts += 1
    rocks.add(new)

print(counts)
