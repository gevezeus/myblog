---
title: "Yılan Oyunu ve Yapay Zeka: Deep Q-Learning ile Kendi Kendine Öğrenen Ajan"
date: 2026-02-07T18:00:00+03:00
draft: false
tags: ["Python", "Artificial Intelligence", "Deep Learning", "SnakeAI"]
categories: ["Tech", "AI"]
author: "Turgut Şimşek"
---

Merhaba! Bugün sizlere boş zamanlarımda geliştirdiğim, klasikleşmiş **Snake (Yılan)** oyununu yapay zeka kullanarak nasıl çözdüğümü anlatacağım.

Bu projede bir ajanın (yılanın) çevresini algılayarak en doğru hamleyi yapmasını sağlayan **Deep Q-Learning (DQN)** algoritmasını kullandım.

### 🧠 Deep Q-Learning Nedir?

Deep Q-Learning, **Pekiştirmeli Öğrenme (Reinforcement Learning)** alanında kullanılan güçlü bir algoritmadır. Temel mantığı, bir sinir ağının (Neural Network) oyundaki her durum (state) için hangi hamlenin (action) en yüksek ödülü (reward) getireceğini tahmin etmesine dayanır.

Yılanımız her saniye şu 11 farklı durumu kontrol ediyor:
- Önünde, sağında veya solunda tehlike var mı?
- Mevcut hareket yönü nedir?
- Yemek (elma) ne tarafta?

### 🐍 Projenin Teknik Altyapısı

- **Python:** Ana geliştirme dili.
- **PyTorch:** Sinir ağı mimarisi ve model eğitimi.
- **Pygame:** Oyun motoru ve canlı görselleştirme.

Yılan, başlangıçta tamamen rastgele hareket ederken, yüzlerce oyun sonunda en kısa yoldan yemeğe gitmeyi ve kuyruğuna çarpmamayı öğreniyor. Eğitimin bir noktasından sonra yılanın sanki bir insan kontrol ediyormuşçasına (hatta daha iyi!) hamleler yaptığını görmek gerçekten heyecan verici.

### 🚀 Kodu İnceleyin

Projenin tüm kaynak kodlarına ve eğitilmiş model dosyasına GitHub üzerinden ulaşabilirsiniz:

👉 [SnakeAI GitHub Repository](https://github.com/gevezeus/SnakeAI)

### 📽️ Nasıl Çalıştırılır?

Eğer yerel makinenizde denemek isterseniz:

```bash
git clone https://github.com/gevezeus/SnakeAI.git
cd SnakeAI
pip install -r requirements.txt
python agent.py
```

Yapay zeka dünyasındaki bu tarz küçük ama öğretici deneyler, teknolojinin nereye evrildiğini anlamak adına harika birer adım. Sorularınız olursa yorumlarda veya sosyal medya üzerinden benimle iletişime geçebilirsiniz!

⚡ **Turgut Şimşek**
