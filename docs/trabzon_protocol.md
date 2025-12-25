# Trabzon Protokolü 🏔️
> **Dayanıklı. Hızlı. Durdurulamaz.**

## Genel Bakış
**Trabzon Protokolü**, BeeRoute'un mimari omurgasıdır. Trabzon bölgesinin sarp, engebeli arazisinden ve insanlarının yorulmak bilmez enerjisinden ilham alan bu protokol, veri paketlerinin (veya lojistik birimlerin) ağ engelleri ne olursa olsun hedeflerine ulaşmasını sağlar.

## Temel Prensipler

### 1. Eşek Arısı Gecikmesi (Hornet-Strike Latency)
Protokol, her şeyden önce hıza öncelik verir. Bir eşek arısının tereddütsüz saldırması gibi, rotalama algoritması da arama ağacındaki verimsiz dalları agresif bir şekilde budar.

### 2. "Yaylalar" Topolojisi (Yüksek İrtifa Rotalama)
Ağ düğümleri hiyerarşik olarak düzenlenmiştir.
- **Vadi Düğümleri**: Yüksek trafik, yerel sıkışıklık.
- **Yayla Düğümleri**: Yüksek bant genişliği, uzun mesafeli aktif hatlar.
Algoritma, uzun mesafeli geçişlerde "Yayla"ya çıkmayı tercih eder; bu, yerel trafikteki sıkışıklığı atlamak için yayla yollarını kullanma pratiğini taklit eder.

## Matematiksel Model

Bir arının $i$ düğümünden $j$ düğümüne geçme olasılığı $P_{ij}$ şu şekilde verilir:

$$ P_{ij} = \frac{\tau_{ij}^\alpha \cdot \eta_{ij}^\beta}{\sum_{k \in \text{izinli}} \tau_{ik}^\alpha \cdot \eta_{ik}^\beta} $$

Burada:
- $\tau_{ij}$: Feromon yoğunluğu (tarihsel başarı)
- $\eta_{ij}$: Sezgisel görünürlük ($1/d_{ij}$)
- $\alpha, \beta$: Kontrol parametreleri (`colony.yaml` içinde yapılandırılır)

## Arıza Kurtarma: "İnat" Modu
Eğer bir rota başarısız olursa, protokol **İnat Modu**na geçer. Geri adım atmaz; artırılmış feromon biriktirmesi ile yerel bir alternatif yolu brute-force (kaba kuvvet) ile dener ve "Buradan *illa ki* geçeceğiz" sinyali verir.

---
*Yazar: Bahattin Yunus Çetin - Mimar*
