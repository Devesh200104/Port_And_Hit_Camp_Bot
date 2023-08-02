import getmac
import mouse
import os
import winreg
import subprocess
import zipfile
import socket
import threading
import imutils
import cv2 as cv
import numpy as np
import pyautogui as py
import time
import keyboard
import win32api, win32con
import pyautogui
import pydirectinput
from ctypes import*
import multiprocessing as mp
from multiprocessing import Pool
from multiprocessing import Manager,freeze_support
import discord
from discord.ext import commands
import datetime
import functools
import cv2
import random
import time
import platform

def process_check(process_name):
    try:
        call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
        # use buildin check_output right away
        output = subprocess.check_output(call).decode()
        # check in last line for process name
        last_line = output.strip().split('\r\n')[-1]
        # because Fail message could be translated
        return last_line.lower().startswith(process_name.lower())

    except Exception as e:
        print(str(e))

def check_present(needle_img,haystack_img,threshold=0.5,eps_val=0.5):

    try:
        result = cv.matchTemplate(haystack_img, needle_img, cv.TM_CCOEFF_NORMED)
        locations = np.any(result >= threshold)
        if locations:
            return 1
        return 0
    except Exception as e:
        print(str(e))
    #locations = list(zip(*locations[::-1]))

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def sortFunction(a, b) :
    if (a[0] == b[0]):
        return 0
     
    else :
        if (a[0] < b[0]):
            return -1
        return 1

def sortArr(arr, n, p):

     
    vp = [0 for _ in range(n)]

    for i in range(n):
   
        dist = pow((p[0] - arr[i][0]), 2) + pow((p[1] - arr[i][1]), 2)
        vp[i] = [dist, [arr[i][0], arr[i][1]]]
     
    vp.sort(key=functools.cmp_to_key(sortFunction))
    sorted_cords=[]
    for i in range(n):
        #print("(", vp[i][1][0], ", ", vp[i][1][1], ") ", sep = "", end = " ")
        sorted_cords.append([vp[i][1][0],vp[i][1][1]])

    return sorted_cords

global video_length
f=open("Depe/Video_length.txt","r")
video_length=float(f.read())
f.close()

global breaker
f=open("Depe/breaker.txt","r")
breaker=int(f.read())
f.close()

global press_time
f=open("Depe/press_time.txt","r")
press_time=float(f.read())
f.close()

global multi_region
f=open("depe/multi_region.txt","r")
multi_region=int(f.read())
f.close()

global extra_sleep
f=open("Depe/extra_sleep.txt","r")
extra_sleep=float(f.read())
f.close()

global time_before_home_click
f=open("S_Depe/time_before_home_click.txt","r")
time_before_home_click=float(f.read())
f.close()

global time_after_home_click
f=open("S_Depe/time_after_home_click.txt","r")
time_after_home_click=float(f.read())
f.close()


global swipe_delay
f=open("Depe/swipe_d_1.txt","r")
content=float(f.read())
swipe_delay=content
f.close()



f=open("Discord_Control.txt","r")
content=str(f.read())
global discord_val
discord_val=content.lower()
f.close()


global same_camp_diff_val
f=open("Depe/same_camp_diff_val.txt","r")
same_camp_diff_val=int(f.read())
f.close()

global diff_value
f=open("S_Depe\diff_val.txt","r")
diff_value=int(f.read())
f.close()


global double_check
f=open("Depe/Double_check.txt","r")
double_check=f.read()
f.close()

global roll_back1
f=open("Depe/roll_back1.txt","r")
roll_back1=float(f.read())
f.close()

global roll_back2
f=open("Depe/roll_back2.txt","r")
roll_back2=float(f.read())
f.close()

global r_swipe
f=open("Depe/r_swipe.txt","r")
r_swipe=int(f.read())
f.close()

global l_swipe
f=open("Depe/l_swipe.txt","r")
l_swipe=int(f.read())
f.close()

global u_swipe
f=open("Depe/u_swipe.txt","r")
u_swipe=int(f.read())
f.close()

global d_swipe
f=open("Depe/d_swipe.txt","r")
d_swipe=int(f.read())
f.close()

global Game_Name
f=open("Depe/name.txt","r")
Game_Name=f.read()
f.close()

def Game_Running():
    return process_check(Game_Name)

global x_s_1920
f=open("Depe/x_y/x_s_1920.txt","r")
x_s_1920=int(f.read())
f.close()

global y_s_1920
f=open("Depe/x_y/y_s_1920.txt","r")
y_s_1920=int(f.read())
f.close()

global x_p_1920
f=open("Depe/x_y/x_p_1920.txt","r")
x_p_1920=int(f.read())
f.close()

global y_p_1920
f=open("Depe/x_y/y_p_1920.txt","r")
y_p_1920=int(f.read())
f.close()


global x_s_1366
f=open("Depe/x_y/x_s_1366.txt","r")
x_s_1366=int(f.read())
f.close()

global y_s_1366
f=open("Depe/x_y/y_s_1366.txt","r")
y_s_1366=int(f.read())
f.close()

global x_p_1366
f=open("Depe/x_y/x_p_1366.txt","r")
x_p_1366=int(f.read())
f.close()

global y_p_1366
f=open("Depe/x_y/y_p_1366.txt","r")
y_p_1366=int(f.read())
f.close()


global n_region
f=open("Depe/n_region.txt","r")
content=int(f.read())
n_region=content
f.close()

global restart_time
f=open("Depe/restart_time.txt","r")
restart_time=float(f.read())*60
f.close()

global fail_safe
f=open("Depe/Fail_Safe.txt","r")
fail_safe= str(f.read())
f.close()

global faa
f= open("Depe/faa.txt","r")
faa=float(f.read())
f.close()

global wait_val
f=open("Depe/wait_val.txt","r")
content= float(f.read())
wait_val=content
f.close()

global max_scroll
f=open("Depe/max_scroll.txt","r")
max_scroll=float(f.read())
f.close()

global s_method
f=open("Depe/scroll_method.txt","r")
s_method=int(f.read())
f.close()


global acc_10
f=open("Depe/th/t_10.txt","r")
acc_10=float(f.read())
f.close()

global acc_9
f=open("Depe/th/t_9.txt","r")
acc_9=float(f.read())
f.close()

global wait_after_port
f=open("Depe/wait_after_port.txt","r")
wait_after_port=float(f.read())
f.close()


global acc_8
f=open("Depe/th/t_8.txt","r")
acc_8=float(f.read())
f.close()

global acc_7
f=open("Depe/th/t_7.txt","r")
acc_7=float(f.read())
f.close()

global acc_6
f=open("Depe/th/t_6.txt","r")
acc_6=float(f.read())
f.close()

global acc_5
f=open("Depe/th/t_5.txt","r")
acc_5=float(f.read())
f.close()

global cfds
f=open("Depe/cfds.txt","r")
cfds=int(f.read())
f.close()


global r_wait
f=open("Depe/r_wait.txt","r")
r_wait=float(f.read())
f.close()

global a_t
f=open("Depe/a_t.txt","r")
a_t=float(f.read())
f.close()

global b_t
f=open("Depe/b_t.txt","r")
b_t=float(f.read())
f.close()

global crash_value
f=open("Depe/Crash_Detection.txt","r")
crash_value=str(f.read())
f.close()

global camp_disappear_time
f=open("S_Depe/camp_disappear_time.txt","r")
camp_disappear_time=float(f.read())
f.close()

def spawn_checker():
    s_time=[int(i) for i in spawn_time.split(":")]
    spawn_h=s_time[0]
    spawn_m=s_time[1]

    now = datetime.datetime.now()

    current_time = (now.strftime("%H:%M:%S"))
    current_time_arr = [int(i) for i in current_time.split(':')]
    current_h= current_time_arr[0]
    current_m= current_time_arr[1]
    current_s= current_time_arr[2]
    FMT = '%H:%M:%S'
    
    if((spawn_h%2)==(current_h%2)):
        spawned_duration=current_m-spawn_m
        if spawned_duration>=0 and spawned_duration<=camp_disappear_time:
            return True
        else:
            return False
    else:
        
        last_spawn_se_time= (60-spawn_m)+current_m
        next_spawn_me_time= (60-current_m)+spawn_m
        if last_spawn_se_time<45:
            return True
        return False

from tkinter import *
from tkinter import messagebox

def display_pannel():

    from PIL import Image,ImageTk


    def Settings():
        
        top=Toplevel()
        top.iconbitmap(resource_path("bot.ico"))
        top.title("Change Settings")
        
        def swipe_finder():
            val=swipe_var.get()
            if val==1:
                my_file=open("S_Depe/swipe_method.txt", mode="w")
                my_file.write(str('slow'))
                my_file.close() 
            else:
                my_file=open("S_Depe/swipe_method.txt", mode="w")
                my_file.write(str('fast'))
                my_file.close() 
                
                
        def Tweaker_Finder():
            curr_value=str(scale.get())
            if curr_value!='':
                my_file=open("Depe/Settings/delay.txt", mode="w")
                my_file.write(str(curr_value))
                my_file.close() 
                
                

        
        
        def spawn_finder():
            val=hit_at_spawn_var.get()
            if val==1:
                my_file=open("Depe/Settings/hit_at_spawn.txt", mode="w")
                my_file.write(str('yes'))
                my_file.close()
            else:
                my_file=open("Depe/Settings/hit_at_spawn.txt", mode="w")
                my_file.write(str('no'))
                my_file.close() 

        
        
        def game_finder():
            val=game_open_var.get()
            if val==1:
                my_file=open("Depe/Settings/start_game.txt", mode="w")
                my_file.write(str('yes'))
                my_file.close() 
                
            else:
                my_file=open("Depe/Settings/start_game.txt", mode="w")
                my_file.write(str('no'))
                my_file.close() 
                


        def spawn_time():
            val1= str(hour_var.get())
            val2= str(min_var.get())
            if val1!='' and val2!='':
                val=val1+":"+val2

                my_file=open("Depe/Settings/spawn_time.txt", mode="w")
                my_file.write(str(val))
                my_file.close() 


        def spawn_duration():
            val1=str(spawn_hour.get())
            val2=str(spawn_min.get())
            if val1!='' and val2!='':
                val=val1+":"+val2

                my_file=open("Depe/Settings/camp_disappear_time.txt",mode="w")
                my_file.write(str(val))
                my_file.close()

        def region_finder():
            val=region_var.get()

            if val==1:
                f=open("Depe/multi_region.txt",mode="w")
                f.write(str(1))
                f.close()

            elif val==2:
                f=open("Depe/multi_region.txt",mode="w")
                f.write(str(2))
                f.close()

            else:

                f=open("Depe/multi_region.txt",mode="w")
                f.write(str(3))
                f.close()





             
        def save_settings():
            Tweaker_Finder()
            spawn_time()

            spawn_finder()

            game_finder()
            spawn_duration()
            region_finder()
            top.destroy()


        all_frame=LabelFrame(top,text="Settings")
        
        
        ## Delay
        
        my_file=open("Depe/Settings/delay.txt", mode="r")
        delay_val=my_file.read()
        my_file.close() 
        
        label_delay=Label(all_frame,text="Delay : ",fg="#990000")
        label_delay.grid(row=1,column=0)

        scale= Scale(all_frame,from_=6, to=16,orient=HORIZONTAL)
        scale.set(delay_val)
        scale.grid(row=1,column=1)

        
        ## Port Type

        label_region=Label(all_frame,text="Region Check : ",fg='#990000').grid(row=2,column=0,pady=10)
        options=[["1 ",1],["4 ",2],["8 ",3]]

        region_var=IntVar()

        f=open("Depe/multi_region.txt","r")
        region_val=f.read()
        f.close()

        if region_val=='1':
            region_var.set(1)

        elif region_val=='2':
            region_var.set(2)

        else:
            region_var.set(3)


        c=1
        for text, val in options :
            R_button= Radiobutton(all_frame,text=text,variable=region_var ,value=val).grid(row=2,column=c)
            c+=1


        

            
        ## Hit At Spawn 
        
        label_port=Label(all_frame,text="Hit Only At Spawn : ",fg="#990000").grid(row=3,column=0,pady=10)
        options= [["Yes ",1],["No ",2]]
        hit_at_spawn_var=IntVar() 
        
        f=open("Depe/Settings/hit_at_spawn.txt","r")
        hit_at_spawn_val=f.read()
        f.close()
        
        if hit_at_spawn_val=='yes':
            hit_at_spawn_var.set(1)
        else:
            hit_at_spawn_var.set(2)
            
        

        c=1
        for text, val in options :
            R_button= Radiobutton(all_frame,text=text,variable=hit_at_spawn_var ,value=val).grid(row=3,column=c)
            c+=1




        
        
        ## Game Restart
        
        label_port=Label(all_frame,text="Close Game After Spawn : ",fg="#990000").grid(row=4,column=0,pady=10)
        options= [["Yes ",1],["No ",2]]
        game_open_var=IntVar() 
        
        f=open("Depe/Settings/start_game.txt","r")
        game_open_val=f.read()
        f.close()
        
        if game_open_val=='yes':
            game_open_var.set(1)
        else:
            game_open_var.set(2)
            
        c=1
        for text, val in options :
            R_button= Radiobutton(all_frame,text=text,variable=game_open_var,value=val).grid(row=4,column=c)
            c+=1
        ### Season
        
        

        
        

        
        ## Spawn Time
        
        
        Entry_Frame = LabelFrame(all_frame,text="Write Spawn Time",padx=20,pady=20,fg="#990000")
        hour_var=StringVar()
        min_var=StringVar()
        entry_hour = Entry(Entry_Frame,textvariable=hour_var,width=5)
        entry_min = Entry(Entry_Frame,textvariable=min_var,width=5)
        
        f=open("Depe/Settings/spawn_time.txt","r")
        time_=f.read()
        time_=time_.split(":")
        f.close()
        hour_var.set(time_[0])
        min_var.set(time_[1])
        

        entry_hour.grid(row=0,column=0)
        h_label=Label(Entry_Frame,text="H").grid(row=0,column=1)
        entry_min.grid(row=0,column=2)
        m_label=Label(Entry_Frame,text="M").grid(row=0,column=3)
        Entry_Frame.grid(row=7,column=0,columnspan=3)


        ### Duration To Run Per Spawn

        Entry_spawn = LabelFrame(all_frame,text="Duration To Run Per Spawn : ",padx=20,pady=20,fg="#990000")
        spawn_hour=StringVar()
        spawn_min=StringVar()
        entry_h = Entry(Entry_spawn,textvariable=spawn_hour,width=5)
        entry_m = Entry(Entry_spawn,textvariable=spawn_min,width=5)
        
        f=open("Depe/Settings/camp_disappear_time.txt","r")
        time_=f.read()
        time_=time_.split(":")
        f.close()
        spawn_hour.set(time_[0])
        spawn_min.set(time_[1])
        

        entry_h.grid(row=0,column=0)
        h_label=Label(Entry_spawn,text="H").grid(row=0,column=1)
        entry_m.grid(row=0,column=2)
        m_label=Label(Entry_spawn,text="M").grid(row=0,column=3)
        Entry_spawn.grid(row=8,column=0,columnspan=3)

        
        ## Info Label
        
        notice_label=Label(all_frame,text="You Just Need To Write One Spawn Time. It Will calculate other spawn times and hit accordingly",fg="#990000").grid(row=10,column=0,columnspan=5)
        
        ## Save Button
        save_button=Button(top,text="Save Changes",command=save_settings,bg='#990000',fg="white").grid(row=10,column=0,columnspan=3)
        all_frame.grid(row=0,column=0,pady=20)


    root= Tk()

    

    root.iconbitmap(resource_path("bot.ico"))
    root.title("Levi Bots : Port And Hit Camp Bot")
    img = ImageTk.PhotoImage(Image.open(resource_path("port_camp.png")))
    label = Label(image=img)

    label.grid(row=0,column=0,columnspan=3)


    Scanner_Button = Button(root,text="Settings",padx=25,command=Settings,fg="white",bg="#990000").grid(row=5,column=1)


    #tw=Tweaker_Finder()
    
    Entry_Frame = LabelFrame(root,text="Select Duration To Run",padx=20,pady=20,fg="#990000")
    entry_hour = Entry(Entry_Frame,width=5)
    entry_min = Entry(Entry_Frame,width=5)

    def time_finder():
        val1= entry_hour.get()
        val2= entry_min.get()
        global hours,mins
        if val1=='':
            hours=0
        else:
            hours=val1
        if val2=='' and val1!='':
            mins=0
        elif val2=='' and val1=='':
            mins=0
            hours=10
        elif val2!='':
            mins=val2

    entry_hour.grid(row=0,column=0)
    h_label=Label(Entry_Frame,text="Hour").grid(row=0,column=1)
    entry_min.grid(row=0,column=2)
    m_label=Label(Entry_Frame,text="Min").grid(row=0,column=3)


    ### March Finder



      
    ### Camp Level Finder
    Check_Box_Frame=LabelFrame(root,text="Camp Lvl",padx=30,pady=20,fg="#990000")

    one=IntVar()
    two=IntVar()
    three=IntVar()
    four=IntVar()
    five=IntVar()
    six= IntVar()
    seven=IntVar()
    eigth=IntVar()
    
    c8=Checkbutton(Check_Box_Frame,variable=eigth,text="12").grid(row=0,column=0)
    c7=Checkbutton(Check_Box_Frame,variable=seven,text="11").grid(row=0,column=1)
    c1=Checkbutton(Check_Box_Frame,variable=one,text=" 10 ").grid(row=0,column=2)
    c2=Checkbutton(Check_Box_Frame,variable=two,text=" 9 ").grid(row=0,column=3)
    c3=Checkbutton(Check_Box_Frame,variable=three,text="8 ").grid(row=0,column=4)
    c4=Checkbutton(Check_Box_Frame,variable=four,text=" 7 ").grid(row=0,column=5)
    c5=Checkbutton(Check_Box_Frame,variable=five,text=" 6 ").grid(row=0,column=6)
    c6=Checkbutton(Check_Box_Frame,variable=six,text=" 5 ").grid(row=0,column=7)



    def food_finder():
        curr_val=one.get()
        global c_10
        c_10=curr_val
        
    def wood_finder():
        curr_val=two.get()
        global c_9
        c_9=curr_val
        
    def iron_finder():
        curr_val=three.get()
        global c_8
        c_8=curr_val
        
    def stone_finder():
        curr_val=four.get()
        global c_7
        c_7=curr_val
        
    def silver_finder():
        curr_val=five.get()
        global c_6
        c_6=curr_val

    def gold_finder():
        curr_val=six.get()
        global c_5
        c_5=curr_val

    def c11_finder():
        curr_val=seven.get()
        global c_11
        c_11=curr_val

    def c12_finder():
        curr_val=eigth.get()
        global c_12
        c_12=curr_val


        
    def All_Finder():
        food_finder()
        wood_finder()
        iron_finder()
        stone_finder()
        silver_finder()
        gold_finder()
        c11_finder()
        c12_finder()
        


    ### Season ###


    def season_finder():
        val=season_var.get()
        f=open("Depe/Settings/season.txt","w")
        if val==1:
            f.write("Summer")
        elif val==2:
            f.write("Spring")
        elif val==3:
            f.write("Autumn")
            
        else:
            f.write("Winter")
        f.close()
            

    season_frame= LabelFrame(root,text="Season",padx=30,pady=20,fg="#990000")

    #label_season=Label(season_frame,text="Season : ",fg="#990000").grid(row=5,column=0,pady=10)
    options= [["Summer ",1],["Spring ",2],["Autumn",3],["Winter",4]]
    season_var=IntVar() 
    
    f=open("Depe/Settings/season.txt")
    season_val=f.read()
    f.close()
    if season_val=='Summer':
        season_var.set(1)
    elif season_val=='Spring':
        season_var.set(2)
    elif season_val=='Autumn':
        season_var.set(3)
    else:
        season_var.set(4)

    c=1
    for text, val in options :
        R_button= Radiobutton(season_frame,text=text,variable=season_var,value=val).grid(row=5,column=c)
        c+=1

    def killer():

        time_finder()
        season_finder()
        All_Finder()

        root.destroy()
        
    Button(root,text="Start",bg="#990000",fg="white",padx=130,pady=10,command=killer,relief=GROOVE).grid(row=5,column=0,columnspan=1)
    message_frame=LabelFrame(root,text="Levi Bots",fg='#990000',padx=10,pady=20)
    label2=Label(message_frame,text="Contact Info : ",fg='#990000',padx=10).grid(row=1,column=0)
    label3=Label(message_frame,text="Line : botsmoe ",fg='#990000',padx=10).grid(row=2,column=0)
    label4=Label(message_frame,text="Discord : levi1709  ",fg='#990000',padx=10).grid(row=3,column=0)
    label5=Label(message_frame,text="Gmail : automationexperts.org@gmail.com",fg='#990000',padx=10).grid(row=4,column=0)

    Entry_Frame.grid(row=3,column=1,pady=10)
    season_frame.grid(row=3,column=0,padx=10,pady=10)
    message_frame.grid(row=4,column=1,pady=10)
    Check_Box_Frame.grid(row=4,column=0,padx=10,pady=10)




    root.mainloop()

    global x_reducer
    f=open("Depe/x_reducer.txt","r")
    x_reducer=int(f.read())
    f.close()

    global y_reducer
    f=open("Depe/y_reducer.txt","r")
    y_reducer=int(f.read())
    f.close()

    s=open("filter.txt",mode="r")
    global accuracy
    amat = s.read()
    accuracy=int(amat)*(0.01)
    s.close()
    global tweaker
    s=open("Depe/Settings/delay.txt","r")
    tweaker=int(s.read())
    global delay
    delay=tweaker*0.1

    s=open("Depe/Settings/march.txt","r")
    global marches
    marches=int(s.read())
    s.close()
    global start_game_at_spawn
    s=open("Depe/Settings/start_game.txt","r")
    start_game_at_spawn=s.read()
    s.close()

    global port_type
    s=open("Depe/Settings/port_type.txt","r")
    port_type=s.read()
    s.close()

    global start_time
    start_time=time.time()

    global samay
    samay= (float(hours)*60*60)+ (float(mins)*60)

    global season
    f=open("Depe/Settings/Season.txt","r")
    season=str(f.read())
    f.close()

    global hit_at_spawn
    f=open("Depe/Settings/hit_at_spawn.txt","r")
    hit_at_spawn=f.read()
    f.close()

    global spawn_time
    f=open("Depe/Settings/spawn_time.txt","r")
    spawn_time=f.read()
    f.close()
    s_t=spawn_time.split(":")
    s_h=int(s_t[0])
    s_m=int(s_t[1])
    print()
    if s_h%2==0:
        print("Spawn Time = Even : ",s_m)
    else:
        print("Spawn Time = Odd  : ",s_m)


    global camp_disappear_time
    f=open("Depe/Settings/camp_disappear_time.txt","r")
    loc_time=f.read()
    f.close()
    loc_time=[float(i) for i in loc_time.split(":")]
    camp_disappear_time=loc_time[0]*60*60 + loc_time[1]*60

    print("Duration To Hit Per Spawn = ",int(loc_time[0]),"H:",int(loc_time[1]),"M")
    

    global map_scan_type
    f=open("Depe/settings/map_scanner.txt","r")
    map_scan_type=f.read()
    f.close()

