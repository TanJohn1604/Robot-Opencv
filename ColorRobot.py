import time

import cv2
import serial
from threading import Thread
from time import  sleep

print(cv2.__version__)
import numpy as np

def send(a):
    global flag
    #code begin
    #init $090 120 100 100
    #     base nang z  kep

    #quay base ve 180
    sendData(ser, [180,120, 100, 100], 3)
    time.sleep(3)
    #ha truc nang 160
    sendData(ser, [180, 160, 100, 100], 3)
    time.sleep(3)
    #kep 127
    sendData(ser, [180, 160, 100, 129], 3)
    time.sleep(2)
    #nang truc nang 120
    sendData(ser, [180, 120, 100, 129], 3)
    time.sleep(3)
    #quay ve goc des 0 tuy mau-------
    sendData(ser, [a, 120, 100, 129], 3)
    time.sleep(4)
    #ha goc nang 160
    sendData(ser, [a, 160, 100, 129], 3)
    time.sleep(3)
    #nha kep 100
    sendData(ser, [a, 160, 100, 100], 3)
    time.sleep(2)
    # nang goc nang
    sendData(ser, [a, 120, 100, 100], 3)
    time.sleep(3)
    # quay base ve home
    sendData(ser, [90, 120, 100, 100], 3)
    time.sleep(3)

    flag=0

def initConnection(port,baud):
    try:
        ser=serial.Serial(port,baud)
        print("Device connected")
        return ser
    except:
        print("Errorrrrrrr")
def sendData(se,data,digits):
    myString="$"
    for d in data:
        myString+= str(d).zfill(digits)
    try:
        se.write(myString.encode())
        print(myString)
    except:
        print("send fail")

def nothing(x):
    pass


# cv2.namedWindow('Trackbars')
# cv2.moveWindow('Trackbars', 640*2, 0)
#
# cv2.createTrackbar('hueLower', 'Trackbars', 50, 179, nothing)
# cv2.createTrackbar('hueUpper', 'Trackbars', 100, 179, nothing)
#
# cv2.createTrackbar('hue2Lower', 'Trackbars', 50, 179, nothing)
# cv2.createTrackbar('hue2Upper', 'Trackbars', 100, 179, nothing)
#
# cv2.createTrackbar('satLow', 'Trackbars', 100, 255, nothing)
# cv2.createTrackbar('satHigh', 'Trackbars', 255, 255, nothing)
# cv2.createTrackbar('valLow', 'Trackbars', 100, 255, nothing)
# cv2.createTrackbar('valHigh', 'Trackbars', 255, 255, nothing)

width = 640
height = 480
flip = 2

flag=0
rcnt=0
bcnt=0
ycnt=0

