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
                for scale in np.linspace(0.9, 0.7, 10)[::-1]:
                    Sub_Image_1_Resized = imutils.resize(c8_888, width=int(c8_888.shape[1] * scale))
                    result_1 = cv.matchTemplate(area_2, Sub_Image_1_Resized, cv.TM_CCOEFF_NORMED)
                    check_1 = np.any(result_1 >= ratio_2)
                    Sub_Image_2_Resized = imutils.resize(c9_888, width=int(c9_888.shape[1] * scale))
                    result_2 = cv.matchTemplate(area_2, Sub_Image_2_Resized, cv.TM_CCOEFF_NORMED)
                    check_2 = np.any(result_2 >= ratio_2)
                    Sub_Image_3_Resized = imutils.resize(c10_888, width=int(c10_888.shape[1] * scale))
                    result_3 = cv.matchTemplate(area_2, Sub_Image_3_Resized, cv.TM_CCOEFF_NORMED)
                    check_3 = np.any(result_3 >= ratio_2)
                    Sub_Image_4_Resized = imutils.resize(sn7, width=int(sn7.shape[1] * scale))
                    result_4 = cv.matchTemplate(area_2, Sub_Image_4_Resized, cv.TM_CCOEFF_NORMED)
                    check_4 = np.any(result_4 >= ratio_3)

                    if (check_1==1 or check_2==1 or check_3==1) and check_4==0:
                        valid_cord=1
                        break




            elif y2 > 365 and y2 <= 635:
                for scale in np.linspace(1, 0.7, 10)[::-1]:
                    Sub_Image_1_Resized = imutils.resize(c8_888, width=int(c8_888.shape[1] * scale))
                    result_1 = cv.matchTemplate(area_2, Sub_Image_1_Resized, cv.TM_CCOEFF_NORMED)
                    check_1 = np.any(result_1 >= ratio_2)
                    Sub_Image_2_Resized = imutils.resize(c9_888, width=int(c9_888.shape[1] * scale))
                    result_2 = cv.matchTemplate(area_2, Sub_Image_2_Resized, cv.TM_CCOEFF_NORMED)
                    check_2 = np.any(result_2 >= ratio_2)
                    Sub_Image_3_Resized = imutils.resize(c10_888, width=int(c10_888.shape[1] * scale))
                    result_3 = cv.matchTemplate(area_2, Sub_Image_3_Resized, cv.TM_CCOEFF_NORMED)
                    check_3 = np.any(result_3 >= ratio_2)
                    Sub_Image_4_Resized = imutils.resize(sn7, width=int(sn7.shape[1] * scale))
                    result_4 = cv.matchTemplate(area_2, Sub_Image_4_Resized, cv.TM_CCOEFF_NORMED)
                    check_4 = np.any(result_4 >= ratio_3)

                    if (check_1==1 or check_2==1 or check_3==1) and check_4==0:
                        valid_cord=1
                        break

            
            elif y2 > 635:
                for scale in np.linspace(1.2, 0.8, 10)[::-1]:
                    Sub_Image_1_Resized = imutils.resize(c8_888, width=int(c8_888.shape[1] * scale))
                    result_1 = cv.matchTemplate(area_2, Sub_Image_1_Resized, cv.TM_CCOEFF_NORMED)
                    check_1 = np.any(result_1 >= ratio_2)
                    Sub_Image_2_Resized = imutils.resize(c9_888, width=int(c9_888.shape[1] * scale))
                    result_2 = cv.matchTemplate(area_2, Sub_Image_2_Resized, cv.TM_CCOEFF_NORMED)
                    check_2 = np.any(result_2 >= ratio_2)
                    Sub_Image_3_Resized = imutils.resize(c10_888, width=int(c10_888.shape[1] * scale))
                    result_3 = cv.matchTemplate(area_2, Sub_Image_3_Resized, cv.TM_CCOEFF_NORMED)
                    check_3 = np.any(result_3 >= ratio_2)
                    Sub_Image_4_Resized = imutils.resize(sn7, width=int(sn7.shape[1] * scale))
                    result_4 = cv.matchTemplate(area_2, Sub_Image_4_Resized, cv.TM_CCOEFF_NORMED)
                    check_4 = np.any(result_4 >= ratio_3)
                    if (check_1==1 or check_2==1 or check_3==1) and check_4==0:
                        valid_cord=1
                        break


            if valid_cord:
                pos_8 = [center_x, center_y]
                final_cords.append(pos_8)

        final_cords.sort()
        return final_cords

    except:
        return []



