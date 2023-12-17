#بسم الله الرحمن الرحيم 

#import modules 
import tkinter as tk
from tkinter import*
from tkinter import messagebox
import random
import glob

# -------------------------- make layout design (game loop )----------------------------------------------------
game = Tk()
game.title(" 🎉 X-O-ALmadrasa_final_project 🎉 ")
game.geometry("500x700")



#creating function to restart whole game when user click restarts
def re_start():
    b1.config(text=" ", font=("poppins", 20), bg="#fff",state=tk.NORMAL)
    b2.config(text=" ", font=("poppins", 20) ,bg="#fff",state=tk.NORMAL)
    b3.config(text=" ", font=("poppins", 20), bg="#fff",state=tk.NORMAL)

    b4.config(text=" ", font=("poppins", 20), bg="#fff",state=tk.NORMAL)
    b5.config(text=" ", font=("poppins", 20) ,bg="#fff",state=tk.NORMAL)
    b6.config(text=" ", font=("poppins", 20), bg="#fff",state=tk.NORMAL)

    b7.config(text=" ", font=("poppins", 20), bg="#fff",state=tk.NORMAL)
    b8.config(text=" ", font=("poppins", 20) ,bg="#fff",state=tk.NORMAL)
    b9.config(text=" ", font=("poppins", 20), bg="#fff",state=tk.NORMAL)
    who_won.config(text=" ")


count_user_win = 0
count_pc_win = 0
#creating label to display winner 
who_won = Label(game , text=(" "),font=("poppins",30),fg="light green")
who_won.grid(row=1 , column=0 ,columnspan=3,sticky="ew")


# creating lable  (user : ) (computer: )
user_lable = Label(game , text=("User Score : " + str( count_user_win) ),font=("poppins",20))
pc_lable = Label(game , text=("PC Score : " + str( count_pc_win)), font=("poppins",20))

# putting lable in place
user_lable.grid(row=0 , column=0, sticky="nw", pady="20")
pc_lable.grid(row=0 , column=1 , sticky="ne", pady="20")

#making restart button 
restart_btn = Button(game,font=("poppins",20),height=1,width=10, text="Restart", command= re_start)
restart_btn.grid(row=2 ,column=1,sticky="nw" , pady="20")



# creating buttons for layout (b1 : b9)

b1 = Button (game,text=" ",width ="10" , height="5" , bg="gray" ,command=lambda:insert(b1), font=("poppins","20"))
b2 = Button (game,text=" ",width ="10" , height="5" , bg="gray" ,command=lambda:insert(b2) , font=("poppins","20"))
b3 = Button (game,text=" ",width ="10" , height="5" , bg="gray" ,command=lambda:insert(b3) , font=("poppins","20"))
 
b4 = Button (game,text=" ",width ="10" , height="5" , bg="gray" ,command=lambda:insert(b4) , font=("poppins","20"))
b5 = Button (game,text=" ",width ="10" , height="5" , bg="gray" ,command=lambda:insert(b5) , font=("poppins","20"))
b6 = Button (game,text=" ",width ="10" , height="5" , bg="gray" ,command=lambda:insert(b6) , font=("poppins","20"))

b7 = Button (game,text=" ",width ="10" , height="5" , bg="gray" ,command=lambda:insert(b7) , font=("poppins","20"))
b8 = Button (game,text=" ",width ="10" , height="5" , bg="gray" ,command=lambda:insert(b8) , font=("poppins","20"))
b9 = Button (game,text=" ",width ="10" , height="5" , bg="gray" ,command=lambda:insert(b9) , font=("poppins","20"))

#put buttons in place 
b1.grid(row=3,column=0)
b2.grid(row=3,column=1)
b3.grid(row=3,column=2)

b4.grid(row=4,column=0)
b5.grid(row=4,column=1)
b6.grid(row=4,column=2)

b7.grid(row=5,column=0)
b8.grid(row=5,column=1)
b9.grid(row=5,column=2)


#Function to  Disable Whole game When Someone won
def disable_btns():
    b1.config(state="disabled")
    b2.config(state="disabled")
    b3.config(state="disabled")

    b4.config(state="disabled")
    b5.config(state="disabled")
    b6.config(state="disabled")

    b7.config(state="disabled")
    b8.config(state="disabled")
    b9.config(state="disabled")


