import streamlit as st

st.set_page_config(
    page_title="Portafolio 2",
    page_icon="✨",
    layout="wide"
)

portfolio_html = """
<!DOCTYPE html>
<html lang="es">

<head>

<meta charset="UTF-8">

<style>

*{
    margin:0;
    padding:0;
    box-sizing:border-box;
    font-family:Arial, sans-serif;
}

body{
    background: linear-gradient(135deg,#f8e8ff,#e0c3fc,#c2e9fb);
    padding:40px;
    color:#2d1b4e;
}

h1{
    text-align:center;
    font-size:55px;
    margin-bottom:10px;
}

.subtitle{
    text-align:center;
    font-size:20px;
    margin-bottom:40px;
}

.container{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(320px,1fr));
    gap:25px;
}

.card{
    background:rgba(255,255,255,0.75);
    border-radius:25px;
    padding:25px;
    box-shadow:0 8px 20px rgba(0,0,0,0.1);
    transition:0.3s;
}

.card:hover{
    transform:translateY(-5px);
}

.card h2{
    color:#6a00f4;
    margin-bottom:15px;
}

.card p{
    margin-bottom:20px;
    line-height:1.5;
}

.links{
    display:flex;
    flex-direction:column;
    gap:12px;
}

.links a{
    text-decoration:none;
    background:#9d4edd;
    color:white;
    padding:12px;
    border-radius:12px;
    text-align:center;
    font-weight:bold;
    transition:0.3s;
}

.links a:hover{
    background:#7b2cbf;
}

footer{
    text-align:center;
    margin-top:50px;
    font-size:16px;
}

</style>

</head>

<body>

<h1>✨ Portafolio 2 ✨</h1>

<p class="subtitle">
Si corre en Streamlit, no se toca.
</p>

<div class="container">

<!-- CLASE 11 -->
<div class="card">

<h2>📚 Clase 11</h2>

<div class="links">

<a href="https://chatpdf-oamzr4rofj3woilddhzbve.streamlit.app/" target="_blank">>
🚀 Chat PDF
</a>

<a href="https://visionapp-eof9e2wdacnswg8tyid97p.streamlit.app/" target="_blank">
🔊 Análisis de imagen
</a>

</div>
</div>

<!-- CLASE 12 -->
<div class="card">

<h2>🌎 Clase 12</h2>

<div class="links">

<a href="https://htrdsk7cxdc4ybc2qiuync.streamlit.app/" target="_blank">
🌐 DigitVision AI
</a>

<a href="https://drawrecog-2gpbw2nf5mwfz34yrsptzs.streamlit.app/" target="_blank">
🎧 NeuroPanel
</a>

<a href="https://touchcanvas-iwgrzowz57w7zg46ddu37a.streamlit.app/" target="_blank">
📸 Draaw
</a>

</div>
</div>

<!-- CLASE 13 -->
<div class="card">

<h2>🧠 Clase 13</h2>

<div class="links">

<a href="https://receptor-kkhar3gggzqmb6gyd3jsd7.streamlit.app/https://receptor-kk
har3gggzqmb6gyd3jsd7.streamlit.app/" target="_blank">
☁️ SensorHub MQTT
</a>

<a href="https://controladormqtt-exrpxaet2ywivh7xz99tdh.streamlit.app/" target="_blank">
📊 GreenControl MQTT
</a>

<a href="https://vozmqtt-vjpxjbm5z4t9isdofedhbv.streamlit.app/" target="_blank">
💜 VoiceControl AI
</a>

</div>
</div>

</div>

<footer>
✨ Desarrollado por Ale • Interfaces Multimodales ✨
</footer>

</body>
</html>
"""

st.components.v1.html(
    portfolio_html,
    height=560,
    scrolling=True
)
