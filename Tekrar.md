- ## 1. Temel Operatörler

    Python'da veriler üzerinde çeşitli işlemler yapmak için kullanılan özel sembollere **operatör** denir. Bu operatörler, matematiksel hesaplamalardan mantıksal karşılaştırmalara kadar geniş bir yelpazede kullanılır.

    ### a. Aritmetik Operatörler

    **Teorik Açıklama:** Sayısal verilerle temel matematiksel işlemleri (toplama, çıkarma, çarpma, bölme vb.) yapmak için kullanılır.

    **Pratik Kod Örnekleri:**

    *Örnek 1: Toplama, Çıkarma, Çarpma*
    ```python
    a = 10
    b = 3

    toplam = a + b  # İki sayıyı toplar
    fark = a - b    # a'dan b'yi çıkarır
    carpim = a * b  # İki sayıyı çarpar

    print(f"Toplam: {toplam}")
    print(f"Fark: {fark}")
    print(f"Çarpım: {carpim}")
    ```
    **Çıktı:**
    ```
    Toplam: 13
    Fark: 7
    Çarpım: 30
    ```

    *Örnek 2: Bölme, Mod Alma, Üs Alma*
    ```python
    a = 10
    b = 3

    bolum = a / b          # Normal bölme, sonucu float olarak verir
    tam_bolum = a // b     # Tam sayı bölmesi, ondalık kısmı atar
    mod = a % b            # Bölümden kalanı verir (mod alma)
    us = a ** b           # a'nın b'ninci kuvvetini alır

    print(f"Bölüm: {bolum}")
    print(f"Tam Bölüm: {tam_bolum}")
    print(f"Mod: {mod}")
    print(f"Üs: {us}")
    ```
    **Çıktı:**
    ```
    Bölüm: 3.3333333333333335
    Tam Bölüm: 3
    Mod: 1
    Üs: 1000
    ```

    ### b. Karşılaştırma Operatörleri

    **Teorik Açıklama:** İki değeri birbiriyle karşılaştırarak aralarındaki ilişkiyi (eşitlik, büyüklük vb.) kontrol eder. Sonuç her zaman `True` (doğru) veya `False` (yanlış) olarak bir boolean değerdir.

    **Pratik Kod Örnekleri:**

    *Örnek 1: Eşitlik ve Eşitsizlik*
    ```python
    x = 5
    y = 5
    z = 6

    print(f"x == y: {x == y}") # x, y'ye eşit mi?
    print(f"x != z: {x != z}") # x, z'ye eşit değil mi?
    ```
    **Çıktı:**
    ```
    x == y: True
    x != z: True
    ```

    *Örnek 2: Büyüklük ve Küçüklük*
    ```python
    x = 10
    y = 15

    print(f"x > y: {x > y}")   # x, y'den büyük mü?
    print(f"x < y: {x < y}")   # x, y'den küçük mü?
    print(f"x >= 10: {x >= 10}") # x, 10'dan büyük veya eşit mi?
    print(f"y <= 10: {y <= 10}") # y, 10'dan küçük veya eşit mi?
    ```
    **Çıktı:**
    ```
    x > y: False
    x < y: True
    x >= 10: True
    y <= 10: False
    ```

    ### c. Mantıksal Operatörler (and, or, not)

    **Teorik Açıklama:** Birden fazla boolean ifadeyi birleştirerek daha karmaşık koşullar oluşturmayı sağlar.
    - `and`: Her iki koşul da `True` ise `True` döner.
    - `or`: Koşullardan en az biri `True` ise `True` döner.
    - `not`: Bir ifadenin boolean değerini tersine çevirir (`True` ise `False`, `False` ise `True` yapar).

    **Pratik Kod Örnekleri:**

    ```python
    yas = 20
    mezun_mu = True

    # İşe alım senaryosu: 18 yaşından büyük VE mezun olmalı
    ise_alim_uygun = (yas > 18) and (mezun_mu == True)
    print(f"İşe alım için uygun mu? {ise_alim_uygun}")

    # İndirim senaryosu: 65 yaşından büyük VEYA öğrenci olmalı
    ogrenci_mi = False
    indirim_uygun = (yas > 65) or (ogrenci_mi == True)
    print(f"İndirim için uygun mu? {indirim_uygun}")

    # Giriş kontrolü: Giriş izni yoksa
    giris_izni_var = False
    print(f"Giriş yapabilir mi? {not giris_izni_var}")
    ```
    **Çıktı:**
    ```
    İşe alım için uygun mu? True
    İndirim için uygun mu? False
    Giriş yapabilir mi? True
    ```

    ### d. `is` ve `==` Farkı

    **Teorik Açıklama:**
    - `==` (Değer Eşitliği): İki değişkenin **değerlerinin** aynı olup olmadığını kontrol eder.
    - `is` (Kimlik Eşitliği): İki değişkenin bellekte **aynı objeyi** gösterip göstermediğini kontrol eder. Yani, bellek adreslerinin aynı olup olmadığına bakar.

    **Pratik Kod Örnekleri:**

    ```python
    # Küçük tamsayılar ve stringler genellikle bellekte önbelleğe alınır
    a = 256
    b = 256
    print(f"a == b: {a == b}") # Değerler aynı
    print(f"a is b: {a is b}") # Bellekte aynı objeyi gösteriyorlar (genellikle)

    # Listeler her zaman farklı objeler olarak oluşturulur
    liste1 = [1, 2, 3]
    liste2 = [1, 2, 3]
    print(f"liste1 == liste2: {liste1 == liste2}") # Değerler (içerik) aynı
    print(f"liste1 is liste2: {liste1 is liste2}") # Ama bellekte farklı objeler

    liste3 = liste1 # liste3, liste1'in gösterdiği objenin aynısını gösterir
    print(f"liste1 is liste3: {liste1 is liste3}") # Şimdi ikisi de aynı obje
    ```
    **Çıktı:**
    ```
    a == b: True
    a is b: True
    liste1 == liste2: True
    liste1 is liste2: False
    liste1 is liste3: True
    ```

    ### e. Operatör Önceliği ve Short-Circuit

    **Teorik Açıklama:**
    - **Operatör Önceliği:** Tıpkı matematikteki gibi, Python'da da operatörlerin bir işlem sırası vardır. Örneğin, `*` ve `/` işlemleri `+` ve `-`'den önce yapılır. Parantezler `()` kullanılarak bu sıra değiştirilebilir.
    - **Short-Circuit (Kısa Devre):** Mantıksal operatörler (`and`, `or`) sonucu belirlemek için gerekenden fazla ifadeyi değerlendirmez.
        - `and` için: İlk ifade `False` ise, ikinci ifadeye bakmadan sonuç `False` olur.
        - `or` için: İlk ifade `True` ise, ikinci ifadeye bakmadan sonuç `True` olur. Bu, özellikle ikinci ifadenin hata verebileceği durumlarda kullanışlıdır.

    **Pratik Kod Örnekleri:**

    *Örnek 1: Operatör Önceliği*
    ```python
    # Önce çarpma, sonra toplama yapılır
    sonuc = 5 + 2 * 3
    print(f"5 + 2 * 3 = {sonuc}") # Beklenen: 11

    # Parantez ile öncelik değiştirme
    sonuc_parantezli = (5 + 2) * 3
    print(f"(5 + 2) * 3 = {sonuc_parantezli}") # Beklenen: 21
    ```
    **Çıktı:**
    ```
    5 + 2 * 3 = 11
    (5 + 2) * 3 = 21
    ```

    *Örnek 2: Short-Circuit*
    ```python
    def ikinci_fonksiyon():
        print("İkinci fonksiyon çalıştı")
        return True

    # 'and' ile kısa devre
    print("--- AND Testi ---")
    deger = False and ikinci_fonksiyon() # İlk ifade False olduğu için ikinci_fonksiyon hiç çağrılmaz
    print(f"Sonuç: {deger}")

    # 'or' ile kısa devre
    print("\n--- OR Testi ---")
    deger = True or ikinci_fonksiyon() # İlk ifade True olduğu için ikinci_fonksiyon hiç çağrılmaz
    print(f"Sonuç: {deger}")
    ```
    **Çıktı:**
    ```
    --- AND Testi ---
    Sonuç: False

    --- OR Testi ---
    Sonuç: True
    ```

    ---


