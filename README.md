# Capital One Hackathon

## 🌾 𝑲𝒓𝒊𝒔𝒉𝒊𝑨𝒅𝒗𝒊𝒔𝒐𝒓 – 𝑨𝑰-𝑷𝒐𝒘𝒆𝒓𝒆𝒅 𝑨𝒈𝒓𝒊𝒄𝒖𝒍𝒕𝒖𝒓𝒂𝒍 𝑨𝒔𝒔𝒊𝒔𝒕𝒂𝒏𝒕

KrishiAdvisor is an AI-driven platform designed to empower farmers with real-time agricultural insights, disease detection, and data visualization.

This project was built during a Hackathon by a team of two developers.

### 𝐅𝐞𝐚𝐭𝐮𝐫𝐞𝐬

✔️ 𝑲𝒓𝒊𝒔𝒉𝒊 𝑨𝒔𝒔𝒊𝒔𝒕𝒂𝒏𝒕 𝑩𝒐𝒕 – Multilingual chatbot for farming, crop recommendation & scheme queries

✔️ 𝑷𝒐𝒕𝒂𝒕𝒐 𝑳𝒆𝒂𝒇 𝑫𝒊𝒔𝒆𝒂𝒔𝒆 𝑫𝒆𝒕𝒆𝒄𝒕𝒊𝒐𝒏 – Deep learning model for early-stage detection

✔️ 𝑻𝒂𝒃𝒍𝒆𝒂𝒖 𝑽𝒊𝒔𝒖𝒂𝒍𝒊𝒛𝒂𝒕𝒊𝒐𝒏 – Dashboards for market prices, rainfall, & crop data

✔️ 𝑫𝒐𝒄𝒌𝒆𝒓𝒊𝒛𝒆𝒅 𝑫𝒆𝒑𝒍𝒐𝒚𝒎𝒆𝒏𝒕 – Easy to run anywhere

### 𝐋𝐢𝐯𝐞 𝐃𝐞𝐦𝐨

## 👉 http://34.9.156.220:5000

# 🛠️ 𝐈𝐧𝐬𝐭𝐚𝐥𝐥𝐚𝐭𝐢𝐨𝐧 & 𝐒𝐞𝐭𝐮𝐩
### ➊ 𝑪𝒍𝒐𝒏𝒆 𝒕𝒉𝒆 𝑹𝒆𝒑𝒐
```
git clone https://github.com/fahamkhan00/KrishiAdvisor.git
cd KrishiAdvisor
```

Or extract the ZIP file attached.

### ➋ 𝑹𝒖𝒏 𝒕𝒉𝒆 𝑩𝒂𝒄𝒌𝒆𝒏𝒅 (𝑲𝒓𝒊𝒔𝒉𝒊 𝑨𝒔𝒔𝒊𝒔𝒕𝒂𝒏𝒕 𝑩𝒐𝒕)
```
cd KrishiAssistant/
docker build -t krishi-advisor .
docker run -d -p 8501:8501 krishi-advisor
```

### ➌ 𝑹𝒖𝒏 𝒕𝒉𝒆 𝑭𝒓𝒐𝒏𝒕𝒆𝒏𝒅 (𝑼𝑰)
```
cd ..
cd krishiUi/
docker build -t my-frontend .
docker run -d -p 5000:5000 --name frontend-container my-frontend
```


### 👉 Visit: http://localhost:5000

### And Click on the "Chat with Us" Button For the Advisor Chatbot

### Or Just Visit http://localhost:8501

---
## 𝐓𝐚𝐛𝐥𝐞𝐚𝐮 𝐃𝐚𝐬𝐡𝐛𝐨𝐚𝐫𝐝𝐬

📈 Market Prices

🌧️ Rainfall Trends

🌱 Crop & Yield Statistics

---
## 𝐓𝐞𝐜𝐡 𝐒𝐭𝐚𝐜𝐤

Backend: Python, Streamlit, TensorFlow/PyTorch

Frontend: React / Streamlit UI (Dockerized)

Visualization: Tableau

Deployment: Docker, Cloud VM

---
## 𝐓𝐞𝐚𝐦

### Developed by:

### [Nigar Khan](https://github.com/nigarkhan152)

### [Faham Khan](https://github.com/fahamkhan00)

## 𝐋𝐢𝐜𝐞𝐧𝐬𝐞
Open-source and free for educational purposes.

---
✨ “Empowering Farmers with AI & Data” ✨
