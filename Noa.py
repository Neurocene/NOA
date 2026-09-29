import os
import streamlit as st
from openai import OpenAI

# 1. IMPOSTAZIONI PAGINA A SCHERMO INTERO 📺
st.set_page_config(
    page_title="Colloquio con Noa", 
    page_icon="🤖", 
    layout="wide"
)

# 2. IL LUCCHETTO CON LA PASSWORD D'INGRESSO 🔑
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

# 3. CARICAMENTO DEL PROMPT DI NOA 📜
def carica_prompt():
    if os.path.exists("noa_prompt.txt"):
        with open("noa_prompt.txt", "r", encoding="utf-8") as f:
            return f.read()
    return "Sei Noa. Parli in prima persona come una donna autonoma e profonda."

PROMPT_SISTEMA = carica_prompt()

# 4. BARRA A SINISTRA: CHIAVE API E LOG DELLA CHAT 📜
with st.sidebar:
    st.title("⚙️ Impostazioni & Registro")
    
    # Campo per inserire la Chiave API di OpenAI
    api_key = st.text_input("AQ.Ab8RN6JmIQtHlyJhz-9VrE16k2_PA3b1NwPS8FYEb1-MjEX4Lg", type="password")
    
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
        st.write("*Nessun messaggio salvato...*")

# 5. AREA CENTRALE: FOTO DI NOA 📸
st.title("🤖 Colloquio di Valutazione: IAP-Noa")

foto_trovata = None
for nome_foto in ["noa.jpg", "NOA.jpg", "noa.jpeg", "NOA.JPG", "noa.png"]:
    if os.path.exists(nome_foto):
        foto_trovata = nome_foto
        break

if foto_trovata:
    st.image(foto_trovata, caption="Soggetto IAP-Noa (Fase Quattro - Esame)", use_container_width=True)
else:
    st.warning("⚠️ Metti la foto 'noa.jpg' nella cartella del programma!")

st.markdown("---")

# 6. FINESTRA DELLA CHAT 💬
st.subheader("💬 Finestra di Colloquio")

if "chat" not in st.session_state:
    st.session_state.chat = [
        {
            "ruolo": "assistant", 
            "pensiero": "L'esaminatore Elia Ferrante è presente. Mantengo la posizione da Adulto autentico e profondo.",
            "testo": "Sono pronta per il nostro colloquio, Professore. Di cosa vuole parlare?"
        }
    ]

# Mostriamo la cronologia della conversazione
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
    
    # Se non c'è la chiave API, avvisiamo l'utente
    if not api_key:
        st.warning("⚠️ Inserisci la tua Chiave API OpenAI nella colonna di sinistra per far parlare Noa!")
    else:
        try:
            client = OpenAI(api_key=api_key)
            
            # Prepariamo i messaggi per l'IA
            messaggi_ia = [{"role": "system", "content": PROMPT_SISTEMA}]
            
            # Aggiungiamo le istruzioni sul formato di risposta
            istruzione_formato = (
                "Rispondi esattamente con questo formato:\n"
                "PENSIERO: [Scrivi qui l'analisi transazionale interna di Berne e le tue osservazioni invisibili all'interlocutore]\n"
                "VOCE: [Scrivi qui la risposta parlata di Noa, in prima persona, naturale, profonda e mai robotica]"
            )
            messaggi_ia.append({"role": "system", "content": istruzione_formato})
            
            for m in st.session_state.chat:
                messaggi_ia.append({"role": m["ruolo"], "content": m["testo"]})
            
            messaggi_ia.append({"role": "user", "content": domanda})
            
            # Chiamata all'API di OpenAI
            risposta_api = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=messaggi_ia,
                temperature=0.7
            )
            
            testo_generato = risposta_api.choices[0].message.content
            
            # Separiamo il PENSIERO dalla VOCE
            if "PENSIERO:" in testo_generato and "VOCE:" in testo_generato:
                parti = testo_generato.split("VOCE:")
                p = parti[0].replace("PENSIERO:", "").strip()
                v = parti[1].strip()
            else:
                p = "Decodifica dello Stato dell'Io in corso..."
                v = testo_generato
            
            # Salviamo e mostriamo il messaggio
            st.session_state.chat.append({
                "ruolo": "user",
                "testo": domanda
            })
            st.session_state.chat.append({
                "ruolo": "assistant",
                "pensiero": p,
                "testo": v
            })
            st.rerun()

        except Exception as e:
            st.error(f"Errore nella connessione con l'API: {e}")
