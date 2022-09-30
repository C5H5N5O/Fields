import pafy
import vlc

url = "https://https://www.youtube.com/watch?v=f1y2Gb7Ori8&list=RDGMEMJQXQAmqrnmK1SEjY_rKBGAVMf1y2Gb7Ori8&start_radio=1&ab_channel=RammsteinOfficial"
video = pafy.new(url)
best = video.getbest()
playurl = best.url

Instance = vlc.Instance()
player = Instance.media_player_new()
Media = Instance.media_new(playurl)
Media.get_mrl()
player.set_media(Media)
player.play()