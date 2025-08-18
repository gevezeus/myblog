+++
title = "CPU daki ALU ne iş yapar? ALU' nun ön beleği olsaydı ne olurdu?"
date = 2025-08-18T11:33:01+03:00
draft = false
author = "tsimsek"
comments = false
image = ""
menu = ""
share = false
slug = "first-post"
tags = ["blog"]
+++

Elbette! Bilgisayarların temel çalışma mantığı **ikili sayı sistemi (binary)** yani **0 ve 1'ler** üzerine kuruludur. Bu sistem, elektrik sinyallerinin varlığı (1) veya yokluğu (0) şeklinde fiziksel olarak temsil edilir. Peki bu 0 ve 1'ler nasıl işleniyor? Adım adım açıklayalım:

---

### **1. Transistörler: 0 ve 1'lerin Fiziksel Karşılığı**

- CPU'da milyarlarca **transistör** (anahtar görevi gören yarı iletken devre elemanları) bulunur.
- Transistörler:
  - **Açık (ON) durumunda → "1"** (elektrik akımı geçer)
  - **Kapalı (OFF) durumunda → "0"** (elektrik akımı geçmez)
- Örneğin, bir transistör grubu **0101** gibi bir ikili diziyi temsil edebilir.

---

### **2. Mantık Kapıları (Logic Gates): Temel İşlem Birimleri**

- Transistörlerin birleşimiyle **mantık kapıları** oluşur (AND, OR, NOT, XOR gibi).
- Her kapı, belirli bir mantıksal işlem yapar. Örneğin:
  - **AND kapısı**: Girişlerin **hepsi 1 ise** çıkış **1**, aksi halde **0**.
  - **OR kapısı**: Girişlerden **en az biri 1 ise** çıkış **1**.
- Örnek: `1 AND 0 = 0`, `1 OR 0 = 1`.

---

### **3. Aritmetik İşlemler: Toplama, Çıkarma, Çarpma**

- Mantık kapıları birleşerek **aritmetik birimleri (ALU)** oluşturur.
- **Örnek (Toplama):**  
  - İki bit toplamak için **yarı toplayıcı (half-adder)** devresi kullanılır:
    - `0 + 0 = 00` (sonuç: 0, elde: 0)  
    - `1 + 1 = 10` (sonuç: 0, elde: 1)  
  - Daha karmaşık işlemler için **tam toplayıcılar (full-adders)** birleştirilir.

---

### **4. Komut Çalıştırma: CPU'nun Adım Adım İşleyişi**