def screen_recorder():

    start=time.time()

    SCREEN_SIZE=(1920,1080) 
    fourcc = cv.VideoWriter_fourcc(*"XVID")
    out="live_video.avi"
    out =cv.VideoWriter(out,fourcc,12.0,(SCREEN_SIZE))

    fps=60
    prev=0 
    v_le=video_length   
    while True:
        end=time.time()
        if (end-start>v_le):
            break
        time_elapsed = time.time()-prev
        img=py.screenshot()

        if time_elapsed> 1.0/fps:
            prev=time.time()
            frame=np.array(img)
            frame=cv.cvtColor(frame,cv.COLOR_BGR2RGB)
            out.write(frame)


global discord_key
f=open("Depe/Discord_Key.txt","r")
discord_key=f.read()
f.close()

global Game_name
f=open("Depe/name.txt","r")
Game_name=f.read()
f.close()


def discord_commander(cmd_number,server_arr,discord_key_arr):

    discord_key="none"
    while True:
        time.sleep(1)
        if server_arr[0]==-1:
            return
        if server_arr[0]==1:
            b=[chr(discord_key_arr[i]) for i in range(discord_key_arr[119])]
            discord_key=""
            for i in b[0:len(b)]:
                #print(i,end="")
                discord_key+=i
            discord_key=str(discord_key)
            break
    if discord_key=='none':
        return
    bot = commands.Bot(command_prefix=".")

    @bot.command()
    async def levi(ctx):
        #time.sleep(0.5)
        await ctx.send(file=discord.File(r'commands_explanation.png'))

    @bot.command()
    async def startgame(ctx):
        if cmd_number[0]==1:
            cmd_number[2]=1
            await ctx.reply('The Game is already opened On Windows')
            os.system("start explorer shell:appsFolder\A278AB0D.MarchofEmpires_h6adky7gbf63m!App")
        else:
            cmd_number[0]=1
            cmd_number[2]=1
            os.system("start explorer shell:appsFolder\A278AB0D.MarchofEmpires_h6adky7gbf63m!App")
            await ctx.reply('The game is opening , You can check The status using .pic command (: ')

    @bot.command()
    async def stopgame(ctx):
        cmd_number[0]=0
        await ctx.reply('The Game will be closed. Make sure to close bot first. (:')
        time.sleep(0.1)
        #py.click(1892,17)
        task_kill="TASKKILL /F /IM "+Game_Name
        os.system(task_kill)
        #time.sleep(0.2)
        #await ctx.reply('Done!')

    @bot.command()
    async def startbot(ctx):
        cmd_number[1]=1
        cmd_number[0]=1
        cmd_number[3]=1
        await ctx.reply('Bot is started.')

    @bot.command()
    async def pause(ctx):
        cmd_number[1]=0
        await ctx.reply('The Bot will be Paused After clearing this region (: ')

    @bot.command()
    async def stopbot(ctx):
        cmd_number[1]=0
        cmd_number[3]=0
        await ctx.reply('The Bot will be Stopped (: ')




    @bot.command()
    async def pic(ctx):
        ss=py.screenshot()
        ss.save(r"test.png")
        #time.sleep(0.5)
        await ctx.send(file=discord.File(r'test.png'))

    @bot.command()
    async def video(ctx):
        await ctx.reply('Live Video Connecting ...')
        screen_recorder()
        await ctx.reply('Connected ')
        #await asyncio.sleep(10)
        time.sleep(1)
        await ctx.send(file=discord.File(r'Live_Video.avi'))


    @bot.command()
    async def retry(ctx):
        py.click(954,690)
        await ctx.reply("Retrying")

    @bot.command()
    async def hello(ctx):
        str = "hello "+ctx.message.author.name+" Sir "+".I am olivia your assistant."
        await ctx.reply(str)




    @bot.command()
    async def about(ctx):
        await ctx.reply("My name is Olivia, a virtual assistant . My job is to convey your messages to my brother Camp Bot . If i missbehave please complain our father at line id :botsmoe . Thank you") 





     
    @bot.command()
    async def status(ctx):
        #now = datetime.now()
        #current_time = now.strftime("%H:%M:%S")
        #print("Current Time =", current_time)
        stra=""
        if cmd_number[0]==1:
            stra+="Game is on. "
        if cmd_number[1]==1 and cmd_number[3]==1:
            stra+="Bot is on. "
        if cmd_number[0]==0:
            stra+="Game is off. "
        if cmd_number[1]==0 or cmd_number[3]==0:
            stra+="Bot is off. "
        stra+="You can check Live Status using : .pic  OR  .video "
        await ctx.reply(stra)



    bot.run(discord_key)










global lvl_check_method
f=open("Depe/lvl_check_method.txt","r")
lvl_check_method=int(f.read())
f.close()


def mod(x):
    if x<0:
        return -1*x
    return x



def mouseclick(a, b):
    mouse.move(a, b, True, 0)
    mouse.click(button='left')


def click(x,y):

    mouseclick(x,y)



is_retina = False
if platform.system() == "Darwin":
    is_retina = subprocess.call("system_profiler SPDisplaysDataType | grep 'retina'", shell=True)

def region_grabber(region):
    if is_retina: region = [n * 2 for n in region]
    x1 = region[0]
    y1 = region[1]
    width = region[2] - x1
    height = region[3] - y1

    return pyautogui.screenshot(region=(x1, y1, width, height))


def imagesearcharea(image, x1, y1, x2, y2, precision=0.8, im=None):
    if im is None:
        im = pyautogui.screenshot(region=(x1, y1, x2, y2))
        if is_retina:
            im.thumbnail((round(im.size[0] * 0.5), round(im.size[1] * 0.5)))

    img_rgb = np.array(im)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(image, 0)
    template.shape[::-1]
    
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if max_val < precision:
        return [-1, -1]
    return max_loc


def click_image(image, pos, action, timestamp, offset=5):
    img = cv2.imread(image)
    height, width, channels = img.shape
    pyautogui.moveTo(pos[0] + r(width / 2, offset), pos[1] + r(height / 2, offset),
                     timestamp)
    py.click(button=action)


def imagesearch(image, precision=0.8):
    im = pyautogui.screenshot()
    if is_retina:
        im.thumbnail((round(im.size[0] * 0.5), round(im.size[1] * 0.5)))
    
    img_rgb = np.array(im)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(image, 0)
    template.shape[::-1]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if max_val < precision:
        return [-1, -1]
    return max_loc


def imagesearch_loop(image, timesample, precision=0.8):
    pos = imagesearch(image, precision)
    while pos[0] == -1:
        print(image + " not found, waiting")
        time.sleep(timesample)
        pos = imagesearch(image, precision)
    return pos


def imagesearch_numLoop(image, timesample, maxSamples, precision=0.8):
    pos = imagesearch(image, precision)
    count = 0
    while pos[0] == -1:
        print(image + " not found, waiting")
        time.sleep(timesample)
        pos = imagesearch(image, precision)
        count = count + 1
        if count > maxSamples:
            break
    return pos


def imagesearch_region_loop(image, timesample, x1, y1, x2, y2, precision=0.8):
    pos = imagesearcharea(image, x1, y1, x2, y2, precision)

    while pos[0] == -1:
        time.sleep(timesample)
        pos = imagesearcharea(image, x1, y1, x2, y2, precision)
    return pos


def imagesearch_numLoop_self(image, maxSamples, precision,reg):
    pos =py.locateOnScreen(image,region=reg,confidence=precision)
    count = 0
    while pos == None:
        #print(image + " not found, waiting")
        #time.sleep(timesample)
        pos = py.locateOnScreen(image,region=reg,confidence=precision)
        count = count + 1
        if count > maxSamples:
            break
    if pos!=None:
        pos=py.center(pos)
        return pos
    return pos


def findClickPositions(needle_img,haystack_img,threshold=0.5,eps_val=0.5):
        

    needle_w = needle_img.shape[1]
    needle_h = needle_img.shape[0]

    # There are 6 methods to choose from:
    # TM_CCOEFF, TM_CCOEFF_NORMED, TM_CCORR, TM_CCORR_NORMED, TM_SQDIFF, TM_SQDIFF_NORMED

    result = cv.matchTemplate(haystack_img, needle_img, cv.TM_CCOEFF_NORMED)


    locations = np.where(result >= threshold)
    locations = list(zip(*locations[::-1]))

    rectangles = []
    for loc in locations:
        rect = [int(loc[0]), int(loc[1]), needle_w, needle_h]
        # Add every box to the list twice in order to retain single (non-overlapping) boxes
        rectangles.append(rect)
        rectangles.append(rect)

    rectangles, weights = cv.groupRectangles(rectangles, groupThreshold=1, eps=eps_val)


    points = []
    if len(rectangles):


        line_color = (0, 255, 0)
        line_type = cv.LINE_4
        marker_color = (255, 0, 255)
        marker_type = cv.MARKER_CROSS

        # Loop over all the rectangles
        for (x, y, w, h) in rectangles:

            # Determine the center position
            center_x = x + int(w/2)
            center_y = y + int(h/2)
            # Save the points
            points.append([center_x,center_y])
    return points

def r(num, rand):
    return num + rand * random.random()




def isNumLockOn():
    return win32api.GetKeyState(win32con.VK_NUMLOCK)

f=open("Depe/tab.txt","r")
tab_check=f.read()
f.close()

    
def scroller_windows():
    py.keyDown("pagedown")
    time.sleep(0.01)
    py.keyUp("pagedown")




  
