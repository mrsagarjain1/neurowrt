import streamlit as st
from router_agent import chain, run_on_router

# --- Page Config ---
st.set_page_config(
    page_title="AI Network Assistant",
    page_icon="📡",
    layout="centered"
)

# --- Header ---
st.markdown("<h1 style='text-align:center; color:#4CAF50;'>📡 AI Network Assistant for OpenWrt</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:gray;'>Ask your router anything and get real-time answers!</p>", unsafe_allow_html=True)

# --- User Input ---
with st.container():
    user_input = st.text_input("💬 What would you like to know about your router?", placeholder="e.g., Show me connected devices")

# --- Process Input ---
if user_input:
    with st.spinner("🤖 Thinking... Contacting your router..."):
        cmd = chain.invoke(input={"user_input": user_input})
        cmd = cmd.content
        result = run_on_router(cmd)

    # --- Results Display ---
    st.success("✅ Command Executed Successfully!")
    st.markdown("### 🔧 Command Sent to Router:")
    st.code(cmd.strip(), language="bash")

    st.markdown("### 📜 Router Response:")
    st.text_area("Output", result.strip(), height=200)

# --- Footer with Social Links ---
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(
    """
    <div style="text-align:center; margin-top:20px;">
        <a href="https://x.com/mrsagarjain" target="_blank" style="margin:0 10px; text-decoration:none;">
            <img src="https://cdn-icons-png.flaticon.com/512/733/733579.png" width="28" style="vertical-align:middle;"> 
            <span style="color:#1DA1F2; font-weight:bold;">Twitter</span>
        </a>
        &nbsp;&nbsp;
        <a href="https://www.linkedin.com/in/mrsagarjain1/" target="_blank" style="margin:0 10px; text-decoration:none;">
            <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="28" style="vertical-align:middle;"> 
            <span style="color:#0077B5; font-weight:bold;">LinkedIn</span>
        </a>
        &nbsp;&nbsp;
        <a href="https://github.com/mrsagarjain1/neurowrt" target="_blank" style="margin:0 10px; text-decoration:none;">
            <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" width="28" style="vertical-align:middle;"> 
            <span style="color:#333; font-weight:bold;">GitHub</span>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)
