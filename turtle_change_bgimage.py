import turtle

def draw_check(pos):
    t.up()
    t.goto(loc_pos[pos][0], loc_pos[pos][1])
    t.down()

    t.color("red")
    t.begin_fill()
    for i in range(3):
        t.forward(10)
        t.left(120)
    t.end_fill()
    
    t.up()
    t.goto(loc_pos[pos][0], loc_pos[pos][1]+10)
    t.down()
    t.write(loc_name[pos] +  " " + loc_captital[pos], font = ("", 10, "bold"))

loc_pos = [(450,50), (-85,50)]
loc_name = ["미국", "한국"]
loc_captital = ["워싱턴", "서울"]

s = turtle.Screen()
s.setup(1200,550)
s.bgpic("world_map.gif")

t = turtle.Turtle()

while True:
    input_nation = input("나라 이름 : ")
    for i in range(len(loc_name)):
        if input_nation == loc_name[i]:
            draw_check(i)
            break
        
        