def windows_1920(cmd_number,settings,server_arr,discord_key_arr):

    dir="img_1920/"

    while True:
        time.sleep(1)
        if server_arr[0]==-1:
            return
        if server_arr[0]==1:
            display_pannel()
            break

    def pause():

        while cmd_number[3]!=1:
            time.sleep(0.1)


    global swipe_delay
    f=open("Depe/swipe_d_1.txt","r")
    content=float(f.read())
    swipe_delay=content
    f.close()



    global extra_check
    f=open("S_Depe/extra_check.txt","r")
    extra_check=f.read()
    f.close()


    global swipe_method
    f=open("S_Depe/swipe_method.txt","r")
    swipe_method=f.read()
    f.close()
    
    global location_opener_stuck
    f=open("S_Depe/location_opener_stuck.txt","r")
    location_opener_stuck=f.read()
    f.close()

    global time_before_location_opener
    f=open("S_Depe/time_before_location_opener.txt","r")
    time_before_location_opener=float(f.read())
    f.close()

    global time_before_home_click
    f=open("S_Depe/time_before_home_click.txt","r")
    time_before_home_click=float(f.read())
    f.close()

    global time_after_home_click
    f=open("S_Depe/time_after_home_click.txt","r")
    time_after_home_click= float(f.read())


    global c8_888
    c8_888 = np.load(resource_path('img_1920/35'))
    global c9_888
    c9_888 = np.load(resource_path('img_1920/36'))
    global c10_888
    c10_888 = np.load(resource_path('img_1920/37'))

    global sn7
    sn7 = np.load(resource_path('img_1920/38'))

    global c7_777
    c7_777=cv.imread(resource_path("img_1920/c7.png"))
    c7_777=cv.cvtColor(np.array(c7_777),cv.COLOR_RGB2GRAY)

    global c6_666
    c6_666=cv.imread(resource_path("img_1920/c6.png"))
    c6_666=cv.cvtColor(np.array(c6_666),cv.COLOR_RGB2GRAY)

    global c5_555
    c5_555=cv.imread(resource_path("img_1920/c5.png"))
    c5_555=cv.cvtColor(np.array(c5_555),cv.COLOR_RGB2GRAY)

    global c11_11
    c11_11=cv.imread(resource_path("img_1920/c11.png"))
    c11_11=cv.cvtColor(np.array(c11_11),cv.COLOR_RGB2GRAY)


    global c12_12
    c12_12=cv.imread(resource_path("img_1920/c12.png"))
    c12_12=cv.cvtColor(np.array(c12_12),cv.COLOR_RGB2GRAY)


    global time_between_clicks
    f=open("Depe/time_between_clicks.txt","r")
    time_between_clicks=float(f.read())
    f.close()

    global cascade_camps
    cascade_camps=cv.CascadeClassifier(resource_path('img_1920/cascade.xml'))


    def get_camp_locations(ss):
        try:
            ss=cv.cvtColor(np.array(ss),cv.COLOR_RGB2BGR)
            rectangles=cascade_camps.detectMultiScale(ss)

            return rectangles

        except Exception as e:
            print(str(e))


    def click_checker(cord):
        
        if cord[0]>0 and cord[1]>223 and cord[0]<578 and cord[1]<615:
            left_value=check_left_area()
            if left_value==1:
                mouseclick(515,321)
                time.sleep(tweaker*0.1-0.4+.25)
            if left_value==2:
                mouseclick(515,413)
                time.sleep(tweaker*0.1-0.4+.25)

            if left_value==3:
                mouseclick(515,515)
                time.sleep(tweaker*0.1-0.4+.25)
            return True
        if cord[1]<=139:
            return False
        if cord[0]>1801 and cord[1]>230 and cord[0]<1900 and cord[1]<551:
            return False

        if cord[1]>880:
            return False
        return True


    def check_left_area():
        

        side_ss=py.screenshot(region=(49,243,67,46))
        side_ss=cv.cvtColor(np.array(side_ss),cv.COLOR_RGB2BGR)

        needle_img1 = cv.imread(resource_path(dir+"side_icon.png"), cv.IMREAD_UNCHANGED)

        needle_img1= cv.cvtColor(np.array(needle_img1), 
                        cv.COLOR_RGB2BGR)

        
        if check_present(needle_img1,side_ss,threshold=0.75,eps_val=1):
            return 2


        needle_img1 = cv.imread(resource_path(dir+"hammer.png"), cv.IMREAD_UNCHANGED)

        needle_img1= cv.cvtColor(np.array(needle_img1), 
                        cv.COLOR_RGB2BGR)

        if check_present(needle_img1,side_ss,threshold=0.60,eps_val=1):
            return 1


        needle_img1 = cv.imread(resource_path(dir+"bell.png"), cv.IMREAD_UNCHANGED)

        needle_img1= cv.cvtColor(np.array(needle_img1), 
                        cv.COLOR_RGB2BGR)

        if check_present(needle_img1,side_ss,threshold=0.75,eps_val=1):
            return 3
        

        return 0


    global b_method
    f=open("Depe/port_settings/b_method_1.txt","r")
    b_method=int(f.read())
    f.close()

    global check_stuck
    f=open("Depe/port_settings/check_stuck.txt","r")
    check_stuck=f.read()
    f.close()

    global diff_value
    f=open("S_Depe\diff_val.txt","r")
    diff_value=int(f.read())
    f.close()

    global port_point_finder
    f=open("Depe/port_point_finder.txt","r")
    port_point_finder=f.read()
    f.close()


    global acc_g
    f=open("Depe/port_settings/1920/acc_g.txt","r")
    acc_g=float(f.read())
    f.close()

    global acc_g2
    f=open("Depe/port_settings/1920/acc_g2.txt","r")
    acc_g2=float(f.read())
    f.close()

    global acc_t
    f=open("Depe/port_settings/1920/acc_t.txt","r")
    acc_t=float(f.read())
    f.close()

    global acc_t2
    f=open("Depe/port_settings/1920/acc_t2.txt","r")
    acc_t2=float(f.read())
    f.close()

    global acc_a
    f=open("Depe/port_settings/1920/acc_a.txt","r")
    acc_a=float(f.read())
    f.close()

    acc_porting=[acc_g,acc_g2,acc_t,acc_t2,acc_a]

    global gola
    f=open("Depe/c_k_d/gola.txt","r")
    gola=float(f.read())
    f.close()

    global r_k_n
    f=open("Depe/c_k_d/r_k_n.txt","r")
    r_k_n=float(f.read())
    f.close()

    global w_interval 
    f=open("Depe/interval.txt","r")
    w_interval=float(f.read())
    f.close()

    global left_doori
    f=open("Depe/left_doori.txt","r")
    left_doori=int(f.read())
    f.close()


    global right_doori
    f=open("Depe/right_doori.txt","r")
    right_doori=int(f.read())
    f.close()

    global top_doori
    f=open("Depe/top_doori.txt","r")
    top_doori=int(f.read())
    f.close()

    global bottom_doori
    f=open("Depe/bottom_doori.txt","r")
    bottom_doori=int(f.read())
    f.close()

    global port_diagonal
    f=open("Depe/port_diagonal.txt","r")
    port_diagonal=int(f.read())
    f.close()


    def filtering_camps(points_camps,points_numbers):
        filtered_points=[]
        if len(points_camps)==0 or len(points_numbers)==0:
            return filtered_points 
        for point_camp in points_camps:
            for point_number in  points_numbers:
                if point_number[0]>=point_camp[0]-120 and point_number[1]>=point_camp[1] and point_number[0]<=point_camp[0] and point_number[1]<=point_camp[1]+140:
                    filtereded_points.append(point_camp)

        return filtered_points


    def image_after_click_camp():
        if c_8==1 or c_9==1 or c_10==1 or c_11==1 or c_12==1:
            img_after_click=imagesearch_numLoop_self(resource_path(dir+"image_after_click.png"),gola,precision=0.9,reg=(836,501,75,49))
            if img_after_click!=None:
                return True


        if c_7==1:
            img_after_click=imagesearch_numLoop_self(resource_path(dir+"image_after_click_7.png"),gola,precision=0.85,reg=(836,501,75,49))
            if img_after_click!=None:
                return True

        if c_6==1:
            img_after_click=imagesearch_numLoop_self(resource_path(dir+"image_after_click_6.png"),gola,precision=0.85,reg=(836,501,75,49))
            if img_after_click!=None:
                return True

        if c_5==1:
            img_after_click=imagesearch_numLoop_self(resource_path(dir+"image_after_click_5.png"),gola,precision=0.85,reg=(836,501,75,49))
            if img_after_click!=None:
                return True

        return False


    def image_after_click_alternative():

        if c_10:
            img_after_click=imagesearch_numLoop_self(resource_path(dir+"image_after_click_10.png"),gola,precision=0.9,reg=(1007,81,76,43))
            if img_after_click!=None:
                return True

        if c_11:
            img_after_click=imagesearch_numLoop_self(resource_path(dir+"image_after_click_11.png"),gola,precision=0.9,reg=(1007,81,76,43))
            if img_after_click!=None:
                return True

        if c_12:
            img_after_click=imagesearch_numLoop_self(resource_path(dir+"image_after_click_12.png"),gola,precision=0.9,reg=(1007,81,76,43))
            if img_after_click!=None:
                return True

        if c_9:
            img_after_click=imagesearch_numLoop_self(resource_path(dir+"image_after_click_9.png"),gola,precision=0.9,reg=(1007,81,76,43))
            if img_after_click!=None:
                return True

        if c_8:
            img_after_click=imagesearch_numLoop_self(resource_path(dir+"image_after_click_8.png"),gola,precision=0.9,reg=(1007,81,76,43))
            if img_after_click!=None:
                return True

        if c_7:
            img_after_click=imagesearch_numLoop_self(resource_path(dir+"image_after_click_7.png"),gola,precision=0.9,reg=(1007,81,76,43))
            if img_after_click!=None:
                return True

        if c_6:
            img_after_click=imagesearch_numLoop_self(resource_path(dir+"image_after_click_6.png"),gola,precision=0.9,reg=(1007,81,76,43))
            if img_after_click!=None:
                return True

        if c_5:
            img_after_click=imagesearch_numLoop_self(resource_path(dir+"image_after_click_5.png"),gola,precision=0.9,reg=(1007,81,76,43))
            if img_after_click!=None:
                return True

        return False


    def shield_1920():
        py.press("w")
        time.sleep(0.2)
        pos=imagesearch_numLoop_self(resource_path(dir+"shield.png"),11,precision=0.65,reg=(32,236,70,53))
        if pos==None:
            click(705,367)
        else:
            click(pos[0],pos[1])
        pos=imagesearch_numLoop_self(resource_path(dir+"eight_hr_shield.png"),15,precision=0.65,reg=(650,216,38,35))
        use=py.locateOnScreen(resource_path(dir+"use.png"),confidence=0.7,region=(935,575,54,59))
        aman="p"
        if use!=None:
            click(1038,607)
            aman="u"
        else:
            click(1225,615)
            aman="g"
            time.sleep(3)
        #click(button="right",clicks=1)

    def shield_checker():
        ss=py.locateOnScreen(resource_path(dir+"shield_img.png"),confidence=0.70,region=(1814,358,85,80))
        if ss==None:
            shield_1920()
            py.click(button="right",clicks=1)
    

    def mod(a):
        if a<0:
            return -1*a
        return a

    def f_points(a):

        bool_arr=[1 for i in range(len(a))]
        for i in range(len(a)):
            if bool_arr[i]==0:
                continue
            for j in range(i+1,len(a),1):
                diff=mod(a[i][0]-a[j][0])+mod(a[i][1]-a[j][1])
                if diff<diff_value:
                    bool_arr[j]=0
        f_points=[]
        for i in range(0,len(a)):
            if bool_arr[i]==1:
                f_points+=[a[i]]
                
        return f_points

    def badha():
        wood_screen=py.locateOnScreen(resource_path(dir+'wood_screen.png'),region=(0,13,60,60),confidence=0.75)
        if wood_screen!=None:
            py.click(button='right', clicks=1)
            time.sleep(.2)

        food_check=py.locateOnScreen(resource_path(dir+'food_check2.png'), region=(1852,46,54,54),confidence=0.55)
        if food_check!=None:
            click(55,978)
            time.sleep(0.6)
            
        ok=pyautogui.locateOnScreen(resource_path(dir+'ok.png'),confidence=0.65)
        if ok!=None:
            time.sleep(0.25)
            try:
                ok=pyautogui.center(ok)
                click(ok[0],ok[1])
            except:
                print("ok missed")


        cross=py.locateOnScreen(resource_path(dir+'cross.png'),confidence=0.75)
        if cross!=None:
            try:
                cross=py.center(cross)
                time.sleep(0.1)
                click(cross[0],cross[1])
            except:
                print("cross missed")

        cross2=py.locateOnScreen(resource_path(dir+'cross2.png'),confidence=0.75)
        if cross2!=None:
            try:
                cross2=py.center(cross)
                time.sleep(0.1)
                click(cross[0],cross[1])
            except:
                print("Cross2 missed")



        if crash_value=="On" or crash_value=="on":
            game_value=Game_Running()
            if game_value==False:
                game_restart()

        continue_lady=py.locateOnScreen(resource_path(dir+'continue_lady.png'),confidence=0.75)
        if continue_lady!=None:
            click(956,790)
            time.sleep(.2)
        rate_us=py.locateOnScreen(resource_path(dir+'rate_us.png'),confidence=0.75)
        if rate_us!=None:
            click(956,790)
            time.sleep(.2)
        


    def game_opener():
        while True:
            retry_check=py.locateOnScreen(resource_path(dir+'retry.png'),region=(858,678,192,66),confidence=0.8)
            if retry_check!=None:
                retry_check=py.center(retry_check)
                click(retry_check[0],retry_check[1])
                time.sleep(0.25)
            ss=py.locateOnScreen(resource_path(dir+"loading_screen.png"),confidence=0.6)
            if ss==None:
                return "khul_gaya"
            time.sleep(1)
        

    def game_restart():

        time.sleep(1)
        os.system("start explorer shell:appsFolder\A278AB0D.MarchofEmpires_h6adky7gbf63m!App")
        time.sleep(4+wait_val)
        game_opener()
        time.sleep(wait_val+1)
        clear_starting_screens()



    def retry_checker():

        retry_check=py.locateOnScreen(resource_path(dir+'retry.png'),region=(858,678,192,66),confidence=0.8)
        if retry_check!=None:
            task_kill="TASKKILL /F /IM "+Game_Name
            os.system(task_kill)
            game_restart()




    if cfds==1:
        def check_for_disturbance(last_loc=None):

            dir='img_1920/'

            ss=py.screenshot()
            ss_gray=cv.cvtColor(np.array(ss),cv.COLOR_RGB2BGR)


            search_area=ss_gray[800:834,98:159]
            

            needle_img1 = cv.imread(resource_path(dir+"tang.png"), cv.IMREAD_UNCHANGED)
            needle_img1= cv.cvtColor(np.array(needle_img1), 
                            cv.COLOR_RGB2BGR)

            if check_present(needle_img1,search_area,0.8):
                py.click(459,999)
                time.sleep(0.5)
                ss=py.screenshot()
                ss_gray=cv.cvtColor(np.array(ss),cv.COLOR_RGB2BGR)


            search_area=ss_gray[13:73, 0:60]

            needle_img1 = cv.imread(resource_path(dir+"wood_screen.png"), cv.IMREAD_UNCHANGED)

            needle_img1= cv.cvtColor(np.array(needle_img1), 
                            cv.COLOR_RGB2BGR)

            
            if check_present(needle_img1,search_area,0.55):
                py.click(button='right', clicks=1)
                time.sleep(.4)
                ss=py.screenshot()
                ss_gray=cv.cvtColor(np.array(ss),cv.COLOR_RGB2BGR)


            search_area=ss_gray[46:100, 1852:1896]
            needle_img1 = cv.imread(resource_path(dir+"food_check2.png"), cv.IMREAD_UNCHANGED)
            needle_img1= cv.cvtColor(np.array(needle_img1), 
                            cv.COLOR_RGB2BGR)

            if check_present(needle_img1,search_area,0.51):
                time.sleep(0.2)
                click(55,978)
                time.sleep(0.7)
                ss=py.screenshot()
                ss_gray=cv.cvtColor(np.array(ss),cv.COLOR_RGB2BGR)



            search_area=ss_gray[572:835, 666:1237]
            

            needle_img1 = cv.imread(resource_path(dir+"ok.png"), cv.IMREAD_UNCHANGED)
            needle_img1= cv.cvtColor(np.array(needle_img1), 
                            cv.COLOR_RGB2BGR)

            if check_present(needle_img1,search_area,0.75):
                time.sleep(0.2)
                flag=False
                needle_img1 = cv.imread(resource_path(dir+"max_march_reached.png"), cv.IMREAD_UNCHANGED)
                needle_img1= cv.cvtColor(np.array(needle_img1), 
                                cv.COLOR_RGB2BGR)
                search_area=ss_gray[279:321,811:898]

                if check_present(needle_img1,search_area,0.65):
                    time.sleep(0.5)
                    flag=True


                needle_img1 = cv.imread(resource_path(dir+"cooldown.png"), cv.IMREAD_UNCHANGED)
                needle_img1= cv.cvtColor(np.array(needle_img1), 
                                cv.COLOR_RGB2BGR)
                search_area=ss_gray[268:321,837:944]

                if check_present(needle_img1,search_area,0.65):
                    #time.sleep(0.5)
                    flag=True

                search_area=ss_gray[572:835, 666:1237]
                

                needle_img1 = cv.imread(resource_path(dir+"ok.png"), cv.IMREAD_UNCHANGED)
                needle_img1= cv.cvtColor(np.array(needle_img1), 
                                cv.COLOR_RGB2BGR)

                p=findClickPositions(needle_img1,search_area,0.5,eps_val=1)
                
                try:
                    if len(p)>0:
                        mouseclick(p[0][0]+666,p[0][1]+572) 
                        ss=py.screenshot()
                        ss_gray=cv.cvtColor(np.array(ss),cv.COLOR_RGB2BGR)

                    if flag:
                        time.sleep(0.5)
                        return 'wapas'
                except:
                    if flag:
                        return 'wapas'
                    print("missed")




            search_area=ss_gray[271:360, 1211:1268]

            needle_img1 = cv.imread(resource_path(dir+"cross.png"), cv.IMREAD_UNCHANGED)
            needle_img1= cv.cvtColor(np.array(needle_img1), 
                            cv.COLOR_RGB2BGR)

            if check_present(needle_img1,search_area,0.5):
                py.click(button='right', clicks=1)
                time.sleep(0.4)
                ss=py.screenshot()
                ss_gray=cv.cvtColor(np.array(ss),cv.COLOR_RGB2BGR)


            search_area=ss_gray[615:716, 961:1154]

            needle_img1 = cv.imread(resource_path(dir+"no.png"), cv.IMREAD_UNCHANGED)
            needle_img1= cv.cvtColor(np.array(needle_img1), 
                            cv.COLOR_RGB2BGR)

            if check_present(needle_img1,search_area,0.5):
                py.click(button='right', clicks=1)
                time.sleep(0.4)
                ss=py.screenshot()
                ss_gray=cv.cvtColor(np.array(ss),cv.COLOR_RGB2BGR)




            search_area=ss_gray[28:66, 36:84]

            needle_img1 = cv.imread(resource_path(dir+"para_army.png"), cv.IMREAD_UNCHANGED)
            needle_img1= cv.cvtColor(np.array(needle_img1), 
                            cv.COLOR_RGB2BGR)


            if check_present(needle_img1,search_area,0.5):
                py.click(button='right',clicks=1)
                time.sleep(0.3)
                py.click(button='right',clicks=1)
                time.sleep(0.3)
                ss=py.screenshot()
                ss_gray=cv.cvtColor(np.array(ss),cv.COLOR_RGB2BGR)


            needle_img1 = cv.imread(resource_path(dir+"heal_icon.png"), cv.IMREAD_UNCHANGED)
            needle_img1= cv.cvtColor(np.array(needle_img1), 
                            cv.COLOR_RGB2BGR)

            search_area=ss_gray[284:351,0:592]

            if check_present(needle_img1,search_area,0.6,1):
                Heal()



            needle_img1 = cv.imread(resource_path(dir+"cross_4.png"), cv.IMREAD_UNCHANGED)
            needle_img1= cv.cvtColor(np.array(needle_img1), 
                            cv.COLOR_RGB2BGR)

            search_area=ss_gray[3:200,0:200]

            if check_present(needle_img1,search_area,0.7,1):
                mouseclick(30,24)
                time.sleep(0.3)
                ss=py.screenshot()
                ss_gray=cv.cvtColor(np.array(ss),cv.COLOR_RGB2BGR)

            search_area=ss_gray[667:746, 840:1054]
            

            needle_img1 = cv.imread(resource_path(dir+"retry.png"), cv.IMREAD_UNCHANGED)
            needle_img1= cv.cvtColor(np.array(needle_img1), 
                            cv.COLOR_RGB2BGR)

            if check_present(needle_img1,search_area,0.75):
                print("Bad Internet Connection , Retrying")
                retry_checker()


            search_area=ss_gray[616:692,847:937]

            needle_img1 = cv.imread(resource_path(dir+"rate_us.png"), cv.IMREAD_UNCHANGED)
            needle_img1= cv.cvtColor(np.array(needle_img1), 
                            cv.COLOR_RGB2BGR)

            if check_present(needle_img1,search_area,0.75):
                time.sleep(0.4)
                py.click(951,814)
                


            if crash_value=="On" or crash_value=="on":
                game_value=Game_Running()
                if game_value==False:
                    game_restart()


        def check_for_disturbance_global():

            dir='img_1920/'

            ss=py.screenshot()
            ss_gray=cv.cvtColor(np.array(ss),cv.COLOR_RGB2BGR)


            search_area=ss_gray[800:834,98:159]
            

            needle_img1 = cv.imread(resource_path(dir+"tang.png"), cv.IMREAD_UNCHANGED)
            needle_img1= cv.cvtColor(np.array(needle_img1), 
                            cv.COLOR_RGB2BGR)

            if check_present(needle_img1,search_area,0.8):
                py.click(459,999)
                time.sleep(0.5)
                ss=py.screenshot()
                ss_gray=cv.cvtColor(np.array(ss),cv.COLOR_RGB2BGR)


            search_area=ss_gray[13:73, 0:60]

            needle_img1 = cv.imread(resource_path(dir+"wood_screen.png"), cv.IMREAD_UNCHANGED)

            needle_img1= cv.cvtColor(np.array(needle_img1), 
                            cv.COLOR_RGB2BGR)

            
            if check_present(needle_img1,search_area,0.55):
                py.click(button='right', clicks=1)
                time.sleep(.4)
                ss=py.screenshot()
                ss_gray=cv.cvtColor(np.array(ss),cv.COLOR_RGB2BGR)


            search_area=ss_gray[46:100, 1852:1896]
            needle_img1 = cv.imread(resource_path(dir+"food_check2.png"), cv.IMREAD_UNCHANGED)
            needle_img1= cv.cvtColor(np.array(needle_img1), 
                            cv.COLOR_RGB2BGR)

            if check_present(needle_img1,search_area,0.51):
                time.sleep(0.2)
                click(55,978)
                time.sleep(0.7)
                ss=py.screenshot()
                ss_gray=cv.cvtColor(np.array(ss),cv.COLOR_RGB2BGR)



            search_area=ss_gray[572:835, 666:1237]
            

            needle_img1 = cv.imread(resource_path(dir+"ok.png"), cv.IMREAD_UNCHANGED)
            needle_img1= cv.cvtColor(np.array(needle_img1), 
                            cv.COLOR_RGB2BGR)

            if check_present(needle_img1,search_area,0.75):
                time.sleep(0.2)
                flag=False
                needle_img1 = cv.imread(resource_path(dir+"max_march_reached.png"), cv.IMREAD_UNCHANGED)
                needle_img1= cv.cvtColor(np.array(needle_img1), 
                                cv.COLOR_RGB2BGR)
                search_area=ss_gray[279:321,811:898]

                if check_present(needle_img1,search_area,0.65):
                    time.sleep(0.5)
                    flag=True


                needle_img1 = cv.imread(resource_path(dir+"cooldown.png"), cv.IMREAD_UNCHANGED)
                needle_img1= cv.cvtColor(np.array(needle_img1), 
                                cv.COLOR_RGB2BGR)
                search_area=ss_gray[268:321,837:944]

                if check_present(needle_img1,search_area,0.65):
                    #time.sleep(0.5)
                    flag=True

                search_area=ss_gray[572:835, 666:1237]
                

                needle_img1 = cv.imread(resource_path(dir+"ok.png"), cv.IMREAD_UNCHANGED)
                needle_img1= cv.cvtColor(np.array(needle_img1), 
                                cv.COLOR_RGB2BGR)

                p=findClickPositions(needle_img1,search_area,0.5,eps_val=1)
                
                try:
                    if len(p)>0:
                        mouseclick(p[0][0]+666,p[0][1]+572) 
                        ss=py.screenshot()
                        ss_gray=cv.cvtColor(np.array(ss),cv.COLOR_RGB2BGR)

                    if flag:
                        time.sleep(0.5)
                        return 'wapas'
                except:
                    if flag:
                        return 'wapas'
                    print("missed")


            search_area=ss_gray[271:360, 1211:1268]

            needle_img1 = cv.imread(resource_path(dir+"cross.png"), cv.IMREAD_UNCHANGED)
            needle_img1= cv.cvtColor(np.array(needle_img1), 
                            cv.COLOR_RGB2BGR)

            if check_present(needle_img1,search_area,0.5):
                py.click(button='right', clicks=1)
                time.sleep(0.4)
                ss=py.screenshot()
                ss_gray=cv.cvtColor(np.array(ss),cv.COLOR_RGB2BGR)


            search_area=ss_gray[124:181,650:719]
            needle_img1 = cv.imread(resource_path(dir+"info_icon.png"), cv.IMREAD_UNCHANGED)
            needle_img1= cv.cvtColor(np.array(needle_img1), 
                            cv.COLOR_RGB2BGR)


            if check_present(needle_img1,search_area,0.7):

                py.click(button='right', clicks=1)
                time.sleep(0.3)


            search_area=ss_gray[28:66, 36:84]

            needle_img1 = cv.imread(resource_path(dir+"para_army.png"), cv.IMREAD_UNCHANGED)
            needle_img1= cv.cvtColor(np.array(needle_img1), 
                            cv.COLOR_RGB2BGR)


            if check_present(needle_img1,search_area,0.5):

                py.click(button='right',clicks=1)
                time.sleep(0.3)
                py.click(button='right',clicks=1)
                time.sleep(0.3)




            needle_img1 = cv.imread(resource_path(dir+"heal_icon.png"), cv.IMREAD_UNCHANGED)
            needle_img1= cv.cvtColor(np.array(needle_img1), 
                            cv.COLOR_RGB2BGR)

            search_area=ss_gray[284:351,0:592]

            if check_present(needle_img1,search_area,0.6,1):
                Heal()


            search_area=ss_gray[692:727,910:994]



            needle_img1 = cv.imread(resource_path(dir+"retry.png"), cv.IMREAD_UNCHANGED)
            needle_img1= cv.cvtColor(np.array(needle_img1), 
                            cv.COLOR_RGB2BGR)


            if check_present(needle_img1,search_area,0.7,1):
                retry_checker()


            needle_img1 = cv.imread(resource_path(dir+"cross_4.png"), cv.IMREAD_UNCHANGED)
            needle_img1= cv.cvtColor(np.array(needle_img1), 
                            cv.COLOR_RGB2BGR)

            search_area=ss_gray[3:63,0:85]

            if check_present(needle_img1,search_area,0.77,1):
                mouseclick(30,24)
                time.sleep(0.3)


            if crash_value=="On" or crash_value=="on":
                game_value=Game_Running()
                if game_value==False:
                    game_restart()


            
    else:

        def check_for_disturbance():


            haystack_img1=py.screenshot(region=(98,800,61,34))
            haystack_img1 = cv.cvtColor(np.array(haystack_img1), 
                            cv.COLOR_RGB2BGR)
            

            needle_img1 = cv.imread(resource_path(dir+"tang.png"), cv.IMREAD_UNCHANGED)
            needle_img1= cv.cvtColor(np.array(needle_img1), 
                            cv.COLOR_RGB2BGR)
            continue_lady=findClickPositions(needle_img1,haystack_img1,0.8,0.8)
            if len(continue_lady)>0:
                py.click(459,999)
                time.sleep(0.5)

            haystack_img1=py.screenshot(region=(0,13,60,60))

            haystack_img1 = cv.cvtColor(np.array(haystack_img1), 
                            cv.COLOR_RGB2BGR)

            needle_img1 = cv.imread(resource_path(dir+"wood_screen.png"), cv.IMREAD_UNCHANGED)

            needle_img1= cv.cvtColor(np.array(needle_img1), 
                            cv.COLOR_RGB2BGR)
            wood_screen=findClickPositions(needle_img1,haystack_img1,0.5)
            if len(wood_screen)>0:
                py.click(button='right', clicks=1)
                time.sleep(.35)

            haystack_img1=py.screenshot(region=(1852,46,54,54))

            haystack_img1 = cv.cvtColor(np.array(haystack_img1), 
                            cv.COLOR_RGB2BGR)
            needle_img1 = cv.imread(resource_path(dir+"food_check2.png"), cv.IMREAD_UNCHANGED)
            needle_img1= cv.cvtColor(np.array(needle_img1), 
                            cv.COLOR_RGB2BGR)
            food_check=findClickPositions(needle_img1,haystack_img1,0.5)
            if len(food_check)>0:
                click(55,978)
                time.sleep(0.6)

            haystack_img1=py.screenshot(region=(666,572,571,263))

            haystack_img1 = cv.cvtColor(np.array(haystack_img1), 
                            cv.COLOR_RGB2BGR)
            

            needle_img1 = cv.imread(resource_path(dir+"ok.png"), cv.IMREAD_UNCHANGED)
            needle_img1= cv.cvtColor(np.array(needle_img1), 
                            cv.COLOR_RGB2BGR)
            ok=findClickPositions(needle_img1,haystack_img1,0.5,1)
            if len(ok)>0:
                flag=False
                haystack_img11=py.screenshot(region=(837,268,117,65))

                haystack_img11 = cv.cvtColor(np.array(haystack_img11), 
                                cv.COLOR_RGB2BGR)
                needle_img11 = cv.imread(resource_path(dir+"cooldown.png"), cv.IMREAD_UNCHANGED)
                needle_img11= cv.cvtColor(np.array(needle_img11), 
                                cv.COLOR_RGB2BGR)
                
                okk=findClickPositions(needle_img11,haystack_img11,0.65)
                if len(okk)>0:
                    flag=True


                haystack_img11=py.screenshot(region=(811,279,87,42))

                haystack_img11 = cv.cvtColor(np.array(haystack_img11), 
                                cv.COLOR_RGB2BGR)
                needle_img11 = cv.imread(resource_path(dir+"max_march_reached.png"), cv.IMREAD_UNCHANGED)
                needle_img11= cv.cvtColor(np.array(needle_img11), 
                                cv.COLOR_RGB2BGR)
                
                okk=findClickPositions(needle_img11,haystack_img11,0.65)
                if len(okk)>0:
                    flag=True
                    time.sleep(1)
                    
                
                ok=pyautogui.locateOnScreen(resource_path(dir+'ok.png'),region=(666,572,571,263),confidence=0.65)

                try:
                    ok=py.center(ok)
                    mouseclick(ok[0],ok[1])
                    time.sleep(0.5)
                    if flag:
                        return 'wapas'
                except:
                    return 'wapas'
                    print("missed")

            haystack_img1=py.screenshot(region=(1211,271,57,89))

            haystack_img1 = cv.cvtColor(np.array(haystack_img1), 
                            cv.COLOR_RGB2BGR)

            needle_img1 = cv.imread(resource_path(dir+"cross.png"), cv.IMREAD_UNCHANGED)
            needle_img1= cv.cvtColor(np.array(needle_img1), 
                            cv.COLOR_RGB2BGR)
            cross=findClickPositions(needle_img1,haystack_img1,0.5)
            if len(cross)>0:
                py.click(button='right', clicks=1)


            haystack_img1=py.screenshot(region=(36,28,48,38))

            haystack_img1 = cv.cvtColor(np.array(haystack_img1), 
                            cv.COLOR_RGB2BGR)

            needle_img1 = cv.imread(resource_path(dir+"para_army.png"), cv.IMREAD_UNCHANGED)
            needle_img1= cv.cvtColor(np.array(needle_img1), 
                            cv.COLOR_RGB2BGR)
            para_army=findClickPositions(needle_img1,haystack_img1,0.7)

            if len(para_army)>0:
                py.click(button='right',clicks=1)
                time.sleep(0.3)
                py.click(button='right',clicks=1)
                time.sleep(0.3)

            if crash_value=="On" or crash_value=="on":
                game_value=Game_Running()
                if game_value==False:
                    game_restart()



        def check_for_disturbance_global():

            haystack_img1=py.screenshot(region=(98,800,61,34))
            haystack_img1 = cv.cvtColor(np.array(haystack_img1), 
                            cv.COLOR_RGB2BGR)
            

            needle_img1 = cv.imread(resource_path(dir+"tang.png"), cv.IMREAD_UNCHANGED)
            needle_img1= cv.cvtColor(np.array(needle_img1), 
                            cv.COLOR_RGB2BGR)
            continue_lady=findClickPositions(needle_img1,haystack_img1,0.8,0.8)
            if len(continue_lady)>0:
                py.click(459,999)
                time.sleep(0.4)

            haystack_img1=py.screenshot(region=(0,13,60,60))

            haystack_img1 = cv.cvtColor(np.array(haystack_img1), 
                            cv.COLOR_RGB2BGR)

            needle_img1 = cv.imread(resource_path(dir+"wood_screen.png"), cv.IMREAD_UNCHANGED)

            needle_img1= cv.cvtColor(np.array(needle_img1), 
                            cv.COLOR_RGB2BGR)
            wood_screen=findClickPositions(needle_img1,haystack_img1,0.5)
            if len(wood_screen)>0:
                py.click(button='right', clicks=1)
                time.sleep(.4)

            haystack_img1=py.screenshot(region=(1852,46,54,54))

            haystack_img1 = cv.cvtColor(np.array(haystack_img1), 
                            cv.COLOR_RGB2BGR)
            needle_img1 = cv.imread(resource_path(dir+"food_check2.png"), cv.IMREAD_UNCHANGED)
            needle_img1= cv.cvtColor(np.array(needle_img1), 
                            cv.COLOR_RGB2BGR)
            food_check=findClickPositions(needle_img1,haystack_img1,0.5)
            if len(food_check)>0:
                click(55,978)
                time.sleep(0.6)

            haystack_img1=py.screenshot(region=(830,646,230,86))

            haystack_img1 = cv.cvtColor(np.array(haystack_img1), 
                            cv.COLOR_RGB2BGR)
            

            needle_img1 = cv.imread(resource_path(dir+"ok.png"), cv.IMREAD_UNCHANGED)
            needle_img1= cv.cvtColor(np.array(needle_img1), 
                            cv.COLOR_RGB2BGR)
            ok=findClickPositions(needle_img1,haystack_img1,0.5)
            if len(ok)>0:
                time.sleep(0.2)
                ok=pyautogui.locateOnScreen(resource_path(dir+'ok.png'),region=(852,639,187,65),confidence=0.65)
                try:
                    ok=pyautogui.center(ok)
                    click(ok[0],ok[1])
                    time.sleep(0.4)
                except:
                    print("missed")

            haystack_img1=py.screenshot(region=(1211,80,57,280))

            haystack_img1 = cv.cvtColor(np.array(haystack_img1), 
                            cv.COLOR_RGB2BGR)

            needle_img1 = cv.imread(resource_path(dir+"cross.png"), cv.IMREAD_UNCHANGED)
            needle_img1= cv.cvtColor(np.array(needle_img1), 
                            cv.COLOR_RGB2BGR)
            cross=findClickPositions(needle_img1,haystack_img1,0.5)
            if len(cross)>0:
                py.click(button='right', clicks=1)



            cross3=py.locateOnScreen(resource_path(dir+"cross3.png"),confidence=0.7)
            if cross3!=None:
                py.click(button='right',clicks=1)



            haystack_img1=py.screenshot(region=(36,28,48,38))

            haystack_img1 = cv.cvtColor(np.array(haystack_img1), 
                            cv.COLOR_RGB2BGR)

            needle_img1 = cv.imread(resource_path(dir+"para_army.png"), cv.IMREAD_UNCHANGED)
            needle_img1= cv.cvtColor(np.array(needle_img1), 
                            cv.COLOR_RGB2BGR)
            para_army=findClickPositions(needle_img1,haystack_img1,0.7)

            if len(para_army)>0:
                py.click(button='right',clicks=1)
                time.sleep(0.3)
                py.click(button='right',clicks=1)
                time.sleep(0.24)


            haystack_img1=py.screenshot(region=(910,692,84,35))

            haystack_img1 = cv.cvtColor(np.array(haystack_img1), 
                            cv.COLOR_RGB2BGR)

            needle_img1 = cv.imread(resource_path(dir+"retry.png"), cv.IMREAD_UNCHANGED)
            needle_img1= cv.cvtColor(np.array(needle_img1), 
                            cv.COLOR_RGB2BGR)
            retry=findClickPositions(needle_img1,haystack_img1,0.7)
            if len(retry)>0:
                retry_checker()
                
            #haystack_img1=py.screenshot(region=(349,983,110,30))


            if crash_value=="On" or crash_value=="on":
                game_value=Game_Running()
                if game_value==False:
                    game_restart()
        

                
    def swift_attack():
        click(1216,930)

        #time.sleep(0)

    def clear_starting_screens():

        while True:
            time.sleep(0.1)
            world=py.locateOnScreen(resource_path(dir+'world.png'),region=(1798,17,112,70),confidence=0.6)
            if world!=None:
                time.sleep(1.2)
                badha()
                world=py.locateOnScreen(resource_path(dir+'world.png'),region=(1798,17,112,70),confidence=0.6)
                if world!=None:
                    return
            else:
                badha()



            
    def random_port():

        py.press("4")
        time.sleep(tweaker*0.1)

        
        click(243,146)
        time.sleep(tweaker*0.1)

        click(1467,241)
        time.sleep(tweaker*0.1)

        
        click(968,315)
        time.sleep(tweaker*0.1)

        c=0

        pyautogui.moveTo(800,650)
        time.sleep(0.15)
        if s_method==1:
            mouse.wheel(-max_scroll)
        if s_method==3:
            for i in range(int(max_scroll)):
                scroller_windows()
                time.sleep(.01)
        if s_method==4:
            abc=-1* int(max_scroll*80)
            py.scroll(abc)
        while True:
            
            c+=1
            #scroller_windows()
            if s_method==1:
                mouse.wheel(-1)
            elif s_method==4:
                py.scroll(-80)
            else:
                scroller_windows()
                #py.scroll(-80)

            if c>1:

                time.sleep(r_wait)
                ss=py.locateOnScreen(resource_path(dir+"random_port.png"),confidence=0.90)
                if ss!=None:

                    if ss[1]+108> 875:
                        pyautogui.scroll(-45)
                        time.sleep(0.1)
                        ss=py.locateOnScreen(resource_path(dir+"random_port.png"),confidence=0.90)
                        if ss[1]+108>875:
                            scroller_windows()
                            time.sleep(0.2)
                            ss=py.locateOnScreen(resource_path(dir+"random_port.png"),confidence=0.90)
                        #time.sleep(0.2)




                    use_region=(ss[0]+336,ss[1]+113,100,47)
                    use=py.locateOnScreen(resource_path(dir+"use.png"),confidence=0.90,region=use_region)

                    if use!=None:
                        use=py.center(use)
                        click(use[0],use[1])
                        return True

                    time.sleep(tweaker*0.11)

                    click(ss[0]+630,ss[1]+108)  

                    time.sleep(tweaker*0.15)

                    click(ss[0]+470,ss[1]+108)

                    time.sleep(1)
                    return True
                    break
            if c>10:
                py.click(button="right",clicks=1)
                time.sleep(.1)
                return

    def Heal():
        ans=check_left_area()
        if ans!=1 and ans!=0:
            click(531, 324)
            time.sleep(wait_val)
        if ans==0:
            click(63, 318)
            time.sleep(wait_val)

        ss=py.locateOnScreen(resource_path("img_1920/h_sign.png"),region=(0,278,111,416),confidence=0.8)
        if ss!=None:
            
            cords=py.center(ss)

        else:
            cords=(395,326)
            time.sleep(0.2)

        click(395,cords[1])

        time.sleep(0.1+(tweaker*0.1))
        time.sleep(0.3)
        click(748,791)
        time.sleep(0.1+(tweaker*0.05))
        click(1176,791)
        time.sleep(0.4)

        py.click(button="right",clicks=1)

        time.sleep(0.5)

        #py.press("ctrl")
        click(53,1022)
        time.sleep(0.7+wait_val)



    def check_heal():

        heal_icon=py.locateOnScreen(resource_path(dir+'heal_icon.png'),confidence=.75,region=(486,296,61,32))
        if heal_icon!=None:
            Heal()

    def side_icon():

        abra=1
        side=py.locateOnScreen(resource_path(dir+"side_icon.png"),confidence=0.8,region=(49,243,67,46))
        #side_screen=py.locateOnScreen(resource_path(dir+'side_icon.png'),confidence=.65,region=(51,252,60,60))
        if side!=None:
            abra=2
        else:
            #py.press("z")
            click(47,415)
            #time.sleep(0.2)
            #click(37,420)
        check_heal()
        if abra==1:
            return True

    def side_screen_closer():

        abra=1
        side=py.locateOnScreen(resource_path(dir+"side_icon.png"),confidence=0.8,region=(49,243,67,46))
        #side_screen=py.locateOnScreen(resource_path(dir+'side_icon.png'),confidence=.65,region=(51,252,60,60))
        if side!=None:
            py.press('z')





    def pass_check(loca):
        pass_needed=imagesearch_numLoop_self(resource_path(dir+"pass_needed.png"),1,precision=0.8,reg=(988,899,123,39))
        if pass_needed!=None:
            #time.sleep(1.5)
            pass_needed=imagesearch_numLoop_self(resource_path(dir+"pass_needed.png"),1,precision=0.8,reg=(988,899,123,39))
            if pass_needed!=None:
                pass_needed=imagesearch_numLoop_self(resource_path(dir+"pass_needed.png"),1,precision=0.8,reg=(988,899,123,39))
                if pass_needed==None:
                    return
                click(1042,932)
                time.sleep(tweaker*0.1+wait_val+0.1)
                click(1018,601)
                time.sleep(wait_val+tweaker*0.1+0.4)
                click(1216,881)




    def march_checker(n):

        if n==1:
            march = py.locateOnScreen(resource_path(dir+"march_"+str(0)+".png"),confidence=0.90,region=(199,249,65,37))
            if march!=None:
                return False
            else:
                return True

        march = py.locateOnScreen(resource_path(dir+"march_"+str(n)+".png"),confidence=0.90,region=(199,249,65,37))
        if march!=None:
            return True
        return False

    def waiter():
        disturbance_checker_timer(time_between_clicks)
        side_icon()
        s=march_checker(marches)
        while(s):
            disturbance_checker_timer(time_between_clicks)
            side_icon()
            s=march_checker(marches)


    def point_filter(conflict_points,tp):
        x_s=x_s_1920
        y_s=y_s_1920
        x_p=x_p_1920
        y_p=y_p_1920
        for points in conflict_points or []:
            x_min=points[0]-x_s
            y_min=points[1]-y_s

            x_max=points[0]+x_p
            y_max=points[1]+y_p

            if( tp[0]>=x_min and tp[1]>=y_min and tp[0]<=x_max and tp[1]<=y_max):
                return True
        if(tp[0]>=0 and tp[1]>=224 and tp[0]<=465 and tp[1]<=617):
            return True

        if(tp[0]>=471 and tp[1]>=272 and tp[0]<=590 and tp[1]<=539):
            return True

        if(tp[0]>=1792 and tp[1]>=228 and tp[0]<=1911 and tp[1]<=557):
            return True

        if(tp[1]<120):
            return True

        return False


    def disturbance_checker_timer(time_between_clicks):
        s=time.time()
        checker=False
        p=int(1)
        if cfds==1:
            p=int(50)
        for i in range(p):
            if check_for_disturbance()=='wapas':
                checker=True
            cu_time=time.time()
            if cu_time-s>time_between_clicks:
                break
            time.sleep(0.05)

        return checker


    def disturbance_checker_timer_global(time_between_clicks):
        s=time.time()
        checker=False
        p=int(1)
        if cfds==1:
            p=int(50)
        for i in range(20):
            if check_for_disturbance_global()=='wapas':
                checker=True
            cu_time=time.time()
            if cu_time-s>time_between_clicks:
                break
            time.sleep(0.05)

        return checker

        





    def wait_loop():
        #py.press("2")
        if side_icon():
            time.sleep(0.3)
        #click(862,868)
        while True:
            check_for_disturbance()
            side_icon()
            ans=check_left_area()
            pos=pyautogui.locateOnScreen(resource_path(dir+'wait.png'),region=(0,298,60,49),confidence=0.65)
            if pos==None and ans==2:
                break


    if b_method==1:
        def location_opener(cord):

            x=str(cord[0])
            y=str(cord[1])
            x= list(x)
            y=list(y)
            #py.press("l")
            time.sleep(time_before_location_opener)
            click(781,42)
            time.sleep((tweaker-2)*0.1+0.35)
            for i in x:
                py.press(i)
                time.sleep(w_interval)
            #py.write(str(x),interval=0.15)
            time.sleep(0.35)
        
            click(1037,173)
            time.sleep((tweaker-2)*0.1+0.35)
            for i in y:
                py.press(i)
                time.sleep(w_interval)
            #py.write(str(y),interval=0.15)
            time.sleep((tweaker-2)*0.1+0.35)
            if location_opener_stuck=='1':
                click(1220,174)
                time.sleep(tweaker*0.1-0.45)
            click(1130,186)

    elif b_method==2:

        def location_opener(cord):

            x=cord[0]
            y=cord[1]
            #py.press("l")
            time.sleep(time_before_location_opener)

            click(781,42)
            time.sleep((tweaker-2)*0.1+0.35)
            keyboard.write(str(x))
            time.sleep((tweaker-2)*0.1+0.35)
    
            click(1037,173)
            time.sleep((tweaker-2)*0.1+0.35)
            keyboard.write(str(y))
            time.sleep((tweaker-2)*0.1+0.35)
            if location_opener_stuck=='1':
                click(1220,174)
                time.sleep(tweaker*0.1-0.45)
            click(1130,186)

    elif b_method==3:

        def location_opener(cord):

            x=cord[0]
            y=cord[1]
            #py.press("l")
            time.sleep(time_before_location_opener)
            #move_mouse(781,42)
            click(781,42)
            time.sleep((tweaker-2)*0.1+0.35)
            py.write(str(x),interval=w_interval)
            time.sleep((tweaker-2)*0.1+0.35)
            #move_mouse(1037,173)
            click(1037,173)
            time.sleep((tweaker-2)*0.1+0.35)
            py.write(str(y),interval=w_interval)
            time.sleep((tweaker-2)*0.1+0.35)
            #move_mouse(1130,186)
            if location_opener_stuck=='1':
                click(1220,174)
                time.sleep(tweaker*0.1-0.45)
            click(1130,186)



    else:
        
        def location_opener(cord):

            x=cord[0]
            y=cord[1]
            #py.press("l")
            time.sleep(time_before_location_opener)

            click(781,42)
            time.sleep((tweaker-2)*0.1+0.35)
            mouseclick(874, 192)
            time.sleep(0.01)
            mouseclick(874, 192)
            keyboard.write(str(x))
            time.sleep((tweaker-2)*0.1+0.35)
            mouseclick(1011, 192)
            time.sleep(0.01)
            mouseclick(1011, 192)
            time.sleep((tweaker-2)*0.1+0.35)

            keyboard.write(str(y))
            time.sleep((tweaker-2)*0.1+0.35)
            if location_opener_stuck=='1':
                click(1220,174)
                time.sleep(tweaker*0.1-0.45)
            click(1130,186)

    def one_screen(c):

        if cmd_number[3]==0:
            return
        try:
            s=time.time()
            final_cords=[]
            ss=py.screenshot()
            ScreenShot_Gray=cv.cvtColor(np.array(ss),cv.COLOR_RGB2GRAY)
            camp_locations=get_camp_locations(ss)
            #print(len(camp_locations))
            for a, b, w, h in camp_locations:
                center_x = a + round(int(w)*0.62)
                center_y = b + round(int(h)*0.45)
                x1 = round(a-w*0.1)
                x2 = round(a+w*1.18)
                y1 = round(0.06*b+25+b)
                y2 = round(0.109*b+80+b)

                ratio_2 = 0.79
                ratio_3 = 0.75
                if y2 < 300: 
                    ratio_2 = 0.75
                if x1 <= 0: 
                    x1 = 0
                if x2 >= 1919: 
                    x2=1919
                area_2 = ScreenShot_Gray[y1:y2, x1:x2]
                
                valid_cord=0
                if y2 <= 365:
                    for scale in np.linspace(0.9, 0.6, 10)[::-1]:

                        if c_8:
                            Sub_Image_1_Resized = imutils.resize(c8_888, width=int(c8_888.shape[1] * scale))
                            result_1 = cv.matchTemplate(area_2, Sub_Image_1_Resized, cv.TM_CCOEFF_NORMED)
                            check_1 = np.any(result_1 >= ratio_2)

                        else:
                            check_1=0

                        if c_9:
                            Sub_Image_2_Resized = imutils.resize(c9_888, width=int(c9_888.shape[1] * scale))
                            result_2 = cv.matchTemplate(area_2, Sub_Image_2_Resized, cv.TM_CCOEFF_NORMED)
                            check_2 = np.any(result_2 >= ratio_2)
                        else:
                            check_2=0

                        if c_10:
                            Sub_Image_3_Resized = imutils.resize(c10_888, width=int(c10_888.shape[1] * scale))
                            result_3 = cv.matchTemplate(area_2, Sub_Image_3_Resized, cv.TM_CCOEFF_NORMED)
                            check_3 = np.any(result_3 >= (ratio_2-0.1))
                        else:
                            check_3=0

                        if c_7:
                            Sub_Image_1_Resized = imutils.resize(c7_777, width=int(c7_777.shape[1] * scale))
                            result_1 = cv.matchTemplate(area_2, Sub_Image_1_Resized, cv.TM_CCOEFF_NORMED)
                            check_5 = np.any(result_1 >= ratio_2)
                        else:
                            check_5=0

                        if c_6:
                            Sub_Image_1_Resized = imutils.resize(c6_666, width=int(c6_666.shape[1] * scale))
                            result_1 = cv.matchTemplate(area_2, Sub_Image_1_Resized, cv.TM_CCOEFF_NORMED)
                            check_6 = np.any(result_1 >= ratio_2)
                        else:
                            check_6=0
                        
                        if c_5:
                            Sub_Image_1_Resized = imutils.resize(c5_555, width=int(c5_555.shape[1] * scale))
                            result_1 = cv.matchTemplate(area_2, Sub_Image_1_Resized, cv.TM_CCOEFF_NORMED)
                            check_7 = np.any(result_1 >= ratio_2)

                        else:
                            check_7=0

                        if c_11:
                            Sub_Image_1_Resized = imutils.resize(c11_11, width=int(c11_11.shape[1] * scale))
                            result_1 = cv.matchTemplate(area_2, Sub_Image_1_Resized, cv.TM_CCOEFF_NORMED)
                            check_8 = np.any(result_1 >= ratio_2)

                        else:
                            check_8=0

                        if c_12:
                            Sub_Image_1_Resized = imutils.resize(c12_12, width=int(c12_12.shape[1] * scale))
                            result_1 = cv.matchTemplate(area_2, Sub_Image_1_Resized, cv.TM_CCOEFF_NORMED)
                            check_9 = np.any(result_1 >= ratio_2)

                        else:
                            check_9=0


                        Sub_Image_4_Resized = imutils.resize(sn7, width=int(sn7.shape[1] * scale))
                        result_4 = cv.matchTemplate(area_2, Sub_Image_4_Resized, cv.TM_CCOEFF_NORMED)
                        check_4 = np.any(result_4 >= ratio_3)

                        if (check_1==1 or check_2==1 or check_3==1 or check_5==1 or check_6==1 or check_7==1 or check_8 or check_9) and check_4==0:
                            valid_cord=1
                            break




                elif y2 > 365 and y2 <= 635:
                    for scale in np.linspace(1.2, 0.7, 10)[::-1]:
                        if c_8:
                            Sub_Image_1_Resized = imutils.resize(c8_888, width=int(c8_888.shape[1] * scale))
                            result_1 = cv.matchTemplate(area_2, Sub_Image_1_Resized, cv.TM_CCOEFF_NORMED)
                            check_1 = np.any(result_1 >= ratio_2)

                        else:
                            check_1=0

                        if c_9:
                            Sub_Image_2_Resized = imutils.resize(c9_888, width=int(c9_888.shape[1] * scale))
                            result_2 = cv.matchTemplate(area_2, Sub_Image_2_Resized, cv.TM_CCOEFF_NORMED)
                            check_2 = np.any(result_2 >= ratio_2)
                        else:
                            check_2=0

                        if c_10:
                            Sub_Image_3_Resized = imutils.resize(c10_888, width=int(c10_888.shape[1] * scale))
                            result_3 = cv.matchTemplate(area_2, Sub_Image_3_Resized, cv.TM_CCOEFF_NORMED)
                            check_3 = np.any(result_3 >= (ratio_2-0.1))
                        else:
                            check_3=0

                        if c_7:
                            Sub_Image_1_Resized = imutils.resize(c7_777, width=int(c7_777.shape[1] * scale))
                            result_1 = cv.matchTemplate(area_2, Sub_Image_1_Resized, cv.TM_CCOEFF_NORMED)
                            check_5 = np.any(result_1 >= ratio_2)
                        else:
                            check_5=0

                        if c_6:
                            Sub_Image_1_Resized = imutils.resize(c6_666, width=int(c6_666.shape[1] * scale))
                            result_1 = cv.matchTemplate(area_2, Sub_Image_1_Resized, cv.TM_CCOEFF_NORMED)
                            check_6 = np.any(result_1 >= ratio_2)
                        else:
                            check_6=0
                        
                        if c_5:
                            Sub_Image_1_Resized = imutils.resize(c5_555, width=int(c5_555.shape[1] * scale))
                            result_1 = cv.matchTemplate(area_2, Sub_Image_1_Resized, cv.TM_CCOEFF_NORMED)
                            check_7 = np.any(result_1 >= ratio_2)

                        else:
                            check_7=0


                        if c_11:
                            Sub_Image_1_Resized = imutils.resize(c11_11, width=int(c11_11.shape[1] * scale))
                            result_1 = cv.matchTemplate(area_2, Sub_Image_1_Resized, cv.TM_CCOEFF_NORMED)
                            check_8 = np.any(result_1 >= ratio_2)

                        else:
                            check_8=0

                        if c_12:
                            Sub_Image_1_Resized = imutils.resize(c12_12, width=int(c12_12.shape[1] * scale))
                            result_1 = cv.matchTemplate(area_2, Sub_Image_1_Resized, cv.TM_CCOEFF_NORMED)
                            check_9 = np.any(result_1 >= ratio_2)

                        else:
                            check_9=0


                        Sub_Image_4_Resized = imutils.resize(sn7, width=int(sn7.shape[1] * scale))
                        result_4 = cv.matchTemplate(area_2, Sub_Image_4_Resized, cv.TM_CCOEFF_NORMED)
                        check_4 = np.any(result_4 >= ratio_3)

                        if (check_1==1 or check_2==1 or check_3==1 or check_5==1 or check_6==1 or check_7==1 or check_8 or check_9) and check_4==0:
                            valid_cord=1
                            break

                
                elif y2 > 635:
                    for scale in np.linspace(1.4, 0.8, 10)[::-1]:
                        if c_8:
                            Sub_Image_1_Resized = imutils.resize(c8_888, width=int(c8_888.shape[1] * scale))
                            result_1 = cv.matchTemplate(area_2, Sub_Image_1_Resized, cv.TM_CCOEFF_NORMED)
                            check_1 = np.any(result_1 >= ratio_2)

                        else:
                            check_1=0

                        if c_9:
                            Sub_Image_2_Resized = imutils.resize(c9_888, width=int(c9_888.shape[1] * scale))
                            result_2 = cv.matchTemplate(area_2, Sub_Image_2_Resized, cv.TM_CCOEFF_NORMED)
                            check_2 = np.any(result_2 >= ratio_2)
                        else:
                            check_2=0

                        if c_10:
                            Sub_Image_3_Resized = imutils.resize(c10_888, width=int(c10_888.shape[1] * scale))
                            result_3 = cv.matchTemplate(area_2, Sub_Image_3_Resized, cv.TM_CCOEFF_NORMED)
                            check_3 = np.any(result_3 >= ratio_2)
                        else:
                            check_3=0

                        if c_7:
                            Sub_Image_1_Resized = imutils.resize(c7_777, width=int(c7_777.shape[1] * scale))
                            result_1 = cv.matchTemplate(area_2, Sub_Image_1_Resized, cv.TM_CCOEFF_NORMED)
                            check_5 = np.any(result_1 >= ratio_2)
                        else:
                            check_5=0

                        if c_6:
                            Sub_Image_1_Resized = imutils.resize(c6_666, width=int(c6_666.shape[1] * scale))
                            result_1 = cv.matchTemplate(area_2, Sub_Image_1_Resized, cv.TM_CCOEFF_NORMED)
                            check_6 = np.any(result_1 >= ratio_2)
                        else:
                            check_6=0
                        
                        if c_5:
                            Sub_Image_1_Resized = imutils.resize(c5_555, width=int(c5_555.shape[1] * scale))
                            result_1 = cv.matchTemplate(area_2, Sub_Image_1_Resized, cv.TM_CCOEFF_NORMED)
                            check_7 = np.any(result_1 >= ratio_2)

                        else:
                            check_7=0


                        if c_11:
                            Sub_Image_1_Resized = imutils.resize(c11_11, width=int(c11_11.shape[1] * scale))
                            result_1 = cv.matchTemplate(area_2, Sub_Image_1_Resized, cv.TM_CCOEFF_NORMED)
                            check_8 = np.any(result_1 >= ratio_2)

                        else:
                            check_8=0

                        if c_12:
                            Sub_Image_1_Resized = imutils.resize(c12_12, width=int(c12_12.shape[1] * scale))
                            result_1 = cv.matchTemplate(area_2, Sub_Image_1_Resized, cv.TM_CCOEFF_NORMED)
                            check_9 = np.any(result_1 >= ratio_2)

                        else:
                            check_9=0


                        Sub_Image_4_Resized = imutils.resize(sn7, width=int(sn7.shape[1] * scale))
                        result_4 = cv.matchTemplate(area_2, Sub_Image_4_Resized, cv.TM_CCOEFF_NORMED)
                        check_4 = np.any(result_4 >= ratio_3)

                        if (check_1==1 or check_2==1 or check_3==1 or check_5==1 or check_6==1 or check_7==1 or check_8 or check_9) and check_4==0:
                            valid_cord=1
                            break




                elif valid_cord and marches>1:
            
                    pos_8 = [center_x, center_y]
                    final_cords.append(pos_8)


      
            #final_cords.sort()
            return final_cords

        except:
            return []

    

    def one_screen(c):

        try:

            final_cords=[]
            ss=py.screenshot()
            ScreenShot_Gray=cv.cvtColor(np.array(ss),cv.COLOR_RGB2GRAY)
            camp_locations=get_camp_locations(ss)
            #print(len(camp_locations))
            for a, b, w, h in camp_locations:
                center_x = a + round(int(w)*0.62)
                center_y = b + round(int(h)*0.45)
                x1 = round(a-w*0.1)
                x2 = round(a+w*1.18)
                y1 = round(0.06*b+25+b)
                y2 = round(0.109*b+80+b)

                ratio_2 = 0.79
                ratio_3 = 0.75
                if y2 < 300: 
                    ratio_2 = 0.75
                if x1 <= 0: 
                    x1 = 0
                if x2 >= 1919: 
                    x2=1919
                area_2 = ScreenShot_Gray[y1:y2, x1:x2]
                
                valid_cord=0
                if y2 <= 365:
                    for scale in np.linspace(0.9, 0.6, 10)[::-1]:

                        if c_8:
                            Sub_Image_1_Resized = imutils.resize(c8_888, width=int(c8_888.shape[1] * scale))
                            result_1 = cv.matchTemplate(area_2, Sub_Image_1_Resized, cv.TM_CCOEFF_NORMED)
                            check_1 = np.any(result_1 >= ratio_2)

                        else:
                            check_1=0

                        if c_9:
                            Sub_Image_2_Resized = imutils.resize(c9_888, width=int(c9_888.shape[1] * scale))
                            result_2 = cv.matchTemplate(area_2, Sub_Image_2_Resized, cv.TM_CCOEFF_NORMED)
                            check_2 = np.any(result_2 >= ratio_2)
                        else:
                            check_2=0

                        if c_10:
                            Sub_Image_3_Resized = imutils.resize(c10_888, width=int(c10_888.shape[1] * scale))
                            result_3 = cv.matchTemplate(area_2, Sub_Image_3_Resized, cv.TM_CCOEFF_NORMED)
                            check_3 = np.any(result_3 >= (ratio_2-0.1))
                        else:
                            check_3=0

                        if c_7:
                            Sub_Image_1_Resized = imutils.resize(c7_777, width=int(c7_777.shape[1] * scale))
                            result_1 = cv.matchTemplate(area_2, Sub_Image_1_Resized, cv.TM_CCOEFF_NORMED)
                            check_5 = np.any(result_1 >= ratio_2)
                        else:
                            check_5=0

                        if c_6:
                            Sub_Image_1_Resized = imutils.resize(c6_666, width=int(c6_666.shape[1] * scale))
                            result_1 = cv.matchTemplate(area_2, Sub_Image_1_Resized, cv.TM_CCOEFF_NORMED)
                            check_6 = np.any(result_1 >= ratio_2)
                        else:
                            check_6=0
                        
                        if c_5:
                            Sub_Image_1_Resized = imutils.resize(c5_555, width=int(c5_555.shape[1] * scale))
                            result_1 = cv.matchTemplate(area_2, Sub_Image_1_Resized, cv.TM_CCOEFF_NORMED)
                            check_7 = np.any(result_1 >= ratio_2)

                        else:
                            check_7=0

                        if c_11:
                            Sub_Image_1_Resized = imutils.resize(c11_11, width=int(c11_11.shape[1] * scale))
                            result_1 = cv.matchTemplate(area_2, Sub_Image_1_Resized, cv.TM_CCOEFF_NORMED)
                            check_8 = np.any(result_1 >= ratio_2)

                        else:
                            check_8=0

                        if c_12:
                            Sub_Image_1_Resized = imutils.resize(c12_12, width=int(c12_12.shape[1] * scale))
                            result_1 = cv.matchTemplate(area_2, Sub_Image_1_Resized, cv.TM_CCOEFF_NORMED)
                            check_9 = np.any(result_1 >= ratio_2)

                        else:
                            check_9=0


                        Sub_Image_4_Resized = imutils.resize(sn7, width=int(sn7.shape[1] * scale))
                        result_4 = cv.matchTemplate(area_2, Sub_Image_4_Resized, cv.TM_CCOEFF_NORMED)
                        check_4 = np.any(result_4 >= ratio_3)

                        if (check_1==1 or check_2==1 or check_3==1 or check_5==1 or check_6==1 or check_7==1 or check_8 or check_9) and check_4==0:
                            valid_cord=1
                            break




                elif y2 > 365 and y2 <= 635:
                    for scale in np.linspace(1.2, 0.7, 10)[::-1]:
                        if c_8:
                            Sub_Image_1_Resized = imutils.resize(c8_888, width=int(c8_888.shape[1] * scale))
                            result_1 = cv.matchTemplate(area_2, Sub_Image_1_Resized, cv.TM_CCOEFF_NORMED)
                            check_1 = np.any(result_1 >= ratio_2)

                        else:
                            check_1=0

                        if c_9:
                            Sub_Image_2_Resized = imutils.resize(c9_888, width=int(c9_888.shape[1] * scale))
                            result_2 = cv.matchTemplate(area_2, Sub_Image_2_Resized, cv.TM_CCOEFF_NORMED)
                            check_2 = np.any(result_2 >= ratio_2)
                        else:
                            check_2=0

                        if c_10:
                            Sub_Image_3_Resized = imutils.resize(c10_888, width=int(c10_888.shape[1] * scale))
                            result_3 = cv.matchTemplate(area_2, Sub_Image_3_Resized, cv.TM_CCOEFF_NORMED)
                            check_3 = np.any(result_3 >= (ratio_2-0.1))
                        else:
                            check_3=0

                        if c_7:
                            Sub_Image_1_Resized = imutils.resize(c7_777, width=int(c7_777.shape[1] * scale))
                            result_1 = cv.matchTemplate(area_2, Sub_Image_1_Resized, cv.TM_CCOEFF_NORMED)
                            check_5 = np.any(result_1 >= ratio_2)
                        else:
                            check_5=0

                        if c_6:
                            Sub_Image_1_Resized = imutils.resize(c6_666, width=int(c6_666.shape[1] * scale))
                            result_1 = cv.matchTemplate(area_2, Sub_Image_1_Resized, cv.TM_CCOEFF_NORMED)
                            check_6 = np.any(result_1 >= ratio_2)
                        else:
                            check_6=0
                        
                        if c_5:
                            Sub_Image_1_Resized = imutils.resize(c5_555, width=int(c5_555.shape[1] * scale))
                            result_1 = cv.matchTemplate(area_2, Sub_Image_1_Resized, cv.TM_CCOEFF_NORMED)
                            check_7 = np.any(result_1 >= ratio_2)

                        else:
                            check_7=0


                        if c_11:
                            Sub_Image_1_Resized = imutils.resize(c11_11, width=int(c11_11.shape[1] * scale))
                            result_1 = cv.matchTemplate(area_2, Sub_Image_1_Resized, cv.TM_CCOEFF_NORMED)
                            check_8 = np.any(result_1 >= ratio_2)

                        else:
                            check_8=0

                        if c_12:
                            Sub_Image_1_Resized = imutils.resize(c12_12, width=int(c12_12.shape[1] * scale))
                            result_1 = cv.matchTemplate(area_2, Sub_Image_1_Resized, cv.TM_CCOEFF_NORMED)
                            check_9 = np.any(result_1 >= ratio_2)

                        else:
                            check_9=0


                        Sub_Image_4_Resized = imutils.resize(sn7, width=int(sn7.shape[1] * scale))
                        result_4 = cv.matchTemplate(area_2, Sub_Image_4_Resized, cv.TM_CCOEFF_NORMED)
                        check_4 = np.any(result_4 >= ratio_3)

                        if (check_1==1 or check_2==1 or check_3==1 or check_5==1 or check_6==1 or check_7==1 or check_8 or check_9) and check_4==0:
                            valid_cord=1
                            break

                
                elif y2 > 635:
                    for scale in np.linspace(1.4, 0.8, 10)[::-1]:
                        if c_8:
                            Sub_Image_1_Resized = imutils.resize(c8_888, width=int(c8_888.shape[1] * scale))
                            result_1 = cv.matchTemplate(area_2, Sub_Image_1_Resized, cv.TM_CCOEFF_NORMED)
                            check_1 = np.any(result_1 >= ratio_2)

                        else:
                            check_1=0

                        if c_9:
                            Sub_Image_2_Resized = imutils.resize(c9_888, width=int(c9_888.shape[1] * scale))
                            result_2 = cv.matchTemplate(area_2, Sub_Image_2_Resized, cv.TM_CCOEFF_NORMED)
                            check_2 = np.any(result_2 >= ratio_2)
                        else:
                            check_2=0

                        if c_10:
                            Sub_Image_3_Resized = imutils.resize(c10_888, width=int(c10_888.shape[1] * scale))
                            result_3 = cv.matchTemplate(area_2, Sub_Image_3_Resized, cv.TM_CCOEFF_NORMED)
                            check_3 = np.any(result_3 >= ratio_2)
                        else:
                            check_3=0

                        if c_7:
                            Sub_Image_1_Resized = imutils.resize(c7_777, width=int(c7_777.shape[1] * scale))
                            result_1 = cv.matchTemplate(area_2, Sub_Image_1_Resized, cv.TM_CCOEFF_NORMED)
                            check_5 = np.any(result_1 >= ratio_2)
                        else:
                            check_5=0

                        if c_6:
                            Sub_Image_1_Resized = imutils.resize(c6_666, width=int(c6_666.shape[1] * scale))
                            result_1 = cv.matchTemplate(area_2, Sub_Image_1_Resized, cv.TM_CCOEFF_NORMED)
                            check_6 = np.any(result_1 >= ratio_2)
                        else:
                            check_6=0
                        
                        if c_5:
                            Sub_Image_1_Resized = imutils.resize(c5_555, width=int(c5_555.shape[1] * scale))
                            result_1 = cv.matchTemplate(area_2, Sub_Image_1_Resized, cv.TM_CCOEFF_NORMED)
                            check_7 = np.any(result_1 >= ratio_2)

                        else:
                            check_7=0


                        if c_11:
                            Sub_Image_1_Resized = imutils.resize(c11_11, width=int(c11_11.shape[1] * scale))
                            result_1 = cv.matchTemplate(area_2, Sub_Image_1_Resized, cv.TM_CCOEFF_NORMED)
                            check_8 = np.any(result_1 >= ratio_2)

                        else:
                            check_8=0

                        if c_12:
                            Sub_Image_1_Resized = imutils.resize(c12_12, width=int(c12_12.shape[1] * scale))
                            result_1 = cv.matchTemplate(area_2, Sub_Image_1_Resized, cv.TM_CCOEFF_NORMED)
                            check_9 = np.any(result_1 >= ratio_2)

                        else:
                            check_9=0


                        Sub_Image_4_Resized = imutils.resize(sn7, width=int(sn7.shape[1] * scale))
                        result_4 = cv.matchTemplate(area_2, Sub_Image_4_Resized, cv.TM_CCOEFF_NORMED)
                        check_4 = np.any(result_4 >= ratio_3)

                        if (check_1==1 or check_2==1 or check_3==1 or check_5==1 or check_6==1 or check_7==1 or check_8 or check_9) and check_4==0:
                            valid_cord=1
                            break




                if valid_cord:
                    pos_8 = [center_x, center_y]
                    final_cords.append(pos_8)

            final_cords.sort()
            return final_cords

        except:
            return []

    

    def one_screen_custom(search_region):

        try:
            s=time.time()
            final_cords=[]
            ss=py.screenshot(region=search_region)
            ScreenShot_Gray=cv.cvtColor(np.array(ss),cv.COLOR_RGB2GRAY)
            camp_locations=get_camp_locations(ss)
            #print(len(camp_locations))
            for a, b, w, h in camp_locations:
                center_x = a + round(int(w)*0.62)
                center_y = b + round(int(h)*0.45)
                x1 = round(a-w*0.1)
                x2 = round(a+w*1.18)
                y1 = round(0.06*b+25+b)
                y2 = round(0.109*b+80+b)

                ratio_2 = 0.79
                ratio_3 = 0.75
                if y2 < 300: 
                    ratio_2 = 0.75
                if x1 <= 0: 
                    x1 = 0
                if x2 >= 1919: 
                    x2=1919
                area_2 = ScreenShot_Gray[y1:y2, x1:x2]
                #area2 = ScreenShot_Gray
                valid_cord=0
                if y2 <= 365:
                    for scale in np.linspace(0.9, 0.6, 10)[::-1]:

                        if c_8:
                            Sub_Image_1_Resized = imutils.resize(c8_888, width=int(c8_888.shape[1] * scale))
                            result_1 = cv.matchTemplate(area_2, Sub_Image_1_Resized, cv.TM_CCOEFF_NORMED)
                            check_1 = np.any(result_1 >= ratio_2)

                        else:
                            check_1=0

                        if c_9:
                            Sub_Image_2_Resized = imutils.resize(c9_888, width=int(c9_888.shape[1] * scale))
                            result_2 = cv.matchTemplate(area_2, Sub_Image_2_Resized, cv.TM_CCOEFF_NORMED)
                            check_2 = np.any(result_2 >= ratio_2)
                        else:
                            check_2=0

                        if c_10:
                            Sub_Image_3_Resized = imutils.resize(c10_888, width=int(c10_888.shape[1] * scale))
                            result_3 = cv.matchTemplate(area_2, Sub_Image_3_Resized, cv.TM_CCOEFF_NORMED)
                            check_3 = np.any(result_3 >= (ratio_2-0.1))
                        else:
                            check_3=0

                        if c_7:
                            Sub_Image_1_Resized = imutils.resize(c7_777, width=int(c7_777.shape[1] * scale))
                            result_1 = cv.matchTemplate(area_2, Sub_Image_1_Resized, cv.TM_CCOEFF_NORMED)
                            check_5 = np.any(result_1 >= ratio_2)
                        else:
                            check_5=0

                        if c_6:
                            Sub_Image_1_Resized = imutils.resize(c6_666, width=int(c6_666.shape[1] * scale))
                            result_1 = cv.matchTemplate(area_2, Sub_Image_1_Resized, cv.TM_CCOEFF_NORMED)
                            check_6 = np.any(result_1 >= ratio_2)
                        else:
                            check_6=0
                        
                        if c_5:
                            Sub_Image_1_Resized = imutils.resize(c5_555, width=int(c5_555.shape[1] * scale))
                            result_1 = cv.matchTemplate(area_2, Sub_Image_1_Resized, cv.TM_CCOEFF_NORMED)
                            check_7 = np.any(result_1 >= ratio_2)

                        else:
                            check_7=0

                        if c_11:
                            Sub_Image_1_Resized = imutils.resize(c11_11, width=int(c11_11.shape[1] * scale))
                            result_1 = cv.matchTemplate(area_2, Sub_Image_1_Resized, cv.TM_CCOEFF_NORMED)
                            check_8 = np.any(result_1 >= ratio_2)

                        else:
                            check_8=0

                        if c_12:
                            Sub_Image_1_Resized = imutils.resize(c12_12, width=int(c12_12.shape[1] * scale))
                            result_1 = cv.matchTemplate(area_2, Sub_Image_1_Resized, cv.TM_CCOEFF_NORMED)
                            check_9 = np.any(result_1 >= ratio_2)

                        else:
                            check_9=0


                        Sub_Image_4_Resized = imutils.resize(sn7, width=int(sn7.shape[1] * scale))
                        result_4 = cv.matchTemplate(area_2, Sub_Image_4_Resized, cv.TM_CCOEFF_NORMED)
                        check_4 = np.any(result_4 >= ratio_3)

                        if (check_1==1 or check_2==1 or check_3==1 or check_5==1 or check_6==1 or check_7==1 or check_8 or check_9) and check_4==0:
                            valid_cord=1
                            break




                elif y2 > 365 and y2 <= 635:
                    for scale in np.linspace(1.2, 0.7, 10)[::-1]:
                        if c_8:
                            Sub_Image_1_Resized = imutils.resize(c8_888, width=int(c8_888.shape[1] * scale))
                            result_1 = cv.matchTemplate(area_2, Sub_Image_1_Resized, cv.TM_CCOEFF_NORMED)
                            check_1 = np.any(result_1 >= ratio_2)

                        else:
                            check_1=0

                        if c_9:
                            Sub_Image_2_Resized = imutils.resize(c9_888, width=int(c9_888.shape[1] * scale))
                            result_2 = cv.matchTemplate(area_2, Sub_Image_2_Resized, cv.TM_CCOEFF_NORMED)
                            check_2 = np.any(result_2 >= ratio_2)
                        else:
                            check_2=0

                        if c_10:
                            Sub_Image_3_Resized = imutils.resize(c10_888, width=int(c10_888.shape[1] * scale))
                            result_3 = cv.matchTemplate(area_2, Sub_Image_3_Resized, cv.TM_CCOEFF_NORMED)
                            check_3 = np.any(result_3 >= (ratio_2-0.1))
                        else:
                            check_3=0

                        if c_7:
                            Sub_Image_1_Resized = imutils.resize(c7_777, width=int(c7_777.shape[1] * scale))
                            result_1 = cv.matchTemplate(area_2, Sub_Image_1_Resized, cv.TM_CCOEFF_NORMED)
                            check_5 = np.any(result_1 >= ratio_2)
                        else:
                            check_5=0

                        if c_6:
                            Sub_Image_1_Resized = imutils.resize(c6_666, width=int(c6_666.shape[1] * scale))
                            result_1 = cv.matchTemplate(area_2, Sub_Image_1_Resized, cv.TM_CCOEFF_NORMED)
                            check_6 = np.any(result_1 >= ratio_2)
                        else:
                            check_6=0
                        
                        if c_5:
                            Sub_Image_1_Resized = imutils.resize(c5_555, width=int(c5_555.shape[1] * scale))
                            result_1 = cv.matchTemplate(area_2, Sub_Image_1_Resized, cv.TM_CCOEFF_NORMED)
                            check_7 = np.any(result_1 >= ratio_2)

                        else:
                            check_7=0


                        if c_11:
                            Sub_Image_1_Resized = imutils.resize(c11_11, width=int(c11_11.shape[1] * scale))
                            result_1 = cv.matchTemplate(area_2, Sub_Image_1_Resized, cv.TM_CCOEFF_NORMED)
                            check_8 = np.any(result_1 >= ratio_2)

                        else:
                            check_8=0

                        if c_12:
                            Sub_Image_1_Resized = imutils.resize(c12_12, width=int(c12_12.shape[1] * scale))
                            result_1 = cv.matchTemplate(area_2, Sub_Image_1_Resized, cv.TM_CCOEFF_NORMED)
                            check_9 = np.any(result_1 >= ratio_2)

                        else:
                            check_9=0


                        Sub_Image_4_Resized = imutils.resize(sn7, width=int(sn7.shape[1] * scale))
                        result_4 = cv.matchTemplate(area_2, Sub_Image_4_Resized, cv.TM_CCOEFF_NORMED)
                        check_4 = np.any(result_4 >= ratio_3)

                        if (check_1==1 or check_2==1 or check_3==1 or check_5==1 or check_6==1 or check_7==1 or check_8 or check_9) and check_4==0:
                            valid_cord=1
                            break

                
                elif y2 > 635:
                    for scale in np.linspace(1.4, 0.8, 10)[::-1]:
                        if c_8:
                            Sub_Image_1_Resized = imutils.resize(c8_888, width=int(c8_888.shape[1] * scale))
                            result_1 = cv.matchTemplate(area_2, Sub_Image_1_Resized, cv.TM_CCOEFF_NORMED)
                            check_1 = np.any(result_1 >= ratio_2)

                        else:
                            check_1=0

                        if c_9:
                            Sub_Image_2_Resized = imutils.resize(c9_888, width=int(c9_888.shape[1] * scale))
                            result_2 = cv.matchTemplate(area_2, Sub_Image_2_Resized, cv.TM_CCOEFF_NORMED)
                            check_2 = np.any(result_2 >= ratio_2)
                        else:
                            check_2=0

                        if c_10:
                            Sub_Image_3_Resized = imutils.resize(c10_888, width=int(c10_888.shape[1] * scale))
                            result_3 = cv.matchTemplate(area_2, Sub_Image_3_Resized, cv.TM_CCOEFF_NORMED)
                            check_3 = np.any(result_3 >= ratio_2)
                        else:
                            check_3=0

                        if c_7:
                            Sub_Image_1_Resized = imutils.resize(c7_777, width=int(c7_777.shape[1] * scale))
                            result_1 = cv.matchTemplate(area_2, Sub_Image_1_Resized, cv.TM_CCOEFF_NORMED)
                            check_5 = np.any(result_1 >= ratio_2)
                        else:
                            check_5=0

                        if c_6:
                            Sub_Image_1_Resized = imutils.resize(c6_666, width=int(c6_666.shape[1] * scale))
                            result_1 = cv.matchTemplate(area_2, Sub_Image_1_Resized, cv.TM_CCOEFF_NORMED)
                            check_6 = np.any(result_1 >= ratio_2)
                        else:
                            check_6=0
                        
                        if c_5:
                            Sub_Image_1_Resized = imutils.resize(c5_555, width=int(c5_555.shape[1] * scale))
                            result_1 = cv.matchTemplate(area_2, Sub_Image_1_Resized, cv.TM_CCOEFF_NORMED)
                            check_7 = np.any(result_1 >= ratio_2)

                        else:
                            check_7=0


                        if c_11:
                            Sub_Image_1_Resized = imutils.resize(c11_11, width=int(c11_11.shape[1] * scale))
                            result_1 = cv.matchTemplate(area_2, Sub_Image_1_Resized, cv.TM_CCOEFF_NORMED)
                            check_8 = np.any(result_1 >= ratio_2)

                        else:
                            check_8=0

                        if c_12:
                            Sub_Image_1_Resized = imutils.resize(c12_12, width=int(c12_12.shape[1] * scale))
                            result_1 = cv.matchTemplate(area_2, Sub_Image_1_Resized, cv.TM_CCOEFF_NORMED)
                            check_9 = np.any(result_1 >= ratio_2)

                        else:
                            check_9=0


                        Sub_Image_4_Resized = imutils.resize(sn7, width=int(sn7.shape[1] * scale))
                        result_4 = cv.matchTemplate(area_2, Sub_Image_4_Resized, cv.TM_CCOEFF_NORMED)
                        check_4 = np.any(result_4 >= ratio_3)

                        if (check_1==1 or check_2==1 or check_3==1 or check_5==1 or check_6==1 or check_7==1 or check_8 or check_9) and check_4==0:
                            valid_cord=1
                            break




                if valid_cord:
                    pos_8 = [center_x, center_y]
                    final_cords.append(pos_8)

            final_cords.sort()
            e=time.time()
            #print("Time Taken = ",e-s)
            tot_cords=len(final_cords)
            i=0

            while i<tot_cords:
                print("No of camps = ",tot_cords)
                loc=final_cords[i]
                if click_checker(loc):
                
                    mouseclick(loc[0]+search_region[0],loc[1]+search_region[1])
                    image_after_click=None
                    time.sleep(0.4)
                    if lvl_check_method==1:
                        img_after_click=imagesearch_numLoop_self(resource_path(dir+"image_after_click.png"),gola,precision=0.9,reg=(836,501,75,49))
                    elif lvl_check_method==2:
                        img_after_click=image_after_click_camp()
                        if img_after_click==False:
                            img_after_click=None

                    else:
                        img_after_click=image_after_click_alternative()
                        if img_after_click==False:
                            img_after_click=None

                    if img_after_click!=None:
                        pass_check(loc)
                        swift_attack()
                    else:
                        print("cant find")
                        py.click(button="right",clicks=1)
                if disturbance_checker_timer(time_between_clicks)==True:
                    i=i-1
                i=i+1        
        except Exception as e:
            print(e)



    def one_screen_customized(search_region):

        threshold2=0.67
        eps=1
        try:
        
            haystack_img1=py.screenshot(region=search_region)

            haystack_img1 = cv.cvtColor(np.array(haystack_img1), 
                            cv.COLOR_RGB2GRAY)

            points=[]

            if c_12:
                needle_img1 = cv.imread(resource_path(dir+'c12.png'), cv.IMREAD_UNCHANGED)
                needle_img1= cv.cvtColor(np.array(needle_img1), 
                                cv.COLOR_RGB2GRAY)

                points+=findClickPositions(needle_img1,haystack_img1,threshold2,eps)



            if c_11:

                needle_img1 = cv.imread(resource_path(dir+'c11.png'), cv.IMREAD_UNCHANGED)
                needle_img1= cv.cvtColor(np.array(needle_img1), 
                                cv.COLOR_RGB2GRAY)

                points+=findClickPositions(needle_img1,haystack_img1,threshold2,eps)

            if c_10:

                needle_img1 = cv.imread(resource_path(dir+'campx2.png'), cv.IMREAD_UNCHANGED)
                needle_img1= cv.cvtColor(np.array(needle_img1), 
                                cv.COLOR_RGB2GRAY)

                points+=findClickPositions(needle_img1,haystack_img1,threshold2,eps)


            if c_9:

                needle_img1 = cv.imread(resource_path(dir+'camp92.png'), cv.IMREAD_UNCHANGED)
                needle_img1= cv.cvtColor(np.array(needle_img1), 
                                cv.COLOR_RGB2GRAY)

                points+=findClickPositions(needle_img1,haystack_img1,threshold2,eps)

            if c_8:

                needle_img1 = cv.imread(resource_path(dir+'camp82.png'), cv.IMREAD_UNCHANGED)
                needle_img1= cv.cvtColor(np.array(needle_img1), 
                                cv.COLOR_RGB2GRAY)

                points+=findClickPositions(needle_img1,haystack_img1,threshold2,eps)

            if c_7:

                needle_img1 = cv.imread(resource_path(dir+'c7.png'), cv.IMREAD_UNCHANGED)
                needle_img1= cv.cvtColor(np.array(needle_img1), 
                                cv.COLOR_RGB2GRAY)

                points+=findClickPositions(needle_img1,haystack_img1,threshold2,eps)

            if c_6:
                needle_img1 = cv.imread(resource_path(dir+'c6.png'), cv.IMREAD_UNCHANGED)
                needle_img1= cv.cvtColor(np.array(needle_img1), 
                                cv.COLOR_RGB2GRAY)

                points+=findClickPositions(needle_img1,haystack_img1,threshold2,eps)

            if c_5:

                needle_img1 = cv.imread(resource_path(dir+'c5.png'), cv.IMREAD_UNCHANGED)
                needle_img1= cv.cvtColor(np.array(needle_img1), 
                                cv.COLOR_RGB2GRAY)

                points+=findClickPositions(needle_img1,haystack_img1,threshold2,eps)

            print(points)
            final_cords=points
            print(final_cords)
            e=time.time()
            #print("Time Taken = ",e-s)
            tot_cords=len(final_cords)
            i=0

            while i<tot_cords:
                if cmd_number[3]==0:
                    return []

                print("No of camps = ",tot_cords)
                loc=final_cords[i]
                if click_checker(loc):
                
                    mouseclick(loc[0]+search_region[0]+x_reducer,loc[1]+search_region[1]-y_reducer)
                    image_after_click=None
                    time.sleep(0.4)
                    if lvl_check_method==1:
                        img_after_click=imagesearch_numLoop_self(resource_path(dir+"image_after_click.png"),gola,precision=0.9,reg=(836,501,75,49))
                    elif lvl_check_method==2:
                        img_after_click=image_after_click_camp()
                        if img_after_click==False:
                            img_after_click=None

                    else:
                        img_after_click=image_after_click_alternative()
                        if img_after_click==False:
                            img_after_click=None

                    if img_after_click!=None:
                        pass_check(loc)
                        swift_attack()
                        waiter()
                    else:
                        print("cant find")
                        py.click(button="right",clicks=1)
                if disturbance_checker_timer(time_between_clicks)==True:
                    i=i-1
                i=i+1   


            return final_cords     

        except Exception as e:
            return []
            print(e)



    def porter(acc_porting,port_area,camp_cord):

        points=port_points_between(acc_porting,port_area,camp_cord)
        for i in range(len(points)):
            ported,success=port_between(port_area,points[i])
            if ported==True and success:
                #time.sleep(1)
                return True
            if ported and success == False:
                return False
            disturbance_checker_timer_global(time_between_clicks)
            time.sleep(0.1)
        return False



    def port_points_between(acc_porting,port_area,camp_cord):

        if port_point_finder=='1':
            return port_point_giver(camp_cord)


        dir_loca=dir+'/'+season+'/'
        print(port_area)
        haystack_img1=py.screenshot(region=port_area)

        haystack_img1 = cv.cvtColor(np.array(haystack_img1), 
                        cv.COLOR_RGB2BGR)
        needle_img1 = cv.imread(resource_path(dir_loca+"ground.png"), cv.IMREAD_UNCHANGED)
        needle_img1= cv.cvtColor(np.array(needle_img1), 
                        cv.COLOR_RGB2BGR)
        
        needle_img2 = cv.imread(resource_path(dir_loca+"tree.png"), cv.IMREAD_UNCHANGED)
        needle_img2= cv.cvtColor(np.array(needle_img2), 
                        cv.COLOR_RGB2BGR)
        
        needle_img3 = cv.imread(resource_path(dir_loca+"ground2.png"), cv.IMREAD_UNCHANGED)
        needle_img3= cv.cvtColor(np.array(needle_img3), 
                        cv.COLOR_RGB2BGR)
        
        needle_img4 = cv.imread(resource_path(dir_loca+"tree2.png"), cv.IMREAD_UNCHANGED)
        needle_img4= cv.cvtColor(np.array(needle_img4), 
                        cv.COLOR_RGB2BGR)
        
        needle_img5 = cv.imread(resource_path(dir_loca+"animal.png"), cv.IMREAD_UNCHANGED)
        needle_img5= cv.cvtColor(np.array(needle_img5), 
                        cv.COLOR_RGB2BGR)


        eps_winter=0.7

        if season=="Winter":
            acc_porting[0]=0.8
            eps_winter=1
        
        port_points=findClickPositions(needle_img1,haystack_img1,acc_porting[0],eps_val=eps_winter)
        port_points+=findClickPositions(needle_img2,haystack_img1,acc_porting[2],eps_val=0.7)

        port_points+=findClickPositions(needle_img3,haystack_img1,acc_porting[1],eps_val=0.7)
        port_points+=findClickPositions(needle_img4,haystack_img1,acc_porting[3],eps_val=0.7)
        port_points+=findClickPositions(needle_img5,haystack_img1,acc_porting[4],eps_val=0.7)

        port_points =sorted(port_points, key = lambda sub: abs((sub[1] - sub[0])-300))
        port_points=random.sample(port_points, k=len(port_points))
        print("Port Loc : ",port_points)
        return port_points



    def port_between(loc,port_area):
        dir_loca=dir+'/'+season+'/'
        if port_point_finder!='1':
            py.click(loc[0]+port_area[0],loc[1]+port_area[1])
        else:
            py.click(port_area[0],port_area[1])
        time.sleep(tweaker*0.1-0.1)
        port_screen=imagesearch_numLoop_self(resource_path(dir+"port_screen.png"),3,precision=0.6,reg=(863,647,185,48))
        if port_screen==None:
            time.sleep(0.1)
            py.click(button="right",clicks=1)
            time.sleep(0.7)
            return False,False

        time.sleep(delay)
        py.click(955,668)
        pos=imagesearch_numLoop_self(resource_path(dir+"confirm_port.png"),8,precision=0.6,reg=(737,663,200,60))
        if pos==None:
            pos=imagesearch_numLoop_self(resource_path(dir+"cant_teleport.png"),0,precision=0.8,reg=(861,243,191,47))
            if pos!=None:
                py.click(button='right',clicks=1)
                return True,False
            pos=imagesearch_numLoop_self(resource_path(dir+"water.png"),0,precision=0.8,reg=(776,271,358,52))
            if pos!=None:
                py.click(button='right',clicks=1)
                return False,False
            
            py.click(button="right",clicks=1)
            return False,False
        time.sleep(0.15)
        py.click(807,698)
        return True,True


    def box_x(x):

        if x<0:
            return 0
        elif x>1796:
            return 0

        return x
        

    def box_y(y):

        if y<143:
            return 0

        elif y>879:
            return 0

        return y 

    def box_limitation_x(x):
        if x<0:
            return 0
        elif x>1796:
            return 1796

        return x

        

    def box_limitation_y(y):

        if y<143:
            return 144

        elif y>879:
            return 878

        return y 


    


    def port_point_giver(camp_cord):
        x=camp_cord[0]
        y=camp_cord[1]

        ## left side

        p_points=[]

        if box_x(x-left_doori)!=0 and box_y(y)!=0:
            p_points.append([x-left_doori,y])

        ### rigth side

        if box_x(x+right_doori)!=0 and box_y(y)!=0:
            p_points.append([x+right_doori,y])

        

        ## top

        if box_x(x)!=0 and box_y(y-top_doori)!=0:
            p_points.append([x,y-top_doori])

        ## bottom

        if box_x(x)!=0 and box_y(y+top_doori)!=0:
            p_points.append([x,y+top_doori])


        if port_diagonal:

            ## top_left

            if box_x(x-left_doori)!=0 and box_y(y-top_doori)!=0:
                p_points.append([x-left_doori,y-top_doori])


            ## top_rigth

            if box_x(x+right_doori)!=0 and box_y(y-top_doori)!=0:
                p_points.append([x+right_doori,y-top_doori])

            

            ## bottom left

            if box_x(x-left_doori)!=0 and box_y(y+bottom_doori)!=0:
                p_points.append([x-left_doori,y+bottom_doori])

            ## bottom right

            if box_x(x+right_doori)!=0 and box_y(y+bottom_doori)!=0:
                p_points.append([x+right_doori,y+bottom_doori])

        return p_points




    def move_up():
        if cmd_number[3]==0:
            return
        Hor_Y = 750
        Drag_X = 470
        DX = 1300
        Ver_X = 960
        Drag_Y = 220
        DY = 550
        time_wait_getpos=0.09
        check_for_disturbance()
        click_checker((300,300))
        mouse.drag(Ver_X, Drag_Y, Ver_X, Drag_Y+DY, True, 0.01)
        mouse.move(Drag_X, 230, True, 0)
        time.sleep(time_wait_getpos)
        mouse.press(button='left')

        time.sleep(press_time)
        mouse.release(button='left')
        mouseclick(Drag_X,73)
        if cfds==1 :
            check_for_disturbance()
        time.sleep(swipe_delay)


    def move_down():
        if cmd_number[3]==0:
            return
        Hor_Y = 750
        Drag_X = 470
        DX = 1300
        Ver_X = 960
        Drag_Y = 220
        DY = 550
        time_wait_getpos=0.09

        check_for_disturbance()

        click_checker((300,300))

        mouse.drag(Ver_X, Drag_Y+DY-220, Ver_X, Drag_Y, True, 0.01)
        mouse.move(Drag_X, 230, True, 0)
        time.sleep(time_wait_getpos)
        mouse.press(button='left')

        time.sleep(press_time)
        mouse.release(button='left')
        mouseclick(Drag_X,73)

        if cfds==1 :
            check_for_disturbance()


        time.sleep(swipe_delay)


    def move_right():
        if cmd_number[3]==0:
            return
        Hor_Y = 750
        Drag_X = 470
        DX = 1300
        Ver_X = 960
        Drag_Y = 220
        DY = 550
        time_wait_getpos=0.09

        check_for_disturbance()
        click_checker((300,300))
        mouse.drag(1746, 723, 178, 723, True, 0.01)
        mouse.move(287, 230, True, 0)
        time.sleep(time_wait_getpos)
        mouse.press(button='left')

        time.sleep(press_time)
        mouse.release(button='left')
        mouseclick(287,73)

        if cfds==1 :
            check_for_disturbance()

        time.sleep(swipe_delay)



    def move_left():
        if cmd_number[3]==0:
            return
        Hor_Y = 750
        Drag_X = 470
        DX = 1300
        Ver_X = 960
        Drag_Y = 220
        DY = 550
        time_wait_getpos=0.09

        

        check_for_disturbance()
        click_checker((300,300))
        mouse.drag(Drag_X, Hor_Y, Drag_X+DX, Hor_Y, True, 0.01)
        mouse.move(1300, 230, True, 0)
        time.sleep(time_wait_getpos)
        mouse.press(button='left')
        time.sleep(press_time)
        mouse.release(button='left')
        mouseclick(1300,50)
 
        if cfds==1 :
            check_for_disturbance()

        time.sleep(swipe_delay)



    def top_left():
        if cmd_number[3]==0:
            return
        Hor_Y = 750
        Drag_X = 470
        DX = 1300
        Ver_X = 960
        Drag_Y = 220
        DY = 550

        time_wait_getpos=0.09

        check_for_disturbance()
        click_checker((300,300))


        mouse.drag(960, 330, 1770, 770, True, 0.01)
        mouse.move(1300, 230, True, 0)
        time.sleep(time_wait_getpos)
        mouse.press(button='left')
        time.sleep(press_time)
        mouse.release(button='left')


        mouseclick(1300,50)
        if cfds==1:
            check_for_disturbance()


        time.sleep(swipe_delay)

    def top_right():
        if cmd_number[3]==0:
            return
        time_wait_getpos=0.09

        check_for_disturbance()
        click_checker((300,300))
        mouse.drag(1513,220,440,710, True, 0.01)
        mouse.move(1300, 230, True, 0)
        time.sleep(time_wait_getpos)
        mouse.press(button='left')
        time.sleep(press_time)
        mouse.release(button='left')
        mouseclick(287,50)
        if cfds==1:
            check_for_disturbance()
        mouseclick(1300,50)
        if cfds==1:
            check_for_disturbance()
        time.sleep(swipe_delay)


    def bottom_right():
        if cmd_number[3]==0:
            return
        time_wait_getpos=0.09

        check_for_disturbance()
        click_checker((300,300))

        mouse.drag(1551,748,250,250, True, 0.01)
        mouse.move(1300, 230, True, 0)
        time.sleep(time_wait_getpos)
        mouse.press(button='left')
        time.sleep(press_time)
        mouse.release(button='left')
        mouseclick(690,50)
        if cfds==1:
            check_for_disturbance()
        mouseclick(1300,50)
        if cfds==1:
            check_for_disturbance()
        time.sleep(swipe_delay)


    def bottom_left():
        if cmd_number[3]==0:
            return
        time_wait_getpos=0.09

        check_for_disturbance()
        click_checker((300,300))
        mouse.drag(223,748,1551,229, True, 0.01)
        mouse.move(1300, 230, True, 0)
        time.sleep(time_wait_getpos)
        mouse.press(button='left')
        time.sleep(press_time)
        mouse.release(button='left')
        mouseclick(1300,50)

        if cfds==1:
            check_for_disturbance()
        mouseclick(1300,50)
        if cfds==1:
            check_for_disturbance()
        time.sleep(swipe_delay)



            




    def area_calculator(camp_cord):
        x=camp_cord[0]
        y=camp_cord[1]

        x1=box_limitation_x(x-115)
        y1=box_limitation_y(y-71)
        x2=box_limitation_x(x1+142)
        y2=box_limitation_y(y1+93)

        return (x1,y1,x2-x1,y2-y1)



    def beside_port(cords_camps):
        f=False
        tot_no=len(cords_camps)
        for i in range(tot_no):
            area= area_calculator(cords_camps[i])
            if porter(acc_porting,area,cords_camps[i])==False:
                time.sleep(time_between_clicks)
                continue
            else:
                f=True
                break

        return f

    def abs_val(x):
        if x<0:
            return -1*x

        return x

    def filter_hitted_cords(hitted_cords,camp_cords):
        final_cords=[]
        
        for i in range(len(camp_cords)):
            a=True
            for j in range(len(hitted_cords)):
                dist= abs_val(hitted_cords[j][0]+x_reducer+762-camp_cords[i][0]) + abs_val(hitted_cords[j][1]+362-camp_cords[i][1])

                if dist<=same_camp_diff_val:
                    a=False

            if a:
                final_cords.append(camp_cords[i])


        print("Final Cords : ",final_cords)


        return final_cords

    def camp_cleaner():

        hitted_cords=[]

        while True:

            if cmd_number[3]==0:
                return None
            
            cords_camps=one_screen(0)
            cords_camps=filter_hitted_cords(hitted_cords,cords_camps)
            print("NUMBER of camps Found = ",len(cords_camps))
            if len(cords_camps)>0:
                if beside_port(cords_camps):
                    time.sleep(wait_after_port)
                    check_area=[762, 362, 398, 362]
                    hitted_cords=one_screen_customized(check_area)
                    wait_loop()
                    click_checker((300,300))
                    time.sleep(extra_sleep)
                    if breaker:
                        break
                    #break
                    #cords_camps=one_screen(0)
                else:
                    break

            else:
                break
                
        return None

    def r_4():

        camp_cleaner()

        move_left()
        val=camp_cleaner()
        '''
        time.sleep(time_before_home_click)
        mouseclick(837,867)
        time.sleep(time_after_home_click)
        '''


        move_up()
        val=camp_cleaner()
        '''
        time.sleep(time_before_home_click)
        mouseclick(837,867)
        time.sleep(time_after_home_click)
        '''


        move_right()
        camp_cleaner()
        '''
        time.sleep(time_before_home_click)
        mouseclick(837,867)
        time.sleep(time_after_home_click)
        '''
        move_right()
        camp_cleaner()

        move_down()
        camp_cleaner()


    def r_8():

        camp_cleaner()

        move_down()
        val=camp_cleaner()
        


        move_left()
        val=camp_cleaner()

        move_up()
        val=camp_cleaner()

        move_up()
        val=camp_cleaner()


        move_right()
        val=camp_cleaner()


        move_right()
        val=camp_cleaner()



        move_down()
        val=camp_cleaner()



        move_down()
        val=camp_cleaner()

    
    
    


    while True:

        time.sleep(0.15)
        if cmd_number[2]==1:
            cmd_number[2]=0
            clear_starting_screens()

        if keyboard.is_pressed("s"):

            cmd_number[0]=1
            cmd_number[1]=1
            cmd_number[3]=1

        right_time=False
        if hit_at_spawn=='yes' and cmd_number[3]==1:
            time.sleep(2)

            if spawn_checker():
                right_time=True
                cmd_number[0]=1
                cmd_number[1]=1
                if Game_Running()==False:
                    game_restart()
                    clear_starting_screens()
                    cmd_number[0]=1
                else:
                    os.system("start explorer shell:appsFolder\A278AB0D.MarchofEmpires_h6adky7gbf63m!App")
                    badha()

            else:
                right_time=False

        else:
            right_time=True 

        if (cmd_number[1]==1 and cmd_number[0]==1 and server_arr[0]==1 and right_time and cmd_number[3]==1):

            f=open("cords_in_text.txt","r")
            cordinates=f.read()
            f.close()

            s=cordinates.split("#")
            region_arr=[]
            for i in s:
                i=i.split(":")
                a=[int(j) for j in i]
                region_arr.append((a[0],a[1]))


            region_arr = random.sample(region_arr, k=len(region_arr))
            global reg_count
            reg_count=0

            
            disturbance_checker_timer_global(time_between_clicks)
            own_castle=[]
            if check_stuck=='yes':
                var_home=0
                while var_home<3:

                    badha()
                    home_screen=py.locateOnScreen(resource_path(dir+"home_screen.png"),region=(829,842,60,47),confidence=0.9)
                    if home_screen!=None:
                        click(837,867)
                        time.sleep(0.3)
                        own_castle=py.screenshot(region=(923,503,65,31))
                        own_castle = cv.cvtColor(np.array(own_castle), cv.COLOR_RGB2BGR)
                        
                        break
                
                    var_home+=1
                        


            if isNumLockOn():
                py.press("numlock")

            while True:

                if hit_at_spawn=='yes':
                    if spawn_checker()==False:
                        if start_game_at_spawn=='yes':
                            task_kill="TASKKILL /F /IM "+Game_Name
                            os.system(task_kill)
                            
                            cmd_number[0]=0
                            time.sleep(60)
                        break

                curr_time=time.time()
                if cmd_number[0]==0:
                    task_kill="TASKKILL /F /IM "+Game_Name
                    os.system(task_kill)
                    break

                if curr_time-start_time>samay :
                    cmd_number[3]=0
                    cmd_number[1]=0
                    break

                if cmd_number[1]==0 or server_arr[0]==0 or cmd_number[3]==0 :
                    cmd_number[1]=0
                    break
                
                time.sleep(wait_val)
                if multi_region==1:
                    camp_cleaner()
                elif multi_region==2:
                    r_4()
                else:
                    r_8()
                
                if reg_count >=len(region_arr):
                    reg_count=0

                location_opener(region_arr[reg_count])
                reg_count+=1
                wait_loop()
                retry_checker()
                click_checker((300,300))
                shield_checker()  
                            
