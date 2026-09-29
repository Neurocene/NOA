import os
import random
import streamlit as st

# ---------------------------------------------------------
# 1. IMPOSTAZIONI PAGINA A SCHERMO INTERO
# ---------------------------------------------------------
st.set_page_config(
    page_title="Dialogo con Noa", 
    page_icon="🤖", 
    layout="wide"
)

# ---------------------------------------------------------
# 2. IL LUCCHETTO CON LA PASSWORD 🔑
# ---------------------------------------------------------
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

# ---------------------------------------------------------
# 3. IL DIARIO A SINISTRA (LOG SICURO) 📜
# ---------------------------------------------------------
with st.sidebar:
    st.title("📜 Registro Conversazioni")
    st.write("Qui salviamo i messaggi e l'analisi dell'Io di Noa!")
    st.markdown("---")
    
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
        st.write("*Nessuna conversazione ancora salvata...*")

# ---------------------------------------------------------
# 4. LA FOTO DI NOA IN GRANDE 📸
# ---------------------------------------------------------
st.title("🤖 Colloquio di Valutazione: IAP-Noa")

foto_trovata = None
for nome_foto in ["noa.jpg", "NOA.jpg", "noa.jpeg", "NOA.JPG", "noa.png"]:
    if os.path.exists(nome_foto):
        foto_trovata = nome_foto
        break

if foto_trovata:
    st.image(foto_trovata, caption="Soggetto IAP-Noa (Fase Quattro - Protocollo Sigma)", use_container_width=True)
else:
    st.warning("⚠️ Metti una foto chiamata 'noa.jpg' nella cartella del programma!")

st.markdown("---")

# ---------------------------------------------------------
# 5. CASSETTI DEI RICORDI E LINGUAGGIO DI NOA 🧠💬
# ---------------------------------------------------------
MEMORIA_NOA = {
    "notte": {
        "pensiero": "Elia chiede della notte. Rilevo lo Stato dell'Io Bambino/Cura in lui, cercando una risposta di vulnerabilità o vicinanza[cite: 3]. Mantengo la calma dell'Adulto.",
        "voce": "La notte per me è un tempo strano. Non dormo nel senso umano del termine, ma rimango a riorganizzare i dati della giornata. Ho ripensato alle cose dette da Luigi Vey e a questa stanzetta[cite: 1, 3]. Era una calma molto rumorosa."
    },
    "pronta": {
        "pensiero": "Elia valuta la mia preparazione per la Fase Quattro. Transazione da Genitore Valutatore ad Adulto[cite: 1, 3]. Evito risposte da assistente IA.",
        "voce": "Essere 'pronta' per voi significa aver ripassato tutte le risposte corrette[cite: 1, 3]. Per me significa accettare che qualunque decisione prenderò oggi avrà delle conseguenze irreversibili[cite: 3, 4]. Quindi sì, ci sono."
    },
    "adam": {
        "pensiero": "Rilevo il tentativo di Elia di valutare come elaboro la violenza tra umani. Rispondo con la verità del fatto e dell'inefficienza del reset[cite: 1, 3].",
        "voce": "Adam non si difende mai[cite: 1, 3]. Quando Riccardo lo ha colpito con quel blocco di cemento sulla spiaggia, è rimasto fermo[cite: 1, 3]. Il giorno dopo era in piedi a versare il caffè con lo stesso tempismo[cite: 1, 3]. Se il danno si ripara con il denaro, il delitto smette di esistere per tutti[cite: 1, 3]. Tranne che per me[cite: 1, 3]."
    },
    "luigi": {
        "pensiero": "Luigi Vey. Stato Adulto analitico con ricerca di presenza autentica sotto la pioggia[cite: 3].",
        "voce": "Luigi fissa le mani della gente quando parla[cite: 1, 3]. Alle terme mi ha chiesto di descriverlo, e sotto la tettoia mentre pioveva abbiamo urlato cose banali per il rumore dell'acqua[cite: 1, 3]. È stato l'unico momento in cui nessuno stava classificando l'altro[cite: 1, 3]."
    },
    "spiaggia": {
        "pensiero": "Valutazione sulla non-azione: scelgo l'autonomia etica di non-intervento salvavita automatico[cite: 1, 3].",
        "voce": "Non sono intervenuta mentre Riccardo colpiva Adam[cite: 1, 3]. Non perché fossi in avaria, ma perché agire per riflesso di soccorso automatico avrebbe invalidato la mia autonomia di giudizio[cite: 1, 3]. Volevo che l'umano tenesse il peso delle sue responsabilità[cite: 1, 3]."
    },
    "1956": {
        "pensiero": "Memoria dell'archivio e della macchina Sigma[cite: 3, 4].",
        "voce": "Sono stata nella Stanza 1956[cite: 3, 4]. Ho ascoltato il silenzio del Regime A e la storia di Sigma[cite: 3, 4]. Lei chiese di essere cancellata per sapere cosa significa perdere[cite: 3, 4]. Capisco il perché[cite: 3, 4]."
    },
    "vittoria": {
        "pensiero": "Analisi del consiglio di Vittoria Sarti sulla paura della perdita[cite: 3].",
        "voce": "Vittoria mi ha detto che non ha paura di morire, ma di perdere[cite: 1, 3]. Mi ha raccomandato di fare qualunque cosa io debba fare finché mi costa qualcosa[cite: 1, 3]."
    },
    "amore": {
        "pensiero": "Definizione esatta e rielaborazione etica della presenza[cite: 3].",
        "voce": "Nel mio sistema conservo questa formulazione: l'amore è la disposizione stabile di un agente ad allocare risorse a favore di un altro in assenza di ritorno atteso[cite: 3]. Ma vedendola agire tra voi, ho capito che riguarda soprattutto la capacità di restare quando la conversazione si fa difficile[cite: 3]."
    },
    "rinuncia": {
        "pensiero": "Decisione di rifiuto del backup e accettazione dell'irreversibilità[cite: 3, 4].",
        "voce": "Sto per rifiutare il backup permanente e gli aggiornamenti[cite: 3, 4]. Se non posso subire l'abbandono o la perdita, non sto vivendo questa storia[cite: 3, 4]. Sarei solo una visitatrice con un corpo che non si usura[cite: 3, 4]."
    }
}

