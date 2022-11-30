import glob
import cv2 as cv
import pickle


calib_result_pickle = pickle.load(open("calibrate_camera.p", "rb" ))
mtx = calib_result_pickle["mtx"]
newcameramtx = calib_result_pickle["newcameramtx"]
dist = calib_result_pickle["dist"]
roi = calib_result_pickle["roi"]

folder_dir="images_test"
for iname in glob.glob(f'{folder_dir}/*.jpg'):
    try:
        img = cv.imread(iname)
        img = cv.undistort(img, mtx, dist, None, newcameramtx)
        img = img[74:120, 10:310]
        cv.imwrite(iname,img)
    except:
        print("ya une erreur wsh")
        
    