# function to check if win 

def check_winner():
    global count_user_win, count_pc_win, game_over

    buttons = [b1, b2, b3, b4, b5, b6, b7, b8, b9]

# check win for user

    if b1.cget("text") == "X" and b2.cget("text") == "X" and b3.cget("text") == "X":
        b1.config(background="green", foreground="white", state=tk.DISABLED)
        b2.config(background="green", foreground="white", state=tk.DISABLED)
        b3.config(background="green", foreground="white", state=tk.DISABLED)
        who_won.config(text=" Congrats You Won 🤩 " ,fg="light green")
        count_user_win += 1
        user_lable.config(text=("User Score : " + str( count_user_win)))
        disable_btns()
        return


    elif b4.cget("text") == "X" and b5.cget("text") == "X" and b6.cget("text") == "X":
        b4.config(background="green", foreground="white", state=tk.DISABLED)
        b5.config(background="green", foreground="white", state=tk.DISABLED)
        b6.config(background="green", foreground="white", state=tk.DISABLED)
        who_won.config(text=" Congrats You Won 🤩 " ,fg="light green")
        count_user_win += 1
        user_lable.config(text=("User Score : " + str( count_user_win)))
        disable_btns()
        return


    elif b7.cget("text") == "X" and b8.cget("text") == "X" and b9.cget("text") == "X":
        b7.config(background="green", foreground="white", state=tk.DISABLED)
        b8.config(background="green", foreground="white", state=tk.DISABLED)
        b9.config(background="green", foreground="white", state=tk.DISABLED)
        who_won.config(text=" Congrats You Won 🤩 " ,fg="light green")
        count_user_win += 1
        user_lable.config(text=("User Score : " + str( count_user_win)))
        disable_btns()
        return


#check vertical 
    elif b1.cget("text") == "X" and b4.cget("text") == "X" and b7.cget("text") == "X":
        b1.config(background="green", foreground="white", state=tk.DISABLED)
        b4.config(background="green", foreground="white", state=tk.DISABLED)
        b7.config(background="green", foreground="white", state=tk.DISABLED)
        who_won.config(text=" Congrats You Won 🤩 " ,fg="light green")
        count_user_win += 1
        user_lable.config(text=("User Score : " + str( count_user_win)))
        disable_btns()
        return


    elif b2.cget("text") == "X" and b5.cget("text") == "X" and b8.cget("text") == "X":
        b2.config(background="green", foreground="white", state=tk.DISABLED)
        b5.config(background="green", foreground="white", state=tk.DISABLED)
        b8.config(background="green", foreground="white", state=tk.DISABLED)
        who_won.config(text=" Congrats You Won 🤩 " ,fg="light green")
        count_user_win += 1
        user_lable.config(text=("User Score : " + str( count_user_win)))
        disable_btns()
        return


    elif b3.cget("text") == "X" and b6.cget("text") == "X" and b9.cget("text") == "X":
        b3.config(background="green", foreground="white", state=tk.DISABLED)
        b6.config(background="green", foreground="white", state=tk.DISABLED)
        b9.config(background="green", foreground="white", state=tk.DISABLED)
        who_won.config(text=" Congrats You Won 🤩 " ,fg="light green")
        count_user_win += 1
        user_lable.config(text=("User Score : " + str( count_user_win)))
        disable_btns()
        return


#check diagonal 

    elif b3.cget("text") == "X" and b5.cget("text") == "X" and b7.cget("text") == "X":
        b3.config(background="green", foreground="white", state=tk.DISABLED)
        b5.config(background="green", foreground="white", state=tk.DISABLED)
        b7.config(background="green", foreground="white", state=tk.DISABLED)
        who_won.config(text=" Congrats You Won 🤩 " ,fg="light green")
        count_user_win += 1
        user_lable.config(text=("User Score : " + str( count_user_win)))
        disable_btns()
        return


    elif b1.cget("text") == "X" and b5.cget("text") == "X" and b9.cget("text") == "X":
        b1.config(background="green", foreground="white", state=tk.DISABLED)
        b5.config(background="green", foreground="white", state=tk.DISABLED)
        b9.config(background="green", foreground="white", state=tk.DISABLED)
        who_won.config(text=" Congrats You Won 🤩 " ,fg="light green")
        count_user_win += 1
        user_lable.config(text=("User Score : " + str( count_user_win)))
        disable_btns()
        return
    
    elif (
    b1.cget("text") == " "
    and b2.cget("text") == " "
    and b3.cget("text") == " "
    and b4.cget("text") == " "
    and b5.cget("text") == " "
    and b6.cget("text") == " "
    and b7.cget("text") == " "
    and b8.cget("text") == " "
    and b9.cget("text") == " " ):
        return

