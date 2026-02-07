---
title: "Yılan Oyunu ve Yapay Zeka: Deep Q-Learning ile Kendi Kendine Öğrenen Ajan"
date: 2026-02-07T18:00:00+03:00
draft: false
tags: ["Python", "Artificial Intelligence", "Deep Learning", "SnakeAI", "PyTorch"]
categories: ["Tech", "AI", "Machine Learning"]
author: "Turgut Şimşek"
---

Merhaba! Bugün sizlerle, klasik **Snake (Yılan)** oyununu bir yapay zekanın nasıl en verimli şekilde oynayabileceğini keşfettiğim projemi paylaşmak istiyorum. Bu proje sadece bir oyun botu değil, aslında modern yapay zekanın temellerinden biri olan **Pekiştirmeli Öğrenme (Reinforcement Learning)** dünyasına atılmış ciddi bir adımdır.

### 🐍 Yapay Zeka Nasıl Öğreniyor?

Ajanımızın eğitim sürecinden iki farklı aşamayı aşağıda görebilirsiniz. Başlangıçta tamamen rastgele hareket eden yılanımız, zamanla strateji geliştirmeyi öğreniyor:

| Başlangıç Evresi (Keşif) | İleri Evre (Uzmanlık) |
| :---: | :---: |
| ![Snake AI Early Stage](/pic/snake_ai_1.gif) | ![Snake AI Expert Stage](/pic/snake_ai_2.gif) |

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
- **Yemek Yeme:** +10 puan
- **Ölüm (Duvara/Kuyruğa Çarpma):** -10 puan
- **Geçen Süre:** 0 puan

### 🚀 Teknik Kurulum ve Kaynak Kodlar

Projenin tüm kodları açık kaynak olarak GitHub'da mevcut:

👉 [SnakeAI GitHub Deposu](https://github.com/gevezeus/SnakeAI)

```bash
# Kurulum
pip install pygame torch numpy

# Başlatma
python agent.py
```

⚡ **Turgut Şimşek**
