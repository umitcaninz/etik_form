import streamlit as st
from pymongo import MongoClient
import datetime
import pymongo

# MongoDB'ye bağlan
from pymongo import MongoClient

# Replace <db_password> with your actual password
import logging
from pymongo import MongoClient

# Configure logging
logging.basicConfig(level=logging.DEBUG)

connection_string = 'mongodb+srv://umitinozu:a2468asd@cluster0.qrjiq.mongodb.net/'
client = MongoClient(connection_string)

try:
    client.admin.command('ping')
    print("Connected to MongoDB successfully!")
except Exception as e:
    print("Could not connect to MongoDB:", e)

db = client["mydatabase"]  # Veritabanı adını girin
collection = db["mydatabase"]  # Koleksiyon adını girin
st.title("İnsan Üzerinde Yapılan Klinik Dışı Araştırmalar Başvuru Formu")

# Başvuru Bilgileri
st.header("Başvuru Bilgileri")
basvuru_tarihi = st.date_input("Başvurunun yapıldığı tarih", datetime.date.today())
bilgi_talebi_tarihi = st.date_input("Başvuruyu geçerli kılmak için bilgi talebi tarihi")
ek_bilgi_talebi_tarihi = st.date_input("Ek bilgi talebi tarihi")
red_olumsuz_neden = st.text_area("Red/Olumsuz görüş nedenleri")
red_tarihi = st.date_input("Red Tarihi", datetime.date.today())
gecerli_basvuru_tarihi = st.date_input("Geçerli başvuru tarihi", datetime.date.today())
islem_baslangic_tarihi = st.date_input("İşlem başlangıç tarihi")
onay_tarihi = st.date_input("Onay/Olumlu görüş tarihi", datetime.date.today())
basvuru_arsiv_num = st.text_input("Başvuru arşiv kayıt numarası")
basvuru_cekildi_tarihi = st.date_input("Başvuru geri çekildi tarihi")

# Araştırma Bilgileri
st.header("Araştırma Bilgileri")
ulkeler = st.text_input("Başvurunun yapıldığı diğer ülkeler")
arastirma_adi = st.text_input("Araştırmanın açık adı")
yeniden_basvuru = st.radio("Yeniden başvuru mu?", ["Evet", "Hayır"])
orselenebilir_grup = st.radio("Araştırmada örselenebilir gruplar söz konusu mu?", ["Evet", "Hayır"])

# Araştırmanın Niteliği
st.header("Araştırmanın Niteliği")
arastirma_nitelik = st.multiselect("Araştırmanın Niteliği", 
    ["Bireysel araştırma projesi", "Doktora Tezi", "Uzmanlık Tezi", "Yüksek Lisans Tezi", "Diğer (DPT, TÜBİTAK vb.)"])

# Araştırmanın Türü
st.header("Araştırmanın Türü")
arastirma_turu = st.multiselect("Araştırmanın Türü", ["Nicel Araştırmalar", "Görgül Araştırmalar", "Diğer"])

# Araştırmada Kullanılacak Veri Toplama Araç ve Yöntemleri
st.header("Veri Toplama Araç ve Yöntemleri")
veri_toplama = st.multiselect("Araştırmada Kullanılacak Veri Toplama Araç ve Yöntemleri", 
    ["Anket", "Mülakat", "Gözlem", "Bilgisayar Ortamında Test", "Görüntü Kaydı", "Ses Kaydı", 
    "Ölçek Geliştirme Çalışmaları", "Dosya Taraması", "Veri Kaynakları Taraması", "Sistem Model Geliştirme"])

# Destekleyici
st.header("Destekleyici Bilgileri")
destekleyici_var = st.radio("Araştırmanın Destekleyicisi Var mı?", ["Evet", "Hayır"])
if destekleyici_var == "Evet":
    
    arastırma_destekleyicisi = st.multiselect('Destekleyici',["Üniversite","TÜBİTAK","DPT","Uluslararası,Diğer"])
    destekleyici_organizasyon = st.text_input("Destekleyici Organizasyonun Adı")
    destekleyici_kisi = st.text_input("Temasa Geçilecek Kişinin Adı")
    destekleyici_adres = st.text_input("Adres")

