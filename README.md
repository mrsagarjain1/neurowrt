# 📡 LangChain Network Assistant for OpenWrt

Conversational AI for your OpenWrt router, powered by LangChain.

This project brings the power of large language models to OpenWrt-based routers, enabling users to interact with their network through natural language. Ask questions, get status updates, or configure settings—all through a simple chat interface.

---

## ✨ Features

- 🔍 **Real-time queries** – Ask about connected devices, uptime, traffic, and more.
- ⚙️ **AI-assisted configuration** – Let the assistant help modify firewall rules, DHCP settings, or wireless config.
- 📊 **Bandwidth and traffic monitoring** – Natural language summaries of network usage.
- 🔐 **Security insights** – Identify suspicious traffic or open ports.
- 🧠 **LangChain-powered logic** – Combines LLM reasoning with OpenWrt APIs and CLI tools.

---

## 🧰 Built With

- **OpenWrt** – The router OS
- **LangChain** – LLM orchestration and tool integration
- **Python**

---

## 💬 Example Commands

Try asking:

- “How many devices are connected right now?”
- “Block all traffic from 192.168.1.50”
- “Restart the Wi-Fi interface”
- “Show me bandwidth usage by IP”
- “Is my router running out of memory?”

---

## 📋 How To Install The Application

- pip install requirements.txt
- Put your router's IP. username and password in router_agent.py
- Create a .env file in the directory and put your openai api key like this OPENAI_API_KEY=your_api_key
- Open the terminal in the same directory and the this command ```streamlit run neurowrt_gui.py```
#### Note your router should be accessible from the host machine.

## 🧪 Development

Feel free to fork, contribute, or suggest improvements.
