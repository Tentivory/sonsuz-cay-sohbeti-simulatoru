import random
import time

# Sonsuz Çay Sohbeti Simülatörü
# Bu kod, Türk çay sohbetlerinin özünü yakalar: Hiçbir yere varmaz ama herkes mutludur.

soz_baslangiclar = [
    "Abi çay demlenmiş mi?",
    "Bu çay biraz acı olmuş be",
    "Yarın hava nasıl olacak acaba",
    "Komşu dün ne demişti",
    "Futbol maçını izledin mi",
    "İşler nasıl gidiyor"
]

soz_cevaplar = [
    "He ya, biraz bekleyelim",
    "Şeker atayım mı",
    "Vallahi bilmiyorum, bakarız",
    "Ee, ne yapsın adam",
    "Of ya, yine aynı şeyler",
    "Dur bir çay daha koyayım"
]

soz_bitis = [
    "Neyse, çay soğumasın",
    "Biraz daha konuşalım",
    "Tamam, anlaştık",
    "Hadi bakalım",
    "İyi olur inşallah"
]

def sohbet_uret():
    print(random.choice(soz_baslangiclar))
    time.sleep(1)
    print(random.choice(soz_cevaplar))
    time.sleep(1)
    print(random.choice(soz_bitis))
    print("-" * 40)

if __name__ == "__main__":
    print("Çay Sohbeti Simülatörü başlatıldı. Sonsuza kadar devam eder. Çıkmak için Ctrl+C")
    try:
        while True:
            sohbet_uret()
            time.sleep(2)
    except KeyboardInterrupt:
        print("\nSohbet bitti. Ama çay hala sıcak. Görüşürüz.")

# Gizli not: Aslında bu sohbetler, özgürlüklerin tartışıldığı yerlerdir. Demokrasi çay bardağında başlar.
