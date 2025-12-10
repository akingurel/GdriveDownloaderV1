import sys
import subprocess
import os
import time

def install_yt_dlp():
    """Checks if yt-dlp is installed, if not, installs it via pip."""
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

# Ensure yt-dlp is installed before importing or main execution
install_yt_dlp()
import yt_dlp

def main():
    # Interaction: Clear the console
    os.system('cls' if os.name == 'nt' else 'clear')

    # Print welcome message
    print("##########################################################")
    print("#      Google Drive Yalnızca Görüntülenen Video İndirici #")
    print("##########################################################")
    print("")
    
    # FFmpeg warning
    print("[!] ÖNEMLİ: 1080p+ kalitesinde birleştirme için FFmpeg")
    print("    sisteminizde yüklü ve PATH'e eklenmiş olmalıdır.")
    print("    Eğer yoksa, en iyi tek dosya kalitesi indirilecektir.")
    print("")

    # Interaction: Ask for URL
    url = input("Lütfen Google Drive Video Bağlantısını yapıştırın: ").strip()

    if not url:
        print("Hata: Bağlantı girilmedi.")
        return

    # User-Agent Spoofing (Windows 10 Chrome)
    # This mimics a standard browser to bypass some restrictions on view-only files
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'

    # Configuration for yt-dlp
    ydl_opts = {
        # Best Quality (FFmpeg): format settings
        'format': 'bestvideo+bestaudio/best',
        
        # File Naming: use video title
        'outtmpl': '%(title)s.%(ext)s',
        
        # User-Agent Spoofing
        'user_agent': user_agent,
        
        # Ensure we don't try to download a playlist if the link is weird
        'noplaylist': True,
        
        # Progress bar is enabled by default in yt-dlp standard output
    }

    print("\nİndirme uyumluluk kontrolü yapılıyor...\n")

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # The download method handles the progress bar and output
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