## 2. Temel Kavramlar

Bu bölümde, Python programlamanın temel taşlarını oluşturan bazı anahtar fonksiyonlar ve konseptler ele alınacaktır.

### a. `type()` ve `isinstance()` Kullanımı

**Teorik Açıklama:**
- `type()`: Bir değişkenin veya nesnenin tam olarak hangi veri tipine ait olduğunu döndürür. Genellikle bir nesnenin tipini doğrudan öğrenmek için kullanılır.
- `isinstance()`: Bir nesnenin, belirtilen bir sınıfın veya bu sınıfın alt sınıflarından birinin örneği olup olmadığını kontrol eder. Daha esnek bir tip kontrolü sağlar ve genellikle polimorfizm (çok biçimlilik) durumlarında tercih edilir.

**Pratik Kod Örnekleri:**

*Örnek 1: `type()` ile Veri Tipini Öğrenme*
```python
sayi = 10
metin = "Merhaba"
liste = [1, 2, 3]

print(f"'sayi' değişkeninin tipi: {type(sayi)}")
print(f"'metin' değişkeninin tipi: {type(metin)}")
print(f"'liste' değişkeninin tipi: {type(liste)}")
```
**Çıktı:**
```
'sayi' değişkeninin tipi: <class 'int'>
'metin' değişkeninin tipi: <class 'str'>
'liste' değişkeninin tipi: <class 'list'>
```