# Araştırmacılar
st.header("Araştırmacılar")
arastirmaci_ad = st.text_input("Sorumlu Araştırmacı Adı")
arastirmaci_soyad = st.text_input("Sorumlu Araştırmacı Soyadı")
arastirmaci_unvan = st.text_input("Sorumlu Araştırmacı Unvanı")
arastirmaci_adres = st.text_input("İş Adresi")
arastirmaci_email = st.text_input("E-posta Adresi")
arastirmaci_telefon = st.text_input("Telefon Numarası")

# Araştırmanın Genel Bilgileri
st.header("Araştırmaya İlişkin Genel Bilgiler")
arastirma_konu = st.text_area("Araştırılan konuyu belirtiniz")
arastirma_aciklama = st.text_area("Kolay anlaşılır bir dilde araştırılan konuyu belirtiniz")
temel_amac = st.text_area("Temel amaç")
ikincil_amac = st.text_area("İkincil amaçlar")
alt_calismalar = st.radio("Alt çalışma var mı?", ["Evet", "Hayır"])
if alt_calismalar == "Evet":
    alt_calismalar_bilgisi = st.text_area("Alt çalışmaların tam başlığı ve ilgili bilgileri belirtiniz")

# Gönüllü Popülasyonu
st.header("Gönüllü Popülasyonu")
yas_araligi = st.multiselect("Yaş Aralığı", 
    ["18 yaş altı", "Çocuk (2-11 yaş)", "Ergen (12-17 yaş)", "Yetişkin (18-65 yaş)", "Yaşlı (65 yaş ve üzeri)"])
cinsiyet = st.radio("Cinsiyet", ["Kadın", "Erkek"])
gonullu_grubu = st.multiselect("Gönüllü Grubu", 
    ["Sağlıklı Gönüllüler", "Hastalar", "Özel Hassas Popülasyonlar", "Gebe Kadınlar", "Emziren Kadınlar", "Acil Vakalar"])
gonullu_sayisi = st.text_input("Araştırmaya Dahil Edilmesi Planlanan Gönüllü Sayısı")

# Belgeler (PDF yükleme)
st.header("Belgeler")
protokol_versiyon = st.text_input("Protokol Versiyon Numarası")
protokol_tarihi = st.date_input("Protokol Tarihi")
protokol_pdf = st.file_uploader("Protokol PDF Yükleyin", type=["pdf"])

gonullu_olur_formu_versiyon = st.text_input("Bilgilendirilmiş Gönüllü Olur Formu Versiyon Numarası")
gonullu_olur_formu_tarihi = st.date_input("Gönüllü Olur Formu Tarihi")
gonullu_olur_formu_pdf = st.file_uploader("Gönüllü Olur Formu PDF Yükleyin", type=["pdf"])

sozlesmeler_pdf = st.file_uploader("Sözleşmeler PDF Yükleyin", type=["pdf"])

olgu_rapor_formu_versiyon = st.text_input("Olgu Rapor Formu Versiyon Numarası")
olgu_rapor_formu_tarihi = st.date_input("Olgu Rapor Formu Tarihi")
olgu_rapor_formu_pdf = st.file_uploader("Olgu Rapor Formu PDF Yükleyin", type=["pdf"])

arastirma_brosuru_versiyon = st.text_input("Araştırma Broşürü Versiyon Numarası")
arastirma_brosuru_tarihi = st.date_input("Araştırma Broşürü Tarihi")
arastirma_brosuru_pdf = st.file_uploader("Araştırma Broşürü PDF Yükleyin", type=["pdf"])

arastirma_butcesi_pdf = st.file_uploader("Araştırma Bütçesi PDF Yükleyin", type=["pdf"])

