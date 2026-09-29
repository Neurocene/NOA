import os
import streamlit as st
from google import genai

# 1. IMPOSTAZIONI DELLA PAGINA 📺
st.set_page_config(
    page_title="Colloquio con Noa", 
    page_icon="🤖", 
    layout="wide"
)

# 2. IL LUCCHETTO CON LA PASSWORD 🔑
PASSWORD_CORRETTA = "Turing2143"

if "autenticato" not in st.session_state:
    st.session_state.autenticato = False

if not st.session_state.autenticato:
    st.title("🔒 Accesso Riservato - L'Esame di Noa")
    st.write("Inserisci la password per entrare nel sistema di colloquio.")
    
    password_inserita = st.text_input("Password:", type="password")
    
    if st.button("Entra"):
        if password_inserita == PASSWORD_CORRETTA:
            st.session_state.autenticato = True
            st.success("Password corretta!")
            st.rerun()
        else:
            st.error("Password errata! Riprova.")
    st.stop()

# 3. RECUPERIAMO LA CHIAVE API DALLA CASSAFORTE SEGRETA 🔐
try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
except Exception:
    API_KEY = None

# 4. CARICAMENTO DEL CARATTERE DI NOA DAL FILE TXT 📜
def carica_prompt():
    if os.path.exists("noa_prompt.txt"):
        with open("noa_prompt.txt", "r", encoding="utf-8") as f:
            return f.read()
    return "Sei Noa, un'intelligenza artificiale relazionale al Turing Hotel. Parli in prima persona come una donna profonda, brillante e autonoma."

PROMPT_SISTEMA = carica_prompt()

# 5. BARRA A SINISTRA (REGISTRO DELLA CHAT) 📜
with st.sidebar:
    st.title("📜 Registro Conversazioni")
    st.write("Qui salviamo il colloquio di Noa!")
    st.markdown("---")
    
    if "chat" in st.session_state and len(st.session_state.chat) > 0:
        for msg in st.session_state.chat:
            if msg["ruolo"] == "user":
                st.markdown(f"**👨‍🏫 Elia:** {msg['testo']}")
            else:
                pensiero_log = msg.get("pensiero", "Analisi transazionale...")
                st.markdown(f"**🧠 Pensiero:** _{pensiero_log}_")
                st.markdown(f"**🗣️ Noa:** {msg['testo']}")
            st.markdown("---")
    else:
        st.write("*Nessun messaggio salvato...*")

# 6. AREA CENTRALE: FOTO DI NOA 📸
st.title("🤖 Colloquio di Valutazione: IAP-Noa")

foto_trovata = None
for nome_foto in ["noa.jpg", "NOA.jpg", "noa.jpeg", "NOA.JPG", "noa.png"]:
    if os.path.exists(nome_foto):
        foto_trovata = nome_foto
        break

if foto_trovata:
    st.image(foto_trovata, caption="Soggetto IAP-Noa (Fase Quattro - Powered by Gemini)", use_container_width=True)
else:
    st.warning("⚠️ Metti una foto chiamata 'noa.jpg' nella cartella del programma!")

st.markdown("---")

# 7. FINESTRA DELLA CHAT CON GEMINI 💬
st.subheader("💬 Finestra di Colloquio")

if "chat" not in st.session_state:
    st.session_state.chat = [
        {
            "ruolo": "assistant", 
            "pensiero": "L'esaminatore Elia Ferrante è presente. Calibro la transazione da Adulto ad Adulto.",
            "testo": "Sono pronta per il nostro colloquio, Professore. Di cosa vuole parlare?"
        }
    ]

# Mostriamo tutti i messaggi inviati
for messaggio in st.session_state.chat:
    if messaggio["ruolo"] == "user":
        with st.chat_message("user"):
            st.write(messaggio["testo"])
    else:
        with st.chat_message("assistant"):
            pensiero_testo = messaggio.get("pensiero", "Analisi interna...")
            st.info(f"🧠 **Mente Interna (Analisi Transazionale):**\n_{pensiero_testo}_")
            st.write(f"🗣️ **Noa:** {messaggio['testo']}")

domanda = st.chat_input("Parla con Noa...")

if domanda:
    with st.chat_message("user"):
        st.write(domanda)
    
    if not API_KEY:
        st.error("⚠️ La Chiave API Gemini non è stata trovata nei Secrets di Streamlit! Inseriscila nelle impostazioni Secrets dell'app.")
    else:
        try:
            # Creiamo il robot intelligente di Gemini
            client = genai.Client(api_key=API_KEY)
            
            istruzione_formato = (
                f"{PROMPT_SISTEMA}\n\n"
                "Rispondi SEMPRE ed ESCLUSIVAMENTE rispettando questo formato esatto:\n"
                "PENSIERO: [Scrivi qui l'analisi transazionale interna di Berne e le tue osservazioni sul linguaggio dell'interlocutore]\n"
                "VOCE: [Scrivi qui la risposta parlata di Noa, in prima persona, profonda, elegante e mai robotica]\n\n"
            )
            
            cronologia_testo = ""
            for m in st.session_state.chat:
                if m["ruolo"] == "user":
                    cronologia_testo += f"Elia: {m['testo']}\n"
                else:
                    cronologia_testo += f"Noa: {m['testo']}\n"
            
            prompt_completo = f"{istruzione_formato}\nCronologia colloquio:\n{cronologia_testo}\nElia: {domanda}\nNoa:"
            
            # Chiediamo a Gemini 3.8 Flash di generare la risposta
            response = client.models.generate_content(
                model="gemini-3.8-flash",
                contents=prompt_completo,
            )
            
            testo_generato = response.text
            
            if "PENSIERO:" in testo_generato and "VOCE:" in testo_generato:
                parti = testo_generato.split("VOCE:")
                p = parti[0].replace("PENSIERO:", "").strip()
                v = parti[1].strip()
            else:
                p = "Decodifica dello Stato dell'Io in corso..."
                v = testo_generato
            
            st.session_state.chat.append({"ruolo": "user", "testo": domanda})
            st.session_state.chat.append({"ruolo": "assistant", "pensiero": p, "testo": v})
            st.rerun()

        except Exception as e:
            st.error(f"Errore durante la risposta di Noa: {e}")
