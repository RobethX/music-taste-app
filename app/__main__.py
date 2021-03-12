import json
import sqlite3

import config
#import db

#from . import db

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials #SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=config.SPOTIFY_CLIENT_ID, client_secret=config.SPOTIFY_CLIENT_SECRET))

def get_tracks():
	print("test")

def get_track_id(q):
	"""Find a song's Spotify ID"""
	results = sp.search(q=q)
	id = results["tracks"]["items"][0]["id"]
	name = results["tracks"]["items"][0]["name"] # for convenience
	artist = results["tracks"]["items"][0]["artists"][0]["name"] # for convenience
	return id, name, artist

def get_track_data(track_id):
	features = sp.audio_features(tracks=[track_id]) #TODO: features is redundant with analysis
	print(features)
	analysis = sp.audio_analysis(track_id)
	print(analysis)
	return features, analysis

def main():
	"""Main function"""
	#db.get_db()
	#con = sqlite3.connect("app.sqlite")

	#get_tracks()
	#track_id, track_name, track_artist = get_track_id("No Bullets Spent")
	#print(f"{track_id}, {track_name}, {track_artist}")
	
	#track_features, track_analysis = get_track_data(track_id)

	#cur = con.cursor()
	#cur.execute(f"INSERT OR IGNORE INTO 'main'.'tracks'('spotify_id','name','artist','features','analysis') VALUES ('{track_id}','{track_name}','{track_artist}','{json.dumps(track_features)}','{json.dumps(track_analysis)}');") # TODO: ignore or replace?
	#con.commit()

	#con.close()
	#db.close_db()

	analysis = sp.audio_analysis("4FQeCXqlUcXRVvOF8K19LD")

	t = []
	loudness = []
	tempo = []

	for s in analysis["sections"]:
		t.append(s["start"])
		loudness.append(s["loudness"])
		tempo.append(s["tempo"])

	import matplotlib.pyplot as plt
	fig = plt.figure()
	ax = fig.add_subplot(111)
	ax.plot(t, loudness, "-ro", label="loudness")
	#ax.plot(t, tempo, "-bo", label="tempo")
	plt.legend(loc="upper left")
	plt.show()

if __name__ == "__main__":
	main()