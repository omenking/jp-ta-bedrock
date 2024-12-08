import streamlit as st

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ("Sentence Constructor Practice", "Katakana Practice", "Particle Practice"))

# Sentence Constructor Practice Page
if page == "Sentence Constructor Practice":
    st.title("Sentence Constructor Practice")
    st.write("Chat interface for the user to converse with the agent.")
    # Add chat interface logic here

# Katakana Practice Page
elif page == "Katakana Practice":
    st.title("Katakana Practice")
    
    # Difficulty toggle
    difficulty = st.selectbox("Select Difficulty", ["Easy", "Medium", "Hard"])
    
    # Katakana character toggles
    katakana_chars = ["ア", "イ", "ウ", "エ", "オ", "カ", "キ", "ク", "ケ", "コ"]
    selected_chars = st.multiselect("Select Katakana Characters", katakana_chars)
    
    # Placeholder for displaying katakana cards
    if st.button("Generate Words"):
        st.write(f"Generated words with difficulty: {difficulty} and characters: {selected_chars}")
        # Logic to display katakana cards
    
    # Placeholder for card display
    for i in range(20):
        st.write(f"Card {i+1}")
        if st.button(f"Reveal {i+1}"):
            st.write(f"Romaji and English meaning for card {i+1}")

# Particle Practice Page
elif page == "Particle Practice":
    st.title("Particle Practice")
    
    # Difficulty toggle
    difficulty = st.selectbox("Select Difficulty", ["Easy", "Medium", "Hard"])
    
    # Placeholder for displaying the sentence with missing particles
    sentence = "これは___です。"
    st.write(sentence)
    
    # Word bank for particles
    particles = ["が", "を", "に", "で", "から"]
    selected_particle = st.selectbox("Choose the correct particle", particles)
    
    if st.button("Check Answer"):
        correct_particle = "が"  # Example correct particle
        if selected_particle == correct_particle:
            st.write("Correct! Explanation here.")
        else:
            st.write(f"Wrong! The correct particle is {correct_particle}. Explanation here.")
    
    if st.button("Generate New Sentence"):
        st.write("New sentence generated here.")
        # Logic to generate a new sentence