def new_update_downloader(name,address):
    import gdown

    def killer():
        top.destroy()
    dir_loc=""
    curr_directory=os.getcwd()
    curr_directory=curr_directory.split('\\')
    rasta=""
    for i in range(len(curr_directory)-1):
        rasta+=curr_directory[i]+'//'
    dir_loc=rasta
    rasta+=name


    url = 'https://drive.google.com/uc?id='+address 
    output = rasta+'.zip'
    gdown.download(url, output, quiet=False)

    #time.sleep(5)
    top=Tk()
    top.iconbitmap(resource_path("bot.ico"))
    top.title("Confirmation")
    label=Label(top,text="Successfully Downloaded At :  "+rasta,fg="#990000",bg="white",pady=30,padx=20).grid(row=0,column=0)
    button=Button(top,text="OK",command=killer,fg="#990000",bg="white",padx=70).grid(row=1,column=0)

    top.mainloop()
    with zipfile.ZipFile(output,"r") as zip_ref:
        zip_ref.extractall(dir_loc)

    print("You May Now Close This Window")

def pop_up_update(n,name,location_,bot_version):

    r_val=0
    root=Tk()
    root.title("Update")

    root.iconbitmap(resource_path("bot.ico"))
    label=Label(root,text="Dear User, New Version of bot is available for download.",fg="#990000",bg="white",pady=30,padx=20).grid(row=1,column=0)

    if n==1:
        title_box="Update"
        a=bot_version.split(".")
        bot_version=str(int(a[0]))+"."+str(int(a[1])+1)
        box_text="v"+bot_version+" is available for download. Download Now ?"
        response=messagebox.askyesno(title_box,box_text)
        r_val=response
        if response==1:
            root.destroy()
        else:
            root.destroy()


    else:
        title_box="Manadatory Update"
        box_text="This Version Is No Longger Supported. Download The Latest Version Now ?"
        
        response=messagebox.askyesno(title_box,box_text)
        r_val=response
        if response==1:
            root.destroy()

        else:
            root.destroy()

    
    root.mainloop()
    return r_val


