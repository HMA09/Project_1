# Vektörel Bilişim - Python98 - Çok Fonksiyonlu Konsol Uygulaması Projesi
14.02.2025 - Menuler Oluşturulmaya Başlandı
14.02.2025 - Hesap Makinesi Fonksiyonu Eklendi (Şimdilik Basit Bir Tane Yazıldı Daha Sonra Hazır Hesap Makinesi ile Değiştirilebilir)
18.02.2025 - Otomatik Menü Sistemi ve Modüler Yapı Tasarımına Geçildi
Menülerin "menu.cfg" dosyasından okunarak otomatik oluşturlması sağlandı
"Ayarlar" ve "Geri"/"Çıkış" seçenekleri sSabit Olarak Eklendi
Genel ayarların "config.cfg" dosyasından okunması sağlandı
"config.cfg" mevcut olamasa programın dahi varsayılan ayarlarla çalışması ve otomatik "config.cfg" oluşturulması sağlandı
"config.cfg" dosyası ile farklı menü dosyaları yada aynı menu dosyası içerisinde farklı ana menülerin aktifleştirilebilmesi sağlandı
"menu.cfg" dosyasındaki seçenekler ile otomatik olarak iilgili nesnenin çağırılması üzerinde çalışılıyor
Yeni tasarıma göre otomatik çerçeveli konsol ekranı sağlandı
Geri dön ve Çıkış eylemlerine sıra numarası yerine sabit olarak "0" seçeneği atandı
Menü görselliği ayarlar dosyasına bağlandı ve renklendirme için yeni fonksiyonlar eklendi. Sadeleştirildi
Ayrıca Gerektiğinde input alabilen menü harici Genel Maksatlı Çerçeve Oluşturma Ekranı Tasarlandı
İlk version için yazdığım hesap makinesi bu versiyona uyarlanıp ilk modül olarak entegre edildi (Geliştirme Devam Ediyor)
Hazır olarak indirilen Adam Asmaca Oyunu birkaç düzenleme yapılarak modül olarak eklendi
Modülden return varsa genel maksatlı çerçeveye alındı. Modül kendi içinde çalışıp bitmişse modül sonu uyarısı verildi
Eğer menü tanımlanmış ancak modül yok ise uyarı mesajı verildi
Eğer modül tanımlanmış ancak fonksiyon adı uyuşmuyor ise uyarı mesajı verildi (Modül Kurulum Klavuzunda Detaylı Anlatacağım)
Bir taş,kağıt,makas oyunu tam uyumlu modül örneği olacak şekilde yazılarak modül olarak eklendi
Modül Yükleyicinin "config.cfg" ilişkisi oluşturuldu
19.02.2025 - Ayarlar Yapısı tasarlanmaya başlandı ve ekran görünümleri ayawrlandı
Menü ve Info ekranları için max, min ve auto genişlikler düzenlendi
Program içinden ayarların değiştirilmesi entegrasyonu yapıldı geliştiriliyor.
Program içinden ayarların değiştirilmesi entegrasyonu tamamlandı
Modüllere gönderilen argümanlarda geliştirme yapıldı (Kullanma Klavuzu Videosunda Açıklanacak)
Hesap Makinesi Modülünde Geliştirmeler Yapıldı
Adam Asmaca Modülünde Geliştirmeler Yapıldı
Taş Kağıt Makas Modülündeki büyük-küçük harf duyarlılığı hatası düzeltildi
