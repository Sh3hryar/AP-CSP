
######################
# Tic Tac Toe        #
######################



import turtle as trtl
# import x and o images for tic tsac toe
x_image="fakex.gif"
o_image="o.gif"
 
# create list to make tic tac toe board
box_list = list()

# store outputs for each game hear
game_state_list = ["", "", "", "", "", "", "", "", "" ]

wn= trtl.Screen()
wn.addshape(x_image)
wn.addshape(o_image)

# define global variables
turn = "x"
box_size = 4

# winning conditions
def checkWinningCondition (state):
    if state[0] != "" and state[0] == state[1] and state[1] == state[2]:
        return state[0]
    
    if state[3] != "" and state[3] == state[4] and state[4] == state[5]:
        return state[3]
    
    if state[6] != "" and state[6] == state[7] and state[7] == state[8]: 
        return state[6]
     
    if state[0] != "" and state[0] == state[3] and state[3] == state[6]: 
        return state[6]
    
    if state[1] != "" and state[1] == state[4] and state[4] == state[7]: 
        return state[7]
    
    if state[2] != "" and state[2] == state[5] and state[5] == state[8]: 
        return state[8]
    
    if state[0] != "" and state[0] == state[4] and state[4] == state[8]: 
        return state[8]
    
    if state[2] != "" and state[2] == state[4] and state[4] == state[6]: 
        return state[6]
    
    if state[0] != "" and state[1] != "" and  state[2] != "" and state[3] != "" and state[4] != "" and state[5] != "" and state[6] != "" and state[7] != "" and state[8] != "":
        return "d" 
    return "c"

# make players be able to take turns
def switch_player():
    global turn
    if turn == "x":
      turn="o"
    elif turn == "o": 
      turn="x"
     
# add each click into the list that records each game   
def process_click(index):
    global game_state_list
    
    if turn == "x":
        box_list[index].shape(x_image)
    elif  turn == "o": 
        box_list[index].shape(o_image) 
    
    game_state_list[index] = turn
    response = checkWinningCondition (game_state_list) 
    
    if response == "c":
        switch_player ()
    else: 
        declare_result (response)
    
# Once game ends show results on screen as neccesary
def declare_result(response):
     
     write_winner=trtl.Turtle()
     result=trtl.Turtle()
     write_winner.penup()
     write_winner.hideturtle()
     write_winner.goto(-200,200)
     write_winner.pencolor("black")
     label=""
     if (response == "o"):
        label = "O Wins!"
     elif (response == "x"):
        label = "X Wins!"
     elif (response == "d"):
        label = "Its a Draw"    
     write_winner.write(label, font=("Arial", 100, "bold"))
        
        
# make each tic tactoe board interactable for users
def draw_onclick_0(x, y):      
   process_click(0)
    
def draw_onclick_1(x,y):      
    process_click(1)
    
def draw_onclick_2(x,y):      
    process_click(2)
 
def draw_onclick_3(x,y):      
   process_click(3)
  
def draw_onclick_4(x,y):      
    process_click(4)
    
def draw_onclick_5(x,y):      
   process_click(5)
    
def draw_onclick_6(x,y):      
    process_click(6)
    
def draw_onclick_7(x,y):      
   process_click(7)
    
def draw_onclick_8(x,y):      
    process_click(8)    

# record each box individually
box_click_list = [draw_onclick_0, draw_onclick_1, draw_onclick_2, 
                  draw_onclick_3, draw_onclick_4, draw_onclick_5, 
                  draw_onclick_6, draw_onclick_7, draw_onclick_8]   


#draw tictactoe board
def draw_board(x, y):
  start_box = 0
  for collum in range(3): 
     for row in range(3):
        game_box=trtl.Turtle()
        game_box.turtlesize(box_size)
        game_box.hideturtle()
        game_box.shape("square")
        game_box.fillcolor("light green")
        game_box.penup()
        game_box.goto(x,y)
        game_box.onclick(box_click_list[start_box])
        start_box = start_box + 1
        game_box.showturtle()
        box_list.append(game_box)
        x = x + 80
     x = x - 80 * 3
     y = y - 80
     
        
# draw the board      
draw_board(-100, 100)
    
wn.mainloop()