from pathlib import Path
from pytube import YouTube
import cv2 
import os


imagepath = Path("./images") 
imagepath.mkdir(exist_ok=True) #check if "./images" exist. if not, make this directory.


# download the sora youtube video
url ="https://www.youtube.com/watch?v=U2Qp5pL3ovA"

yt = YouTube(url) #store the youtube object with url as input.


video = yt.streams.get_by_itag(160)
video.download()

frame_no = 0

cap = cv2.VideoCapture("Dune Part Two  Official Trailer 3.mp4")
while (cap.isOpened()):
	ret, frame = cap.read()
	if(frame_no % 1 == 0):
		name =  f"frame_{frame_no}.jpg"
		target = os.path.join(imagepath,name)
		cv2.imwrite(target, frame)
	frame_no +=1	