*Örnek 2: `isinstance()` ile Tip Kontrolü*
```python
veri = 15.5

# veri bir float mı?
if isinstance(veri, float):
    print("Değişken bir float.")

# veri bir int veya float mı? (Birden fazla tip kontrolü)
if isinstance(veri, (int, float)):
    print("Değişken sayısal bir değerdir (int veya float).")
```
**Çıktı:**
```
Değişken bir float.
Değişken sayısal bir değerdir (int veya float).
```

### b. Tip Dönüşümleri (Type Casting)

**Teorik Açıklama:** Bir veri tipini başka bir veri tipine dönüştürme işlemidir. Örneğin, kullanıcıdan alınan bir metin (string) girdisini matematiksel işlem yapmak için bir sayıya (integer veya float) dönüştürmek gerekebilir.

**Pratik Kod Örnekleri:**

```python
# String'i integer'a dönüştürme
str_sayi = "123"
int_sayi = int(str_sayi)
print(f"String '{str_sayi}' -> Integer: {int_sayi}")

# Integer'ı float'a dönüştürme
rakam = 10
float_rakam = float(rakam)
print(f"Integer {rakam} -> Float: {float_rakam}")

# Float'ı integer'a dönüştürme (ondalık kısım atılır)
ondalikli_sayi = 9.8
int_ondalikli = int(ondalikli_sayi)
print(f"Float {ondalikli_sayi} -> Integer: {int_ondalikli}")

# Sayıyı string'e dönüştürme
numara = 500
str_numara = str(numara)
print(f"Integer {numara} -> String: '{str_numara}'")
```
**Çıktı:**
```
String '123' -> Integer: 123
Integer 10 -> Float: 10.0
Float 9.8 -> Integer: 9
Integer 500 -> String: '500'
```

### c. Girdi/Çıktı İşlemleri (`input()` ve `print()`)

**Teorik Açıklama:**
- `input()`: Programın kullanıcıdan veri almasını sağlar. Kullanıcıdan alınan her veri, program tarafından **string** olarak okunur.
- `print()`: Ekrana veri (metin, sayı, değişken değeri vb.) yazdırmak için kullanılır.

**Pratik Kod Örnekleri:**

*Örnek 1: Kullanıcıdan Bilgi Alıp Ekrana Yazdırma*
```python
# Kullanıcıdan ismini al
isim = input("Lütfen adınızı girin: ")

# Kullanıcıyı selamla
print(f"Merhaba, {isim}! Python dünyasına hoş geldin.")
```
**Örnek Çalışma:**
```
Lütfen adınızı girin: Ali
Merhaba, Ali! Python dünyasına hoş geldin.
```

