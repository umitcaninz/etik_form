import streamlit as st

# Sayfa başlığı
st.title("İnsan Üzerinde Yapılan Klinik Dışı Araştırmalar Başvuru Formu")

# 1. Başvurunun yapıldığı tarih
basvuru_tarihi = st.date_input("1. Başvurunun yapıldığı tarih:")

# 2. Başvuruyu geçerli kılmak için bilgi talebi tarihi
bilgi_talebi_tarihi = st.date_input("2. Başvuruyu geçerli kılmak için bilgi talebi tarihi:")

# 3. Ek bilgi talebi tarihi
ek_bilgi_talebi_tarihi = st.date_input("3. Ek bilgi talebi tarihi:")

# 4. Red/olumsuz görüş
red_gorus = st.text_area("4. Red/olumsuz görüş Nedenleri:")

# 4. Red/olumsuz görüş Tarih
red_gorus_tarihi = st.date_input("Red/olumsuz görüş Tarih:")

# 5. Geçerli başvuru tarihi
gecerli_basvuru_tarihi = st.date_input("5. Geçerli başvuru tarihi:")

# 5. İşlem başlangıç tarihi
islem_baslangic_tarihi = st.date_input("İşlem başlangıç tarihi:")

# 6. Ek bilgi/değiştirilmiş bilgi alınış tarihi
ek_bilgi_alinis_tarihi = st.date_input("6. Ek bilgi/değiştirilmiş bilgi alınış tarihi:")

# 7. Onay/olumlu görüş
onay_gorus = st.text_area("7. Onay/olumlu görüş:")

# 7. Onay/olumlu görüş Tarih
onay_gorus_tarihi = st.date_input("Onay/olumlu görüş Tarih:")

# 8. Başvuru arşiv kayıt numarası
arsiv_kayit_numarasi = st.text_input("8. Başvuru arşiv kayıt numarası:")

# 9. Başvuru geri çekildi mi?
geri_cekildi = st.radio("9. Başvuru geri çekildi mi?", ("Evet", "Hayır"))
geri_cekildi_tarih = st.date_input("Başvuru geri çekildi Tarih:")



# A. Araştırma Bölümü
st.header("A. Araştırma")

a1 = st.text_input("A.1. Başvurunun yapıldığı diğer ülkeler")
a2 = st.text_input("A.2. Araştırmanın açık adı")

a3 = st.radio("A.3. Yeniden başvuru mu?", ("Evet", "Hayır"))
a4 = st.radio("A.4. Araştırmada örselenebilir gruplar söz konusu mu?", ("Evet", "Hayır"))

st.subheader("A.5. Araştırmanın Niteliği")
a5_1 = st.checkbox("A.5.1. Bireysel araştırma projesi")
a5_2 = st.checkbox("A.5.2. Doktora Tezi")
a5_3 = st.checkbox("A.5.3. Uzmanlık Tezi")
a5_4 = st.checkbox("A.5.4. Yüksek Lisans Tezi")
a5_5 = st.text_input("A.5.5. Diğer (DPT, TÜBİTAK vb.)")

st.subheader("A.6. Araştırmanın Türü")
a6 = st.radio("Araştırmanın Türü", ("Nicel Araştırmalar", "Görgül Araştırmalar", "Diğer"))

st.subheader("A.7. Araştırmada Kullanılacak Veri Toplama Araç ve Yöntemleri")
a7_1 = st.checkbox("Anket")
a7_2 = st.checkbox("Mülakat")
a7_3 = st.checkbox("Gözlem")
a7_4 = st.checkbox("Bilgisayar Ortamında Test Uygulaması")
a7_5 = st.checkbox("Görüntü Kaydı")
a7_6 = st.checkbox("Ses Kaydı")
a7_7 = st.checkbox("Ölçek Geliştirme Çalışmaları")
a7_8 = st.checkbox("Dosya Taraması")
a7_9 = st.checkbox("Veri Kaynakları Taraması")
a7_10 = st.checkbox("Sistem Model Geliştirme Çalışması")
a7_11 = st.text_input("Diğer (belirtiniz)")



st.header("B. DESTEKLEYİCİ")

# B.1. Araştırmanın destekleyicisi var mı?
b1 = st.radio("B.1. Araştırmanın destekleyicisi var mı?", ("Evet", "Hayır"))

