# -*- coding: utf-8 -*-
import streamlit as st

# --- Page Configuration ---
st.set_page_config(
    page_title="PaperCast",
    page_icon="🎙️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- Custom CSS for Dark Theme Styling ---
st.markdown("""
<style>
    /* Base theme adjustments */
    body {
        color: #fafafa; /* Ensure base text color is light */
    }
    .stApp {
        background-color: #0e1117; /* Dark background */
        color: #fafafa; /* Light text */
    }
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: #1f2229; /* Slightly lighter dark for sidebar */
        padding-top: 2rem;
    }
    [data-testid="stSidebar"] .stButton>button {
        color: #fafafa;
        border-radius: 0.5rem;
        width: 100%;
        text-align: left;
        padding: 0.75rem 1rem;
        margin-bottom: 0.5rem;
        transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out;
        background-color: transparent; /* Make default transparent */
        border: none; /* Remove default border */
    }
    [data-testid="stSidebar"] .stButton>button:hover {
        background-color: #313642;
        color: #fafafa;
    }
    [data-testid="stSidebar"] .stButton>button:focus {
        background-color: #454c5a;
        color: #fafafa;
        box-shadow: none;
    }

    /* Main content styling */
    h1, h2, h3, h4, h5, h6 {
        color: #fafafa;
    }
    .stTextInput > div > div > input {
        background-color: #1f2229;
        color: #fafafa;
        border-radius: 0.5rem;
        border: 1px solid #313642;
    }
    .stTextInput > div > div > input:focus {
        border: 1px solid #1f77b4;
        box-shadow: none;
    }
    .stButton > button {
        border-radius: 0.5rem;
        padding: 0.5rem 1rem;
    }
    /* Podcast Card Styling */
    .podcast-card {
        background-color: #1f2229;
        border-radius: 0.75rem;
        padding: 1rem;
        margin-bottom: 1rem;
        transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
        border: 1px solid #313642;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        overflow: hidden;
    }
    .podcast-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
    }
    /* --- Image Sizing Fix --- */
    .podcast-card .stImage img { /* Target the img element within stImage */
        border-radius: 0.5rem;
        margin-bottom: 0.75rem;
        object-fit: cover;    /* Crop to cover */
        height: 180px;        /* Fixed height */
        width: 100%;         /* Fill width */
        display: block;      /* Prevents potential inline spacing issues */
    }
    /* --- End Image Sizing Fix --- */

    .podcast-card .title {
        font-weight: 600;
        font-size: 1.1em;
        margin-bottom: 0.25rem;
        color: #fafafa;
        flex-grow: 1;
        line-height: 1.3;
    }
    .podcast-card .details {
        font-size: 0.9em;
        color: #a0a0a0;
        margin-bottom: 0.75rem;
    }
    .podcast-card .stButton {
         margin-top: auto;
    }
    .podcast-card .stButton button {
        background-color: #1f77b4;
        color: white;
        border: none;
        width: 100%;
        padding: 0.6rem 1rem;
    }
     .podcast-card .stButton button:hover {
        background-color: #175a8c;
    }

    /* Audio Player Styling */
    /* Add specific styling for the container holding the player */
    .audio-player-container {
        background-color: #1f2229; /* Match card background */
        padding: 1rem 1.5rem;
        border-radius: 0.75rem;
        border: 1px solid #313642;
        margin-top: 1rem; /* Space above the player */
    }
    .audio-player-container .stAudio > audio {
        width: 100%; /* Make audio player take full width */
        /* Basic dark theme attempt for controls (browser dependent) */
        filter: invert(1) hue-rotate(180deg);
    }
    .audio-player-container .stButton button { /* Style close button */
        background-color: #454c5a;
        color: #fafafa;
        margin-top: 0.5rem;
    }
     .audio-player-container .stButton button:hover {
         background-color: #5a6373;
     }


    /* Divider */
    hr {
        border-top: 1px solid #313642;
        margin: 1.5rem 0;
    }

</style>
""", unsafe_allow_html=True)

# --- Data ---
podcasts = [
    {
        "id": "transformer_networks",
        "title": "Transformer Networks: Attention Without Recurrence",
        "author": "Dr. Emily Chen",
        "duration": "24:00",
        "image_url": "https://heidloff.net/assets/img/2023/02/transformers.png", 
        "audio_url": "https://spitzpebcxgarkskdqgv.supabase.co/storage/v1/object/public/pepercastbucket/covers/Transformer%20Networks_%20Attention%20Without%20Recurrence.wav",
        "tags": ["featured", "ai", "nlp", "deep learning"]
    },
    {
        "id": "brain_tumor_radiology",
        "title": "Radiological Perspective in Brain Tumor Treatment",
        "author": "Prof. James Wilson",
        "duration": "32:00",
        "image_url": "https://www.massgeneralbrigham.org/content/mgb-global/global/en/about/newsroom/articles/confronting-brain-cancer/_jcr_content/root/container_1214295969/image.coreimg.jpeg/1732049471207/brain-tumor-examination-2200x1200.jpeg", 
        "audio_url": "https://spitzpebcxgarkskdqgv.supabase.co/storage/v1/object/public/pepercastbucket/covers/Radiological%20Perspective%20in%20Brain%20Tumor%20Treatment.wav",
        "tags": ["featured", "medical", "radiology", "oncology"]
    },
    {
        "id": "quantum_computing_advances",
        "title": "Quantum Computing Advances",
        "author": "Dr. Alex Mercer",
        "duration": "19:00",
        "image_url": "https://images.newscientist.com/wp-content/uploads/2025/04/15184836/SEI_247621663.jpg", 
        "audio_url": None,
         "tags": ["featured", "most_listened", "physics", "computing", "quantum"]
    },
    {
        "id": "frontend_frameworks",
        "title": "Modern Frontend Frameworks",
        "author": "Sarah Lee",
        "duration": "28:00",
        "image_url": "https://images.unsplash.com/photo-1542831371-29b0f74f9713?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8Y29kaW5nfGVufDB8fHx8MTYxNjc2MzkxMA&ixlib=rb-1.2.1&q=80&w=1080", # Coding screen image
        "audio_url": None,
        "tags": ["most_listened", "web development", "coding", "software"]
    },
    {
        "id": "climate_change_models",
        "title": "Climate Change: Data & Models",
        "author": "Dr. Kenji Tanaka",
        "duration": "35:00",
        "image_url": "https://images.unsplash.com/photo-1447752875215-b2761acb3c5d?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8bmF0dXJlfGVufDB8fHx8MTYxNjc2Mzk1MA&ixlib=rb-1.2.1&q=80&w=1080", # Nature image
        "audio_url": None,
        "tags": ["most_listened", "data science", "environment", "climate"]
    },
]

# --- Session State Initialization ---
if 'selected_podcast' not in st.session_state:
    st.session_state.selected_podcast = None
if 'page' not in st.session_state:
    st.session_state.page = "Discover"

# --- Helper function to display podcast cards ---
def display_podcast_card(podcast, section_prefix):
    # Use a container *per card* for better isolation and layout control
    with st.container():
        # Apply the card class to the container itself for styling
        st.markdown(f'<div class="podcast-card" data-testid="podcast-card-{section_prefix}-{podcast["id"]}">', unsafe_allow_html=True)

        # Image Display (inside the card div)
        try:
            # The CSS now targets img within stImage, use_container_width fills column
            st.image(podcast["image_url"], use_container_width=True)
        except Exception as e:
            # Simple text placeholder if image fails
             st.markdown(f'<div style="height: 180px; width: 100%; background-color: #333; display: flex; align-items: center; justify-content: center; border-radius: 0.5rem; margin-bottom: 0.75rem;"><span style="color: #888;">Image Error</span></div>', unsafe_allow_html=True)
            # st.warning(f"Img Error: {e}") # Optional: show warning

        # Title and Details (inside the card div)
        st.markdown(f'<p class="title">{podcast["title"]}</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="details">{podcast["author"]} • {podcast["duration"]}</p>', unsafe_allow_html=True)

        # Play Button (inside the card div, CSS pushes it down)
        button_key = f"play_{section_prefix}_{podcast['id']}"
        if st.button("Play Now", key=button_key):
            if podcast["audio_url"]:
                # --- Audio Debug ---
                # st.write(f"DEBUG: Button {button_key} clicked. Setting state to:")
                # st.write(podcast)
                # --- End Debug ---
                st.session_state.selected_podcast = podcast
                st.rerun() # Essential to trigger re-render with updated state
            else:
                st.toast("Audio not available for this podcast yet.", icon="🎧")

        # Close the card div (essential for CSS containment)
        st.markdown('</div>', unsafe_allow_html=True)


# --- Sidebar Navigation ---
with st.sidebar:
    st.markdown("# 🎙️ PaperCast")
    st.markdown("---")
    nav_buttons = {
        "Home": "🏠 Home",
        "Discover": "🧭 Discover",
        "Trending": "📈 Trending",
        "Saved": "💾 Saved",
        "Settings": "⚙️ Settings",
        "Profile": "👤 Profile"
    }
    for page_id, page_title in nav_buttons.items():
        if st.button(page_title, key=f"nav_{page_id}", use_container_width=True):
            st.session_state.page = page_id
            # Clear player *only if* navigating away from a page where it might be open
            if st.session_state.selected_podcast:
                 st.session_state.selected_podcast = None
                 st.rerun() # Rerun needed if we cleared the player state
            else:
                 # No need to rerun if player wasn't open, button click handles it
                 pass


# --- Main Content Area ---

# --- Audio Player Placeholder ---
# Define this container *once* near the top of the main area
player_placeholder = st.empty() # Use st.empty to reserve a spot

# --- Page Rendering Logic --- (Keep dummy content from previous step)

if st.session_state.page == "Home":
    st.header("Welcome to PaperCast! 👋")
    st.markdown("Your gateway to understanding research papers through engaging podcasts. Explore featured content below or use the Discover tab.")
    st.markdown("---")

    st.subheader("Featured Research")
    featured_podcasts = [p for p in podcasts if "featured" in p["tags"]]
    cols_featured = st.columns(3)
    for i, podcast in enumerate(featured_podcasts):
        with cols_featured[i % len(cols_featured)]:
            display_podcast_card(podcast, "home_featured")
    st.markdown("<br>", unsafe_allow_html=True)

elif st.session_state.page == "Discover":
    st.header("Discover Research Podcasts")
    search_query = st.text_input("Search research papers, authors, or topics...", key="search_bar", placeholder="E.g., 'quantum physics', 'Dr. Chen'")
    st.markdown("---")

    if search_query:
        search_lower = search_query.lower()
        filtered_podcasts = [
            p for p in podcasts if
            search_lower in p['title'].lower() or
            search_lower in p['author'].lower() or
            any(search_lower in tag for tag in p['tags'])
        ]
        st.subheader(f"Search Results for '{search_query}'")
        if not filtered_podcasts:
            st.info("No podcasts found matching your search.")
        else:
            cols_search = st.columns(3)
            for i, podcast in enumerate(filtered_podcasts):
                 with cols_search[i % len(cols_search)]:
                     display_podcast_card(podcast, f"search_{i}")
            st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("---")

    else:
        st.subheader("Featured Research")
        featured_podcasts = [p for p in podcasts if "featured" in p["tags"]]
        cols_featured = st.columns(3)
        for i, podcast in enumerate(featured_podcasts):
            with cols_featured[i % len(cols_featured)]:
                display_podcast_card(podcast, "discover_featured")
        st.markdown("<br>", unsafe_allow_html=True)

        st.subheader("Most Listened")
        most_listened_podcasts = [p for p in podcasts if "most_listened" in p["tags"]]
        cols_watched = st.columns(3)
        for i, podcast in enumerate(most_listened_podcasts):
            with cols_watched[i % len(cols_watched)]:
                 display_podcast_card(podcast, "discover_listened")
        st.markdown("<br>", unsafe_allow_html=True)

        st.subheader("Focus on AI & NLP")
        ai_podcasts = [p for p in podcasts if "ai" in p["tags"] or "nlp" in p["tags"]]
        cols_ai = st.columns(3)
        for i, podcast in enumerate(ai_podcasts):
            with cols_ai[i % len(cols_ai)]:
                 display_podcast_card(podcast, "discover_ai")
        st.markdown("<br>", unsafe_allow_html=True)


elif st.session_state.page == "Trending":
    st.header("📈 Trending Podcasts")
    st.write("Discover what's popular in the academic community right now.")
    trending_podcasts = sorted(podcasts, key=lambda x: x.get("duration"), reverse=True)[:5]
    cols_trending = st.columns(3)
    for i, podcast in enumerate(trending_podcasts):
         with cols_trending[i % len(cols_trending)]:
            display_podcast_card(podcast, "trending")
    st.markdown("<br>", unsafe_allow_html=True)


elif st.session_state.page == "Saved":
    st.header("💾 Saved Podcasts")
    st.write("Your personal library of podcasts saved for later listening.")
    saved_items_ids = ["transformer_networks", "climate_change_models"]
    saved_podcasts = [p for p in podcasts if p["id"] in saved_items_ids]

    if not saved_podcasts:
        st.info("You haven't saved any podcasts yet. Browse 'Discover' and click 'Save'!")
    else:
        cols_saved = st.columns(3)
        for i, podcast in enumerate(saved_podcasts):
             with cols_saved[i % len(cols_saved)]:
                display_podcast_card(podcast, "saved")
        st.markdown("<br>", unsafe_allow_html=True)


elif st.session_state.page == "Settings":
    st.header("⚙️ Settings")
    st.write("Customize your PaperCast experience.")
    st.markdown("---")
    st.subheader("Playback")
    st.selectbox("Audio Quality", ["Standard (128kbps)", "High (256kbps)", "Lossless (if available)"], index=0)
    st.slider("Playback Speed", 0.5, 2.0, 1.0, 0.25, format="%.2fx")
    st.toggle("Auto-play next podcast", value=True)
    st.markdown("---")
    st.subheader("Downloads")
    st.toggle("Download over Wi-Fi only", value=True)
    st.selectbox("Download Quality", ["Standard", "High"])
    st.button("Clear Download Cache")
    st.markdown("---")
    st.subheader("Account")
    st.write("Manage your subscription and notification preferences (Dummy).")
    st.button("Manage Subscription")


elif st.session_state.page == "Profile":
    st.header("👤 Profile")
    st.markdown("---")
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("https://media.istockphoto.com/id/1424540260/photo/user-green-check-mark-sign-on-white-background-3d-render-concept-for.jpg?s=2048x2048&w=is&k=20&c=8bI_L4CyGPMAvmY1D5kM-hJmMi7HYRWHasB9Y-279QA=", width=120)
    with col2:
        st.subheader("Kunal Goel")
        st.caption("Research Enthusiast | BTech Candidate")
        st.write("📧 26aiyatal@rkgit.edu.in")
        st.write("📍Ghaziabad ,UP")

    st.markdown("---")
    st.subheader("Activity")
    listened_count = len([p for p in podcasts if p['audio_url']])
    saved_count = 2
    col_m1, col_m2 = st.columns(2)
    with col_m1:
        st.metric("Podcasts Listened", f"{listened_count}", "+2 this week")
    with col_m2:
        st.metric("Saved Podcasts", f"{saved_count}")

    st.markdown("---")
    st.button("Edit Profile")
    st.button("Change Password")
    st.button("Logout", type="secondary")


# --- Display Audio Player ---
# This logic runs *after* the page content for the current state is determined.
# It checks the session state and updates the player_placeholder accordingly.
if st.session_state.selected_podcast and st.session_state.selected_podcast["audio_url"]:
    selected = st.session_state.selected_podcast
    # --- Audio Debug ---
    # st.sidebar.write("DEBUG: Rendering Player for:")
    # st.sidebar.write(selected)
    # --- End Debug ---
    with player_placeholder.container(): # Use the placeholder's container method
         # Apply custom class for styling the player container
        st.markdown('<div class="audio-player-container">', unsafe_allow_html=True)
        st.subheader(f"Now Playing: {selected['title']}")
        st.caption(f"{selected['author']} • {selected['duration']}")
        try:
            # Use the direct URL and specify format
            st.audio(selected["audio_url"], format="audio/wav", start_time=0)
            # --- Audio Debug ---
            # st.write(f"DEBUG: Audio URL passed to st.audio: {selected['audio_url']}")
            # --- End Debug ---
        except Exception as e:
            st.error(f"Error loading audio: {e}")
            # --- Audio Debug ---
            # st.write(f"DEBUG: Exception during st.audio rendering for URL: {selected['audio_url']}")
            # --- End Debug ---

        if st.button("Close Player", key="close_player", use_container_width=True):
            st.session_state.selected_podcast = None
            # --- Audio Debug ---
            # st.write("DEBUG: Close button clicked. Clearing state.")
            # --- End Debug ---
            st.rerun() # Rerun to clear the player via the placeholder
        st.markdown('</div>', unsafe_allow_html=True) # Close the player container div

else:
    # If nothing is selected, ensure the placeholder is actually empty
    player_placeholder.empty()
  
