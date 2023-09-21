from django.shortcuts import render
from rest_framework.response import Response    
# Create your views here.
import cv2
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import  HttpResponse



@csrf_exempt
def index(requests):
    if requests.method == "POST":
        
        print(requests.POST)
        return HttpResponse("Yoo")
        
    # video = cv2.VideoCapture(1)
    # while True:
    #     ret, frame = video.read()
    #     gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #     cv2.imshow("Attendence Frame", gray_frame)
    #     k = cv2.waitKey(1)
    #     if k == ord('q'):
    #         break

    # video.release()
    # cv2.destroyAllWindows()
    # print("done")