# Destekleyici var ise detaylar
if b1 == "Evet":
    b1_1 = st.checkbox("B.1.1. Üniversite")
    b1_2 = st.checkbox("B.1.2. TÜBİTAK")
    b1_3 = st.checkbox("B.1.3. DPT")
    b1_4 = st.text_input("B.1.4. Uluslararası (belirtiniz)")
    b1_5 = st.text_input("B.1.5. Diğer (belirtiniz)")

    # B.2. Destekleyici Bilgileri
    st.subheader("B.2. Destekleyici")
    b2_1 = st.text_input("B.2.1. Organizasyonun adı:")
    b2_2 = st.text_input("B.2.2. Temasa geçilecek kişinin adı:")
    b2_3 = st.text_input("B.2.3. Adres:")
    b2_4 = st.text_input("B.2.4. Telefon numarası:")
    b2_5 = st.text_input("B.2.5. Faks numarası:")
    b2_6 = st.text_input("B.2.6. E-posta:")

    # B.3. Destekleyicinin Yasal Temsilcisi
    st.subheader("B.3. Destekleyicinin Yasal Temsilcisi")
    b3_1 = st.text_input("B.3.1. Organizasyonun adı:")
    b3_2 = st.text_input("B.3.2. İletişim kurulacak kişinin adı:")
    b3_3 = st.text_input("B.3.3. Adres:")
    b3_4 = st.text_input("B.3.4. Telefon numarası:")
    b3_5 = st.text_input("B.3.5. Faks numarası:")
    b3_6 = st.text_input("B.3.6. E-posta:")

else:
    b1_1, b1_2, b1_3, b1_4, b1_5 = None, None, None, None, None
    b2_1, b2_2, b2_3, b2_4, b2_5, b2_6 = None, None, None, None, None
    b3_1, b3_2, b3_3, b3_4, b3_5, b3_6 = None, None, None, None, None


st.header("C. ARAŞTIRMAYA İLİŞKİN GENEL BİLGİLER")

# C.1. Araştırılan Konu
st.subheader("C.1. Araştırılan Konu")
c1_1 = st.text_area("C.1.1. Araştırılan konuyu belirtiniz (serbest metin):")
c1_2 = st.text_area("C.1.2. Kolay anlaşılır bir dilde araştırılan konuyu belirtiniz (serbest metin):")

# C.2. Araştırmanın Amacı
st.subheader("C.2. Araştırmanın Amacı")
c2_1 = st.text_area("C.2.1. Temel amaç:")
c2_2 = st.text_area("C.2.2. İkincil amaçlar:")
c2_3 = st.radio("C.2.3. Alt çalışma var mı?", ("Evet", "Hayır"))

if c2_3 == "Evet":
    c2_3_alt = st.text_area("Alt çalışmaların tam başlığı, tarihi, versiyonu ve ilgili amaçlarını belirtiniz:")
else:
    c2_3_alt = None

# C.3. Gönüllülerin Araştırmaya Dahil Edilme Kriterleri
st.subheader("C.3. Gönüllülerin Araştırmaya Dahil Edilme Kriterleri")
c3 = st.text_area("Maddeler Halinde Sıralayınız:")

# C.4. Gönüllülerin Araştırmaya Dahil Edilmeme Kriterleri
st.subheader("C.4. Gönüllülerin Araştırmaya Dahil Edilmeme Kriterleri")
c4 = st.text_area("Maddeler Halinde Sıralayınız:", key="unique_key_1")
c4_1 = st.text_area("Başka Bir Metin Alanı:", key="unique_key_2")

# C.5. Araştırmanın Sonlanım Noktası
st.subheader("C.5. Araştırmanın Sonlanım Noktası")
c5_1 = st.text_area("C.5.1. Primer Sonlanım Noktası:")
c5_2 = st.text_area("C.5.2. Sekonder Sonlanım Noktası:")

# C.6. Araştırmanın Özellikleri
st.subheader("C.6. Araştırmanın Özellikleri")
c6_1 = st.radio("C.6.1. Araştırma, çalışmanın amacını gizli tutmayı gerektiriyor mu?", ("Evet", "Hayır"))
if c6_1 == "Evet":
    c6_1_explain = st.text_area("Evet ise açıklayınız:")
else:
    c6_1_explain = None

# C.6.2
c6_2 = st.radio("C.6.2. Araştırma katılımcıların fiziksel ve ruhsal sağlıklarını tehdit edici sorular içeriyor mu?", ("Evet", "Hayır"))
if c6_2 == "Evet":
    c6_2_explain = st.text_area("Evet ise açıklayınız:", key="c6_2_explain")  # Benzersiz key eklendi
    if not c6_2_explain:
        st.warning("Lütfen açıklamanızı giriniz.")