#check for tie
    elif b1.cget("text") != " " and b2.cget("text") != " " and b3.cget("text") != " " and b4.cget("text") != " " and b5.cget("text") != " " and b6.cget("text") != " " and b7.cget("text") != " " and b8.cget("text") != " " and b9.cget("text") != " " :

        b1.config(background="red",state="disabled")
        b2.config(background="red",state="disabled")
        b3.config(background="red",state="disabled")
        b4.config(background="red",state="disabled")
        b5.config(background="red",state="disabled")
        b6.config(background="red",state="disabled")
        b7.config(background="red",state="disabled")
        b8.config(background="red",state="disabled")
        b9.config(background="red",state="disabled")
        who_won.config(text="it's tie , Restart to play again" , foreground="Red")

    else:
        return



# check computer win 
#check horizontal

def pc_win_check():
    global count_pc_win
    if b1.cget("text") == "o" and b2.cget("text") == "o" and b3.cget("text") == "O":
        b1.config(background="aqua", foreground="black", state=tk.DISABLED)
        b2.config(background="aqua", foreground="black", state=tk.DISABLED)
        b3.config(background="aqua", foreground="black", state=tk.DISABLED)
        who_won.config(text="PC wins! Tough luck 😔",foreground="light blue")
        count_pc_win += 1
        pc_lable.config(text=("PC Score : " + str( count_pc_win)))
        disable_btns()
        return



    elif b4.cget("text") == "o" and b5.cget("text") == "o" and b6.cget("text") == "o":
        b4.config(background="aqua", foreground="black", state=tk.DISABLED)
        b5.config(background="aqua", foreground="black", state=tk.DISABLED)
        b6.config(background="aqua", foreground="black", state=tk.DISABLED)
        who_won.config(text="PC wins! Tough luck 😔",foreground="light blue")
        count_pc_win += 1
        pc_lable.config(text=("PC Score : " + str( count_pc_win)))
        disable_btns()
        return

    elif b7.cget("text") == "o" and b8.cget("text") == "o" and b9.cget("text") == "o":
        b7.config(background="aqua", foreground="black", state=tk.DISABLED)
        b8.config(background="aqua", foreground="black", state=tk.DISABLED)
        b9.config(background="aqua", foreground="black", state=tk.DISABLED)
        who_won.config(text="PC wins! Tough luck 😔",foreground="light blue")
        count_pc_win += 1
        pc_lable.config(text=("PC Score: " + str( count_pc_win)))
        disable_btns()
        return

#check vertical 
    elif b1.cget("text") == "o" and b4.cget("text") == "o" and b7.cget("text") == "o":
        b1.config(background="aqua", foreground="black", state=tk.DISABLED)
        b4.config(background="aqua", foreground="black", state=tk.DISABLED)
        b7.config(background="aqua", foreground="black", state=tk.DISABLED)
        who_won.config(text="PC wins! Tough luck 😔",foreground="light blue")
        count_pc_win += 1
        pc_lable.config(text=("PC Score : " + str( count_pc_win)))
        disable_btns()
        return


    elif b2.cget("text") == "o" and b5.cget("text") == "o" and b8.cget("text") == "o":
        b2.config(background="aqua", foreground="black", state=tk.DISABLED)
        b5.config(background="aqua", foreground="black", state=tk.DISABLED)
        b8.config(background="aqua", foreground="black", state=tk.DISABLED)
        who_won.config(text="PC wins! Tough luck 😔",foreground="light blue")
        count_pc_win += 1
        pc_lable.config(text=("PC Score : " + str( count_pc_win)))
        disable_btns()
        return

    elif b3.cget("text") == "o" and b6.cget("text") == "o" and b9.cget("text") == "o":
        b3.config(background="aqua", foreground="black", state=tk.DISABLED)
        b6.config(background="aqua", foreground="black", state=tk.DISABLED)
        b9.config(background="aqua", foreground="black", state=tk.DISABLED)
        who_won.config(text="PC wins! Tough luck 😔",foreground="light blue")
        count_pc_win += 1
        pc_lable.config(text=("PC Score : " + str( count_pc_win)))
        disable_btns()
        return

