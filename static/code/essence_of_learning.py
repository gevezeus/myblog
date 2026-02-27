import math
import random
from typing import List, Tuple

class Neuron:
    """
    Yapay bir sinir hücresini (nöron) temsil eder.
    Kendini geliştiren sistemin en küçük yapı taşıdır.
    """
    def __init__(self, num_inputs: int):
        # Ağırlıklar (weights) ve sapma (bias) başlangıçta rastgele atanır (Kaos)
        self.weights: List[float] = [random.uniform(-1, 1) for _ in range(num_inputs)]
        self.bias: float = random.uniform(-1, 1)
        
        # Geriye yayılım (backpropagation) için son değerleri hafızada tutar
        self.last_inputs: List[float] = []
        self.last_output: float = 0.0

    def activate(self, x: float) -> float:
        """Sigmoid aktivasyon fonksiyonu: Girdiyi 0 ile 1 arasına sıkıştırır."""
        return 1 / (1 + math.exp(-x))

    def activate_derivative(self, x: float) -> float:
        """Sigmoid fonksiyonunun türevi: Hatalardan ders çıkarmak için kullanılır."""
        return x * (1 - x)

    def forward(self, inputs: List[float]) -> float:
        """İleri besleme: Veriyi alır, işler ve bir tahmin üretir."""
        self.last_inputs = inputs
        # Nokta çarpım (Dot product) + Bias
        total = sum(w * i for w, i in zip(self.weights, inputs)) + self.bias
        self.last_output = self.activate(total)
        return self.last_output

class EssenceOfLearning:
    """
    Çok Katmanlı Algılayıcı (Multi-Layer Perceptron).
    Klasik mantığın çözemediği XOR problemini öğrenerek çözer.
    """
    def __init__(self):
        # Mimari: 2 Girdi -> 2 Gizli Nöron -> 1 Çıktı Nöronu
        self.hidden_layer: List[Neuron] = [Neuron(2), Neuron(2)]
        self.output_neuron: Neuron = Neuron(2)
        self.learning_rate: float = 0.5

    def predict(self, inputs: List[float]) -> float:
        """Sistemin tahmini."""
        hidden_outputs = [neuron.forward(inputs) for neuron in self.hidden_layer]
        return self.output_neuron.forward(hidden_outputs)

    def train(self, training_data: List[Tuple[List[float], float]], epochs: int = 5000):
        """
        Eğitim döngüsü. Sistem hatalarıyla yüzleşir ve kendini yeniden yapılandırır.
        """
        print("🧠 Öz-Ogrenme Sureci Basliyor...\n")
        
        for epoch in range(epochs):
            total_error = 0
            
            for inputs, target in training_data:
                # 1. Tahmin Et
                prediction = self.predict(inputs)
                
                # 2. Hatayı Hesapla (Ne kadar yanıldık?)
                error = target - prediction
                total_error += error ** 2
                
                # 3. Çıktı Nöronunun Hatasını Düzelt
                out_delta = error * self.output_neuron.activate_derivative(prediction)
                
                for i in range(len(self.output_neuron.weights)):
                    self.output_neuron.weights[i] += self.learning_rate * out_delta * self.output_neuron.last_inputs[i]
                self.output_neuron.bias += self.learning_rate * out_delta
                
                # 4. Gizli Katman Nöronlarının Hatalarını Düzelt
                for i, hidden_neuron in enumerate(self.hidden_layer):
                    hidden_error = out_delta * self.output_neuron.weights[i]
                    hidden_delta = hidden_error * hidden_neuron.activate_derivative(hidden_neuron.last_output)
                    
                    for j in range(len(hidden_neuron.weights)):
                        hidden_neuron.weights[j] += self.learning_rate * hidden_delta * hidden_neuron.last_inputs[j]
                    hidden_neuron.bias += self.learning_rate * hidden_delta

            # Gelişimi Raporla
            if (epoch + 1) % 1000 == 0:
                print(f"Evrim Adimi {epoch + 1:04d} | Hata Orani: {total_error:.4f}")

if __name__ == "__main__":
    # XOR Problemi: Benzerler 0, Farklılar 1 üretmelidir.
    # Klasik bir bilgisayar programı if-else olmadan bunu çözemez.
    xor_data = [
        ([0.0, 0.0], 0.0),
        ([0.0, 1.0], 1.0),
        ([1.0, 0.0], 1.0),
        ([1.0, 1.0], 0.0)
    ]

    ai = EssenceOfLearning()
    
    print("--- EGITIM ONCESI (CAHIL DURUM) ---")
    for inputs, _ in xor_data:
        print(f"Girdi: {inputs} -> Tahmin: {ai.predict(inputs):.4f}")
    
    print("\n")
    ai.train(xor_data, epochs=5000)
    print("\n--- EGITIM SONRASI (BILGE DURUM) ---")
    
    for inputs, target in xor_data:
        prediction = ai.predict(inputs)
        # Tahmini 0 veya 1'e yuvarla
        result = 1 if prediction > 0.5 else 0
        status = "BASARILI" if result == target else "BASARISIZ"
        print(f"Girdi: {inputs} -> Hedef: {target} | Tahmin: {prediction:.4f} ({result}) [{status}]")
