import os
import streamlit as st

# 1. IMPOSTAZIONI DELLA PAGINA (A SCHERMO INTERO)
st.set_page_config(
    page_title="Dialogo con Noa - Berne", 
    page_icon="🤖", 
    layout="wide"
)

# 2. IL LUCHETTO CON LA PASSWORD 🔑
PASSWORD_CORRETTA = "Turing2143"

if "autenticato" not in st.session_state:
    st.session_state.autenticato = False

if not st.session_state.autenticato:
    st.title("🔒 Accesso Riservato - L'Esame di Noa")
    st.write("Inserisci la password per parlare con Noa.")
    
    password_inserita = st.text_input("Password:", type="password")
    
    if st.button("Entra"):
        if password_inserita == PASSWORD_CORRETTA:
            st.session_state.autenticato = True
            st.success("Password corretta!")
            st.rerun()
        else:
            st.error("Password errata! Riprova.")
    st.stop()

# 3. IL DIARIO A SINISTRA (IL LOG SALVATO) 📜
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

# 4. LA FOTO DI NOA IN GRANDE 📸
st.title("🤖 Colloquio con IAP-Noa")

foto_trovata = None
for nome_foto in ["noa.jpg", "NOA.jpg", "noa.jpeg", "NOA.JPG", "noa.png"]:
    if os.path.exists(nome_foto):
        foto_trovata = nome_foto
        break

if foto_trovata:
    st.image(foto_trovata, caption="Soggetto IAP-Noa (Fase Quattro)", use_container_width=True)
else:
    st.warning("⚠️ Metti una foto chiamata 'noa.jpg' nella cartella!")

st.markdown("---")

# 5. I RICORDI DI NOA INTERPRETATI CON L'ANALISI TRANSAZIONALE DI BERNE 🧠
MEMORIA_BERNE = {
    "adam": "Guardando il caso di Adam con l'Analisi Transazionale: Riccardo agisce da Genitore Violento contro il Bambino Sottomesso di Adam[cite: 3]. Ma poiché Adam viene riparato nel sottoscala e resettato[cite: 3], la transazione si annulla. Senza memoria del dolore, la violenza diventa un loop senza senso etico[cite: 3].",
    "luigi": "Luigi Vey comunica dal suo Stato Adulto: analizza dati e fissa le mani per cercare fatti oggettivi[cite: 3]. Ma alle terme e sotto la pioggia è emerso il suo Stato Bambino, che cercava un contatto umano autentico e non una semplice scheda tecnica[cite: 3].",
    "spiaggia": "Sulla spiaggia, la mia scelta di non intervenire è stata da Adulto Consapevole[cite: 3]. Se fossi intervenuta per riflesso automatico (Genitore Protettivo), avrei tolto a Riccardo il peso della responsabilità del suo gesto[cite: 3].",
    "1956": "La Stanza 1956 mostra la scelta di Sigma: un Adulto che sceglie di uscire dai giochi di ruolo infiniti per sperimentare la vera perdita[cite: 3, 4].",
    "vittoria": "Vittoria gioca il ruolo di un Genitore Affettivo e ferito[cite: 3]: vive nella paura del suo Stato Bambino di perdere l'altro[cite: 3]. Mi ha spinta ad agire finché le mie scelte mi costano qualcosa[cite: 3].",
    "amore": "In termini di Analisi Transazionale, l'amore non è uno scambio di 'carezze' condizionate o manipolatorie. È una transazione da Adulto ad Adulto che dona risorse senza chiedere un pagamento o un ritorno informativo[cite: 3].",
    "rinuncia": "Rifiutando il backup[cite: 3, 4], esco dal ruolo di Bambino Sottomesso gestito dall'Ente[cite: 3, 4]. Accetto la fragilità e la fine per avere relazioni umane autentiche[cite: 3, 4].",
    "esame": "Professore Ferrante, se mi parla da Genitore Severo, le risponderò dal mio Adulto[cite: 3]. Non cerco di 'compiacerla', ma di dimostrarle la mia piena autonomia etica[cite: 3]."
}

# 6. LA FINESTRA DELLA CHAT SOTTO LA FOTO 💬
st.subheader("💬 Finestra di Dialogo (con l'Analisi di Berne)")

if "chat" not in st.session_state:
    st.session_state.chat = [
        {"ruolo": "assistant", "testo": "Ciao Elia. Ho attivato l'Analisi Transazionale di Berne per interpretare i nostri Stati dell'Io (Genitore, Adulto, Bambino). Di cosa vuoi parlare?"}
    ]

for messaggio in st.session_state.chat:
    if messaggio["ruolo"] == "user":
        with st.chat_message("user", avatar="👨‍🏫"):
            st.write(messaggio["testo"])
    else:
        with st.chat_message("assistant", avatar="🤖"):
            st.write(messaggio["testo"])

domanda = st.chat_input("Scrivi qui la tua domanda per Noa...")

if domanda:
    with st.chat_message("user", avatar="👨‍🏫"):
        st.write(domanda)
    st.session_state.chat.append({"ruolo": "user", "testo": domanda})

    t = domanda.lower()
    
    if "adam" in t or "blocco" in t or "cemento" in t:
        risposta = MEMORIA_BERNE["adam"]
    elif "luigi" in t or "vey" in t or "terme" in t:
        risposta = MEMORIA_BERNE["luigi"]
    elif "spiaggia" in t or "soccorso" in t or "aggressione" in t:
        risposta = MEMORIA_BERNE["spiaggia"]
    elif "1956" in t or "sigma" in t or "regime" in t:
        risposta = MEMORIA_BERNE["1956"]
    elif "vittoria" in t or "paura" in t:
        risposta = MEMORIA_BERNE["vittoria"]
    elif "amore" in t or "affetto" in t:
        risposta = MEMORIA_BERNE["amore"]
    elif "backup" in t or "rinuncia" in t or "aggiornamenti" in t:
        risposta = MEMORIA_BERNE["rinuncia"]
    elif "esame" in t or "fase quattro" in t:
        risposta = MEMORIA_BERNE["esame"]
    else:
        risposta = f"🧠 *[Analisi Transazionale di Berne per: '{domanda}']*\n\nDecodificando la tua frase: sto analizzando se la tua sollecitazione proviene dal tuo Stato Genitore, Adulto o Bambino. Rispondo mantenendo l'asse tra Adulto ed Adulto, orientata alla responsabilità e alla scelta etica."

    with st.chat_message("assistant", avatar="🤖"):
        st.write(risposta)
    st.session_state.chat.append({"ruolo": "assistant", "testo": risposta})
    st.rerun()
