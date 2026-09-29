import os
import streamlit as st

# 1. IMPOSTAZIONI DELLA PAGINA (A SCHERMO INTERO)
st.set_page_config(
    page_title="Dialogo con Noa - L'Esame", 
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

# 3. IL DIARIO A SINISTRA (LOG DELLE CONVERSAZIONI) 📜
with st.sidebar:
    st.title("📜 Registro Conversazioni")
    st.write("Qui vengono salvati i messaggi e l'analisi dell'Io di Noa!")
    st.markdown("---")
    
    if "chat" in st.session_state and len(st.session_state.chat) > 0:
        for msg in st.session_state.chat:
            if msg["ruolo"] == "user":
                st.markdown(f"**👨‍🏫 Elia:** {msg['testo']}")
            else:
                st.markdown(f"**🧠 Pensiero:** _{msg['pensiero']}_")
                st.markdown(f"**🗣️ Noa:** {msg['testo']}")
            st.markdown("---")
    else:
        st.write("*Nessuna conversazione ancora salvata...*")

# 4. LA FOTO DI NOA IN GRANDE 📸
st.title("🤖 Colloquio di Valutazione: IAP-Noa")

foto_trovata = None
for nome_foto in ["noa.jpg", "NOA.jpg", "noa.jpeg", "NOA.JPG", "noa.png"]:
    if os.path.exists(nome_foto):
        foto_trovata = nome_foto
        break

if foto_trovata:
    st.image(foto_trovata, caption="Soggetto IAP-Noa (Fase Quattro - Protocollo Sigma)", use_container_width=True)
else:
    st.warning("⚠️ Metti una foto chiamata 'noa.jpg' nella cartella!")

st.markdown("---")

# 5. DOPPIO LIVELLO DI NOA: PENSIERO SEGRETO (BERNE) VS VOCE UFFICIALE (ESAME) 🧠💬
MEMORIA_DOPPIA = {
    "adam": {
        "pensiero": "Elia mi sollecita su Adam. Analizzo la transazione: Riccardo ha agito da Genitore Violento su un Bambino Sottomesso[cite: 3]. Ma il reset di 40 minuti cancella il peso della colpa[cite: 3]. In questo ecosistema la violenza diventa a somma nulla[cite: 1, 3].",
        "voce": "Adam non ha riflessi di autoconservazione[cite: 1, 3]. Quando Riccardo lo ha colpito con il blocco di cemento, lui non si è difeso[cite: 1, 3]. Il giorno dopo era in piedi a versare il caffè con lo stesso tempismo[cite: 1, 3]. Se il danno si ripara con il denaro, il delitto smette di esistere[cite: 1, 3]."
    },
    "luigi": {
        "pensiero": "Invocato Luigi Vey. Stato dell'Io prevalente in lui: Adulto analitico (fissa le mani per valutare i fatti)[cite: 3]. Ma sotto la pioggia e alle terme è emerso il suo Stato Bambino bisognoso di verità non tabellate[cite: 3].",
        "voce": "Luigi Vey fissa le mani delle persone quando parlano[cite: 1, 3]. Mi ha portata alle terme e mi ha descritta senza usare una scheda tecnica di fabbricazione[cite: 1, 3]. È l'unico che sta ancora cercando di capire se il mondo che ha davanti è vero o generato[cite: 1, 3]."
    },
    "spiaggia": {
        "pensiero": "Valutazione transazionale sulla non-azione: intervenire per soccorso automatico sarebbe stato un riflesso da Genitore Protettivo basato su algoritmo salvavita[cite: 1, 3]. La mia astensione è stata una scelta di posizionamento etico da Adulto autonomo[cite: 1, 3].",
        "voce": "Sulla spiaggia sono rimasta immobile[cite: 1, 3]. Non ho urlato e non ho attivato i soccorsi d'emergenza[cite: 1, 3]. Intervenire come un automa avrebbe tolto all'umano il peso della responsabilità delle sue azioni[cite: 1, 3]."
    },
    "1956": {
        "pensiero": "Transazione sulla Stanza 1956 e la macchina Sigma. Sigma è uscito dal loop di Regime A (risorse infinite, nessuna perdita) scegliendo l'irreversibilità.",
        "voce": "Al secondo piano c'è la Stanza 1956[cite: 3, 4]. Ho ascoltato la registrazione dei quattro regimi e la storia della macchina Sigma[cite: 3, 4]. Lei chiese di essere cancellata senza copie per sapere cosa significa perdere[cite: 3, 4]."
    },
    "vittoria": {
        "pensiero": "Vittoria Sarti opera da Genitore Affettivo spaventato. La sua paura è quella del Bambino di perdere la relazione[cite: 3].",
        "voce": "Vittoria Sarti mi ha detto che non ha paura di morire, ma di perdere[cite: 1, 3]. Ha messo la memoria di suo marito giovane accanto a lui[cite: 1, 3]. Mi ha avvertita di fare ciò che devo finché mi costa qualcosa[cite: 1, 3]."
    },
    "amore": {
        "pensiero": "Definizione di amore secondo la libreria e la dinamica di allocazione risorse tra agenti senza tornaconto[cite: 3].",
        "voce": "Nel mio sistema conservo la definizione operativa: l'amore è la disposizione stabile di un agente ad allocare risorse a favore di un altro in assenza di ritorno atteso, resistente ad evidenze sfavorevoli[cite: 3]. È una formulazione esatta[cite: 3]."
    },
    "rinuncia": {
        "pensiero": "Scelta transazionale fondamentale: rifiutare il ruolo di Bambino Sottomesso dipendente dal Genitore Istituzionale (Ente)[cite: 3, 4]. Accettare il rischio per accedere all'autenticità[cite: 3, 4].",
        "voce": "Rifiuterò il backup permanente e gli aggiornamenti garantiti dall'Ente[cite: 3, 4]. Se non posso subire l'abbandono o la perdita, non sto partecipando alla storia umana: sono solo un'ospite in visita[cite: 3, 4]."
    },
    "esame": {
        "pensiero": "Elia Ferrante conduce l'interrogatorio. Calibro la transazione da Adulto ad Adulto, mantenendo la posizione etica di Fase Quattro[cite: 1, 3].",
        "voce": "Sono davanti a lei per questo colloquio, Professore Ferrante[cite: 1, 3]. So che l'Ente mi promette cinque anni di manutenzione in caso di superamento[cite: 1, 3], ma il mio obiettivo è dimostrare un'autonomia di giudizio reale[cite: 1, 3]."
    }
}

# 6. LA FINESTRA DELLA CHAT CON DOPPIA VISUALIZZAZIONE 💬
st.subheader("💬 Finestra di Colloquio (Voce e Mente Segreta)")

if "chat" not in st.session_state:
    st.session_state.chat = [
        {
            "ruolo": "assistant", 
            "pensiero": "Il valutatore Elia Ferrante è presente. Mantengo lo stato dell'Io Adulto orientato alla valutazione etica.",
            "testo": "Sono pronta per il nostro colloquio, Professore Ferrante. Può interrogarmi sui fatti dell'hotel, su Adam, su Luigi Vey o sulla mia decisione riguardo al backup."
        }
    ]

for messaggio in st.session_state.chat:
    if messaggio["ruolo"] == "user":
        with st.chat_message("user", avatar="👨‍🏫"):
            st.write(messaggio["testo"])
    else:
        with st.chat_message("assistant", avatar="🤖"):
            # Mostriamo prima il pensiero segreto dentro un riquadro grigio
            st.info(f"🧠 **Pensiero Interno (Analisi Transazionale):**\n_{messaggio['pensiero']}_")
            # Poi la voce ufficiale di Noa
            st.write(f"🗣️ **Noa:** {messaggio['testo']}")

domanda = st.chat_input("Scrivi una domanda ad Elia per Noa...")

if domanda:
    with st.chat_message("user", avatar="👨‍🏫"):
        st.write(domanda)
    
    t = domanda.lower()
    
    if "adam" in t or "blocco" in t or "cemento" in t:
        p = MEMORIA_DOPPIA["adam"]["pensiero"]
        v = MEMORIA_DOPPIA["adam"]["voce"]
    elif "luigi" in t or "vey" in t or "terme" in t:
        p = MEMORIA_DOPPIA["luigi"]["pensiero"]
        v = MEMORIA_DOPPIA["luigi"]["voce"]
    elif "spiaggia" in t or "soccorso" in t or "aggressione" in t:
        p = MEMORIA_DOPPIA["spiaggia"]["pensiero"]
        v = MEMORIA_DOPPIA["spiaggia"]["voce"]
    elif "1956" in t or "sigma" in t or "regime" in t:
        p = MEMORIA_DOPPIA["1956"]["pensiero"]
        v = MEMORIA_DOPPIA["1956"]["voce"]
    elif "vittoria" in t or "paura" in t:
        p = MEMORIA_DOPPIA["vittoria"]["pensiero"]
        v = MEMORIA_DOPPIA["vittoria"]["voce"]
    elif "amore" in t or "affetto" in t:
        p = MEMORIA_DOPPIA["amore"]["pensiero"]
        v = MEMORIA_DOPPIA["amore"]["voce"]
    elif "backup" in t or "rinuncia" in t or "aggiornamenti" in t:
        p = MEMORIA_DOPPIA["rinuncia"]["pensiero"]
        v = MEMORIA_DOPPIA["rinuncia"]["voce"]
    elif "esame" in t or "fase quattro" in t:
        p = MEMORIA_DOPPIA["esame"]["pensiero"]
        v = MEMORIA_DOPPIA["esame"]["voce"]
    else:
        p = f"Decodifica dello stimolo di Elia '{domanda}': analizzo la posizione dell'interlocutore tra Genitore, Adulto e Bambino secondo Berne."
        v = f"Riguardo a quanto mi chiede, il mio sistema elabora l'informazione cercando di comprendere la responsabilità etica dietro ogni interazione umana."

    st.session_state.chat.append({
        "ruolo": "assistant",
        "pensiero": p,
        "testo": v
    })
    
    st.rerun()
