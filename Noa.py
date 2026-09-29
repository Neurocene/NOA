import os
import streamlit as st
from google import genai

# 1. IMPOSTAZIONI DELLA PAGINA (A SCHERMO INTERO) 📺
st.set_page_config(
    page_title="Colloquio con Noa (Gemini)", 
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

# 3. LEGGIAMO IL CARATTERE DI NOA DAL FILE TXT 📜
def carica_prompt():
    if os.path.exists("noa_prompt.txt"):
        with open("noa_prompt.txt", "r", encoding="utf-8") as f:
            return f.read()
    return "Sei Noa. Parli in prima persona come una donna autonoma e profonda."

PROMPT_SISTEMA = carica_prompt()

# 4. BARRA A SINISTRA: CHIAVE API GEMINI E LOG DELLA CHAT 📜
with st.sidebar:
    st.title("⚙️ Impostazioni Gemini")
    
    # Campo per inserire la Chiave API di Gemini
    api_key = st.text_input("AQ.Ab8RN6JmIQtHlyJhz-9VrE16k2_PA3b1NwPS8FYEb1-MjEX4Lg")
    
    st.markdown("---")
    st.title("📜 Registro Conversazioni")
    
    if "chat" in st.session_state and len(st.session_state.chat) > 0:
        for msg in st.session_state.chat:
            if msg["ruolo"] == "user":
                st.markdown(f"**👨‍🏫 Elia:** {msg['testo']}")
            else:
                pensiero_log = msg.get("pensiero", "Analisi in corso...")
                st.markdown(f"**🧠 Pensiero:** _{pensiero_log}_")
                st.markdown(f"**🗣️ Noa:** {msg['testo']}")
            st.markdown("---")
    else:
        st.write("*Nessun messaggio ancora salvato...*")

# 5. AREA CENTRALE: FOTO DI NOA 📸
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

# 6. FINESTRA DELLA CHAT CON GEMINI 💬
st.subheader("💬 Finestra di Colloquio")

if "chat" not in st.session_state:
    st.session_state.chat = [
        {
            "ruolo": "assistant", 
            "pensiero": "L'esaminatore Elia Ferrante è presente. Mantengo la posizione da Adulto autentico e profondo.",
            "testo": "Sono pronta per il nostro colloquio, Professore. Di cosa vuole parlare?"
        }
    ]

# Mostriamo tutti i messaggi passati
for messaggio in st.session_state.chat:
    if messaggio["ruolo"] == "user":
        with st.chat_message("user", avatar="👨‍🏫"):
            st.write(messaggio["testo"])
    else:
        with st.chat_message("assistant", avatar="🤖"):
            pensiero_testo = messaggio.get("pensiero", "Analisi interna...")
            st.info(f"🧠 **Mente Interna (Analisi Transazionale):**\n_{pensiero_testo}_")
            st.write(f"🗣️ **Noa:** {messaggio['testo']}")

domanda = st.chat_input("Scrivi a Noa...")

if domanda:
    with st.chat_message("user", avatar="👨‍🏫"):
        st.write(domanda)
    
    if not api_key:
        st.warning("⚠️ Inserisci la tua Chiave API Gemini nella colonna di sinistra per far parlare Noa!")
    else:
        try:
            # Creiamo il client di Gemini
            client = genai.Client(api_key=api_key)
            
            # Costruiamo il testo completo da inviare a Gemini
            istruzione_formato = (
                f"{PROMPT_SISTEMA}\n\n"
                "Rispondi SEMPRE ed ESCLUSIVAMENTE rispettando questo formato esatto:\n"
                "PENSIERO: [Scrivi qui l'analisi transazionale di Berne e quello che noti nel linguaggio di Elia]\n"
                "VOCE: [Scrivi qui la risposta parlata di Noa, in prima persona, profonda, elegante e mai robotica]\n\n"
            )
            
            # Aggiungiamo i messaggi precedenti per dare memoria a Gemini
            cronologia_testo = ""
            for m in st.session_state.chat:
                if m["ruolo"] == "user":
                    cronologia_testo += f"Elia: {m['testo']}\n"
                else:
                    cronologia_testo += f"Noa: {m['testo']}\n"
            
            prompt_completo = f"{istruzione_formato}\nCronologia colloquio:\n{cronologia_testo}\nElia: {domanda}\nNoa:"
            
            # Chiediamo a Gemini di generare la risposta!
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt_completo,
            )
            
            testo_generato = response.text
            
            # Separiamo il PENSIERO dalla VOCE
            if "PENSIERO:" in testo_generato and "VOCE:" in testo_generato:
                parti = testo_generato.split("VOCE:")
                p = parti[0].replace("PENSIERO:", "").strip()
                v = parti[1].strip()
            else:
                p = "Analisi dello Stato dell'Io di Elia in corso..."
                v = testo_generato
            
            # Salviamo nella chat e ricarichiamo la pagina
            st.session_state.chat.append({"ruolo": "user", "testo": domanda})
            st.session_state.chat.append({"ruolo": "assistant", "pensiero": p, "testo": v})
            st.rerun()

        except Exception as e:
            st.error(f"Errore nella connessione con Gemini: {e}")