CPU, **makine kodları** (0 ve 1'lerden oluşan komutlar) ile çalışır. Örneğin:

1. **Fetch (Getir)**: Bellekten bir komut okunur (örn: `10110011`).
2. **Decode (Çöz)**: Komutun ne yapacağı çözülür (örn: "A ve B'yi topla").
3. **Execute (Çalıştır)**: ALU devreleri devreye girer, sonuç hesaplanır.
4. **Store (Sakla)**: Sonuç belleğe veya kaydediciye yazılır.

---

### **5. Örnek: "5 + 7" İşlemi Nasıl Yapılır?**

1. Sayılar ikiliye çevrilir:  
   - `5 → 0101`  
   - `7 → 0111`  
2. ALU, bit bit toplama yapar (elde bitleriyle birlikte):  

   ```
     0101 (5)  
   + 0111 (7)  
   --------  
     1100 (12)  
   ```

3. Sonuç **1100** (12) olarak kaydedilir.

---

### **6. Bellek ve Programlarla Etkileşim**

- Tüm programlar ve veriler en nihayetinde **ikili kodlara** dönüştürülür.
- Örneğin, `A harfi` ASCII'de `01000001` ile temsil edilir.
- CPU, bu kodları işleyerek ekrana "A" yazdırabilir veya matematik işlem yapabilir.

---

### **Özetle:**

1. **Fiziksel Katman**: Transistörler 0/1'i elektrik sinyaliyle temsil eder.
2. **Mantıksal Katman**: Kapılar, temel işlemleri yapar.
3. **Aritmetik Katman**: ALU, matematiksel işlemleri gerçekleştirir.
4. **Komut Katmanı**: Makine kodları, CPU'ya ne yapacağını söyler.

Bu hiyerarşi sayesinde, karmaşık yazılımlar bile en basit elektrik sinyallerine indirgenerek işlenebilir.  

"ALU işlemleri yapıyor anladım. peki aynı işlem bir daha ALU ya gelirse aynı işlemi daha önce hesapladığı için sonucu biliyor. bu işlemi tekrar mı yapar yoksa daha önce yaptığı sonucu mu döndürür?"

Bu çok ilginç bir soru! CPU'lar genellikle **aynı işlemi tekrar hesaplar**, çünkü ALU (Aritmetik Mantık Birimi) **durumsuz (stateless)** bir birimdir ve geçmiş işlemleri hatırlamaz. Ancak modern işlemciler, performansı artırmak için **önbellek (cache)** ve **sonuç tekrar kullanımı (reuse)** gibi optimizasyon teknikleri kullanır. Detaylı açıklayalım:

---

### **1. ALU'nun Temel Çalışma Mantığı**

- ALU, her seferinde **girdilere bakar ve sonucu anında hesaplar**. Önceki işlemlerin sonucunu saklamaz.
- Örneğin:  
  - İlk seferde `5 + 7` işlemi yapıldığında ALU `1100` (12) sonucunu üretir.  
  - Aynı işlem tekrar gelirse, ALU **yeniden hesaplama yapar**.  
  - Neden? Çünkü ALU'nun **hafızası yoktur**; her işlem bağımsızdır.

---

### **2. Optimizasyon: Önbellek (Cache) ile Sonuç Tekrar Kullanımı**

Modern CPU'lar, ALU'nun her seferinde yeniden hesaplama yapmasının performans kaybını azaltmak için şu yöntemleri kullanır:

#### **a. Önbellek (Cache) Sistemi**

- CPU, sık kullanılan veri ve işlem sonuçlarını **önbellekte** saklar.  
- Örneğin:  
  - `5 + 7` işlemi ilk kez yapıldığında sonuç (`1100`) **L1 önbelleğe** kaydedilir.  
  - Aynı işlem tekrar gelirse, CPU önce önbelleği kontrol eder. Sonuç oradaysa **ALU'ya gitmeden** doğrudan önbellekten okur.  
  - Bu, enerji ve zaman tasarrufu sağlar.

#### **b. Instruction-Level Parallelism (ILP)**

- CPU'lar, aynı işlemin tekrarını tespit edip **sonucu yeniden kullanabilir**.  
- Örneğin bir döngüde `5 + 7` defalarca çalıştırılıyorsa, bazı mimariler (örneğin **superscalar işlemciler**) bu sonucu tekrar hesaplamak yerine **kaydedicilerde (register) tutabilir**.

#### **c. Compiler Optimizasyonları**

- Derleyiciler (GCC, Clang vb.), kodunuzda aynı işlemi tekrar tekrar yapıyorsanız, **gereksiz hesaplamaları atlayıp** sonucu bir kez saklayabilir.  
- Örneğin:  

  ```c
  int x = 5 + 7;  // Derleyici bunu "int x = 12;" olarak optimize eder.
  ```

---

### **3. Neden ALU Geçmişi Hatırlamaz?**

1. **Basitlik ve Hız**: ALU'nun geçmiş işlemleri saklaması, devre karmaşıklığını artırır ve hızı düşürür.  
2. **Güç Tüketimi**: Ek hafıza birimleri enerji tüketimini artırır.  
3. **Paralel İşlemler**: Modern CPU'lar aynı anda birden fazla işlem yapar. Her ALU işlemi bağımsız olmalıdır.

---

### **4. Özel Durum: "Memoization" Tekniği**

- Yazılım tarafında, fonksiyonların sonuçlarını saklayan **memoization** gibi teknikler kullanılabilir.  
- Ancak bu, CPU seviyesinde değil, **yazılım/yüksek seviye optimizasyonudur**. Örneğin:  

  ```python
  from functools import lru_cache
  @lru_cache
  def add(a, b):
      return a + b
  # add(5, 7) ilk kez hesaplanır, sonraki çağrılar önbellekten gelir.
  ```

---

### **Sonuç**

- **Saf ALU**: Her işlemi sıfırdan hesaplar (geçmişi hatırlamaz).  
- **Gerçek Dünya CPU'ları**: Önbellek, paralellik ve derleyici optimizasyonları sayesinde **aynı işlemi tekrar hesaplamaktan kaçınır**.  

Yani teknik olarak ALU her seferinde hesaplar, ancak sistemin diğer bileşenleri bu sonucu **daha akıllıca yöneterek** performansı artırır. 😊  

Başka sorunuz varsa bekliyorum!