#check diagonal 

    elif b3.cget("text") == "o" and b5.cget("text") == "o" and b7.cget("text") == "o":
        b3.config(background="aqua", foreground="black", state=tk.DISABLED)
        b5.config(background="aqua", foreground="black", state=tk.DISABLED)
        b7.config(background="aqua", foreground="black", state=tk.DISABLED)
        who_won.config(text="PC wins! Tough luck 😔" ,foreground="light blue")
        count_pc_win += 1
        pc_lable.config(text=("PC Score: " + str( count_pc_win)))
        disable_btns()
        return

    elif b1.cget("text") == "o" and b5.cget("text") == "o" and b9.cget("text") == "o":
        b1.config(background="aqua", foreground="black", state=tk.DISABLED)
        b5.config(background="aqua", foreground="black", state=tk.DISABLED)
        b9.config(background="aqua", foreground="black", state=tk.DISABLED)
        who_won.config(text="PC wins! Tough luck 😔",foreground="light blue")
        count_pc_win += 1
        pc_lable.config(text=("PC Score : " + str( count_pc_win)))
        disable_btns()
        return
    
    elif (
    b1.cget("text") == " "
    and b2.cget("text") == " "
    and b3.cget("text") == " "
    and b4.cget("text") == " "
    and b5.cget("text") == " "
    and b6.cget("text") == " "
    and b7.cget("text") == " "
    and b8.cget("text") == " "
    and b9.cget("text") == " " ):
        return

#check for tie
    elif b1.cget("text") != " " and b2.cget("text") != " " and b3.cget("text") != " " and b4.cget("text") != " " and b5.cget("text") != " " and b6.cget("text") != " " and b7.cget("text") != " " and b8.cget("text") != " " and b9.cget("text") != " " :

        b1.config(background="red",state="disabled")
        b2.config(background="red",state="disabled")
        b3.config(background="red",state="disabled")
        b4.config(background="red",state="disabled")
        b5.config(background="red",state="disabled")
        b6.config(background="red",state="disabled")
        b7.config(background="red",state="disabled")
        b8.config(background="red",state="disabled")
        b9.config(background="red",state="disabled")
        who_won.config(text="it's tie , Restart to play again" , foreground="Red")
    #something wrong in here check it please 
    else:
        return

#Function to insert random pc choice recalled in player insert function

def pc_choice():
    buttons = [b1, b2, b3, b4, b5, b6, b7, b8, b9]
   
    result = random.choice(buttons)
    if result.cget("text") == " " and result.cget("state") != "disabled" :
        result.config(text="o", font=("poppins", 20), state="disabled", disabledforeground="black", bg="gray")
    
    elif result.cget("text") != " ":      
          pc_choice()
          
         
          


# function to restart whole game when user click restarts
def re_start():
    b1.config(text=" ", font=("poppins", 20), bg="#fff",state=tk.NORMAL)
    b2.config(text=" ", font=("poppins", 20) ,bg="#fff",state=tk.NORMAL)
    b3.config(text=" ", font=("poppins", 20), bg="#fff",state=tk.NORMAL)

    b4.config(text=" ", font=("poppins", 20), bg="#fff",state=tk.NORMAL)
    b5.config(text=" ", font=("poppins", 20) ,bg="#fff",state=tk.NORMAL)
    b6.config(text=" ", font=("poppins", 20), bg="#fff",state=tk.NORMAL)

    b7.config(text=" ", font=("poppins", 20), bg="#fff",state=tk.NORMAL)
    b8.config(text=" ", font=("poppins", 20) ,bg="#fff",state=tk.NORMAL)
    b9.config(text=" ", font=("poppins", 20), bg="#fff",state=tk.NORMAL)


#function to  insert x when user click
def insert(button):
    if button.cget("text") == " " and button.cget("state") == "normal":
        button.config(text="X", font=("poppins", 20), state="disabled", disabledforeground="black", bg="black")
        #check_winner()
        if check_winner():
            disable_btns()
        

        else :
            pc_choice()
            pc_win_check()


   
#remember to call mainloop after all code
game.mainloop()