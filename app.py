import streamlit as st
from gtts import gTTS
from streamlit_mic_recorder import mic_recorder
import io

# Sayfa Ayarları
st.set_page_config(page_title="Telaffuz Akademisi", page_icon="🗣️")

st.title("🗣️ Telaffuz Karşılaştırma")
st.write("Doğruyu dinle, kaydını yap ve farkı hisset! (Sesler kaydedilmez)")

# Senin verdiğin 12 kelimelik liste
kelimeler = [
    "think", "thought", "the", "are", "accept", 
    "she", "chat", "wear", "use", "umbrella", 
    "library", "come"
]

# Kelime Seçimi
secilen = st.selectbox("Çalışmak istediğin kelimeyi seç:", kelimeler)

st.divider()

# --- 1. BÖLÜM: DOĞRU TELAFFUZ (Yapay Zeka) ---
st.subheader(f"✅ '{secilen}' Kelimesinin Doğru Telaffuzu")

# Yapay zeka sesi oluşturuyor (İngilizce aksanıyla)
tts = gTTS(text=secilen, lang='en')
fp = io.BytesIO()
tts.write_to_fp(fp)
st.audio(fp, format='audio/mp3')

st.divider()

# --- 2. BÖLÜM: ÖĞRENCİ KAYDI (Anlık ve Geçici) ---
st.subheader("🎤 Senin Denemen")
st.write("Kaydı Başlat'a bas ve konuş. Durdurduğunda sesini hemen dinleyebilirsin.")

kayit = mic_recorder(
    start_prompt="Kaydı Başlat ⏺️",
    stop_prompt="Kaydı Durdur ⏹️",
    key='recorder'
)

if kayit:
    st.write("Senin Ses Kaydın:")
    st.audio(kayit['bytes'])
    st.warning("⚠️ Bu ses şu an cihazının belleğinde. Sayfayı kapatırsan veya başka kelimeye geçersen silinecektir.")

st.divider()
st.info("İpucu: 'th' seslerinde dilini ön dişlerinin arasına hafifçe değdirmeyi unutma!")
