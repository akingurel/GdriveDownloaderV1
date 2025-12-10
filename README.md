# Video İndirici (GUI) 🎥

"Yalnızca Görüntülenen" (View-Only / İndirme Kısıtlamalı) videoları yüksek kalitede indirmek için geliştirilmiş modern bir masaüstü uygulaması.

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![GUI](https://img.shields.io/badge/GUI-CustomTkinter-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 🌟 Özellikler

*   **📺 Modern Arayüz**: `CustomTkinter` ile hazırlanmış, karanlık mod destekli şık ve kullanıcı dostu arayüz.
*   **🔓 Kısıtlamaları Aşın**: İndirme izni kapalı olan "salt okunur" videoları kolayca indirin.
*   **⚡ Otomatik Kurulum**: Gerekli olan `yt-dlp` kütüphanesini sisteminizde yoksa otomatik kurar ve yapılandırır.
*   **💎 En İyi Kalite**: Videoları mümkün olan en yüksek çözünürlükte (1080p+) indirir ve birleştirir.
*   **📜 İndirme Geçmişi**: İndirdiğiniz videoları ve kayıt yerlerini uygulama içinde liste halinde görün.
*   **📦 Taşınabilir EXE**: Kurulum gerektirmeyen tek bir `.exe` dosyası olarak çalışabilir.

## 🚀 Kurulum ve Kullanım

### Seçenek 1: Hazır EXE Kullanımı (Önerilen)
`Releases` kısmından en son sürümü indirin ve uygulamanın `.exe` dosyasını çalıştırın. Python kurmanıza gerek yoktur.

### Seçenek 2: Kaynak Koddan Çalıştırma
1.  Bu depoyu klonlayın:
    ```bash
    git clone https://github.com/KULLANICI_ADINIZ/REPO_ADINIZ.git
    cd REPO_ADINIZ
    ```
2.  Gerekli kütüphaneleri yükleyin:
    ```bash
    pip install customtkinter yt-dlp packaging pyinstaller
    ```
3.  Uygulamayı başlatın:
    ```bash
    python gdrive_gui.py
    ```

## ⚠️ FFmpeg Notu
1080p ve üzeri yüksek çözünürlükleri ses ile birleştirmek için **FFmpeg** sisteminizde yüklü olmalıdır. Yüklü değilse uygulama çalışmaya devam eder ancak maksimum 720p (veya ses/video birleşimi gerektirmeyen en iyi formatı) indirir.

## 🤝 Katkıda Bulunma
Katkılarınızı bekliyoruz! Hata bildirimleri (issue) açabilir veya Pull Request gönderebilirsiniz.

## 📝 Lisans
Bu proje MIT Lisansı altında lisanslanmıştır.

---

# Video Downloader (GUI) 🎥 [English]

A modern desktop application developed to download "View-Only" (download restricted) videos from online sources in high quality.

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![GUI](https://img.shields.io/badge/GUI-CustomTkinter-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 🌟 Features

*   **📺 Modern UI**: Stylish, dark-mode friendly interface built with `CustomTkinter`.
*   **🔓 Bypass Restrictions**: Easily download "view-only" videos where the download button is disabled.
*   **⚡ Auto-Setup**: Automatically installs and configures the required `yt-dlp` library if missing.
*   **💎 Best Quality**: Downloads and merges videos in the highest possible resolution (1080p+).
*   **📜 History**: View a list of downloaded videos and their file paths within the app.
*   **📦 Portable EXE**: Can run as a standalone `.exe` file without requiring Python installation.

## 🚀 Installation & Usage

### Option 1: Using the EXE (Recommended)
Download the latest release from the `Releases` section and run the application's `.exe` file. No Python required.

### Option 2: Running from Source
1.  Clone this repository:
    ```bash
    git clone https://github.com/YOUR_USERNAME/REPO_NAME.git
    cd REPO_NAME
    ```
2.  Install required libraries:
    ```bash
    pip install customtkinter yt-dlp packaging pyinstaller
    ```
3.  Start the application:
    ```bash
    python gdrive_gui.py
    ```

## ⚠️ FFmpeg Note
**FFmpeg** must be installed on your system to merge high resolutions (1080p+) with audio. If missing, the app will continue to work but will download the best single-file format available (usually 720p).

## 🤝 Contributing
Contributions are welcome! Feel free to open issues or submit Pull Requests.

## 📝 License
This project is licensed under the MIT License.
