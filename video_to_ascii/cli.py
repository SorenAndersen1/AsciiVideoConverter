"""This module contains a CLI interface"""

from video_to_ascii import player

def main():
    filename = "C:/Users/Soren/PycharmProjects/SideProjects/asciiVideo/ascii-to-video-vid.mp4"
    ##

    try:
        player.play(filename, strategy=None, output=None, play_audio=False)
    except (KeyboardInterrupt):
        pass

if __name__ == '__main__':
    main()
