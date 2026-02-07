---
title: "Yılan Oyunu ve Yapay Zeka: Deep Q-Learning ile Kendi Kendine Öğrenen Ajan"
date: 2026-02-07T18:00:00+03:00
draft: false
tags: ["Python", "Artificial Intelligence", "Deep Learning", "SnakeAI", "PyTorch"]
categories: ["Tech", "AI", "Machine Learning"]
author: "Turgut Şimşek"
---

Merhaba! Bugün sizlerle, klasik **Snake (Yılan)** oyununu bir yapay zekanın nasıl en verimli şekilde oynayabileceğini keşfettiğim projemi paylaşmak istiyorum. Bu proje sadece bir oyun botu değil, aslında modern yapay zekanın temellerinden biri olan **Pekiştirmeli Öğrenme (Reinforcement Learning)** dünyasına atılmış ciddi bir adımdır.

![Snake AI Learning Process](/pic/snake_ai.gif)

### 🧠 Deep Q-Learning (DQN) Derinlemesine İnceleme

Bu projede ajanın (yılanın) beyni olarak **Deep Q-Learning (DQN)** algoritmasını kullandım. Geleneksel Q-Learning'den farklı olarak DQN, durum-aksiyon ilişkilerini bir tablo yerine **Yapay Sinir Ağları (Neural Networks)** kullanarak öğrenir.

#### 1. Ajanın Algı Dünyası (State)
Yılan, dünyayı 11 farklı parametre üzerinden algılıyor. Bu veriler sinir ağımıza girdi (input) olarak iletiliyor:
- **Tehlike Algısı (3 bit):** Tam önünde, sağında veya solunda bir engel (kendi kuyruğu veya duvar) var mı?
- **Hareket Yönü (4 bit):** Şu an hangi yöne (Sol, Sağ, Yukarı, Aşağı) gidiyor?
- **Yemek Yönü (4 bit):** Yemek yılana göre tam olarak nerede (Kuzey, Güney, Doğu, Batı)?

#### 2. Sinir Ağı Mimarisi
Ajanın kararlarını veren sinir ağı, **PyTorch** ile inşa edildi:
- **Input Layer:** 11 nöron (State verileri).
- **Hidden Layer:** 256 nöronluk yoğun bir katman.
- **Output Layer:** 3 nöron (Düz git, Sola dön, Sağa dön).

#### 3. Ödül Sistemi (Reward Engineering)
Ajanı eğitmek için şu "havuç-sopa" yöntemini kullandım:
- **Yemek Yeme:** +10 puan (Aferin, doğru yoldasın!)
- **Ölüm (Duvara/Kuyruğa Çarpma):** -10 puan (Bunu bir daha yapma!)
- **Geçen Süre:** 0 puan (Amaç en kısa sürede yemeğe ulaşmak).

### 🐍 Eğitim Süreci Nasıl İlerliyor?

Yılan ilk başladığında tamamen bir "bebek" gibidir; sağa sola rastgele çarpar. Ancak **Exploration vs. Exploitation** (Keşfetme ve Faydalanma) dengesi sayesinde zamanla tecrübe kazanır:
- **Epsilon:** Başlarda yüksek tutulur ki yılan dünyayı keşfetsin.
- **Memory (Deneyim Tekrarı):** Geçmişteki hamlelerini hatırlar ve bu deneyimlerden rastgele örnekler çekerek öğrenmesini pekiştirir.

Birkaç yüz oyun sonunda yılanın elmayı gördüğü anda saniyeler içinde hedefe kitlenmesini ve kendi gövdesine çarpmamak için yaptığı kıvrak manevraları izlemek gerçekten büyüleyici.

### 🚀 Teknik Kurulum ve Kaynak Kodlar

Projenin tüm kodları açık kaynak olarak GitHub'da mevcut. Kendi makinenizde eğitmek veya canlı izlemek için:

👉 [SnakeAI GitHub Deposu](https://github.com/gevezeus/SnakeAI)

**Gerekli Kütüphaneler:**
- `Pygame`: Görselleştirme için.
- `PyTorch`: Sinir ağını eğitmek için.
- `Numpy`: Matematiksel hesaplamalar için.

```bash
# Kurulum
pip install pygame torch numpy

# Başlatma
python agent.py
```

Bu proje, yapay zekanın "deneme-yanılma" yoluyla ne kadar kompleks problemleri çözebileceğinin küçük ama etkili bir kanıtıdır. Gelecekte bu modeli daha karmaşık oyunlar veya gerçek dünya senaryoları için geliştirmeyi planlıyorum.

Sorularınız ve katkılarınız için GitHub üzerinden bir Issue açabilir veya yorumlarda belirtebilirsiniz!

⚡ **Turgut Şimşek**
