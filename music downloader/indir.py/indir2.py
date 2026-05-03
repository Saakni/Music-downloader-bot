import os
import subprocess

# Şarkı listen (Senin attığın kağıtlardaki liste)
sarkilar = [
    "Tekrar, örnek 1"
    "örnek 2"
]

def sarki_indir():
    print(f"Toplam {len(sarkilar)} şarkı indirilecek...")
    
    for sarki in sarkilar:
        print(f"\n[İndiriliyor] -> {sarki}")
        # yt-dlp komutu: Arama yapar (ytsearch1), ilk sonucu alır, mp3'e çevirir.
        # ffmpeg gerektirir. Eğer hata verirse ffmpeg kurman gerekir.
        komut = [
            "yt-dlp",
            "-x", # Sesi ayıkla
            "--audio-format", "mp3", # MP3 yap
            "--output", "%(title)s.%(ext)s", # Dosya adı formatı
            f"ytsearch1:{sarki}" # YouTube'da ara ve ilk videoyu al
        ]
        
        try:
            subprocess.run(komut, check=True)
        except subprocess.CalledProcessError:
            print(f"[HATA] {sarki} indirilemedi.")
        except FileNotFoundError:
             print("HATA: 'yt-dlp' bulunamadı. Lütfen 'pip install yt-dlp' yazarak kurun.")
             break

if __name__ == "__main__":
    sarki_indir()
