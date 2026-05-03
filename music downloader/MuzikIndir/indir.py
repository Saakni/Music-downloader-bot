import os
import subprocess
import sys

# Şarkı listesi
sarkilar = [
    "buraya indirmek istediğimiz şarkıları yazıyoruz"
    "örnek 1"
    "örnek 2"
]

def sarki_indir():
    print(f"--- Toplam {len(sarkilar)} şarkı indirilecek ---")
    
    # FFmpeg kontrolü
    if not os.path.exists("ffmpeg.exe"):
        print("UYARI: ffmpeg.exe bu klasörde görünmüyor. Eğer kurulu değilse indirme hata verebilir.")
        # Devam etmeyi dene, belki sistemde kuruludur.

    for i, sarki in enumerate(sarkilar, 1):
        print(f"\n[{i}/{len(sarkilar)}] İndiriliyor: {sarki}")
        
        komut = [
            sys.executable, "-m", "yt_dlp", 
            "--extract-audio",
            "--audio-format", "mp3",
            "--audio-quality", "192K",
            "--output", "%(title)s.%(ext)s",
            "--ffmpeg-location", ".", 
            "--no-playlist",
            f"ytsearch1:{sarki}"
        ]
        
        try:
            subprocess.run(komut, check=True)
            print(f"✓ Tamamlandı: {sarki}")
        except Exception as e:
            print(f"X Hata oluştu: {sarki}")

if __name__ == "__main__":
    sarki_indir()
    input("\nBitti! Çıkmak için Enter'a bas...")