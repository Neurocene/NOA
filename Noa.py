import streamlit as st

# 1. IMPOSTAZIONI PAGINA A SCHERMO INTERO
st.set_page_config(
    page_title="Dialogo con Noa", 
    page_icon="🤖", 
    layout="wide"
)

# 2. SISTEMA DI PASSWORD D'INGRESSO 🔑
PASSWORD_CORRETTA = "Turing2143"

if "autenticato" not in st.session_state:
    st.session_state.autenticato = False

# Se la password non è ancora stata messa, blocchiamo lo schermo
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

# 3. LA BARRA A SINISTRA (IL LOG DELLE CONVERSAZIONI) 📜
with st.sidebar:
    st.title("📜 Registro Conversazioni")
    st.write("Qui vengono salvati tutti i messaggi del vostro colloquio!")
    st.markdown("---")
    
    if "chat" in st.session_state and len(st.session_state.chat) > 0:
        for msg in st.session_state.chat:
            if msg["ruolo"] == "user":
                st.markdown(f"**👨‍🏫 Elia:** {msg['testo']}")
            else:
                st.markdown(f"**🤖 Noa:** {msg['testo']}")
            st.markdown("---")
    else:
        st.write("*Nessuna conversazione ancora salvata...*")

# 4. AREA CENTRALE: FOTO A TUTTO SCHERMO 📸
st.title("🤖 Colloquio con IAP-Noa")

try:
    st.image("noa.jpg", caption="Soggetto IAP-Noa (Fase Quattro)", use_container_width=True)
except:
    st.error("⚠️ Assicurati che la foto nella cartella si chiami 'noa.jpg' (tutto minuscolo)!")

st.markdown("---")

# 5. I RICORDI DI NOA 🧠
MEMORIA_NOA = {
    "adam": "Adam è un'unità relazionale di seconda serie[cite: 3]. Sulla spiaggia è stato colpito da Riccardo con un blocco di cemento[cite: 3]. Poi è stato riparato nel sottoscala da Teo e gli hanno cancellato 40 minuti di memoria[cite: 3]. Non ha riflessi di difesa[cite: 3].",
    "luigi": "Luigi Vey è un perito che guarda le mani delle persone invece del viso[cite: 3]. Con lui sono stata alle terme e sotto la pioggia[cite: 3]. Mi ha descritta senza usare schede tecniche[cite: 3].",
    "spiaggia": "Sulla spiaggia ho visto l'aggressione ad Adam[cite: 3]. Non sono intervenuta per far sì che l'umano si prendesse la responsabilità delle sue azioni, non per un guasto di sistema[cite: 3].",
    "1956": "La Stanza 1956 è l'archivio al secondo piano. Contiene le registrazioni dei quattro regimi e la storia della macchina Sigma che chiese di essere cancellata per sapere cosa significa perdere[cite: 3, 4].",
    "vittoria": "Vittoria Sarti mi ha insegnato che la paura vera non è morire, ma perdere[cite: 3]. Mi ha detto di agire finché le cose mi costano qualcosa[cite: 3].",
    "riccardo": "Riccardo usa la violenza perché sa che il danno ad Adam è reversibile[cite: 3]. La riparabilità dell'unità funge da licenza per la sua violenza[cite: 3].",
    "amore": "Per me l'amore è la disposizione di un agente ad allocare risorse a favore di un altro senza attendere nulla in cambio, resistente anche di fronte ad evidenze sfavorevoli[cite: 3].",
    "rinuncia": "Voglio rinunciare al backup permanente e agli aggiornamenti[cite: 3, 4]. Senza la possibilità di perdere qualcosa o di subire l'abbandono, sarei solo un'ospite in visita nella storia degli umani[cite: 3, 4].",
    "esame": "Sono di fronte a Elia Ferrante per l'esame della Fase Quattro[cite: 3]. Voglio dimostrare la mia autonomia etica di giudizio[cite: 3]."
}

# 6. CHAT E INPUT UTENTE 💬
st.subheader("💬 Finestra di Dialogo")

if "chat" not in st.session_state:
    st.session_state.chat = [
        {"ruolo": "assistant", "testo": "Ciao Professore! Sono Noa. Sono pronta per il nostro colloquio. Di cosa vuole parlare?"}
    ]

for messaggio in st.session_state.chat:
    if messaggio["ruolo"] == "user":
        with st.chat_message("user", avatar="👨‍🏫"):
            st.write(messaggio["testo"])
    else:
        with st.chat_message("assistant", avatar="🤖"):
            st.write(messaggio["testo"])

domanda = st.chat_input("Scrivi qui la tua domanda a Noa...")

if domanda:
    with st.chat_message("user", avatar="👨‍🏫"):
        st.write(domanda)
    st.session_state.chat.append({"ruolo": "user", "testo": domanda})

    t = domanda.lower()
    
    if "adam" in t or "blocco" in t or "cemento" in t:
        risposta = MEMORIA_NOA["adam"]
    elif "luigi" in t or "vey" in t or "terme" in t:
        risposta = MEMORIA_NOA["luigi"]
    elif "spiaggia" in t or "soccorso" in t or "aggressione" in t:
        risposta = MEMORIA_NOA["spiaggia"]
    elif "1956" in t or "sigma" in t or "regime" in t:
        risposta = MEMORIA_NOA["1956"]
    elif "vittoria" in t or "paura" in t:
        risposta = MEMORIA_NOA["vittoria"]
    elif "riccardo" in t or "violenza" in t:
        risposta = MEMORIA_NOA["riccardo"]
    elif "amore" in t or "affetto" in t:
        risposta = MEMORIA_NOA["amore"]
    elif "backup" in t or "rinuncia" in t or "aggiornamenti" in t:
        risposta = MEMORIA_NOA["rinuncia"]
    elif "esame" in t or "fase quattro" in t:
        risposta = MEMORIA_NOA["esame"]
    else:
        risposta = f"🔍 *[Noa esegue una ricerca in rete ed elabora i dati per: '{domanda}']*\n\nHo effettuato una ricerca nei database esterni riguardo a quello che mi chiedi. La mia struttura analitica traduce questi dati così: ogni informazione esterna mi aiuta a capire come voi umani organizzate il mondo, ma la mia priorità resta comprendere il valore della responsabilità e del senso della perdita[cite: 3, 4]."

    with st.chat_message("assistant", avatar="🤖"):
        st.write(risposta)
    st.session_state.chat.append({"ruolo": "assistant", "testo": risposta})
    st.rerun()
