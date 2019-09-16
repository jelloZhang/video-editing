import os
import pymysql

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
	
def get_videosInfo_fromDB():
	db = pymysql.connect("localhost","jello","Jello@123","db_Videos")
	cursor = db.cursor()
	sql = "select * from videos_explanation"
	try:
		cursor.execute(sql)
		results = cursor.fetchall()
		print("number of single videos: ",len(results))
	except:
		print("Error: unable to fetch data")
	return results
	
def cut_many_videos():
	videos = []
	results = get_videosInfo_fromDB()
	for row in results:
		new_video = Video(row[1],row[2],row[3],row[4])
		videos.append(new_video)
	
	for video in videos:
		video.cut_video()
def concat_many_videos(videos):
	
cut_many_videos()