# Verileri MongoDB'ye kaydetme
if st.button("Başvuruyu Gönder"):
    basvuru_data = {
        "basvuru_tarihi": str(basvuru_tarihi),
        "bilgi_talebi_tarihi": str(bilgi_talebi_tarihi),
        "ek_bilgi_talebi_tarihi": str(ek_bilgi_talebi_tarihi),
        "red_olumsuz_neden": red_olumsuz_neden,
        "red_tarihi": str(red_tarihi),
        "gecerli_basvuru_tarihi": str(gecerli_basvuru_tarihi),
        "islem_baslangic_tarihi": str(islem_baslangic_tarihi),
        "onay_tarihi": str(onay_tarihi),
        "basvuru_arsiv_num": basvuru_arsiv_num,
        "basvuru_cekildi_tarihi": str(basvuru_cekildi_tarihi),
        "ulkeler": ulkeler,
        "arastirma_adi": arastirma_adi,
        "yeniden_basvuru": yeniden_basvuru,
        "orselenebilir_grup": orselenebilir_grup,
        "arastirma_nitelik": arastirma_nitelik,
        "arastirma_turu": arastirma_turu,
        "veri_toplama": veri_toplama,
        "destekleyici_var": destekleyici_var,
        "destekleyici_organizasyon": destekleyici_organizasyon if destekleyici_var == "Evet" else None,
        "destekleyici_kisi": destekleyici_kisi if destekleyici_var == "Evet" else None,
        "destekleyici_adres": destekleyici_adres if destekleyici_var == "Evet" else None,
        "arastirmaci_ad": arastirmaci_ad,
        "arastirmaci_soyad": arastirmaci_soyad,
        "arastirmaci_unvan": arastirmaci_unvan,
        "arastirmaci_adres": arastirmaci_adres,
        "arastirmaci_email": arastirmaci_email,
        "arastirmaci_telefon": arastirmaci_telefon,
        "arastirma_konu": arastirma_konu,
        "arastirma_aciklama": arastirma_aciklama,
        "temel_amac": temel_amac,
        "ikincil_amac": ikincil_amac,
        "alt_calismalar": alt_calismalar,
        "yas_araligi": yas_araligi,
        "cinsiyet": cinsiyet,
        "gonullu_grubu": gonullu_grubu,
        "gonullu_sayisi": gonullu_sayisi,
        "protokol_versiyon": protokol_versiyon,
        "protokol_tarihi": str(protokol_tarihi),
        "gonullu_olur_formu_versiyon": gonullu_olur_formu_versiyon,
        "gonullu_olur_formu_tarihi": str(gonullu_olur_formu_tarihi),
        "olgu_rapor_formu_versiyon": olgu_rapor_formu_versiyon,
        "olgu_rapor_formu_tarihi": str(olgu_rapor_formu_tarihi),
        "arastirma_brosuru_versiyon": arastirma_brosuru_versiyon,
        "arastirma_brosuru_tarihi": str(arastirma_brosuru_tarihi),
        # PDF dosyaları byte formatında kaydedilir
        "protokol_pdf": protokol_pdf.read() if protokol_pdf else None,
        "gonullu_olur_formu_pdf": gonullu_olur_formu_pdf.read() if gonullu_olur_formu_pdf else None,
        "sozlesmeler_pdf": sozlesmeler_pdf.read() if sozlesmeler_pdf else None,
        "olgu_rapor_formu_pdf": olgu_rapor_formu_pdf.read() if olgu_rapor_formu_pdf else None,
        "arastirma_brosuru_pdf": arastirma_brosuru_pdf.read() if arastirma_brosuru_pdf else None,
        "arastirma_butcesi_pdf": arastirma_butcesi_pdf.read() if arastirma_butcesi_pdf else None,
    }

    # MongoDB'ye kaydet
    collection.insert_one(basvuru_data)
    st.success("Başvurunuz başarıyla kaydedildi!")
