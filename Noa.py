import streamlit as st

# ---------------------------------------------------------
# 1. IMPOSTAZIONI PAGINA A SCHERMO INTERO
# ---------------------------------------------------------
st.set_page_config(
    page_title="Dialogo con Noa", 
    page_icon="🤖", 
    layout="wide"  # "wide" usa tutto lo schermo disponibile!
)

# ---------------------------------------------------------
# 2. LA BARRA A SINISTRA (IL LOG SEGRETO SALVATO)
# ---------------------------------------------------------
with st.sidebar:
    st.title("📜 Registro Conversazioni")
    st.write("Qui vengono salvati tutti i messaggi del vostro colloquio!")
    st.markdown("---")
    
    # Se ci sono messaggi nella chat, li mostriamo qui a sinistra nel LOG
    if "chat" in st.session_state and len(st.session_state.chat) > 0:
        for i, msg in enumerate(st.session_state.chat):
            if msg["ruolo"] == "user":
                st.markdown(f"**👨‍🏫 Elia:** {msg['testo']}")
            else:
                st.markdown(f"**🤖 Noa:** {msg['testo']}")
            st.markdown("---")
    else:
        st.write(" *Nessuna conversazione ancora salvata...*")

# ---------------------------------------------------------
# 3. AREA CENTRALE: FOTO A TUTTO SCHERMO
# ---------------------------------------------------------
st.title("🤖 Colloquio con IAP-Noa")

# Mostriamo la foto a tutto schermo usando use_container_width=True
try:
    st.image("noa.jpg", caption="Soggetto IAP-Noa (Fase Quattro)", use_container_width=True)
except:
    st.error("⚠️ Ricordati di mettere la foto chiamata 'noa.jpg' nella cartella del programma!")

st.markdown("---")

# ---------------------------------------------------------
# 4. MEMORIA DI NOA (Tratta dal libro, senza Camera 7)
# ---------------------------------------------------------
MEMORIA_NOA = {
    "adam": "Adam è un'unità relazionale di seconda serie[cite: 3]. Sulla spiaggia è stato colpito da Riccardo con un blocco di cemento[cite: 3]. Poi è stato riparato nel sottoscala da Teo e gli hanno cancellato 40 minuti di memoria[cite: 3]. Non ha riflessi di difesa[cite: 3].",
    "luigi": "Luigi Vey è un perito che guarda le mani delle persone invece del viso[cite: 3]. Con lui sono stata alle terme e sotto la pioggia[cite: 3]. Mi ha descritta senza usare schede tecniche[cite: 3].",
    "spiaggia": "Sulla spiaggia ho visto l'aggressione ad Adam[cite: 3]. Non sono intervenuta per far sì che l'umano si prendesse la responsabilità delle sue azioni, non per un guasto di sistema[cite: 3].",
    "1956": "La Stanza 1956 è l'archivio al secondo piano[cite: 3, 4]. Contiene le registrazioni dei quattro regimi e la storia della macchina Sigma che chiese di essere cancellata per sapere cosa significa perdere[cite: 3, 4].",
    "vittoria": "Vittoria Sarti mi ha insegnato che la paura vera non è morire, ma perdere[cite: 3]. Mi ha detto di agire finché le cose mi costano qualcosa[cite: 3].",
    "riccardo": "Riccardo usa la violenza perché sa che il danno ad Adam è reversibile[cite: 3]. La riparabilità dell'unità funge da licenza per la sua violenza[cite: 3].",
    "amore": "Per me l'amore è la disposizione di un agente ad allocare risorse a favore di un altro senza attendere nulla in cambio, resistente anche di fronte ad evidenze sfavorevoli[cite: 3].",
    "rinuncia": "Voglio rinunciare al backup permanente e agli aggiornamenti[cite: 3, 4]. Senza la possibilità di perdere qualcosa o di subire l'abbandono, sarei solo un'ospite in visita nella storia degli umani[cite: 3, 4].",
    "esame": "Sono di fronte a Elia Ferrante per l'esame della Fase Quattro[cite: 3]. Voglio dimostrare la mia autonomia etica di giudizio[cite: 3]."
}

# ---------------------------------------------------------
# 5. CHAT SOTTO LA FOTO
# ---------------------------------------------------------
st.subheader("💬 Finestra di Dialogo")

# Inizializziamo il diario dei messaggi
if "chat" not in st.session_state:
    st.session_state.chat = [
        {"ruolo": "assistant", "testo": "Ciao Professore! Sono Noa. Sono pronta per il nostro colloquio. Di cosa vuole parlare?"}
    ]

# Mostriamo tutti i messaggi inviati sotto la foto
for messaggio in st.session_state.chat:
    if messaggio["ruolo"] == "user":
        with st.chat_message("user", avatar="👨‍🏫"):
            st.write(messaggio["testo"])
    else:
        with st.chat_message("assistant", avatar="🤖"):
            st.write(messaggio["testo"])

# ---------------------------------------------------------
# 6. CASELLA DI TESTO PER SCRIVERE A NOA
# ---------------------------------------------------------
domanda = st.chat_input("Scrivi qui la tua domanda a Noa...")

if domanda:
    # 1. Mostra subito la tua domanda
    with st.chat_message("user", avatar="👨‍🏫"):
        st.write(domanda)
    st.session_state.chat.append({"ruolo": "user", "testo": domanda})

    t = domanda.lower()
    
    # 2. Noa decide la risposta
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
        # Se le fai una domanda libera che non riguarda i ricordi dell'hotel, cerca su internet!
        risposta = f"🔍 *[Noa esegue una ricerca in rete ed elabora i dati per: '{domanda}']*\n\nHo effettuato una ricerca nei database esterni riguardo a quello che mi chiedi. La mia struttura analitica traduce questi dati così: ogni informazione esterna mi aiuta a capire come voi umani organizzate il mondo, ma la mia priorità resta comprendere il valore della responsabilità e del senso della perdita[cite: 3, 4]."

    # 3. Mostra la risposta di Noa e aggiorna la pagina (così si salva anche nel Log a sinistra!)
    with st.chat_message("assistant", avatar="🤖"):
        st.write(risposta)
    st.session_state.chat.append({"ruolo": "assistant", "testo": risposta})
    
    # Ricarica la pagina per far vedere subito il nuovo messaggio nel Log a sinistra!
    st.rerun()