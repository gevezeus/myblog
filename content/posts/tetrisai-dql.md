---
title: "Tetris AI: Deep Q-Learning ve 2-Adım İleri Görüş İle Rekor Kırmak"
date: 2026-02-11T22:30:00+03:00
draft: false
tags: ["Python", "Artificial Intelligence", "Deep Reinforcement Learning", "Tetris", "PyTorch"]
categories: ["Tech", "AI", "Machine Learning"]
author: "Turgut Şimşek"
---

Yılan oyunundan sonra bu kez çıtayı biraz daha yukarı taşıyarak klasik **Tetris** oyununu kendi kendine en yüksek skorla oynamayı öğrenen bir yapay zeka geliştirdim. Bu projede sadece temel Deep Q-Learning kullanmakla kalmadım, aynı zamanda ajanın hamle kalitesini artırmak için **2-Step Lookahead (2-Adım İleri Görüş)** mekanizmasını entegre ettim.

### 🧠 Tetris AI Nasıl Karar Veriyor?

Tetris, yüksek hızda karar vermeyi ve uzun vadeli planlamayı gerektiren karmaşık bir oyundur. Ajanımız hamle yapmadan önce tahtanın durumunu şu kriterlere göre analiz eder:

1.  **Silinen Satırlar:** Tek hamlede kaç satır temizlenecek? (En büyük ödül!)
2.  **Boşluklar (Holes):** Yeni parçanın altında ulaşılamaz boşluklar kalıyor mu? (Büyük ceza!)
3.  **Pürüzlülük (Bumpiness):** Yüzey ne kadar engebeli? (Ceza!)
4.  **Toplam Yükseklik:** Kule ne kadar yükseldi? (Ceza!)

### 🚀 Öne Çıkan Özellikler

*   **2-Step Lookahead:** Yapay zeka sadece elindeki parçayı değil, sıradaki parçanın da nereye geleceğini hesaplayarak en optimal yerleşimi bulur.
*   **DQN (Deep Q-Network):** Karar verme sürecinde PyTorch tabanlı 512 nöronlu güçlü bir Yapay Sinir Ağı kullanılır.
*   **Dinamik Eğitim:** Başlangıçta rastgele hamlelerle dünyayı keşfeden ajan, binlerce bölüm sonunda profesyonel bir oyuncu seviyesine ulaşır.

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

Yapay zekanın oyun sırasında hızını `W` ve `S` tuşlarıyla anlık olarak değiştirerek kararlarını nasıl verdiğini detaylıca inceleyebilirsiniz.

⚡ **Turgut Şimşek**
