import os
import subprocess

# Şarkı listen (Senin attığın kağıtlardaki liste)
sarkilar = [
    "Erkan Oğur Ey Benim Divane Gönlüm",
    "Havanur Hem Sivaslı Hem de Bizim Oralı",
    "İzzet Altınmeşe Benim O Köylerde Alacağım Var",
    "Nazlı Öksüz Tel Tel Olmuş Saçların",
    "Şu Dağlar Kömürdendir Türkü",
    "Ya Hızır Semahı",
    "Ilgıt Ilgıt Esen Seher Yeli",
    "Hey Erenler",
    "Ervah-ı Ezelden",
    "Sana Kolay Gelir Türkü",
    "Yusuf Gül Yandır Beni",
    "Ali Eren Çınar Yol Üstüne Bir Gül Diktim",
    "Gökhan Göçmen Baba",
    "Ali Eren Çınar Şu Dağlar Kömürdendir",
    "Özcan Türe Yaşlanırsın",
    "Arzu Şahin Kıvırcık Ali Bak Şu Feleğin İşine",
    "Feyza Nur Gönlünde Başka Yar Var mı",
    "Ervah-ı Ezelden Kurusa Fidanım",
    "Ey Sevdiğim Sana Şikayetim Var",
    "Bergen Bana Neler Vadettin",
    "Kamuran Akkor Ateşe Attın",
    "Volkan Konak Gurbet",
    "Volkan Konak Yalan Dünya",
    "Volkan Konak Neredesin Karagözlüm",
    "Volkan Konak Dertli Yoldaş",
    "Volkan Konak Aşkın Beni Deleyledi",
    "Volkan Konak Ağlatma Beni",
    "Volkan Konak Bir Dost Bulamadım",
    "Volkan Konak Göklerde Kartal Gibiyim",
    "Volkan Konak Keklik Gibi",
    "Volkan Konak Hem Okudum Hem Yazdım",
    "Volkan Konak Hastane Önünde İncir Ağacı",
    "Havva Öğüt Karışık",
    "Aşık Gülabi Gam Kasavetli Dünya",
    "Ali Ekber Çiçek Gönül Gel Seninle",
    "Erkan Oğur Mecnunum Leylayı Gördüm",
    "Hozan Beşir Elfida",
    "Anatolian Rock Yaşlanırsın",
    "Mesut Dağlı Dağlarına Kar Olurum",
    "Haşim Gülistan Tokdemir Küstüm Sevdiğim",
    "Neşet Ertaş Perişan Hallerim",
    "Neşet Ertaş Yazımı Kışa Çevirdin",
    "Neşet Ertaş Mühür Gözlüm",
    "Erkan Aydar Yar Bulamadım",
    "Ferhat Üngür Giden Yalan Oldu",
    "Ferhat Üngür Oy Benim Ceylanım",
    "Ferhat Üngür Sana Gelmek İstiyorum",
    "Ferhat Üngür Taşa Verdim Yanımı",
    "Müslüm Bozkurt Bu Derdimi Aşma Benim",
    "Gülay Geçti Dost Kervanı",
    "Tufan Altaş Yasemen",
    "Mehmet Nazlı Tokat Yaylası",
    "Yıldız Tilbe Sende Sev Ama Sevilme",
    "Hakan Altun Gönül Yarası",
    "Hakan Altun Her Sevda Bir Ölümmüş",
    "Hakan Altun Kaç Kadeh Kırıldı",
    "Hirai Zerdüş Dargınım",
    "Hirai Zerdüş Uyuyamıyorum",
    "Hirai Zerdüş Kimin Var Ki Senden Başka",
    "Mustafa Küçük Bu Perişan Hallerimi",
    "Mustafa Küçük O Kadar",
    "Hasan Erdoğan Sen Bizim Sevdamızı Bitti Demişsin",
    "Abdullah Papur Kan Ağlar İçim",
    "Ercan Papur Bundan Sonra",
    "İbrahim Yıldız Sanki Sam Yeliysin",
    "Dilber Ay Ben Bende Değilim",
    "Dilber Ay Taşa Dönderdin",
    "Dilber Ay Yas mı Var Mahallede",
    "Ferdi Tayfur Yüreğimde Yara Var",
    "Ferdi Tayfur Dur Dinle Sevgilim",
    "Bergen Seni Kalbimden Kovdum",
    "Mehmet Ali Yıldırım Daha Benden Alacağın Kalmadı",
    "Mehmet Ali Yıldırım Verin Tabancamı Ben Beni Vuram",
    "Nilüfer Sarıtaş Şu Sinemde Neler Var",
    "Nilüfer Sarıtaş Turnalar Göçü",
    "Nilüfer Sarıtaş Sabah Olsun",
    "Nilüfer Sarıtaş Gelsene",
    "Nilüfer Sarıtaş Derdim Gizli",
    "Nilüfer Sarıtaş Bağışla Beni",
    "Ömer Şahin Neyleyim",
    "Ali Rıza Gültekin İstemem Evimden Gurbete Çıkmak",
    "Hazar Yıldız Nedeyim",
    "Gönül Çalamazsın Aşkın Sazını"
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