*Örnek 2: Sayısal Girdi Alıp İşlem Yapma*
```python
# Kullanıcıdan doğum yılını string olarak al
dogum_yili_str = input("Doğum yılınızı girin: ")

# Tip dönüşümü yaparak string'i integer'a çevir
dogum_yili_int = int(dogum_yili_str)

# Yaşı hesapla
guncel_yil = 2024
yas = guncel_yil - dogum_yili_int

# Sonucu ekrana yazdır
print(f"Yaklaşık olarak {yas} yaşındasınız.")
```
**Örnek Çalışma:**
```
Doğum yılınızı girin: 1995
Yaklaşık olarak 29 yaşındasınız.
```

---



## 3. Kontrol Akışı

**Gerçek Hayat Senaryosu:**
Bir e-ticaret sitesinde olduğunuzu düşünün. Sepetinizdeki ürünlerin toplam tutarı belirli bir limitin (örneğin 200 TL) üzerindeyse kargo ücretsiz oluyor, değilse kargo ücreti ekleniyor. İşte bu kararı vermek için **if-else** yapısı kullanılır. Ardından, sepetinizdeki her bir ürünü ekrana yazdırmak için bir **for döngüsü** kullanılır. Eğer bir ürün stokta kalmamışsa, **while döngüsü** ile stok güncellenene kadar bekleme simülasyonu yapılabilir. Kontrol akışı, programların bu gibi kararları almasını ve belirli işlemleri tekrar etmesini sağlar.

### a. Karar Yapıları (if, elif, else)

**Teorik Açıklama:** Programın akışını belirli koşullara göre yönlendiren yapılardır.
- `if`: Bir koşul doğruysa (`True`) belirtilen kod bloğunu çalıştırır.
- `elif` (else if): Önceki `if` veya `elif` koşulları yanlışsa ve kendi koşulu doğruysa çalışır. Birden fazla alternatif durum için kullanılır.
- `else`: Yukarıdaki hiçbir koşul doğru değilse çalışacak olan varsayılan kod bloğudur.

**Pratik Kod Örnekleri:**

*Örnek 1: Not Değerlendirme Sistemi*
```python
not_degeri = 75

if not_degeri >= 90:
    harf_notu = "AA"
elif not_degeri >= 80:
    harf_notu = "BA"
elif not_degeri >= 70:
    harf_notu = "BB"
elif not_degeri >= 60:
    harf_notu = "CB"
else:
    harf_notu = "FF" # Geriye kalan tüm durumlar (60'dan küçük)

print(f"Öğrencinin harf notu: {harf_notu}")
```
**Çıktı:**
```
Öğrencinin harf notu: BB
```

*Örnek 2: Kullanıcı Girişi Kontrolü*
```python
kullanici_adi = "admin"
parola = "12345"

girilen_ad = input("Kullanıcı adınızı girin: ")
girilen_parola = input("Parolanızı girin: ")

if girilen_ad == kullanici_adi and girilen_parola == parola:
    print("Giriş başarılı!")
elif girilen_ad == kullanici_adi and girilen_parola != parola:
    print("Parola yanlış.")
else:
    print("Kullanıcı adı veya parola hatalı.")
```
**Örnek Çalışma:**
```
Kullanıcı adınızı girin: admin
Parolanızı girin: 1234
Giriş başarılı!
```

### b. Ternary Operatör (Kısa if-else)

**Teorik Açıklama:** Tek satırda basit bir `if-else` koşulu yazmayı sağlayan bir operatördür. Genellikle bir değişkene koşula bağlı olarak değer atamak için kullanılır. Yapısı: `deger_dogru_ise if kosul else deger_yanlis_ise`.

**Pratik Kod Örnekleri:**

```python
yas = 22

# Geleneksel if-else ile
if yas >= 18:
    durum = "Yetişkin"
else:
    durum = "Çocuk"

# Ternary operatör ile aynı işlem
durum_kisa = "Yetişkin" if yas >= 18 else "Çocuk"

print(f"Geleneksel yöntem: {durum}")
print(f"Ternary operatör: {durum_kisa}")
```
**Çıktı:**
```
Geleneksel yöntem: Yetişkin
Ternary operatör: Yetişkin
```

