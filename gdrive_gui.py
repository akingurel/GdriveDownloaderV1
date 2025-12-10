import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox, filedialog
import yt_dlp
import threading
import os
import json
import sys
from datetime import datetime

APP_NAME = "Google Drive İndirici"
WIDTH = 700
HEIGHT = 600
HISTORY_FILE = "history.json"

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class GDriveDownloaderApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title(APP_NAME)
        self.geometry(f"{WIDTH}x{HEIGHT}")
        self.resizable(False, False)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(3, weight=1)

        self.download_folder = os.getcwd()
        self.history = self.load_history()

        self.create_widgets()

    def create_widgets(self):
        self.header_frame = ctk.CTkFrame(self, corner_radius=0)
        self.header_frame.grid(row=0, column=0, sticky="ew")
        
        self.header_label = ctk.CTkLabel(self.header_frame, text="Google Drive Video İndirici", font=ctk.CTkFont(size=20, weight="bold"))
        self.header_label.pack(pady=10)

        self.input_frame = ctk.CTkFrame(self)
        self.input_frame.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

        self.url_label = ctk.CTkLabel(self.input_frame, text="Video URL:")
        self.url_label.grid(row=0, column=0, padx=10, pady=10)

        self.url_entry = ctk.CTkEntry(self.input_frame, placeholder_text="Google Drive bağlantısını buraya yapıştırın...", width=400)
        self.url_entry.grid(row=0, column=1, padx=10, pady=10)

        self.paste_btn = ctk.CTkButton(self.input_frame, text="Yapıştır", width=80, command=self.paste_url)
        self.paste_btn.grid(row=0, column=2, padx=10, pady=10)

        self.action_frame = ctk.CTkFrame(self)
        self.action_frame.grid(row=2, column=0, padx=20, pady=10, sticky="ew")

        self.folder_label = ctk.CTkLabel(self.action_frame, text=f"Konum: {self.truncate_text(self.download_folder, 30)}")
        self.folder_label.grid(row=0, column=0, padx=20, pady=10, sticky="w")

        self.browse_btn = ctk.CTkButton(self.action_frame, text="Gözat", width=80, command=self.browse_folder)
        self.browse_btn.grid(row=0, column=1, padx=10, pady=10)

        self.download_btn = ctk.CTkButton(self.action_frame, text="İNDİR BAŞLAT", font=ctk.CTkFont(size=14, weight="bold"), command=self.start_download_thread, fg_color="#2CC985", hover_color="#229965")
        self.download_btn.grid(row=1, column=0, columnspan=3, padx=20, pady=(10, 20), sticky="ew")

        self.progress_bar = ctk.CTkProgressBar(self.action_frame)
        self.progress_bar.grid(row=2, column=0, columnspan=3, padx=20, pady=(0, 10), sticky="ew")
        self.progress_bar.set(0)

        self.status_label = ctk.CTkLabel(self.action_frame, text="Hazır", text_color="gray")
        self.status_label.grid(row=3, column=0, columnspan=3, pady=(0, 10))

        self.history_frame = ctk.CTkFrame(self)
        self.history_frame.grid(row=3, column=0, padx=20, pady=10, sticky="nsew")
        self.history_frame.grid_columnconfigure(0, weight=1)
        self.history_frame.grid_rowconfigure(1, weight=1)

        ctk.CTkLabel(self.history_frame, text="İndirme Geçmişi", anchor="w").grid(row=0, column=0, padx=10, pady=5, sticky="ew")

        self.history_list = ctk.CTkTextbox(self.history_frame, activate_scrollbars=True)
        self.history_list.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")
        self.history_list.configure(state="disabled")

        self.update_history_view()

    def paste_url(self):
        try:
            self.url_entry.delete(0, 'end')
            self.url_entry.insert(0, self.clipboard_get())
        except:
            pass

    def browse_folder(self):
        folder = filedialog.askdirectory(initialdir=self.download_folder)
        if folder:
            self.download_folder = folder
            self.folder_label.configure(text=f"Konum: {self.truncate_text(self.download_folder, 30)}")

    def truncate_text(self, text, length):
        if len(text) > length:
            return text[:length-3] + "..."
        return text

    def start_download_thread(self):
        url = self.url_entry.get().strip()
        if not url:
            messagebox.showerror("Hata", "Lütfen bir URL girin.")
            return

        self.lock_ui(True)
        self.status_label.configure(text="İndirme başlatılıyor...", text_color="orange")
        self.progress_bar.set(0)
        
        thread = threading.Thread(target=self.download_video, args=(url,))
        thread.start()

    def download_video(self, url):
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': os.path.join(self.download_folder, '%(title)s.%(ext)s'),
            'user_agent': user_agent,
            'noplaylist': True,
            'keepvideo': False, 
            'progress_hooks': [self.my_hook],
            'postprocessor_args': {'ffmpeg': ['-c', 'copy']},
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                filename = ydl.prepare_filename(info)
                
            self.save_to_history(info.get('title', 'Unknown'), filename)
            self.after(0, lambda: self.finish_download(True))
        except Exception as e:
            self.after(0, lambda msg=str(e): self.finish_download(False, msg))

    def my_hook(self, d):
        if d['status'] == 'downloading':
            try:
                p = d.get('_percent_str', '0%').replace('%','')
                progress = float(p) / 100
                text = f"İndiriliyor: {d.get('_percent_str')} - Hız: {d.get('_speed_str')} - Kalan: {d.get('_eta_str')}"
                self.after(0, lambda: self.update_progress(progress, text))
            except:
                pass
        elif d['status'] == 'finished':
            self.after(0, lambda: self.update_progress(1.0, "Birleştiriliyor/Dönüştürülüyor..."))

    def update_progress(self, val, text):
        self.progress_bar.set(val)
        self.status_label.configure(text=text)

    def finish_download(self, success, error_msg=None):
        self.lock_ui(False)
        if success:
            self.status_label.configure(text="İndirme Tamamlandı!", text_color="green")
            self.progress_bar.set(1)
            self.update_history_view()
            messagebox.showinfo("Başarılı", "Video başarıyla indirildi.")
        else:
            self.status_label.configure(text="Hata oluştu", text_color="red")
            self.progress_bar.set(0)
            messagebox.showerror("Hata", f"İndirme başarısız:\n{error_msg}")

    def lock_ui(self, lock):
        state = "disabled" if lock else "normal"
        self.download_btn.configure(state=state)
        self.url_entry.configure(state=state)
        self.browse_btn.configure(state=state)

    def load_history(self):
        if os.path.exists(HISTORY_FILE):
            try:
                with open(HISTORY_FILE, "r", encoding="utf-8") as f:
                    return json.load(f)
            except:
                return []
        return []

    def save_to_history(self, title, path):
        record = {
            "title": title,
            "path": path,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.history.insert(0, record)
        try:
            with open(HISTORY_FILE, "w", encoding="utf-8") as f:
                json.dump(self.history, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"History save error: {e}")

    def update_history_view(self):
        self.history_list.configure(state="normal")
        self.history_list.delete("0.0", "end")
        
        for item in self.history:
            self.history_list.insert("end", f"[{item['date']}] {item['title']}\n   -> {item['path']}\n\n")
            
        self.history_list.configure(state="disabled")

if __name__ == "__main__":
    app = GDriveDownloaderApp()
    app.mainloop()
