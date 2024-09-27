import streamlit as st
import random
from datetime import datetime, timedelta
import os


# Funktion zum Laden und Abrufen eines zufälligen Tipps aus der Datei
def get_random_tip(filename):
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as file:
            tips = file.read().splitlines()
            tips = [tip for tip in tips if tip.strip()]  # Entferne leere Zeilen
        return random.choice(tips) if tips else "Keine Tipps verfügbar."
    else:
        return "Tipps-Datei nicht gefunden."


# Funktion zum Abrufen der Imporegeln
def get_impro_rules():
    rules = [
        "1. **Annehmen und Ja sagen**: Im Improtheater ist es wichtig, die Vorschläge und Ideen der anderen anzunehmen und weiterzuführen. Sag nicht 'Nein' und blockiere die Szene, sondern sage 'Ja' und baue darauf auf.",
        "2. **CBZO: Charakter - Beziehung - Ziel - Ort**: Diese Abkürzung steht für die vier Grundpfeiler einer Impro-Szene. Charakter: Wer bin ich? Beziehung: Wie stehe ich zu den anderen? Ziel: Was will ich? Ort: Wo bin ich?",
        "3. **Keine Fragen stellen**: Vermeide es, in der Szene Fragen zu stellen, die den anderen zwingen, die Geschichte voranzutreiben. Stattdessen mach konkrete Aussagen, die die Handlung voranbringen.",
        "4. **Den anderen gut dastehen lassen**: Das Ziel im Improtheater ist es, als Team zusammenzuarbeiten. Hilf den anderen, gut auszusehen, und sie werden dasselbe für dich tun."
    ]
    return rules


# Funktion zum Laden der Spiele aus der Datei
def get_games(filename):
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as file:
            games = file.read().split("\n\n")
        return [game.strip() for game in games if game.strip()]
    else:
        return ["Spiele-Datei nicht gefunden."]


# Funktion zum Laden und Abrufen eines zufälligen Wortes aus einer Datei
def get_random_word_from_file(filename):
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
            words = [word.strip() for word in content.split(",") if word.strip()]
        return random.choice(words) if words else "Keine Worte verfügbar."
    else:
        return f"Datei {filename} nicht gefunden."


# Setze den Seitentitel und das Favicon
st.set_page_config(page_title="IMPROfessionell", page_icon="🎭", layout="wide")

# CSS für ein schöneres Design
st.markdown("""
    <style>
    .big-font {
        font-size:30px !important;
        font-weight: bold;
        color: #1E90FF;
    }
    .stButton>button {
        color: #ffffff;
        background-color: #1E90FF;
        border-radius: 5px;
    }
    .stButton>button:hover {
        background-color: #4169E1;
    }
    .game-title {
        font-size: 24px;
        font-weight: bold;
        color: #1E90FF;
    }
    .game-description {
        font-size: 16px;
        margin-bottom: 20px;
    }
    .social-icon {
        font-size: 24px;
        color: #1E90FF;
        text-decoration: none;
        margin-right: 20px;
    }
    .centered {
        display: flex;
        justify-content: center;
        align-items: center;
    }
    </style>
    """, unsafe_allow_html=True)

# Navigation zwischen Seiten
st.sidebar.title("Navigation")
page = st.sidebar.radio("Wähle eine Seite", ["Startseite", "Was ist Impro?", "Imporegeln", "Improgenerator", "Spiele"])

if page == "Startseite":
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown('<div class="centered">', unsafe_allow_html=True)
        if os.path.exists("imprologo.png"):
            st.image("imprologo.png", width=200)  # Reduzierte Größe des Logos
        else:
            st.write("Logo nicht gefunden.")
        st.markdown('</div>', unsafe_allow_html=True)
    st.title("Willkommen bei IMPROfessionell!")
    st.markdown('<p class="big-font">Jeden Dienstag um 18:00 Uhr (Zusatztermin: Mittwoch 18:00 Uhr)</p>', unsafe_allow_html=True)

    # Countdown zum nächsten Dienstag
    today = datetime.now()
    next_tuesday = today + timedelta((1 - today.weekday()) % 7)
    next_tuesday = next_tuesday.replace(hour=18, minute=0, second=0, microsecond=0)
    time_diff = next_tuesday - today
    days, seconds = time_diff.days, time_diff.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60

    st.info(f"Nächstes Treffen in: {days} Tagen, {hours} Stunden und {minutes} Minuten")

    # Zufälliger Tipp des Tages aus tipps.txt
    random_tip = get_random_tip("tipps.txt")
    st.subheader("💡 Tipp des Tages")
    st.success(random_tip)

    # Instagram-Verweis
    st.markdown("---")
    col1, col2 = st.columns([1, 3])
    with col1:
        if os.path.exists("Insta.jpg"):
            st.image("Insta.jpg", width=50)
        else:
            st.write("Instagram-Logo")
    with col2:
        st.markdown(
            '<a href="https://www.instagram.com/impro_fessionell" target="_blank" class="social-icon">Folge uns auf Instagram @impro_fessionell</a>',
            unsafe_allow_html=True)

elif page == "Was ist Impro?":
    st.title("Was ist Improvisationstheater?")

    # Lesen und Anzeigen des Inhalts von about.txt
    if os.path.exists("about.txt"):
        with open("about.txt", "r", encoding="utf-8") as file:
            about_content = file.read()
        st.markdown(about_content)
    else:
        st.write("Die Datei 'about.txt' wurde nicht gefunden.")

elif page == "Imporegeln":
    st.title("Die wichtigsten Imporegeln")

    rules = get_impro_rules()
    for rule in rules:
        st.markdown(rule)

elif page == "Improgenerator":
    st.title("Improgenerator")
    st.header("Klicke auf die Buttons, um zufällige Impro-Inputs zu erhalten.")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Ort 🏠"):
            random_place = get_random_word_from_file("orte.txt")
            st.success(f"Zufälliger Ort: **{random_place}**")

    with col2:
        if st.button("Beziehung 👥"):
            random_relationship = get_random_word_from_file("beziehungen.txt")
            st.success(f"Zufällige Beziehung: **{random_relationship}**")

    with col3:
        if st.button("Emotion 😊"):
            random_emotion = get_random_word_from_file("emotionen.txt")
            st.success(f"Zufällige Emotion: **{random_emotion}**")

elif page == "Spiele":
    st.title("Impro-Spiele")

    games = get_games("spiele.txt")
    for game in games:
        if ":" in game:
            title, description = game.split(":", 1)
            st.markdown(f'<p class="game-title">{title.strip()}</p>', unsafe_allow_html=True)
            st.markdown(f'<p class="game-description">{description.strip()}</p>', unsafe_allow_html=True)
        else:
            st.write(game)
        st.markdown("---")

# Footer auf jeder Seite
st.markdown("<br><br><hr><p style='text-align: center;'>Made with 💙 by IMPROfessionell</p>", unsafe_allow_html=True)

if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "run":
        import streamlit.web.cli as stcli

        sys.argv = ["streamlit", "run", sys.argv[0]]
        sys.exit(stcli.main())