def one_screen_custome(search_region):

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
            
            valid_cord=0
            if y2 <= 365:
                for scale in np.linspace(0.9, 0.7, 10)[::-1]:
                    Sub_Image_1_Resized = imutils.resize(c8_888, width=int(c8_888.shape[1] * scale))
                    result_1 = cv.matchTemplate(area_2, Sub_Image_1_Resized, cv.TM_CCOEFF_NORMED)
                    check_1 = np.any(result_1 >= ratio_2)
                    Sub_Image_2_Resized = imutils.resize(c9_888, width=int(c9_888.shape[1] * scale))
                    result_2 = cv.matchTemplate(area_2, Sub_Image_2_Resized, cv.TM_CCOEFF_NORMED)
                    check_2 = np.any(result_2 >= ratio_2)
                    Sub_Image_3_Resized = imutils.resize(c10_888, width=int(c10_888.shape[1] * scale))
                    result_3 = cv.matchTemplate(area_2, Sub_Image_3_Resized, cv.TM_CCOEFF_NORMED)
                    check_3 = np.any(result_3 >= ratio_2)
                    Sub_Image_4_Resized = imutils.resize(sn7, width=int(sn7.shape[1] * scale))
                    result_4 = cv.matchTemplate(area_2, Sub_Image_4_Resized, cv.TM_CCOEFF_NORMED)
                    check_4 = np.any(result_4 >= ratio_3)

                    if (check_1==1 or check_2==1 or check_3==1) and check_4==0:
                        valid_cord=1
                        break




            elif y2 > 365 and y2 <= 635:
                for scale in np.linspace(1, 0.7, 10)[::-1]:
                    Sub_Image_1_Resized = imutils.resize(c8_888, width=int(c8_888.shape[1] * scale))
                    result_1 = cv.matchTemplate(area_2, Sub_Image_1_Resized, cv.TM_CCOEFF_NORMED)
                    check_1 = np.any(result_1 >= ratio_2)
                    Sub_Image_2_Resized = imutils.resize(c9_888, width=int(c9_888.shape[1] * scale))
                    result_2 = cv.matchTemplate(area_2, Sub_Image_2_Resized, cv.TM_CCOEFF_NORMED)
                    check_2 = np.any(result_2 >= ratio_2)
                    Sub_Image_3_Resized = imutils.resize(c10_888, width=int(c10_888.shape[1] * scale))
                    result_3 = cv.matchTemplate(area_2, Sub_Image_3_Resized, cv.TM_CCOEFF_NORMED)
                    check_3 = np.any(result_3 >= ratio_2)
                    Sub_Image_4_Resized = imutils.resize(sn7, width=int(sn7.shape[1] * scale))
                    result_4 = cv.matchTemplate(area_2, Sub_Image_4_Resized, cv.TM_CCOEFF_NORMED)
                    check_4 = np.any(result_4 >= ratio_3)

                    if (check_1==1 or check_2==1 or check_3==1) and check_4==0:
                        valid_cord=1
                        break

            
            elif y2 > 635:
                for scale in np.linspace(1.2, 0.8, 10)[::-1]:
                    Sub_Image_1_Resized = imutils.resize(c8_888, width=int(c8_888.shape[1] * scale))
                    result_1 = cv.matchTemplate(area_2, Sub_Image_1_Resized, cv.TM_CCOEFF_NORMED)
                    check_1 = np.any(result_1 >= ratio_2)
                    Sub_Image_2_Resized = imutils.resize(c9_888, width=int(c9_888.shape[1] * scale))
                    result_2 = cv.matchTemplate(area_2, Sub_Image_2_Resized, cv.TM_CCOEFF_NORMED)
                    check_2 = np.any(result_2 >= ratio_2)
                    Sub_Image_3_Resized = imutils.resize(c10_888, width=int(c10_888.shape[1] * scale))
                    result_3 = cv.matchTemplate(area_2, Sub_Image_3_Resized, cv.TM_CCOEFF_NORMED)
                    check_3 = np.any(result_3 >= ratio_2)
                    Sub_Image_4_Resized = imutils.resize(sn7, width=int(sn7.shape[1] * scale))
                    result_4 = cv.matchTemplate(area_2, Sub_Image_4_Resized, cv.TM_CCOEFF_NORMED)
                    check_4 = np.any(result_4 >= ratio_3)
                    if (check_1==1 or check_2==1 or check_3==1) and check_4==0:
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
            loc=final_cords[i]
            if click_checker(loc):
            
                mouseclick(loc[0],loc[1])
                time.sleep(0.4)
                img_after_click=imagesearch_numLoop_self(resource_path(dir+"image_after_click.png"),gola,precision=0.9,reg=(835,479,75,49))
                if img_after_click!=None:
                    pass_check(loc)
                    swift_attack()
                else:
                    py.click(button="right",clicks=1)
            if disturbance_checker_timer(time_between_clicks)==True:
                i=i-1
            i=i+1        
    except Exception as e:
        print(e)




