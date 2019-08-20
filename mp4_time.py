import ffmpeg._probe as fp
import ffmpeg
import os

def ffmpeg_time(file_path):
    dic = ffmpeg.probe(file_path)
    # vedio in second
    vedio_t_sec = float(dic['format']['duration'])
    # vedio in minute
    vedio_t_min = round(vedio_t_sec/60, 2)
    return vedio_t_min

if __name__ == '__main__':
    time_list = []
    time = 0
    dir_path_list = ['/media/mi/FAD8-7542/计算机网络北大']
    for d in dir_path_list:
        for i in os.listdir(d):
            time += ffmpeg_time(os.path.join(d, i))
        time_list.append(time/45)
        time = 0
    print(time_list)
    print(sum(time_list)/2)
