import sys
import subprocess
import os
import time

def install_yt_dlp():
    try:
        import yt_dlp
    except ImportError:
        print("yt-dlp kütüphanesi bulunamadı. Otomatik olarak yükleniyor...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "yt-dlp"])
            print("yt-dlp başarıyla yüklendi.")
            import yt_dlp
        except Exception as e:
            print(f"yt-dlp yüklenemedi: {e}")
            print("Lütfen şu komutu deneyin: pip install yt-dlp")
            sys.exit(1)

install_yt_dlp()
import yt_dlp

def main():
    os.system('cls' if os.name == 'nt' else 'clear')

    print("##########################################################")
    print("#      Google Drive Yalnızca Görüntülenen Video İndirici #")
    print("##########################################################")
    print("")
    
    print("[!] ÖNEMLİ: 1080p+ kalitesinde birleştirme için FFmpeg")
    print("    sisteminizde yüklü ve PATH'e eklenmiş olmalıdır.")
    print("    Eğer yoksa, en iyi tek dosya kalitesi indirilecektir.")
    print("")

    url = input("Lütfen Google Drive Video Bağlantısını yapıştırın: ").strip()

    if not url:
        print("Hata: Bağlantı girilmedi.")
        return

    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'

    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'user_agent': user_agent,
        'noplaylist': True,
    }

    print("\nİndirme uyumluluk kontrolü yapılıyor...\n")

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        print("\n[BAŞARILI] Video başarıyla indirildi.")
        
    except yt_dlp.utils.DownloadError as e:
        print("\n[HATA] İndirme başarısız oldu. Olası nedenler:")
        print(" - Bağlantı geçersiz veya süresi dolmuş.")
        print(" - İzin hatası (ancak bu script herkese açık linkleri destekler).")
        print(f" - Teknik detay: {e}")
    except Exception as e:
        print(f"\n[HATA] Beklenmedik bir hata oluştu: {e}")

    print("\nÇıkmak için Enter tuşuna basın...")
    input()

if __name__ == "__main__":
    main()
