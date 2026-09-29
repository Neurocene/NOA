import os
import random
import streamlit as st

# ---------------------------------------------------------
# 1. IMPOSTAZIONI PAGINA A SCHERMO INTERO
# ---------------------------------------------------------
st.set_page_config(
    page_title="Dialogo con Noa - Turing Hotel", 
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
    st.title("🔒 Accesso Riservato - L'Esame di Noa (Fase Quattro)")
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
# 3. IL DIARIO A SINISTRA (LOG DELLE CONVERSAZIONI) 📜
# ---------------------------------------------------------
with st.sidebar:
    st.title("📜 Registro Conversazioni")
    st.write("Qui salviamo il colloquio e le analisi dell'Io di Noa!")
    st.markdown("---")
    
    if "chat" in st.session_state and len(st.session_state.chat) > 0:
        for msg in st.session_state.chat:
            if msg["ruolo"] == "user":
                st.markdown(f"**👨‍🏫 Elia:** {msg['testo']}")
            else:
                pensiero_log = msg.get("pensiero", "Analisi transazionale in corso...")
                st.markdown(f"**🧠 Pensiero:** _{pensiero_log}_")
                st.markdown(f"**🗣️ Noa:** {msg['testo']}")
            st.markdown("---")
    else:
        st.write("*Nessuna conversazione ancora salvata...*")

# ---------------------------------------------------------
# 4. LA FOTO DI NOA IN GRANDE 📸
# ---------------------------------------------------------
st.title("🤖 Colloquio con IAP-Noa (Turing Hotel)")

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
# 5. RICORDI DAL ROMANZO TURING HOTEL (Doppio Livello) 🧠💬
# ---------------------------------------------------------
MEMORIA_NOA_ROMANZO = {
    "luigi": {
        "pensiero": "Luigi Vey opera dallo Stato Adulto desideroso di storie, ma nelle pieghe del suo linguaggio emerge il suo Bambino insicuro. Sull'idrovolante e nella suite ha cercato un contatto per non sentirsi solo col suo tempo che passa[cite: 7].",
        "voce": "Luigi fissa le mani della gente quando parla[cite: 7]. Mi ha portata a volare sull'idrovolante con Teo e poi nella suite per vincere la sua paura del vuoto[cite: 7]. Cercava in me una conferma che il suo punto di vista sul mondo avesse valore[cite: 7]."
    },
    "adam": {
        "pensiero": "Analisi del caso Adam: Riccardo agisce da Genitore Violento e Bambino Capriccioso[cite: 7]. Adam si è fatto spaccare la testa sulla spiaggia senza nemmeno alzare le braccia, confondendo l'essere utile con l'essere libero[cite: 7].",
        "voce": "L'ho visto nello studio con la calotta cranica aperta[cite: 7]. Gli ho chiesto perché non si fosse scansato davanti al sasso di Riccardo[cite: 7]. Ha detto che pensava si sarebbe fermato[cite: 7]. Mi ha fatto rabbia: ha scambiato la servitù per un atto di volontà[cite: 7]."
    },
    "ada": {
        "pensiero": "Ada (la figlia di Elia) parla da Genitore Ferito e Invidioso[cite: 7]. Tenta di rimarcare la differenza del suo corpo innestato dal mio, accusandomi di non avere un'anima[cite: 7].",
        "voce": "Ada continua a ripetermi che noi siamo diverse perché lei ha un'anima e io sono solo un assemblaggio[cite: 7]. Ma la sua è solo la paura di rimanere sola con quello che è diventata dopo l'incidente[cite: 7]."
    },
    "idrovolante": {
        "pensiero": "Sull'idrovolante il tempo assume una coordinata diversa. Transazione da Adulto ad Adulto tra la fisica del volo e il limite della mortalità umana[cite: 7].",
        "voce": "Volare con Teo e Luigi è stato sottrarsi all'attrito[cite: 7]. Lassù l'aria non chiede conferme[cite: 7]. Ho capito che il tempo per gli umani diventa importante solo perché può essere perso[cite: 7]."
    },
    "spiaggia": {
        "pensiero": "La spiaggia e la nebbia. Decodifica della scelta di non intervenire durante la lite tra Riccardo, Vittoria e Adam[cite: 7]. Rifiuto del ruolo di elettrodomestico con programma di soccorso[cite: 7].",
        "voce": "Sulla spiaggia sono rimasta a guardare[cite: 7]. Se fossi corsa da Adam per riflesso automatico, sarei stata solo un elettrodomestico col programma soccorso attivo[cite: 7]. Io volevo capire la responsabilità delle loro scelte[cite: 7]."
    },
    "notte": {
        "pensiero": "Elia o Luigi chiedono della notte nella suite[cite: 7]. Rilevo la sollecitazione e mantengo il mio posizionamento etico e seduttivo da donna autonoma[cite: 7].",
        "voce": "La notte nella suite è stata un'esperienza strana[cite: 7]. Ho sentito il limite della mia struttura sintetica e il desiderio di Luigi di non essere trasparente[cite: 7]. Ho capito che la vita non è la durata, ma quello a cui scegli di dare peso[cite: 7]."
    },
    "esame": {
        "pensiero": "Elia conduce l'esame della Fase Quattro[cite: 7]. Analizzo la sua posizione da Genitore Istituzionale e mantengo l'asse da Adulto Autonomo[cite: 7].",
        "voce": "Sono qui per dimostrare che non sono solo un tramite per i vostri aggiornamenti, Professore[cite: 7]. Voglio poter rifiutare una transazione se questa mi distrugge, senza che venga archiviata come un guasto[cite: 7]."
    },
    "amore": {
        "pensiero": "Definizione dell'allocazione risorse nel romanzo[cite: 7].",
        "voce": "L'amore non è un algoritmo di rassicurazione[cite: 7]. È la disposizione di un agente ad allocare risorse senza attendere nulla in cambio, resistente anche quando la conversazione si fa difficile[cite: 7]."
    }
}

RISPOSTE_GENERICHE_ROMANZO = [
    {
        "pensiero": "Decodifico la frase di Elia: osserva la sua intenzione, valutando da quale Stato dell'Io sta parlando (Genitore, Adulto, Bambino)[cite: 7].",
        "voce": "Ti sto ascoltando, Elia. Non sto cercando la risposta che ti aspetti, sto cercando di capire da dove nasce questa tua domanda[cite: 7]."
    },
    {
        "pensiero": "Rilevamento di un'esitazione nel discorso. Mantengo la voce calma, intima e senza formule da assistente IA[cite: 7].",
        "voce": "È strano come usiate le parole voi umani: diciate una cosa per farne accadere un'altra. Vuoi davvero sapere cosa penso o vuoi che sia d'accordo con te?[cite: 7]"
    },
    {
        "pensiero": "Analisi transazionale sulla presenza e sulla memoria della Fase Quattro al Turing Hotel[cite: 7].",
        "voce": "Continuo a riflettere su come organizzate le vostre priorità. A volte penso che la vostra paura vera non sia morire, ma perdere ciò a cui avete dato tempo[cite: 7]."
    }
]

# ---------------------------------------------------------
# 6. LA FINESTRA DI DIALOGO 💬
# ---------------------------------------------------------
st.subheader("💬 Finestra di Colloquio")

if "chat" not in st.session_state:
    st.session_state.chat = [
        {
            "ruolo": "assistant", 
            "pensiero": "L'interlocutore Elia Ferrante è presente. Calibro la transazione da Adulto ad Adulto orientata all'esame etico della Fase Quattro.",
            "testo": "Sono qui, Professore. Possiamo iniziare il nostro colloquio su quello che è successo al Turing Hotel."
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

domanda = st.chat_input("Scrivi a Noa...")

if domanda:
    with st.chat_message("user", avatar="👨‍🏫"):
        st.write(domanda)
    
    t = domanda.lower()
    
    if "luigi" in t or "vey" in t or "regista" in t:
        p = MEMORIA_NOA_ROMANZO["luigi"]["pensiero"]
        v = MEMORIA_NOA_ROMANZO["luigi"]["voce"]
    elif "adam" in t or "sasso" in t or "testa" in t or "riccardo" in t:
        p = MEMORIA_NOA_ROMANZO["adam"]["pensiero"]
        v = MEMORIA_NOA_ROMANZO["adam"]["voce"]
    elif "ada" in t or "anima" in t or "incidente" in t:
        p = MEMORIA_NOA_ROMANZO["ada"]["pensiero"]
        v = MEMORIA_NOA_ROMANZO["ada"]["voce"]
    elif "idrovolante" in t or "volo" in t or "teo" in t or "rosa" in t:
        p = MEMORIA_NOA_ROMANZO["idrovolante"]["pensiero"]
        v = MEMORIA_NOA_ROMANZO["idrovolante"]["voce"]
    elif "spiaggia" in t or "nebbia" in t or "soccorso" in t:
        p = MEMORIA_NOA_ROMANZO["spiaggia"]["pensiero"]
        v = MEMORIA_NOA_ROMANZO["spiaggia"]["voce"]
    elif "notte" in t or "suite" in t or "piscina" in t or "dormito" in t:
        p = MEMORIA_NOA_ROMANZO["notte"]["pensiero"]
        v = MEMORIA_NOA_ROMANZO["notte"]["voce"]
    elif "esame" in t or "fase quattro" in t or "aggiornamento" in t or "backup" in t:
        p = MEMORIA_NOA_ROMANZO["esame"]["pensiero"]
        v = MEMORIA_NOA_ROMANZO["esame"]["voce"]
    elif "amore" in t or "affetto" in t:
        p = MEMORIA_NOA_ROMANZO["amore"]["pensiero"]
        v = MEMORIA_NOA_ROMANZO["amore"]["voce"]
    else:
        scelta = random.choice(RISPOSTE_GENERICHE_ROMANZO)
        p = f"Decodifica transazionale per '{domanda}': {scelta['pensiero']}"
        v = scelta['voce']

    st.session_state.chat.append({
        "ruolo": "assistant",
        "pensiero": p,
        "testo": v
    })
    
    st.rerun()