### c. Döngüler (for, while)

**Teorik Açıklama:** Belirli bir kod bloğunu tekrar tekrar çalıştırmak için kullanılır.
- `for`: Bir dizi (liste, tuple, string vb.) veya yinelenebilir (iterable) bir nesnenin her bir elemanı üzerinde gezinmek için kullanılır. Tekrar sayısı genellikle dizinin eleman sayısıyla sınırlıdır.
- `while`: Belirli bir koşul `True` olduğu sürece çalışmaya devam eder. Koşul `False` olduğunda döngü sona erer. Döngünün bir noktada sona ermesi için koşulun değişmesini sağlayan bir mantık içermesi gerekir, aksi takdirde **sonsuz döngü** oluşur.

**Pratik Kod Örnekleri:**

*Örnek 1: `for` ile Liste Elemanlarını Yazdırma*
```python
meyveler = ["elma", "armut", "çilek"]

print("Sepetteki meyveler:")
for meyve in meyveler:
    print(f"- {meyve}")
```
**Çıktı:**
```
Sepetteki meyveler:
- elma
- armut
- çilek
```

*Örnek 2: `while` ile Geri Sayım*
```python
sayac = 5

print("Geri sayım başlıyor...")
while sayac > 0:
    print(sayac)
    sayac -= 1 # sayac değişkenini her adımda bir azaltarak döngünün bitmesini sağlıyoruz

print("Fırlat!")
```
**Çıktı:**
```
Geri sayım başlıyor...
5
4
3
2
1
Fırlat!
```

*Örnek 3: `break` ve `continue` Kullanımı*
- `break`: İçinde bulunduğu döngüyü tamamen sonlandırır.
- `continue`: Döngünün mevcut adımını atlar ve bir sonraki adıma geçer.

```python
# 1'den 10'a kadar olan sayılardan 5'i atlayıp, 8'e gelince döngüyü bitirelim
for i in range(1, 11):
    if i == 5:
        print("(5 atlandı)")
        continue # Bu adımı atla, döngüye devam et
    if i == 8:
        print("Döngü 8'de sonlandırıldı.")
        break # Döngüyü tamamen bitir
    print(f"Sayı: {i}")
```
**Çıktı:**
```
Sayı: 1
Sayı: 2
Sayı: 3
Sayı: 4
(5 atlandı)
Sayı: 6
Sayı: 7
Döngü 8'de sonlandırıldı.
```

---



## 4. Veri Yapıları

**Gerçek Hayat Senaryosu:**
Bir sosyal medya uygulamasında, bir kullanıcının arkadaşlarını bir **liste** içinde saklayabilirsiniz çünkü arkadaş listesi zamanla değişebilir (yeni arkadaş ekleme/çıkarma). Bir ülkenin coğrafi koordinatlarını (enlem, boylam) bir **tuple** içinde saklamak mantıklıdır çünkü bu değerler sabittir. Bir kullanıcının takip ettiği etiketleri bir **set** içinde tutabilirsiniz çünkü her etiket benzersiz olmalıdır ve sırası önemli değildir. Bir kullanıcının profil bilgilerini (ad: "Ali", yaş: 30, şehir: "İstanbul") bir **dictionary** içinde saklamak en uygunudur çünkü her bilgi bir anahtar (ad, yaş) ile etiketlenmiştir.

### a. List

**Teorik Açıklama:** Sıralı ve değiştirilebilir bir veri koleksiyonudur. Elemanlar köşeli parantezler `[]` içinde virgülle ayrılarak tanımlanır. Listeler, farklı veri tiplerini bir arada tutabilir ve elemanları eklenebilir, silinebilir veya değiştirilebilir.

**Pratik Kod Örnekleri:**