def porter(cord,acc_porting,port_area):

    points=port_points_between(acc_porting,port_area)
    for i in range(len(points)):
        ported,success=port_between(points[i])
        if ported==True and success:
            #time.sleep(1)
            return True
        if ported and success == False:
            return False
        disturbance_checker_timer_global(time_between_clicks)
    return False

def port_points_between(acc_porting,port_area):

    dir_loca=dir+'/'+season+'/'
    
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
    port_points=findClickPositions(needle_img2,haystack_img1,acc_porting[2],eps_val=0.7)

    port_points+=findClickPositions(needle_img3,haystack_img1,acc_porting[1],eps_val=0.7)
    port_points+=findClickPositions(needle_img4,haystack_img1,acc_porting[3],eps_val=0.7)
    port_points+=findClickPositions(needle_img5,haystack_img1,acc_porting[4],eps_val=0.7)

    port_points =sorted(port_points, key = lambda sub: abs((sub[1] - sub[0])-300))
    port_points=random.sample(port_points, k=len(port_points))

    return port_points

def port_between(loc,port_area):
    dir_loca=dir+'/'+season+'/'
    py.click(loc[0]+port_area[0],loc[1]+port_area[1])
    time.sleep(tweaker*0.1-0.4)
    port_screen=imagesearch_numLoop_self(resource_path(dir+"port_screen.png"),3,precision=0.6,reg=(863,647,185,48))
    if port_screen==None:
        py.click(button="right",clicks=1)
        time.sleep(0.7)
        return False,False

    time.sleep(delay)
    py.click(955,668)
    pos=imagesearch_numLoop_self(resource_path(dir+"confirm_port.png"),8,precision=0.6,reg=(737,663,200,60))
    if pos==None:
        pos=imagesearch_numLoop_self(resource_path(dir+"cant_teleport.png"),0,precision=0.8,reg=(839,275,234,46))
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



def box_limitation(x):

    if x<0:
        return 0

    elif x<143:
        return 143

    elif x>1796:
        return 179

    elif x>879:
        return 879

    return x

    


def area_calculator(camp_cord):
    x=camp_cord[0]
    y=camp_cord[1]

    x1=box_limitation(x-115)
    y1=box_limitation(y-71)
    x2=box_limitation(x1+142)
    y2=box_limitation(y1+93)

    return (x1,y1,x2-x1,y2-y1)



def beside_port(cords_camps):
    f=False
    tot_no=len(cords_camps)
    for i in range(tot_no):
        area= area_calculator(cords_camps[i])
        if porter(area)==False:
            continue
        else:
            f=True
            break

    return f

def camp_cleaner():

    while True:
        cords_camps=one_screen()
        if len(cords_camps)>0:
            if beside_port(cords_camps):
                check_area=[762, 362, 398, 362]
                one_screen_custom(check_area)
                wait()
                cords_camps=one_screen()
            else:
                break

        else:
            break



while True:
    location_opener()
    time.sleep(wait_val)
    camp_cleaner()
    #wait()



#### task to be in little component working stage by end of the day.