else:
    c6_2_explain = None


c6_3 = st.radio("C.6.3. Gönüllü katılımını bozacak tehditler mevcut mu?", ("Evet", "Hayır"))
if c6_3 == "Evet":
    c6_3_explain = st.text_area("Evet ise açıklayınız:", key="c6_3_explain")  # Benzersiz key eklendi
else:
    c6_3_explain = None
    
    
    
st.header("D. ARAŞTIRMADAKİ GÖNÜLLÜ POPÜLASYONU")

# D.1. Yaş Aralığı
st.subheader("D.1. Yaş Aralığı (Araştırmanın tamamı için her yaş aralığında planlanan tahmini gönüllü sayısını belirtiniz :)")
d1_1 = st.radio("D.1.1. 18 yaşın altı", ("Evet", "Hayır"))
d1_2 = st.radio("D.1.2. Çocuk (2-11 yaş)", ("Evet", "Hayır"))
d1_3 = st.radio("D.1.3. Ergen (12-17 yaş)", ("Evet", "Hayır"))
d1_4 = st.radio("D.1.4. Yetişkin (18-65 yaş)", ("Evet", "Hayır"))
d1_5 = st.radio("D.1.5. Yaşlı (>=65 yaş)", ("Evet", "Hayır"))

# D.2. Cinsiyet
st.subheader("D.2. Cinsiyet")
d2_1 = st.checkbox("D.2.1. Kadın")
d2_2 = st.checkbox("D.2.2. Erkek")

# D.3. Araştırmadaki Gönüllü Grubu
st.subheader("D.3. Araştırmadaki Gönüllü Grubu")
d3_1 = st.radio("D.3.1. Sağlıklı Gönüllüler", ("Evet", "Hayır"))
d3_2 = st.radio("D.3.2. Hastalar", ("Evet", "Hayır"))
d3_3 = st.radio("D.3.3. Özel Hassas Popülasyonlar", ("Evet", "Hayır"))
d3_4 = st.radio("D.3.4. Gebe Kadınlar", ("Evet", "Hayır"))
d3_5 = st.radio("D.3.5. Emziren Kadınlar", ("Evet", "Hayır"))
d3_6 = st.radio("D.3.6. Acil Vakalar", ("Evet", "Hayır"))
d3_7 = st.radio("D.3.7. Şahsen Olur Veremeyecek Gönüllüler", ("Evet", "Hayır"))

if d3_7 == "Evet":
    d3_7_explain = st.text_area("Lütfen belirtiniz:")
else:
    d3_7_explain = None

d3_8 = st.radio("D.3.8. Diğer", ("Evet", "Hayır"))
if d3_8 == "Evet":
    d3_8_explain = st.text_area("Diğer: Lütfen belirtiniz:")
else:
    d3_8_explain = None

# D.4. Araştırmaya Dahil Edilmesi Planlanan Gönüllü Sayısı
st.subheader("D.4. Araştırmaya Dahil Edilmesi Planlanan Gönüllü Sayısı")
d4_1 = st.number_input("D.4.1. Ülkemizdeki gönüllü sayısını belirtiniz", min_value=0)
d4_2 = st.text_input("D.4.2. Çok uluslu araştırma ise; (Lütfen uygun olan bölümü doldurunuz)")
d4_3 = st.text_input("D.4.3. Avrupa Birliği’ne üye ülkelerdeki gönüllü sayısını belirtiniz")
d4_4 = st.text_input("D.4.4. ABD’deki gönüllü sayısını belirtiniz")
d4_5 = st.text_input("D.4.5. Diğer ülkelerdeki gönüllü sayısını belirtiniz (ülkeleri de belirterek)")
d4_6 = st.number_input("D.4.6. Araştırmanın tamamındaki gönüllü sayısını belirtiniz", min_value=0)



# E. ARAŞTIRMACILAR Bölümü
st.header("E. ARAŞTIRMACILAR")

# E.1. Koordinasyondan Sorumlu Araştırmacı
st.subheader("E.1. Koordinasyondan Sorumlu Araştırmacı (Koordinatör ya da Danışman)")
e1_1 = st.text_input("E.1.1. Adı")
e1_2 = st.text_input("E.1.2. Soyadı")
e1_3 = st.text_input("E.1.3. Unvan (Dr., ...)")
e1_4 = st.text_input("E.1.4. Uzmanlık alanı")
e1_5 = st.text_input("E.1.5. İş adresi")
e1_6 = st.text_input("E.1.6. E-posta adresi")
e1_7 = st.text_input("E.1.7. Telefon numarası")

