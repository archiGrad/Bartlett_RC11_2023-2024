from pathlib import Path
from pytube import YouTube
import cv2 
import os


imagepath = Path("./images")
imagepath.mkdir(exist_ok=True)

url ="https://www.youtube.com/watch?v=HK6y8DAPN_0"

yt = YouTube(url)
video = yt.streams.get_by_itag(137)
video.download()


frame_no = 0


cap = cv2.VideoCapture("Introducing Sora — OpenAI’s text-to-video model.mp4")
while (cap.isOpened()):
	ret, frame = cap.read()
	if(frame_no % 10 == 0):
		name =  f"frame_{frame_no}.jpg"
		target = os.path.join(imagepath,name)
		cv2.imwrite(target, frame)
	frame_no +=1		
	
