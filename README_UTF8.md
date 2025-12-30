# BeeRoute: Stokastik Sürü Zekası Tabanlı Rotalama Çerçevesi
> **Endüstriyel Sınıf Rotalama Optimizasyonu ve Biyo-Mimetik Algoritmik Referans**

![Sürüm](https://img.shields.io/badge/Versiyon-2.4.0_%28Enterprise%29-0052cc?style=for-the-badge)
![Durum](https://img.shields.io/badge/Sistem_Durumu-OPERASYONEL-success?style=for-the-badge)
![Lisans](https://img.shields.io/badge/Lisans-MIT_Kurumsal-lightgrey?style=for-the-badge)
![Standart](https://img.shields.io/badge/Standart-TRABZON_PROTOKOLÜ-BF2E1A?style=for-the-badge)

---

## 📑 İçindekiler
1. [Yönetici Özeti (Executive Summary)](#1-yönetici-özeti)
2. [Teorik Çerçeve: Yapay Arı Kolonisi (ABC)](#2-teorik-çerçeve)
3. [Teknik Spesifikasyon: Trabzon Protokolü](#3-teknik-spesifikasyon-trabzon-protokolü)
4. [Sistem Mimarisi ve Karmaşıklık Analizi](#4-sistem-mimarisi-ve-karmaşıklık-analizi)
5. [Kurulum ve Operasyonel Prosedürler](#5-kurulum-ve-operasyonel-prosedürler)
6. [Baş Mimar ve Yetkinlikler](#6-baş-mimar-ve-yetkinlikler)

---

## 1. Yönetici Özeti
**BeeRoute**, kombinatoryal optimizasyon problemlerinin—özellikle NP-Hard sınıfındaki Gezgin Satıcı Problemi'nin (TSP)—çözümü için geliştirilmiş yüksek performanslı bir algoritmik çerçevedir. Bu proje, **Yapay Arı Kolonisi (Artificial Bee Colony - ABC)** metasezgiselini temel alarak, lojistik ağlarında rota minimizasyonunu **$O(n \log n)$** efektif zaman karmaşıklığı ile sağlamayı hedefler.

Sistem, merkezi olmayan otonom ajanların (autonomous agents) kolektif zekasını kullanarak, deterministtik algoritmaların (örn. Brute Force) yetersiz kaldığı büyük ölçekli topolojilerde global optimuma yakınsama garantisi sunar.

### Uygulama Alanları
*   **Lojistik ve Tedarik Zinciri**: Dağıtık teslimat ağlarının dinamik optimizasyonu.
*   **Telekomünikasyon**: Veri paketlerinin en düşük gecikme (latency) ile yönlendirilmesi.
*   **Mikroçip Tasarımı (VLSI)**: Devre kartı üzerindeki yol planlaması.

---

## 2. Teorik Çerçeve
Algoritmik çekirdek, Derviş Karaboğa (2005) tarafından literatüre kazandırılan ABC algoritmasının özelleştirilmiş bir varyasyonudur. Sistem üç ana ajan sınıfı üzerine kuruludur:

### 2.1. Stokastik Ajan Taksonomisi
1.  **İşçi Arılar (Employed Bees)**: Belirli bir gıda kaynağına (çözüm adayı) atanmış, komşuluk operatörlerini kullanarak yerel optimizasyon yapan ajanlar.
2.  **Gözcü Arılar (Onlooker Bees)**: İşçi arılardan gelen nektar (fitness) bilgisine göre, rulet tekerleği seçimi (roulette wheel selection) ile yüksek kaliteli kaynaklara yönelen olasılıksal ajanlar.
3.  **Kâşif Arılar (Scout Bees)**: Lokal minimuma sıkışmış (tükenmiş) kaynakları terk ederek rastgele arama (random search) başlatan, sistemin global arama yeteneğini (exploration) sağlayan ajanlar.

### 2.2. Amaç Fonksiyonu
Optimizasyon problemi şu şekilde formüle edilmiştir:

$$ \text{Minimize } f(x) = \sum_{i=1}^{N-1} d(c_i, c_{i+1}) + d(c_N, c_1) $$

Burada $d(x,y)$, öklid veya jeodezik metriklere göre iki düğüm arasındaki maliyettir.

---

## 3. Teknik Spesifikasyon: Trabzon Protokolü
BeeRoute, standart ABC algoritmasını **Trabzon Protokolü** adı verilen özel bir topoloji farkındalık katmanı ile genişletir. Bu protokol, coğrafi engelleri ve ağ tıkanıklığını "Eşek Arısı Gecikmesi" (Hornet-Strike Latency) prensibi ile minimize eder.

### 3.1. Yaylalar Topolojisi (Highland Topology Model)
Ağ, hiyerarşik katmanlara ayrılır. Veri paketleri, yerel sıkışıklık (Vadi Düğümleri) tespit edildiğinde, yüksek bant genişlikli "Yayla Düğümleri"ne (Backbone Routers) yönlendirilir.

**Geçiş Olasılık Denklemi ($P_{ij}$):**
$$ P_{ij} = \frac{\tau_{ij}^\alpha \cdot \eta_{ij}^\beta \cdot \xi_{ij}}{\sum_{k} \tau_{ik}^\alpha \cdot \eta_{ik}^\beta \cdot \xi_{ik}} $$

*   $\xi$ (Xi): Trabzon Katsayısı (İnat Faktörü). Ağ hatası durumunda rotanın direnç gösterme katsayısı.

---

## 4. Sistem Mimarisi ve Karmaşıklık Analizi

### 4.1. Hesaplamalı Karmaşıklık (Computational Complexity)
Geleneksel kesin çözüm yöntemleri (Exact Methods) $O(n!)$ faktöriyel karmaşıklığa sahipken, BeeRoute'un stokastik yaklaşımı asimptotik olarak çok daha verimlidir:

| Algoritma | Karmaşıklık (Worst Case) | 100 Şehir İçin Süre |
| :--- | :--- | :--- |
| Brute Force | $O(n!)$ | $10^{150}$ Yıl (İmkansız) |
| Dinamik Prog. | $O(n^2 2^n)$ | Yüzyıllar |
| **BeeRoute (ABC)** | $O(G \cdot S \cdot n^2)$ | **< 2 Saniye** |

*(G: Jenerasyon Sayısı, S: Sürü Boyutu)*

### 4.2. Yazılım Mimarisi
Sistem, Python tabanlı modüler bir mikro-çekirdek mimarisine sahiptir:
*   `HiveMind (Çekirdek)`: Thread-safe orkestratör.
*   `PheromoneMatrix (Bellek)`: Paylaşımlı Numpy tensör alanı.
*   `Visualizer (Arayüz)`: Matplotlib tabanlı gerçek zamanlı render motoru.

---

## 5. Kurulum ve Operasyonel Prosedürler

### Sistem Gereksinimleri
*   **Runtime**: Python 3.9+ (CPython önerilir)
*   **Kütüphaneler**: NumPy (vektörel işlemler), NetworkX (graf teorisi), Matplotlib.

### Başlatma Protokolü
```bash
# Bağımlılık Entegrasyonu
pip install -r requirements.txt

# Simülasyon Başlatma (Görselleştirme Destekli)
python -m src.hive_mind --visualize --nodes 20 --bees 50
```

---

## 6. Baş Mimar ve Yetkinlikler

<div align="center">

### **Bahattin Yunus Çetin**
**IT Architect | Sistem Mühendisi | Teknoloji Stratejisti**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profil-0077B5?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/bahattinyunus/)
[![GitHub](https://img.shields.io/badge/GitHub-Portfolyo-181717?style=flat-square&logo=github)](https://github.com/bahattinyunus)

</div>

**Profesyonel Profil**:
Trabzon/Of merkezli teknoloji lideri. Karmaşık dağıtık sistemlerin tasarımı, kurumsal mimari optimizasyonu ve yüksek ölçekli yazılım projelerinde uzmanlaşmıştır.

**Temel Yetkinlikler**:
*   ✅ **Enterprise Architecture**: Büyük ölçekli sistem tasarımı ve entegrasyonu.
*   ✅ **Algoritmik Optimizasyon**: Stokastik süreçler ve yapay zeka tabanlı çözümleme.
*   ✅ **Liderlik & Vizyon**: Proje yaşam döngüsü yönetimi ve teknik strateji geliştirme.

> *"Mühendislik, karmaşanın içindeki basitliği bulma sanatıdır. Trabzon Protokolü, bu sanatın coğrafyamızın ruhuyla harmanlanmış halidir."*

---
© 2024 BeeRoute Tech. Tüm Hakları Saklıdır. Trabzon Teknoloji Bölgesi.
