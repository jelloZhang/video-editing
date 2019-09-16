import os

class Video():

	def __init__(self,start_time,end_time,from_name,name):
		self.start_time = start_time
		self.end_time = end_time
		self.from_name = from_name
		self.name = name
		self.command_string = "ffmpeg -ss " + self.start_time + " -to " + self.end_time + " -accurate_seek -i " + from_name + " -codec copy " + name 

	def cut_video(self):
		 # print(self.command_string)
		os.system(self.command_string)  	


def cut_many_videos():
	video_mushroomGirl = {
		'start_time': '00:31:40',
		'end_time': '00:39:25',
		'from_name': '/home/jello/Videos/child01.mp4',
		'name': '/home/jello/Videos/mushroomGirl.mp4',
		}
	video_shoeMaker = {
		'start_time':'00:39:55',
		'end_time': '00:45:15',
		'from_name': '/home/jello/Videos/child01.mp4',
		'name': '/home/jello/Videos/shoeMaker.mp4',
		}
	
	videos = [video_mushroomGirl, video_shoeMaker]

	for video in videos:
		eachVideo = Video(video['start_time'],
				video['end_time'],
				video['from_name'],
				video['name'])
		
		eachVideo.cut_video()

cut_many_videos()