*Örnek 1: Liste Oluşturma ve Elemanlara Erişme*
```python
# Bir alışveriş listesi oluşturalım
alisveris_listesi = ['elma', 'süt', 'ekmek', 'peynir']

# İlk elemana erişme (indeksler 0'dan başlar)
print(f"Listenin ilk elemanı: {alisveris_listesi[0]}")

# Son elemana erişme
print(f"Listenin son elemanı: {alisveris_listesi[-1]}")
```
**Çıktı:**
```
Listenin ilk elemanı: elma
Listenin son elemanı: peynir
```

*Örnek 2: Listeyi Değiştirme (Ekleme, Silme, Güncelleme)*
```python
alisveris_listesi = ['elma', 'süt', 'ekmek']

# Listeye yeni eleman ekleme
alisveris_listesi.append('zeytin')
print(f"Yeni liste: {alisveris_listesi}")

# Belirli bir elemanı silme
alisveris_listesi.remove('süt')
print(f"'süt' silindikten sonra: {alisveris_listesi}")

# Belirli bir indeksteki elemanı güncelleme
alisveris_listesi[0] = 'kırmızı elma'
print(f"Güncellenmiş liste: {alisveris_listesi}")
```
**Çıktı:**
```
Yeni liste: ['elma', 'süt', 'ekmek', 'zeytin']
'süt' silindikten sonra: ['elma', 'ekmek', 'zeytin']
Güncellenmiş liste: ['kırmızı elma', 'ekmek', 'zeytin']
```

### b. Tuple

**Teorik Açıklama:** Sıralı ve **değiştirilemez** bir veri koleksiyonudur. Elemanlar normal parantezler `()` içinde tanımlanır. Tanımlandıktan sonra içeriği değiştirilemediği için, program içinde sabit kalması gereken veriler için kullanılır (örneğin, haftanın günleri, koordinatlar).

**Pratik Kod Örnekleri:**

```python
# Bir noktanın (x, y, z) koordinatları
koordinatlar = (10, 20, 30)

# Elemanlara erişim listelerle aynıdır
print(f"X koordinatı: {koordinatlar[0]}")

# Tuple'ın içeriğini değiştirmeye çalışmak hata verir
# koordinatlar[0] = 15  # Bu satır TypeError hatası verir

# Tuple unpacking (elemanları değişkenlere atama)
x, y, z = koordinatlar
print(f"x: {x}, y: {y}, z: {z}")
```
**Çıktı:**
```
X koordinatı: 10
x: 10, y: 20, z: 30
```

### c. Set

**Teorik Açıklama:** Sırasız ve benzersiz (unique) elemanlardan oluşan bir koleksiyondur. Süslü parantezler `{}` ile tanımlanır. Bir elemanın bir koleksiyonda olup olmadığını hızlıca kontrol etmek ve tekrar eden elemanları bir listeden kaldırmak için çok kullanışlıdır.

**Pratik Kod Örnekleri:**

*Örnek 1: Set Oluşturma ve Tekrar Eden Elemanları Temizleme*
```python
rakamlar_listesi = [1, 2, 2, 3, 4, 4, 4, 5]
benzersiz_rakamlar = set(rakamlar_listesi)

print(f"Orijinal liste: {rakamlar_listesi}")
print(f"Benzersiz elemanlar (set): {benzersiz_rakamlar}")
```
**Çıktı:**
```
Orijinal liste: [1, 2, 2, 3, 4, 4, 4, 5]
Benzersiz elemanlar (set): {1, 2, 3, 4, 5}
```

*Örnek 2: Set Operasyonları (Birleşim, Kesişim)*
```python
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Birleşim: İki setteki tüm benzersiz elemanlar
birlesim = set_a.union(set_b)
print(f"Birleşim: {birlesim}")

# Kesişim: Her iki sette de ortak olan elemanlar
kesisim = set_a.intersection(set_b)
print(f"Kesişim: {kesisim}")
```
**Çıktı:**
```
Birleşim: {1, 2, 3, 4, 5, 6}
Kesişim: {3, 4}
```

### d. Dictionary

**Teorik Açıklama:** Anahtar-değer (key-value) çiftlerinden oluşan sırasız (Python 3.7+ sürümlerinde sıralı) ve değiştirilebilir bir koleksiyondur. Her bir değere, ona özel olan bir anahtar ile erişilir. Süslü parantezler `{}` içinde `anahtar: deger` formatında tanımlanır.