cam = cv2.VideoCapture(1)
ser=initConnection("COM7",9600)
sendData(ser, [90,120, 100, 100], 3)
# Or, if you have a WEB cam, uncomment the next line
# (If it does not work, try setting to '1' instead of '0')
# cam=cv2.VideoCapture(0)
while True:
    ret, frame = cam.read()



    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # hueLow = cv2.getTrackbarPos('hueLower', 'Trackbars')
    # hueUp = cv2.getTrackbarPos('hueUpper', 'Trackbars')
    #
    # hue2Low = cv2.getTrackbarPos('hue2Lower', 'Trackbars')
    # hue2Up = cv2.getTrackbarPos('hue2Upper', 'Trackbars')
    #
    # Ls = cv2.getTrackbarPos('satLow', 'Trackbars')
    # Us = cv2.getTrackbarPos('satHigh', 'Trackbars')
    #
    # Lv = cv2.getTrackbarPos('valLow', 'Trackbars')
    # Uv = cv2.getTrackbarPos('valHigh', 'Trackbars')

    # l_b = np.array([hueLow, Ls, Lv])
    # u_b = np.array([hueUp, Us, Uv])
    #
    # l_b2 = np.array([hue2Low, Ls, Lv])
    # u_b2 = np.array([hue2Up, Us, Uv])
    #
    # FGmask = cv2.inRange(hsv, l_b, u_b)
    # FGmask2 = cv2.inRange(hsv, l_b2, u_b2)
    # FGmaskComp = cv2.add(FGmask, FGmask2)

    #-------------------------red------------------------------
    rl_b = np.array([0, 83, 84])
    ru_b = np.array([14, 197, 233])

    rl_b2 = np.array([127, 83, 84])
    ru_b2 = np.array([179, 197, 233])

    RFGmask = cv2.inRange(hsv, rl_b, ru_b)
    RFGmask2 = cv2.inRange(hsv, rl_b2, ru_b2)
    RFGmaskComp = cv2.add(RFGmask, RFGmask2)

    # -------------------------yellow------------------------------
    yl_b = np.array([19, 134, 64])
    yu_b = np.array([43, 255, 255])

    yl_b2 = np.array([19, 134, 64])
    yu_b2 = np.array([43, 255, 255])

    YFGmask = cv2.inRange(hsv, yl_b, yu_b)
    YFGmask2 = cv2.inRange(hsv, yl_b2, yu_b2)
    YFGmaskComp = cv2.add(YFGmask, YFGmask2)

    # -------------------------blue------------------------------
    bl_b = np.array([37, 69, 28])
    bu_b = np.array([113, 224, 249])

    bl_b2 = np.array([37, 69, 28])
    bu_b2 = np.array([113, 224, 249])

    BFGmask = cv2.inRange(hsv, bl_b, bu_b)
    BFGmask2 = cv2.inRange(hsv, bl_b2, bu_b2)
    BFGmaskComp = cv2.add(BFGmask, BFGmask2)


    # cv2.imshow('RFGmaskComp', RFGmaskComp)
    # cv2.moveWindow('RFGmaskComp', 640, 0)

    # FG = cv2.bitwise_and(frame, frame, mask=FGmaskComp)
    # # cv2.imshow('FG', FG)
    # # cv2.moveWindow('FG', 700, 0)
    # #
    # bgMask = cv2.bitwise_not(FGmaskComp)
    # # cv2.imshow('bgMask', bgMask)
    # # cv2.moveWindow('bgMask', 700, 530)
    # #
    # BG = cv2.cvtColor(bgMask, cv2.COLOR_GRAY2BGR)
    # final = cv2.add(FG, BG)

    # -------------------------red------------------------------
    Rcontours, _ = cv2.findContours(RFGmaskComp, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    Rcontours = sorted(Rcontours, key=lambda x: cv2.contourArea(x), reverse=True)
    # -------------------------yellow------------------------------
    Ycontours, _ = cv2.findContours(YFGmaskComp, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    Ycontours = sorted(Ycontours, key=lambda x: cv2.contourArea(x), reverse=True)
    # -------------------------blue------------------------------
    Bcontours, _ = cv2.findContours(BFGmaskComp, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    Bcontours = sorted(Bcontours, key=lambda x: cv2.contourArea(x), reverse=True)





    # -------------------------red-------------------------------
    if Rcontours:
        rarea = cv2.contourArea(Rcontours[0])
        (rx, ry, rw, rh) = cv2.boundingRect(Rcontours[0])
        if rarea >= 100:
            # cv2.drawContours(frame,[cnt],0,(255,0,0),3)
            if flag==0:
                cv2.rectangle(frame, (rx, ry), (rx + rw, ry + rh), (0, 0, 255), 3)
                cv2.circle(frame, (int( rx+rw/2), int(ry+rh/2)), 3, (0, 255, 0), 2, 1)
                cv2.circle(frame, (int(rx + rw / 2), int(ry + rh / 2)), 1, (0, 255, 0), 2, 1)
        rerrorx = int(rx+rw/2 - int(width / 2))
        rerrory= int(ry+rh/2 -int(height/2))
        if (abs(rerrorx) <15) and (abs(rerrory) <15):
            if flag==0:
                rcnt=rcnt+1
                cv2.putText(frame, "red :" + str(rcnt) + "%", (340, 40), cv2.FONT_HERSHEY_PLAIN, 3,
                            (0, 0, 255), 2)
                if(rcnt>100):
                    rcnt=0
                    flag = 1
                    thread = Thread(target=send, args=(0,))
                    thread.start()
        else:
            rcnt=0
    # -------------------------yellow----------------------------
    if Ycontours:
        yarea = cv2.contourArea(Ycontours[0])
        (yx, yy, yw, yh) = cv2.boundingRect(Ycontours[0])
        if yarea >= 100:
            # cv2.drawContours(frame,[cnt],0,(255,0,0),3)
            if flag==0:
                cv2.rectangle(frame, (yx, yy), (yx + yw, yy + yh), (0, 255, 255), 3)
                cv2.circle(frame, (int( yx+yw/2), int(yy+yh/2)), 3, (0, 255, 0), 2, 1)
                cv2.circle(frame, (int(yx + yw / 2), int(yy + yh / 2)), 1, (0, 255, 0), 2, 1)
        yerrorx = int(yx+yw/2 - int(width / 2))
        yerrory= int(yy+yh/2 -int(height/2))
        if (abs(yerrorx) <15) and (abs(yerrory) <15):
            if flag == 0:
                ycnt = ycnt + 1
                cv2.putText(frame, "yellow :" + str(ycnt) + "%", (340, 40), cv2.FONT_HERSHEY_PLAIN, 3,
                            (0, 255, 255), 2)
                if (ycnt > 100):
                    ycnt = 0
                    flag = 2
                    thread = Thread(target=send, args=(25,))
                    thread.start()
            else:
                ycnt = 0
    # -------------------------blue------------------------------
    if Bcontours:
        barea = cv2.contourArea(Bcontours[0])
        (bx, by, bw, bh) = cv2.boundingRect(Bcontours[0])
        if barea >= 100:
            # cv2.drawContours(frame,[cnt],0,(255,0,0),3)
            if flag==0:
                cv2.rectangle(frame, (bx, by), (bx + bw, by + bh), (255, 0, 0), 3)
                cv2.circle(frame, (int( bx+bw/2), int(by+bh/2)), 3, (0, 255, 0), 2, 1)
                cv2.circle(frame, (int(bx + bw / 2), int(by + bh / 2)), 1, (0, 255, 0), 2, 1)
        berrorx = int(bx+bw/2 - int(width / 2))
        berrory= int(by+bh/2 -int(height/2))
        if (abs(berrorx) <15) and (abs(berrory) <15):
            if flag == 0:
                bcnt = bcnt + 1
                cv2.putText(frame, "blue :" + str(bcnt) + "%", (340, 40), cv2.FONT_HERSHEY_PLAIN, 3,
                            (255, 0, 0), 2)
                if (bcnt > 100):
                    bcnt = 0
                    flag = 3
                    thread = Thread(target=send, args=(50,))
                    thread.start()
            else:
                bcnt = 0


    if flag==1:
        cv2.putText(frame, "Dang gap vat do", (2, 40), cv2.FONT_HERSHEY_PLAIN, 3,
                    (0, 0, 255), 2)
    if flag==2:
        cv2.putText(frame, "Dang gap vat vang", (2, 40), cv2.FONT_HERSHEY_PLAIN, 3,
                    (0, 255, 255), 2)
    if flag==3:
        cv2.putText(frame, "Dang gap vat xanh duong", (2, 40), cv2.FONT_HERSHEY_PLAIN, 3,
                    (255, 0, 0), 2)
    if flag == 0:
        cv2.putText(frame, "Chuan bi gap: ", (0, 40), cv2.FONT_HERSHEY_PLAIN, 3,
                    (0, 150, 0), 2)

    cv2.line(frame, (int(width / 2)-15, int(height / 2)), (int(width/2)+15, int(height / 2)), (0, 0, 0), 2, 1)
    cv2.line(frame, (int(width / 2), int(height / 2)-15), (int(width / 2), int(height/2)+15), (0, 0, 0), 2, 1)
    cv2.circle(frame, (int(width / 2), int(height / 2)), 15, (0, 0, 0), 2, 1)

    cv2.imshow('nanoCam', frame)
    cv2.moveWindow('nanoCam', 0, 0)
    if cv2.waitKey(1) == ord('q'):
        break

    # sendData(ser, [1, 255, 152], 3)
cam.release()
cv2.destroyAllWindows()