# E.2. Sorumlu Araştırmacı/Yürütücü
st.subheader("E.2. Sorumlu Araştırmacı/Yürütücü")
e2_1 = st.text_input("E.2.1. Adı")
e2_2 = st.text_input("E.2.2. Soyadı")
e2_3 = st.text_input("E.2.3. Unvan (Dr., ...)")
e2_4 = st.text_input("E.2.4. Uzmanlık Alanı")
e2_5 = st.text_input("E.2.5. İş Adresi")
e2_6 = st.text_input("E.2.6. E-posta Adresi")
e2_7 = st.text_input("E.2.7. Telefon Numarası")

# E.3. Yardımcı Araştırmacı
st.subheader("E.3. Yardımcı Araştırmacı")
e3_1 = st.text_input("E.3.1. Adı")
e3_2 = st.text_input("E.3.2. Soyadı")
e3_3 = st.text_input("E.3.3. Unvan (Dr., ...)")
e3_4 = st.text_input("E.3.4. Uzmanlık alanı")
e3_5 = st.text_input("E.3.5. İş adresi")
e3_6 = st.text_input("E.3.6. E-posta adresi")
e3_7 = st.text_input("E.3.7. Telefon numarası")



# "F. VERİ TOPLANMASI PLANLANAN YERLER" başlığı

# Veri toplanacak yerleri depolamak için bir liste

# F. VERİ TOPLANMASI PLANLANAN YERLER
# F. VERİ TOPLANMASI PLANLANAN YERLER
# F. VERİ TOPLANMASI PLANLANAN YERLER
st.subheader("F. VERİ TOPLANMASI PLANLANAN YERLER")

# İlk 4 yer için yer isimleri depolanacak liste
yerler = []

# İlk 4 yer için metin giriş alanları
for i in range(4):
    yer = st.text_input(f"{i + 1}. Yer adı:", "", key=f"yer_{i+1}")  # Benzersiz key eklendi
    if yer:
        yerler.append(yer)

# Daha fazla yer eklemek için sayaç
if "counter" not in st.session_state:
    st.session_state.counter = 0

# Daha fazla yer ekle butonuna basıldıkça sayaç artırılıyor
if st.button("Daha Fazla Yer Ekle"):
    st.session_state.counter += 1

# Sayaç değeri kadar yeni yer ekleme giriş alanları oluşturuluyor
for i in range(st.session_state.counter):
    yer = st.text_input(f"{len(yerler) + 1}. Yer adı:", "", key=f"yer_more_{i+1}")  # Benzersiz key eklendi
    if yer:
        yerler.append(yer)

# Toplanan yerleri göster
st.write("Veri toplanması planlanan yerler:")
for index, yer in enumerate(yerler, start=1):
    st.write(f"{index}. {yer}")






# Kullanıcıdan araştırma ile ilgili bilgileri alma
h1_konu = st.text_area("H.1. Konu")
h2_amac = st.text_area("H.2. Amaç")
h3_kapsam = st.text_area("H.3. Kapsam")
h4_yontem = st.text_area("H.4. Yöntem")
h5_kaynaklar = st.text_area("H.5. Kaynaklar")



st.subheader("I. ETİK KURUL")

# Kullanıcıdan bilgileri alma
adi_ve_adresi = st.text_area("Adı ve Adresi:")
sunulma_tarihi = st.date_input("Sunulma tarihini gün/ay/yıl olarak belirtiniz:")
st.subheader("I.1 Onay / Görüş")
onay_talep = st.radio("I.1.1. Talep edilecek", ("Evet", "Hayır"))
isleme_kondu = st.radio("I.1.2. İşleme kondu", ("Evet", "Hayır"))
verildi = st.radio("I.1.3. Verildi", ("Evet", "Hayır"))
onay_gorus_tarihi = st.date_input("I.2 Onay / görüş tarihi:")
onay_kabul = st.radio("I.2.1. Onay kabul edildi / lehte görüş verildi:", ("Evet", "Hayır"))
kabul_edilmedi = st.radio("I.2.2. Kabul edilmedi / aleyhte görüş verildi:", ("Evet", "Hayır"))
nedenler = st.text_area("I.2.3. Nedenleri:")
yeniden_basvuru_tarihi = st.date_input("I.2.4. Yeniden başvurunun sunulması için öngörülen tarihi belirtiniz:")
