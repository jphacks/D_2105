from moviepy.editor import *
import cv2, wave

def get_music_length(music_frames):
    """
    音楽の長さが何秒かを浮動小数で返す関数

    Parameter
    ---------
    music_frames : int
        フレームレート数

    Return
    ------
    1.0 * music_frames / SAMPLING_RATE : float
        音楽の長さ(秒)
    """
    SAMPLING_RATE = 44100

    return 1.0 * music_frames / SAMPLING_RATE

if __name__ == '__main__':
    MOVIE_PATH = '../movie/'

    # 背景画像を取得
    BASE_IMG_PATH = './common_images/cake.PNG'
    base_img = cv2.imread(BASE_IMG_PATH)
    base_img = cv2.cvtColor(base_img, cv2.COLOR_BGR2RGB)
    height = base_img.shape[0]
    width = base_img.shape[1]

    # 音楽を取得
    with wave.open(MOVIE_PATH + 'sample.wav', 'r') as music:
        length = get_music_length(music.getnframes())

    # スライドショーを作る元となる静止画情報を格納する処理
    clips = []
    clip = ImageClip(base_img).set_duration(length)
    clip = clip.resize(newsize=(width, height))
    clips.append(clip)

    # スライドショーの動画像を作成する処理
    concat_clip = concatenate_videoclips(clips, method="compose")
    concat_clip.write_videofile(MOVIE_PATH + 'output.mp4', fps=30)