**Pratik Kod Örnekleri:**

*Örnek 1: Dictionary Oluşturma ve Değerlere Erişme*
```python
# Bir kişinin profil bilgileri
kullanici_profili = {
    "ad": "Ayşe",
    "yas": 28,
    "sehir": "Ankara",
    "meslek": "Mühendis"
}

# Bir değere anahtarı ile erişme
print(f"Kullanıcının adı: {kullanici_profili['ad']}")

# get() metodu ile daha güvenli erişim (anahtar yoksa hata vermez)
print(f"Kullanıcının hobileri: {kullanici_profili.get('hobiler', 'Belirtilmemiş')}")
```
**Çıktı:**
```
Kullanıcının adı: Ayşe
Kullanıcının hobileri: Belirtilmemiş
```

*Örnek 2: Dictionary'i Değiştirme*
```python
kullanici_profili = {
    "ad": "Ayşe",
    "yas": 28
}

# Yeni bir anahtar-değer çifti ekleme
kullanici_profili['sehir'] = "İzmir"
print(f"Güncellenmiş profil: {kullanici_profili}")

# Mevcut bir değeri güncelleme
kullanici_profili['yas'] = 29
print(f"Yaş güncellendi: {kullanici_profili}")

# Bir anahtar-değer çiftini silme
del kullanici_profili['ad']
print(f"Ad silindi: {kullanici_profili}")
```
**Çıktı:**
```
Güncellenmiş profil: {'ad': 'Ayşe', 'yas': 28, 'sehir': 'İzmir'}
Yaş güncellendi: {'ad': 'Ayşe', 'yas': 29, 'sehir': 'İzmir'}
Ad silindi: {'yas': 29, 'sehir': 'İzmir'}
```

---



## 5. Fonksiyonlar

**Gerçek Hayat Senaryosu:**
Bir programda, kullanıcının yaşını sık sık hesaplamanız gerektiğini düşünün. Her seferinde `guncel_yil - dogum_yili` kodunu tekrar tekrar yazmak yerine, bu işlemi yapan `yas_hesapla()` adında bir **fonksiyon** yazarsınız. Artık yaş hesaplamanız gerektiğinde sadece bu fonksiyonu çağırmanız yeterlidir. Eğer bu fonksiyona bazen ek bilgiler (örneğin, gelecekteki bir yıldaki yaşını hesaplamak için) göndermeniz gerekirse, bunu **argümanlar** (`*args`, `**kwargs`) ile esnek bir şekilde yapabilirsiniz. Fonksiyonlar, kod tekrarını önler, programı daha modüler ve okunabilir hale getirir.

### a. Değer Döndüren ve Döndürmeyen Fonksiyonlar

**Teorik Açıklama:**
- **Değer Döndürmeyen (void) Fonksiyonlar:** Belirli bir işi yaparlar ancak geriye bir sonuç değeri döndürmezler. Genellikle ekrana bir şey yazdırmak veya bir dosya üzerinde değişiklik yapmak gibi eylemler için kullanılırlar. `return` ifadesi kullanılmaz veya tek başına kullanılır.
- **Değer Döndüren Fonksiyonlar:** Bir hesaplama veya işlem yapıp, sonucunu `return` anahtar kelimesiyle çağrıldığı yere geri gönderirler. Bu dönen değer, bir değişkene atanabilir veya başka bir ifadede kullanılabilir.

**Pratik Kod Örnekleri:**

*Örnek 1: Değer Döndürmeyen Fonksiyon (Selamlama)*
```python
def selamla(isim):
    # Bu fonksiyon sadece ekrana bir mesaj yazar, bir değer döndürmez.
    print(f"Merhaba, {isim}!")

# Fonksiyonu çağırma
selamla("Ahmet")
```
**Çıktı:**
```
Merhaba, Ahmet!
```