def Invalide_User():

    root=Tk()
    root.title("Alert")
    root.iconbitmap(resource_path("bot.ico"))
    #root.withdraw()
    message_frame=LabelFrame(root,text="Levi Bots",fg='#990000',padx=20,pady=20)
    label1=Label(root,text="Hi, You are Not Authorised To The Use Of Levi Bots",fg='#990000',padx=20,pady=20).grid(row=0,column=0)
    label2=Label(message_frame,text="Please Contact At Information Shown Below : ",fg='#990000',padx=20).grid(row=1,column=0)
    label3=Label(message_frame,text="Line : botsmoe ",fg='#990000',padx=20).grid(row=2,column=0)
    label4=Label(message_frame,text="Discord : LEVI#1709     (All Capital: L E V I)",fg='#990000',padx=20).grid(row=3,column=0)
    label5=Label(message_frame,text="Gmail : automationexperts.org@gmail.com",fg='#990000',padx=20).grid(row=4,column=0)
    response=messagebox.showinfo("Alert","Please Contact At Information Shown Below. \n Line : botsmoe .\n Discord : LEVI#1709. \n Gmail : automationexperts.org@gmail.com")
    message_frame.grid(row=1,column=0)

    root.mainloop()

def user_expired():
    root=Tk()
    root.title("Expired")
    root.iconbitmap(resource_path("bot.ico"))
    label=Label(root,text="Dear User Your Bot Has Expired . Please Recharge To Continue The Use. Thank You.",fg="#990000",bg="white",pady=30,padx=20).pack()
    root.mainloop()