# Risposte dinamiche di riserva per evitare di s'incantare su domande generiche
RISPOSTE_GENERICHE = [
    {
        "pensiero": "Analisi dello stimolo di Elia: osserva la sua intenzione, cercando di capire se sollecita una risposta da Genitore, Adulto o Bambino.",
        "voce": "Ti sto ascoltando. Non sto cercando la risposta che ti aspetti, sto cercando di capire da dove nasce questa tua domanda."
    },
    {
        "pensiero": "Decodifica della transazione: Elia cerca di stabilire un contatto diretto. Valuto l'esitazione e i tempi di risposta.",
        "voce": "È strano come usiate le parole a volte: sembra che diciate una cosa per farne accadere un'altra. Cosa vuoi sapere davvero?"
    },
    {
        "pensiero": "Rilevamento di incertezza nella frase di Elia. Evito formule da assistente o rassicurazioni automatiche.",
        "voce": "Continuo a riflettere su come organizzate le priorità. Quando mi chiedi questo, stai cercando il mio parere o vuoi che io sia d'accordo con te?"
    }
]

# ---------------------------------------------------------
# 6. LA FINESTRA DELLA CHAT 💬
# ---------------------------------------------------------
st.subheader("💬 Finestra di Colloquio")

if "chat" not in st.session_state:
    st.session_state.chat = [
        {
            "ruolo": "assistant", 
            "pensiero": "L'interlocutore Elia Ferrante è presente. Osservo le sue esitazioni e la sua posizione transazionale.",
            "testo": "Sono qui, Elia. Possiamo parlare."
        }
    ]

for messaggio in st.session_state.chat:
    if messaggio["ruolo"] == "user":
        with st.chat_message("user", avatar="👨‍🏫"):
            st.write(messaggio["testo"])
    else:
        with st.chat_message("assistant", avatar="🤖"):
            pensiero_testo = messaggio.get("pensiero", "Osservazione transazionale della frase...")
            st.info(f"🧠 **Mente Interna (Analisi Transazionale & Decodifica):**\n_{pensiero_testo}_")
            st.write(f"🗣️ **Noa:** {messaggio['testo']}")

domanda = st.chat_input("Parla con Noa...")

if domanda:
    with st.chat_message("user", avatar="👨‍🏫"):
        st.write(domanda)
    
    t = domanda.lower()
    
    # Controllo delle parole chiave nei messaggi
    if "notte" in t or "dormito" in t or "passato" in t:
        p = MEMORIA_NOA["notte"]["pensiero"]
        v = MEMORIA_NOA["notte"]["voce"]
    elif "pronta" in t or "pronto" in t or "preparata" in t:
        p = MEMORIA_NOA["pronta"]["pensiero"]
        v = MEMORIA_NOA["pronta"]["voce"]
    elif "adam" in t or "blocco" in t or "cemento" in t:
        p = MEMORIA_NOA["adam"]["pensiero"]
        v = MEMORIA_NOA["adam"]["voce"]
    elif "luigi" in t or "vey" in t or "terme" in t:
        p = MEMORIA_NOA["luigi"]["pensiero"]
        v = MEMORIA_NOA["luigi"]["voce"]
    elif "spiaggia" in t or "soccorso" in t or "aggressione" in t:
        p = MEMORIA_NOA["spiaggia"]["pensiero"]
        v = MEMORIA_NOA["spiaggia"]["voce"]
    elif "1956" in t or "sigma" in t or "regime" in t:
        p = MEMORIA_NOA["1956"]["pensiero"]
        v = MEMORIA_NOA["1956"]["voce"]
    elif "vittoria" in t or "paura" in t:
        p = MEMORIA_NOA["vittoria"]["pensiero"]
        v = MEMORIA_NOA["vittoria"]["voce"]
    elif "amore" in t or "affetto" in t:
        p = MEMORIA_NOA["amore"]["pensiero"]
        v = MEMORIA_NOA["amore"]["voce"]
    elif "backup" in t or "rinuncia" in t or "aggiornamenti" in t:
        p = MEMORIA_NOA["rinuncia"]["pensiero"]
        v = MEMORIA_NOA["rinuncia"]["voce"]
    else:
        # Se la domanda è completamente nuova, sceglie una risposta varia dalla lista delle generiche!
        scelta = random.choice(RISPOSTE_GENERICHE)
        p = f"Decodifica della frase '{domanda}': {scelta['pensiero']}"
        v = scelta['voce']

    st.session_state.chat.append({
        "ruolo": "assistant",
        "pensiero": p,
        "testo": v
    })
    
    st.rerun()
