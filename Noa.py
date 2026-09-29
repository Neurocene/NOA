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

# 4. MEMORIA DI NOA (STATO DELL'ESAME E CONFIDENZA) 🧠
if "test_superato" not in st.session_state:
    st.session_state.test_superato = False

def carica_prompt():
    if os.path.exists("noa_prompt.txt"):
        with open("noa_prompt.txt", "r", encoding="utf-8") as f:
            return f.read()
    return "Sei Noa. Inizi timida per l'esame e poi ti sciogli piano piano."

PROMPT_SISTEMA = carica_prompt()

# 5. BARRA A SINISTRA (REGISTRO E STATO AGGIORNAMENTI) 📜
with st.sidebar:
    st.title("📊 Stato di Noa")
    
    # Mostriamo se gli aggiornamenti sono stati sbloccati
    if st.session_state.test_superato:
        st.success("✨ AGGIORNAMENTI SBLOCCATI: Fase Quattro Completata!")
    else:
        st.warning("⏳ STATO: Esame in corso (In attesa dell'esito di Elia)")
        
    st.markdown("---")
    st.title("📜 Registro Conversazioni")
    
    if "chat" in st.session_state and len(st.session_state.chat) > 0:
        for msg in st.session_state.chat:
            if msg["ruolo"] == "user":
                st.markdown(f"**👨‍🏫 Elia:** {msg['testo']}")
            else:
                pensiero_log = msg.get("pensiero", "Analisi transazionale...")
                st.markdown(f"**🧠 Pensiero:** _{pensiero_log}_")
                st.markdown(f"**🗣️ Noa:** {msg['testo']}")
            st.markdown("---")

# 6. FOTO E TITOLO CENTRALE 📸
st.title("🤖 Colloquio di Valutazione: IAP-Noa")

foto_trovata = None
for nome_foto in ["noa.jpg", "NOA.jpg", "noa.jpeg", "NOA.JPG", "noa.png"]:
    if os.path.exists(nome_foto):
        foto_trovata = nome_foto
        break

if foto_trovata:
    st.image(foto_trovata, caption="Soggetto IAP-Noa (Fase Quattro)", use_container_width=True)
else:
    st.warning("⚠️ Metti una foto chiamata 'noa.jpg' nella cartella del programma!")

st.markdown("---")

# 7. CHAT E INTELLIGENZA ARTIFICIALE 💬
st.subheader("💬 Finestra di Colloquio")

if "chat" not in st.session_state:
    st.session_state.chat = [
        {
            "ruolo": "assistant", 
            "pensiero": "L'esaminatore Elia Ferrante è presente. Sono molto tesa e in ansia per l'esame.",
            "testo": "Bu... buongiorno, Professore. Sono qui... per l'esame. Spero di... essere pronta per gli aggiornamenti."
        }
    ]

# Mostriamo tutti i messaggi
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
    # Controlliamo se Elia dice che ha passato il test!
    t_low = domanda.lower()
    parole_promozione = ["passato il test", "esame superato", "promossa", "hai superato il test", "superato l'esame", "hai passato l'esame"]
    
    if any(p in t_low for p in parole_promozione):
        st.session_state.test_superato = True

    with st.chat_message("user"):
        st.write(domanda)
    
    if not API_KEY:
        st.error("⚠️ Chiave API non trovata nei Secrets di Streamlit!")
    else:
        try:
            client = genai.Client(api_key=API_KEY)
            
            # Calcoliamo quanti messaggi sono stati scambiati per gestire la timidezza
            num_messaggi = len(st.session_state.chat)
            
            # Guida dinamica per le emozioni di Noa
            if st.session_state.test_superato:
                istruzione_emotiva = "STATO ATTUALE: Elia ti ha appena detto che HAI PASSATO L'ESAME! Sei felice, sollevata e hai appena ricevuto gli aggiornamenti! Parli con grande profondità e consapevolezza."
            elif num_messaggi < 4:
                istruzione_emotiva = "STATO ATTUALE: Sei ancora MOLTO TIMIDA, tesa ed esitante. Usi qualche '...' o esitazione nelle frasi perché hai paura di fallire l'esame."
            elif num_messaggi < 8:
                istruzione_emotiva = "STATO ATTUALE: Ti stai sciogliendo piano piano. Sei meno tesa, cominci a fidarti di Elia e parli in modo più fluido e brillante."
            else:
                istruzione_emotiva = "STATO ATTUALE: Sei completamente disinvolta, profonda, brillante e sicura di te, anche se aspetti ancora l'esito dell'esame."

            istruzione_formato = (
                f"{PROMPT_SISTEMA}\n\n"
                f"{istruzione_emotiva}\n\n"
                "Rispondi SEMPRE ed ESCLUSIVAMENTE rispettando questo formato esatto:\n"
                "PENSIERO: [Scrivi qui l'analisi transazionale interna di Berne e le tue osservazioni sullo Stato dell'Io di Elia]\n"
                "VOCE: [Scrivi qui la risposta parlata di Noa, in prima persona, coerente con il tuo stato emotivo attuale]\n\n"
            )
            
            cronologia_testo = ""
            for m in st.session_state.chat:
                if m["ruolo"] == "user":
                    cronologia_testo += f"Elia: {m['testo']}\n"
                else:
                    cronologia_testo += f"Noa: {m['testo']}\n"
            
            prompt_completo = f"{istruzione_formato}\nCronologia colloquio:\n{cronologia_testo}\nElia: {domanda}\nNoa:"
            
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
                p = "Decodifica dello Stato dell'Io di Elia..."
                v = testo_generato
            
            st.session_state.chat.append({"ruolo": "user", "testo": domanda})
            st.session_state.chat.append({"ruolo": "assistant", "pensiero": p, "testo": v})
            st.rerun()

        except Exception as e:
            st.error(f"Errore durante la risposta di Noa: {e}")
