import streamlit as st
from graph import graph

st.set_page_config(
    page_title="AI Deep Research",
    page_icon="🤖",
    layout="wide"
)

if "messages" not in st.session_state:
    st.session_state.messages = []

st.markdown("""
<style>

#MainMenu{visibility:hidden;}
footer{visibility:hidden;}
header{visibility:hidden;}

.block-container{
    padding-top:2rem;
}

.title{
    text-align:center;
    font-size:52px;
    font-weight:700;
}

.subtitle{
    text-align:center;
    color:gray;
    margin-bottom:30px;
}

.chat{
    border-radius:18px;
    padding:18px;
}

</style>
""", unsafe_allow_html=True)

st.markdown(
"<div class='title'>🤖 AI Deep Research</div>",
unsafe_allow_html=True
)

st.markdown(
"<div class='subtitle'>Research the Web • GitHub • Wikipedia • ArXiv</div>",
unsafe_allow_html=True
)

st.divider()

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):

        st.markdown(msg["content"])

question = st.chat_input(
    "Ask anything..."
)
if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):

        st.markdown(question)

    with st.chat_message("assistant"):

        status = st.status(
            "🧠 Thinking...",
            expanded=True
        )

        status.write("🧠 Planning research...")

        state = {

            "question": question,

            "tools": [],

            "tavily_results": [],

            "wikipedia_results": [],

            "arxiv_results": [],

            "github_results": [],

            "combined_results": "",

            "summary": ""

        }

        status.write("🌐 Searching latest web...")

        status.write("📚 Searching Wikipedia...")

        status.write("📄 Searching research papers...")

        status.write("💻 Searching GitHub...")

        status.write("🧠 Analyzing everything...")

        result = graph.invoke(state)

        status.update(
            label="✅ Research Complete",
            state="complete"
        )
        st.markdown(result["summary"])

        with st.expander("🌐 Web Sources"):

            if result["tavily_results"]:

                for item in result["tavily_results"]:

                    st.markdown(f"- {item}")

            else:

                st.info("No web results found.")

        with st.expander("📚 Wikipedia"):

            if result["wikipedia_results"]:

                st.write(result["wikipedia_results"][0])

            else:

                st.info("No Wikipedia information found.")

        with st.expander("📄 Research Papers"):

            if result["arxiv_results"]:

                for paper in result["arxiv_results"]:

                    st.markdown(paper)

                    st.divider()

            else:

                st.info("No research papers found.")

        with st.expander("💻 GitHub Repositories"):

            if result["github_results"]:

                for repo in result["github_results"]:

                    st.markdown(
                        f"""
### {repo.get("name")}

⭐ **Stars:** {repo.get("stars")}

💻 **Language:** {repo.get("language")}

{repo.get("description")}

🔗 {repo.get("url")}

---
"""
                    )

            else:

                st.info("No GitHub repositories found.")
                st.session_state.messages.append(
            {
                "role": "assistant",
                "content": result["summary"]
            }
        )