*Örnek 2: Değer Döndüren Fonksiyon (Toplama)*
```python
def topla(a, b):
    # a ve b'nin toplamını hesaplar ve sonucu geri döndürür.
    sonuc = a + b
    return sonuc

# Fonksiyondan dönen değeri bir değişkene atama
toplam_deger = topla(10, 20)
print(f"İki sayının toplamı: {toplam_deger}")

# Dönen değeri doğrudan başka bir işlemde kullanma
print(f"Sonucun iki katı: {topla(5, 3) * 2}")
```
**Çıktı:**
```
İki sayının toplamı: 30
Sonucun iki katı: 16
```

### b. Argüman Çeşitleri (Positional, *args, **kwargs)

**Teorik Açıklama:** Fonksiyonlara veri aktarmak için kullanılan parametrelerin farklı türleri vardır.
- **Positional Arguments (Konumsal Argümanlar):** Fonksiyon tanımındaki sırayla eşleşen, en temel argüman türüdür.
- `*args` (Non-Keyword Arguments): Fonksiyona belirsiz sayıda konumsal argüman göndermeyi sağlar. Bu argümanlar fonksiyon içinde bir **tuple** olarak toplanır.
- `**kwargs` (Keyword Arguments): Fonksiyona belirsiz sayıda anahtar-değer çifti şeklinde argüman göndermeyi sağlar. Bu argümanlar fonksiyon içinde bir **dictionary** olarak toplanır.

**Pratik Kod Örnekleri:**

*Örnek 1: Konumsal Argümanlar*
```python
def kullanici_bilgisi(ad, soyad, yas):
    print(f"Ad: {ad}, Soyad: {soyad}, Yaş: {yas}")

# Argümanlar sırayla gönderilir
kullanici_bilgisi("Mehmet", "Yılmaz", 35)
```
**Çıktı:**
```
Ad: Mehmet, Soyad: Yılmaz, Yaş: 35
```

*Örnek 2: `*args` Kullanımı*
```python
def sayilari_topla(*args):
    # args burada bir tuple'dır (örneğin, (1, 2, 3, 4, 5))
    print(f"Gelen sayılar (tuple): {args}")
    toplam = 0
    for sayi in args:
        toplam += sayi
    return toplam

# Fonksiyona istediğimiz kadar sayı gönderebiliriz
print(f"Toplam: {sayilari_topla(1, 2, 3)}")
print(f"Toplam: {sayilari_topla(10, 20, 30, 40, 50)}")
```
**Çıktı:**
```
Gelen sayılar (tuple): (1, 2, 3)
Toplam: 6
Gelen sayılar (tuple): (10, 20, 30, 40, 50)
Toplam: 150
```

*Örnek 3: `**kwargs` Kullanımı*
```python
def profil_olustur(**kwargs):
    # kwargs burada bir dictionary'dir
    print("--- Kullanıcı Profili ---")
    for anahtar, deger in kwargs.items():
        print(f"{anahtar.capitalize()}: {deger}")

# Fonksiyona istediğimiz kadar anahtar-değer bilgisi gönderebiliriz
profil_olustur(ad="Zeynep", sehir="İstanbul", meslek="Doktor", yas=42)
profil_olustur(kullanici_adi="coder123", email="coder@example.com")
```
**Çıktı:**
```
--- Kullanıcı Profili ---
Ad: Zeynep
Sehir: İstanbul
Meslek: Doktor
Yas: 42
--- Kullanıcı Profili ---
Kullanici_adi: coder123
Email: coder@example.com
```

*Örnek 4: Tüm Argüman Türlerini Birlikte Kullanma*
```python
def her_seyi_kullan(konumsal_arg, *args, **kwargs):
    print(f"Zorunlu Konumsal Argüman: {konumsal_arg}")
    print(f"Ekstra Konumsal Argümanlar (*args): {args}")
    print(f"Anahtar-Değer Argümanları (**kwargs): {kwargs}")

her_seyi_kullan("Merhaba", 10, 20, 30, ad="Ali", yas=25)
```
**Çıktı:**
```
Zorunlu Konumsal Argüman: Merhaba
Ekstra Konumsal Argümanlar (*args): (10, 20, 30)
Anahtar-Değer Argümanları (**kwargs): {'ad': 'Ali', 'yas': 25}
```

---

