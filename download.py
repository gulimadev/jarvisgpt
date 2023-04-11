import threading
from pytube import YouTube
from moviepy.editor import *
from main import Main

class Download:
    def download_and_convert_video(self):
            url = input("Digite a URL do vídeo ou digite 'sair' para sair:")
            
            downloader_thread = threading.Thread(target=d.download_and_convert_video, args=())
            downloader_thread.start()
            if url == "sair":
                os.system("explorer.exe .")
                exit()
            # Download do vídeo
            m = Main()
            yt = YouTube(url)
            video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
            video.download()
            # Conversão para mp3
            video_file = video.default_filename
            video_clip = VideoFileClip(video_file)
            audio_clip = video_clip.audio
            audio_clip.write_audiofile(f"{yt.title}.mp3")
            audio_clip.close()
            video_clip.close()

            print(f"Download e conversão da {yt.title} concluídos com sucesso.")
            m.voz_reprodutor(f"Download e conversão da {yt.title} concluídos com sucesso.")

            # Exemplo de uso
            # download_thread = threading.Thread(target=download_and_convert_video, args=(url,))
            # download_thread.start()

            # # Continua a execução do programa principal
            # print("A aplicação principal continua executando...")
            
            
if __name__ == "__main__":
    d = Download()
    d.download_and_convert_video()