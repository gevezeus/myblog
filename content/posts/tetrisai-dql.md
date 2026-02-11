---
title: "Tetris AI: Deep Q-Learning ve 2-Adım İleri Görüş İle Rekor Kırmak"
date: 2026-02-11T22:30:00+03:00
draft: false
tags: ["Python", "Artificial Intelligence", "Deep Reinforcement Learning", "Tetris", "PyTorch"]
categories: ["Tech", "AI", "Machine Learning"]
author: "Turgut Şimşek"
---

Yılan oyunundan sonra bu kez çıtayı biraz daha yukarı taşıyarak klasik **Tetris** oyununu kendi kendine en yüksek skorla oynamayı öğrenen bir yapay zeka geliştirdim. Bu projede sadece temel Deep Q-Learning kullanmakla kalmadım, aynı zamanda ajanın hamle kalitesini artırmak için **2-Step Lookahead (2-Adım İleri Görüş)** mekanizmasını entegre ettim.

### 🐍 Tetris AI Nasıl Öğreniyor?

Tetris, yüksek hızda karar vermeyi ve uzun vadeli planlamayı gerektiren karmaşık bir oyundur. Yapay zeka sadece ekrandaki pikselleri görmekle kalmaz; tahtanın durumunu analiz ederek en iyi hamleyi hesaplar.

#### 🧠 Beyin (Yapay Sinir Ağı)
Ajanımız hamle yapmadan önce tahtanın durumunu 512 nöronlu bir **Tam Bağlantılı Sinir Ağımız (Fully Connected Neural Network)** üzerinden şu kriterlere göre analiz eder:

1.  **Silinen Satırlar:** Tek hamlede kaç satır temizlenecek? (En büyük ödül!)
2.  **Boşluklar (Holes):** Yeni parçanın altında ulaşılamaz boşluklar kalıyor mu? (Büyük ceza!)
3.  **Pürüzlülük (Bumpiness):** Yüzey ne kadar engebeli? (Ceza!)
4.  **Toplam Yükseklik:** Kule ne kadar yükseldi? (Ceza!)

### 🚀 Öne Çıkan Özellikler

*   **2-Step Lookahead:** Yapay zeka sadece elindeki parçayı değil, sıradaki parçanın da nereye geleceğini hesaplayarak en optimal yerleşimi bulur.
*   **Ödül Sistemi (Reward Shaping):** Satır silmeyi ödüllendiren, hatalı yerleşimleri sert şekilde cezalandıran hassas bir ödül dengesi kuruldu.
*   **Görselleştirme & Kontrol:** Yapay zekanın hamlelerini animasyonlu şekilde izleyebilir, `W` ve `S` tuşlarıyla oyun hızını anlık olarak değiştirebilirsiniz.

### 📊 Eğitim Süreci ve Performans

Eğitim süreci **Keşif (Exploration)** aşamasından başlayarak zamanla **Uygulama (Exploitation)** aşamasına geçer:
- **0-100 Bölüm:** Rastgele hareketler, kuralları tanıma aşaması.
- **500+ Bölüm:** Düz zeminler oluşturmaya ve boşluklardan kaçınmaya başlar.
- **1000+ Bölüm:** "Tetris" (aynı anda 4 satır silme) hamleleri yapmaya başlar ve oyunu neredeyse sonsuza kadar sürdürebilir.

### 🛠 Teknik Detaylar ve Kaynak Kod

Projenin kurulumu ve kendi eğitiminizi başlatmak için GitHub deposunu ziyaret edebilirsiniz:

👉 [TetrisAI GitHub Deposu](https://github.com/gevezeus/TetrisAI)

```bash
# Depoyu klonlayın
git clone https://github.com/gevezeus/TetrisAI.git
cd TetrisAI

# Gerekli kütüphaneleri yükleyin
pip install -r requirements.txt

# Eğitimi ve oyunu başlatın
python main.py
```

Model, her 25 bölümde bir ilerlemesini `tetris_dqn.pth` dosyasına otomatik olarak kaydeder, böylece eğitim kaldığı yerden devam edebilir.

⚡ **Turgut Şimşek**