def pop_up_handler(msg):
    root=Tk()
    root.title("INFO")
    root.iconbitmap(resource_path("bot.ico"))
    root.withdraw()

    messagebox.showinfo("Message From Levi : ",msg)
    root.destroy()
    root.mainloop()



def server_communication(server_arr,discord_key_arr):
    SERVER="3.73.231.132"
    PORT=80
    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect((SERVER,PORT))

    ############ Sending User Details ###########

    game="moe"
    bot_type="port_camp"
    auth_key = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
    bot_version='1.2'

    d_d=""
    result_w_g=""

    try:
        key_w_g = winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE,
            "SOFTWARE\\Microsoft\\Cryptography",
            0,
            winreg.KEY_READ | winreg.KEY_WOW64_64KEY
        )

        result_w_g = winreg.QueryValueEx(key_w_g, "MachineGuid")
        result_w_g=result_w_g[0]
    except:
        result_w_g="notfound"

    try:
        d_d=subprocess.check_output('wmic DISKDRIVE get SerialNumber').decode().split('\n')[1].strip()

    except:
        d_d="notfound"

    '''
    auth_key='03000200-0400-0500-0006-000700080009'
    d_d='AA0000000000000011488d57f8d2-771b-4cce-'
    result_wg="8ed1-a2f1ca5f753f"
    '''
        

    Handshake_info= game+'/r'+bot_type+'/r'+auth_key+'/r'+bot_version+'/r'+d_d+'/r'+result_w_g
    
    client.send(Handshake_info.encode('utf-8'))
    print("Game : ",game)
    print("Bot  : ",bot_type)
    print("Current Bot Version : ",bot_version)

    ############# End of sending details ################

    last_sent_time=time.time()

    while True:
        msg=client.recv(1024).decode('utf-8')
                     
        if msg=='Invalid User':

            #print("Invalid User")
            server_arr[0]=0
            Invalide_User()
            #time.sleep(5)
            break

        if msg[0:21]=='Connection Successful':
            msg=msg.split(";;")
            print("Successfully logged In")
            print(" ")
            print("Keys :")
            print("s : start")
            print("d : stop ( It will stop After clearing current region)")
            if float(msg[1])>float(bot_version):
                print("Please Use The Latest Version")
                time.sleep(6)
                #client.send('disconnect'.encode('utf-8'))
                return

            discord_key=msg[2]
            #print(f'Discord Auth Key : {discord_key}')

            dicord_bytes=bytes(discord_key,'ascii')
     
            for i in range(len(dicord_bytes)):
                discord_key_arr[i]=dicord_bytes[i]

            discord_key_arr[119]=len(dicord_bytes)
            if msg[3]!="None":
                pop_up_handler(msg[3])

            server_arr[0]=1

            

        if msg[0:8]=='update_n':
            msg_content=[i for i in msg.split(';;')]
            if pop_up_update(1,msg_content[1],msg_content[2],bot_version)==1:
                root_e=Tk()

                root_e.after(6000,lambda:root_e.destroy())
                root_e.title("Info")
                label=Label(root_e,text="Download Will Be Started Soon. Kindly Do Not Close The Application",fg="#990000",bg="white").pack()
                root_e.mainloop()
                print("Connecting...")

                new_update_downloader(msg_content[1],msg_content[2])
                return 
            

        if msg[0:8]=='update_m':
            msg_content=[i for i in msg.split(';;')]
            if pop_up_update(2,msg_content[1],msg_content[2],bot_version)==1:

                root_e=Tk()

                root_e.after(6000,lambda:root_e.destroy())
                root_e.title("Info")
                label=Label(root_e,text="Download Will Be Started Soon. Kindly Do Not Close The Application",fg="#990000",bg="white").pack()
                root_e.mainloop()
                print("Connecting..")
                new_update_downloader(msg_content[1],msg_content[2])
            return




        if msg=='Expired':
            #print("Dear User Your Bot Has Expired .Please Recharge to continue The use.")
            #time.sleep(10)
            user_expired()
            return

        
        if keyboard.is_pressed("d"):
            server_arr[0]=0
            #client.send("disconnect".encode('utf-8'))
                            

def stoping_game(cmd_number):
    while True:
        time.sleep(0.3)
        if keyboard.is_pressed('d'):
            cmd_number[3]=0


if __name__=="__main__" :

    freeze_support()

    cmd_number =mp.Array('i',4)
    settings= mp.Array('d',15)
    server_arr=mp.Array('i',3)
    for k in range(len(server_arr)):
        server_arr[k]=0

    discord_key_arr=mp.Array('i',120)

    cmd_number[0]=0
    cmd_number[1]=0
    cmd_number[2]=0
    cmd_number[3]=1


    manager=Manager()

    #display_pannel()

    p1=mp.Process(target=windows_1920,args=(cmd_number,settings,server_arr,discord_key_arr))
    p2=mp.Process(target=discord_commander,args=(cmd_number,server_arr,discord_key_arr))
    p3=mp.Process(target=server_communication,args=(server_arr,discord_key_arr))
    p4=mp.Process(target=stoping_game,args=(cmd_number,))





    p1.start()
    p2.start()
    p3.start()
    p4.start()