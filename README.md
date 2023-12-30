# Korelasyon nedir?
Korelasyon, istatistiksel bir terimdir ve genellikle iki değişken arasındaki ilişkiyi ifade eder. İki değişken arasındaki ilişkinin gücünü ve yönünü ölçmek için kullanılan bir istatistiksel ölçüdür. Korelasyon, bu ilişkinin ne kadar güçlü olduğunu ve eğer varsa, hangi yönde olduğunu belirtir.

>Niçin Kullanılır?
>Korelasyon analizi, istatistiksel ilişkileri anlamak ve veriler arasındaki ilişkileri ölçmek için kullanılır.

Korelasyonun mutlak değeri, ilişkinin gücünü gösterirken işaret ise ilişkinin yönünü gösterir. Yani bir korelasyon katsayısı ne kadar büyükse, ilişki o kadar güçlüdür. Pozitif bir korelasyon katsayısı, değişkenler arasında pozitif bir ilişki olduğunu gösterirken, negatif bir korelasyon katsayısı ise negatif bir ilişki olduğunu gösterir.

## Pearson Katsayısı
Korelasyon genellikle Pearson korelasyon katsayısı olarak adlandırılan bir ölçüyle ifade edilir. Pearson korelasyon katsayısı, -1 ile 1 arasında bir değer alır.

* 1, mükemmel negatif bir ilişkiyi (-1'e yaklaştıkça, değişkenler arasındaki ilişki daha güçlü bir şekilde negatif yönlüdür)
* 0, iki değişken arasında hiçbir ilişki olmadığını (düz bir çizgi)
* 1, mükemmel pozitif bir ilişkiyi (1'e yaklaştıkça, değişkenler arasındaki ilişki daha güçlü bir şekilde pozitif yönlüdür) ifade eder.

## Avantajları?
1. İlişkiyi Ölçmek: Korelasyon, iki değişken arasındaki ilişkiyi ölçer. Bu, değişkenler arasındaki ilişkinin gücünü ve yönünü anlamamıza yardımcı olur. 
2. Öngörü Gücü: Korelasyon, bir değişkenin diğerine olan etkisini öngörmemize yardımcı olabilir. Yüksek korelasyon, bir değişkenin diğerine daha güçlü bir şekilde etki ettiğini gösterebilir.
3. Veri Analizi ve Keşif: Korelasyon, veri analizinde kullanılarak değişkenler arasındaki ilişkileri keşfetmemize yardımcı olur. Bu, veri setindeki önemli ilişkileri anlamamıza ve veri keşfi yapmamıza olanak tanır.

## Dezavantajları?
1. Neden-Sonuç İlişkisi: Korelasyon, iki değişken arasında bir ilişki olduğunu gösterir, ancak bu ilişkinin neden-sonuç ilişkisi olup olmadığını belirtmez.2. İki değişken arasında korelasyon bulunması, birinin diğerini doğrudan etkilediği anlamına gelmez.
3. Ek Açıklama İhtiyacı: Korelasyon, genellikle ek açıklama ve analiz gerektirir. İki değişken arasında korelasyon bulunması, diğer değişkenlerin etkisinin  göz ardı edildiği anlamına gelmez.
4. Sınırlı Kapsam: Korelasyon, sadece iki değişken arasındaki ilişkiyi ölçer. Ancak bir veri setinde birden fazla değişkenin etkileşimi olabilir ve bu etkileşimleri korelasyon analiziyle ölçmek zor olabilir.

>Korelasyon analizi genellikle ek analizlerle birlikte kullanılır ve tek başına bir veri setinin tüm özelliklerini anlamak için yeterli olmayabilir. Ancak, doğru şekilde kullanıldığında, korelasyon analizi veri setindeki ilişkileri anlamak ve keşfetmek için güçlü bir araç olabilir.

---

# Pearson Korelasyon Katsayısı Nasıl Hesaplanır?

```Python
def calculate_r(x, y):
    mean_x = sum(x) / len(x)
    a = [(x_i - mean_x) ** 2 for x_i in x]
    b = sum(a) / len(a)
    sd_x = b ** 0.5

    mean_y = sum(y) / len(y)
    a = [(y_i - mean_y) ** 2 for y_i in y]
    b = sum(a) / len(a)
    sd_y = b ** 0.5

    t = 0
    for i in range(len(x)):
        x_z_or_standard_value = (x[i] - mean_x) / sd_x
        y_z_or_standard_value = (y[i] - mean_y) / sd_y
        t = t + x_z_or_standard_value * y_z_or_standard_value

    return t / len(x)
```

`calculate_r()` fonksiyonu, verilen x ve y listeleri için Pearson korelasyon katsayısını (r) hesaplamak için kullanılır. Sırasıyla yaptığı işler;
1. `mean_x` ve `mean_y` değişkenleri, `x` ve `y` listelerinin ortalamalarını hesaplar.
2. `a` ve `b` değişkenleri, `x` ve `y` listelerindeki değerlerin varyanslarını hesaplar.
3. `sd_x` ve `sd_y` değişkenleri, `x` ve `y` listelerindeki değerlerin standart sapmalarını hesaplar.
4. Bir döngü içinde, her bir `x[i]` ve `y[i]` değerinin standart sapma ile bölünmüş halinin çarpımını toplar.
5. Toplamı, listenin uzunluğuna bölerek Pearson korelasyon katsayısını hesaplar ve bu değeri döndürür.

## Hesaplama

```Python
x = [random.randint(20, 60) for i in range(20)]
y = [random.randint(50, 100) for i in range(20)]
plt.scatter(x, y, marker='x')
calculate_r(x, y)
print(calculate_r(x,y))
plt.show()
```
```Python
0.4364771706566383
```

<img src="/cıktı.png" alt="MarineGEO circle logo"/>

Bu kod bloğu aslında bir dizi farklı `x` ve `y` veri seti oluşturuyor ve her biri için Pearson korelasyon katsayısını hesaplıyor. Kodun her bölümünün ne yaptığını adım adım açıklayalım:

1. İlk olarak, `x` ve `y` listeleri rastgele oluşturuluyor ve `plt.scatter()` fonksiyonuyla bu veriler bir scatter plot (nokta grafiği) olarak görselleştiriliyor. Daha sonra, `calculate_r(x, y)` fonksiyonu çağrılarak `x` ve `y` veri setleri için Pearson korelasyon katsayısı hesaplanıyor ve bu değer ekrana yazdırılıyor. `plt.show()` fonksiyonu grafiği göstermek için kullanılıyor.

2. Bu işlem birkaç farklı `x` ve `y` veri seti için tekrarlanıyor. Her bir `x` ve `y` veri seti için aynı işlemler yapılıyor: veriler scatter plot olarak görselleştiriliyor, Pearson korelasyon katsayısı hesaplanıyor ve bu değer ekrana yazdırılıyor.

>Bu kod bloğu, farklı veri setleri üzerinde Pearson korelasyon katsayısının nasıl değiştiğini göstermek için kullanılıyor. `calculate_r()` fonksiyonu, veri setindeki değişkenler arasındaki ilişkinin gücünü ve yönünü ölçer ve bu ölçüm, scatter plot grafikleriyle görselleştirilir. Bu sayede, farklı veri setleri arasındaki ilişkilerin ne kadar güçlü olduğunu ve hangi yönde olduğunu görmemizi sağlar.