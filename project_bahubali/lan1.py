import cv2
import numpy as np
import lane_detection4
#from motor import motors,motors2


curveList = []
avgVal = 10


def getLaneCurve(img,display):
    imgCopy = img.copy()
    imgResult = img.copy()
    #### STEP 1
    imgThres =  lane_detection4.thresholding(img)

    #### STEP 2
    hT, wT, c = img.shape
    points = lane_detection4.valTrackbars()
    imgWarp = lane_detection4.warpImg(imgThres, points, wT, hT)
    imgWarpPoints = lane_detection4.drawPoints(imgCopy, points)
    cv2.imshow('im2',imgWarpPoints)

    #### STEP 3
    middlePoint, imgHist = lane_detection4.getHistogram(imgWarp, display=True, minPer=0.5, region=2)
    curveAveragePoint, imgHist = lane_detection4.getHistogram(imgWarp, display=True, minPer=1)
    curveRaw = curveAveragePoint - middlePoint

    #### SETP 4
    curveList.append(curveRaw)
    if len(curveList) > avgVal:
        curveList.pop(0)
    curve = int(sum(curveList) / len(curveList))

    #### STEP 5
    if display != 0:
        imgInvWarp = lane_detection4.warpImg(imgWarp, points, wT, hT, inv=True)
        imgInvWarp = cv2.cvtColor(imgInvWarp, cv2.COLOR_BGR2RGB)
        imgInvWarp[0:hT // 3, 0:wT] = 0, 0, 0
        imgLaneColor = np.zeros_like(img)
        imgLaneColor[:] = 0, 255, 0
        imgLaneColor = cv2.bitwise_and(imgInvWarp, imgLaneColor)
        imgResult = cv2.addWeighted(imgResult, 1, imgLaneColor, 1, 0)
        midY = 450
        cv2.putText(imgResult, str(curve), (wT // 2 - 80, 85), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 0, 255), 3)

        a=cv2.line(imgResult, (wT // 2, midY), (wT // 2 + (curve * 3), midY), (255, 0, 255), 5)


        cv2.line(imgResult, ((wT // 2 + (curve * 3)), midY - 25), (wT // 2 + (curve * 3), midY + 25), (0, 255, 0), 5)
        for x in range(-30, 30):
            w = wT // 20
            cv2.line(imgResult, (w * x + int(curve // 50), midY - 10),
                     (w * x + int(curve // 50), midY + 10), (0, 0, 255), 2)
        # fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);
        # cv2.putText(imgResult, 'FPS ' + str(int(fps)), (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (230, 50, 50), 3);
    if display == 2:
        imgStacked = lane_detection4.stackImages(0.7, ([img, imgWarpPoints, imgWarp],[imgHist, imgLaneColor, imgResult]))
        cv2.imshow('ImageStack', imgStacked)

    elif display == 1:
        cv2.imshow('Resutlt', imgResult)

    #### NORMALIZATION
    curve = curve / 100
    #print(curve)
    if curve > 1: curve == 1
    if curve < -1: curve == -1

    return curve


if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    intialTrackBarVals = [102, 80, 20, 214]
    lane_detection4.initializeTrackbars(intialTrackBarVals)
    frameCounter = 0
    #LSM = motors(2, 3, 4)
    #RSM = motors2(17, 27, 22)
    while True:
        '''frameCounter += 1
        if cap.get(cv2.CAP_PROP_FRAME_COUNT) == frameCounter:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            frameCounter = 0'''

        success, img = cap.read()
        img = cv2.resize(img, (480, 240))
        curve = getLaneCurve(img, display=1)
        #print(curve)
        #curve=int(curve)
        #print(curve)
        '''if curve==0.0:


            LSM.moveF(50)

            RSM.moveF(50)
        elif curve>0.0:
            while curve != 0.0:
                RSM.stop()
                LSM.left(50)
                RSM.right(30)
        elif curve<0.0:
            while curve!=0.0:
                LSM.stop()

                LSM.left(30)
                RSM.right(50)


        # cv2.imshow('Vid',img)'''
        cv2.waitKey(1)
