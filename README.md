<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Tahir Sayyaf Portfolio</title>
  <style>
    body {
      margin: 0;
      font-family: 'Roboto', Arial, sans-serif;
      background: linear-gradient(to bottom, #0f2027, #203a43, #2c5364);
      color: white;
      overflow-x: hidden;
      perspective: 2000px;
    }
    header {
      position: relative;
      height: 800px;
      text-align: center;
      background: linear-gradient(135deg, #00d4ff 0%, #ffcc00 100%);
      overflow: hidden;
      transform-style: preserve-3d;
      animation: holoFlicker 5s infinite ease-in-out;
    }
    @keyframes holoFlicker {
      0%, 100% { opacity: 1; filter: brightness(1); }
      50% { opacity: 0.95; filter: brightness(1.2); }
    }
    #hero-canvas {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      z-index: 0;
    }
    .header-content {
      position: relative;
      z-index: 1;
      padding: 120px 20px;
      transform: translateZ(150px);
    }
    .logo {
      width: 200px;
      height: auto;
      margin-bottom: 30px;
      animation: spinIn 1.5s ease-out, float 2.5s ease-in-out infinite;
      filter: drop-shadow(0 0 30px rgba(0, 212, 255, 1));
    }
    @keyframes spinIn {
      0% { transform: rotateY(360deg) scale(0); opacity: 0; }
      100% { transform: rotateY(0deg) scale(1); opacity: 1; }
    }
    @keyframes float {
      0%, 100% { transform: translateY(0) translateZ(150px); }
      50% { transform: translateY(-30px) translateZ(150px); }
    }
    .welcome {
      font-size: 5em;
      font-weight: 700;
      animation: fadeIn 3s ease-in-out, holoGlow 1.5s ease-in-out infinite alternate;
      margin: 0;
      transform: translateZ(100px);
      text-shadow: 0 0 20px rgba(0, 212, 255, 0.9);
    }
    .welcome-sub {
      font-size: 2.2em;
      font-weight: 300;
      color: #ddd;
      margin-top: 20px;
      animation: fadeIn 4s ease-in-out;
      transform: translateZ(80px);
    }
    @keyframes fadeIn {
      0% { opacity: 0; transform: translateY(-30px) translateZ(0); }
      100% { opacity: 1; transform: translateY(0) translateZ(0); }
    }
    @keyframes holoGlow {
      0% { text-shadow: 0 0 10px #00d4ff, 0 0 20px #ffcc00; }
      100% { text-shadow: 0 0 30px #00d4ff, 0 0 50px #ffcc00; }
    }
    nav {
      background-color: #222;
      display: flex;
      justify-content: center;
      padding: 15px 0;
      position: sticky;
      top: 0;
      z-index: 100;
      box-shadow: 0 2px 5px rgba(0, 0, 0, 0.3);
      transform: translateZ(100px);
    }
    nav a {
      color: white;
      text-decoration: none;
      margin: 0 25px;
      font-size: 1.3em;
      font-weight: 500;
      transition: color 0.3s ease, transform 0.3s ease;
      transform: translateZ(30px);
      position: relative;
    }
    nav a::after {
      content: '';
      position: absolute;
      width: 0;
      height: 2px;
      bottom: -5px;
      left: 0;
      background: linear-gradient(90deg, #00d4ff, #ffcc00);
      transition: width 0.3s ease;
    }
    nav a:hover::after {
      width: 100%;
    }
    nav a:hover {
      color: #00d4ff;
      transform: translateZ(80px) scale(1.2);
    }
    section {
      padding: 100px 20px;
      max-width: 1200px;
      margin: auto;
      transform-style: preserve-3d;
    }
    .stickers {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 30px;
      margin-top: 30px;
      perspective: 2000px;
    }
    .sticker {
      background: linear-gradient(45deg, #333, #444);
      padding: 30px;
      border-radius: 15px;
      font-size: 1.3em;
      text-align: center;
      transition: transform 0.3s ease, box-shadow 0.3s ease;
      position: relative;
      overflow: hidden;
      cursor: pointer;
      transform-style: preserve-3d;
      transform: translateZ(80px);
      border: 2px solid transparent;
      background-clip: padding-box;
    }
    .sticker::before {
      content: '';
      position: absolute;
      top: 0;
      left: -100%;
      width: 100%;
      height: 100%;
      background: linear-gradient(90deg, transparent, rgba(0, 212, 255, 0.6), transparent);
      transition: left 0.5s ease;
      z-index: 0;
    }
    .sticker::after {
      content: '';
      position: absolute;
      top: -2px;
      left: -2px;
      right: -2px;
      bottom: -2px;
      background: linear-gradient(45deg, #00d4ff, #ffcc00);
      z-index: -1;
      animation: holoFlicker 3s infinite;
    }
    .sticker:hover::before {
      left: 100%;
    }
    .sticker:hover {
      box-shadow: 0 5px 30px rgba(0, 212, 255, 0.9);
      transform: translateZ(200px) rotateY(10deg);
    }
    .sticker > * {
      position: relative;
      z-index: 1;
    }
    .sticker-logo {
      position: absolute;
      top: 10px;
      right: 10px;
      width: 35px;
      height: 35px;
      animation: rotateLogo 8s linear infinite, holoFlicker 2s infinite;
      transform: translateZ(50px);
    }
    @keyframes rotateLogo {
      0% { transform: rotate(0deg) translateZ(50px); }
      100% { transform: rotate(360deg) translateZ(50px); }
    }
    .contact-form {
      max-width: 600px;
      margin: auto;
      background: linear-gradient(45deg, #333, #444);
      padding: 30px;
      border-radius: 15px;
      perspective: 2000px;
      position: relative;
      overflow: hidden;
      transform: translateZ(80px);
      border: 2px solid transparent;
      background-clip: padding-box;
    }
    .contact-form::before {
      content: '';
      position: absolute;
      top: 0;
      left: -100%;
      width: 100%;
      height: 100%;
      background: linear-gradient(90deg, transparent, rgba(0, 212, 255, 0.5), transparent);
      transition: left 0.5s ease;
      z-index: 0;
    }
    .contact-form::after {
      content: '';
      position: absolute;
      top: -2px;
      left: -2px;
      right: -2px;
      bottom: -2px;
      background: linear-gradient(45deg, #00d4ff, #ffcc00);
      z-index: -1;
      animation: holoFlicker 4s infinite;
    }
    .contact-form:hover::before {
      left: 100%;
    }
    .contact-form:hover {
      transform: translateZ(200px);
      box-shadow: 0 5px 30px rgba(0, 212, 255, 0.9);
    }
    .contact-form > * {
      position: relative;
      z-index: 1;
    }
    input, textarea {
      margin: 12px 0;
      padding: 15px;
      border-radius: 8px;
      border: 1px solid #00d4ff;
      background-color: rgba(85, 85, 85, 0.8);
      color: white;
      font-size: 1em;
      transform: translateZ(30px);
      transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    input:hover, textarea:hover {
      transform: translateZ(50px);
      box-shadow: 0 0 15px rgba(0, 212, 255, 0.7);
    }
    input::placeholder, textarea::placeholder {
      color: #bbb;
    }
    button {
      padding: 15px;
      background: linear-gradient(45deg, #00d4ff, #ffcc00);
      color: #111;
      font-size: 1.1em;
      font-weight: 500;
      border: none;
      border-radius: 8px;
      cursor: pointer;
      transition: transform 0.3s ease, box-shadow 0.3s ease;
      transform: translateZ(50px);
      position: relative;
      overflow: hidden;
    }
    button::before {
      content: '';
      position: absolute;
      top: 0;
      left: -100%;
      width: 100%;
      height: 100%;
      background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.4), transparent);
      transition: left 0.5s ease;
    }
    button:hover::before {
      left: 100%;
    }
    button:hover {
      transform: translateZ(100px) translateY(-5px);
      box-shadow: 0 5px 20px rgba(0, 212, 255, 0.9);
    }
    .download-section {
      text-align: center;
      position: relative;
      transform: translateZ(80px);
    }
    .download-section h2 {
      margin-bottom: 25px;
      transform: translateZ(50px);
      text-shadow: 0 0 15px rgba(0, 212, 255, 0.8);
    }
    .download-button {
      display: inline-block;
      padding: 15px 50px;
      background: linear-gradient(45deg, #00d4ff, #ffcc00);
      color: #111;
      font-size: 1.3em;
      font-weight: bold;
      text-decoration: none;
      border-radius: 50px;
      transition: all 0.3s ease;
      position: relative;
      overflow: hidden;
      perspective: 2000px;
      transform-style: preserve-3d;
      transform: translateZ(80px);
    }
    .download-button::before {
      content: '📥 Download Now';
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      display: flex;
      align-items: center;
      justify-content: center;
      background: linear-gradient(45deg, #00d4ff, #ffcc00);
      transition: transform 0.4s ease;
      transform-origin: bottom;
    }
    .download-button::after {
      content: '📥 Get It!';
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      display: flex;
      align-items: center;
      justify-content: center;
      background: linear-gradient(45deg, #ffcc00, #00d4ff);
      transform: rotateX(-90deg);
      transition: transform 0.4s ease;
      transform-origin: top;
    }
    .download-button:hover::before {
      transform: rotateX(90deg);
    }
    .download-button:hover::after {
      transform: rotateX(0deg);
    }
    .download-button:hover {
      box-shadow: 0 5px 30px rgba(0, 212, 255, 0.9);
      transform: translateZ(200px);
    }
    .download-counter {
      margin-top: 20px;
      font-size: 1.1em;
      color: #bbb;
      transform: translateZ(30px);
    }
    .faq {
      margin-bottom: 25px;
      padding: 20px;
      background: linear-gradient(45deg, #333, #444);
      border-radius: 12px;
      cursor: pointer;
      perspective: 2000px;
      position: relative;
      overflow: hidden;
      transform: translateZ(80px);
      border: 2px solid transparent;
      background-clip: padding-box;
    }
    .faq::before {
      content: '';
      position: absolute;
      top: 0;
      left: -100%;
      width: 100%;
      height: 100%;
      background: linear-gradient(90deg, transparent, rgba(0, 212, 255, 0.5), transparent);
      transition: left 0.5s ease;
      z-index: 0;
    }
    .faq::after {
      content: '';
      position: absolute;
      top: -2px;
      left: -2px;
      right: -2px;
      bottom: -2px;
      background: linear-gradient(45deg, #00d4ff, #ffcc00);
      z-index: -1;
      animation: holoFlicker 3s infinite;
    }
    .faq:hover::before {
      left: 100%;
    }
    .faq:hover {
      transform: translateZ(200px) scale(1.05);
      box-shadow: 0 5px 30px rgba(0, 212, 255, 0.9);
    }
    .faq > * {
      position: relative;
      z-index: 1;
    }
    .faq h4 {
      margin: 10px 0 5px;
      color: #00d4ff;
      font-size: 1.3em;
      transform: translateZ(30px);
      text-shadow: 0 0 10px rgba(0, 212, 255, 0.7);
    }
    .faq p {
      display: none;
      margin: 10px 0 0;
      transform: translateZ(20px);
    }
    .faq-media {
      display: none;
      margin-top: 10px;
      max-width: 100%;
      border-radius: 8px;
      border: 2px solid #00d4ff;
      transform: translateZ(20px);
      box-shadow: 0 0 15px rgba(0, 212, 255, 0.5);
    }
    .faq.active p, .faq.active .faq-media {
      display: block;
      animation: slideIn 0.3s ease-in-out;
    }
    @keyframes slideIn {
      0% { opacity: 0; transform: translateY(-10px) translateZ(0); }
      100% { opacity: 1; transform: translateY(0) translateZ(0); }
    }
    /* Chatbot Styles */
    .chatbot-container {
      position: fixed;
      bottom: 40px;
      right: 40px;
      z-index: 1000;
      transform: translateZ(100px);
      perspective: 2000px;
    }
    .chatbot-toggle {
      background: url('data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iODAiIGhlaWdodD0iODAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PGNpcmNsZSBjeD0iNDAiIGN5PSI0MCIgcj0iNDAiIGZpbGw9IiNmZmNjMDAiLz48dGV4dCB4PSI0MCIgeT0iNTAiIGZvbnQtZmFtaWx5PSJSb2JvdG8iIGZvbnQtc2l6ZT0iMzAiIGZvbnQtd2VpZ2h0PSI3MDAiIGZpbGw9IiMxMTEiIHRleHQtYW5jaG9yPSJtaWRkbGUiPlRTPC90ZXh0Pjwvc3ZnPg==') no-repeat center;
      background-size: cover;
      border: none;
      border-radius: 50%;
      width: 80px;
      height: 80px;
      cursor: pointer;
      box-shadow: 0 2px 15px rgba(255, 204, 0, 0.8);
      transition: transform 0.3s ease, box-shadow 0.3s ease;
      transform: translateZ(100px);
      animation: rotateChatbotLogo 10s linear infinite;
    }
    @keyframes rotateChatbotLogo {
      0% { transform: rotate(0deg) translateZ(100px); }
      100% { transform: rotate(360deg) translateZ(100px); }
    }
    .chatbot-toggle:hover {
      transform: translateZ(200px) scale(1.2);
      box-shadow: 0 5px 25px rgba(0, 212, 255, 1);
    }
    .chatbot-window {
      display: none; /* Default closed */
      background: linear-gradient(45deg, #333, #444);
      border-radius: 15px;
      width: 320px;
      max-height: 450px;
      overflow-y: auto;
      box-shadow: 0 5px 25px rgba(0, 0, 0, 0.5);
      margin-top: 10px;
      padding: 15px;
      position: relative;
      transform: translateZ(100px);
      border: 2px solid #00d4ff;
    }
    .chatbot-window.active {
      display: block;
    }
    .chatbot-messages {
      display: flex;
      flex-direction: column;
      gap: 10px;
      transform-style: preserve-3d;
    }
    .chatbot-message {
      background-color: #555;
      padding: 10px;
      border-radius: 10px;
      font-size: 0.9em;
      transform: translateZ(30px);
      transition: transform 0.3s ease;
    }
    .chatbot-message.bot {
      background: linear-gradient(45deg, #00d4ff, #ffcc00);
      color: #111;
      align-self: flex-start;
    }
    .chatbot-message.user {
      align-self: flex-end;
    }
    .chatbot-message:hover {
      transform: translateZ(60px);
    }
    .chatbot-input {
      display: flex;
      margin-top: 10px;
      transform: translateZ(30px);
    }
    .chatbot-input input {
      flex: 1;
      padding: 10px;
      border-radius: 8px 0 0 8px;
      border: 1px solid #00d4ff;
      background-color: #555;
      color: white;
    }
    .chatbot-input button {
      padding: 10px;
      border-radius: 0 8px 8px 0;
      background: linear-gradient(45deg, #00d4ff, #ffcc00);
      color: #111;
      border: none;
      cursor: pointer;
    }
    .chatbot-input button:hover {
      background: linear-gradient(45deg, #ffcc00, #00d4ff);
    }
    /* Footer Styles */
    footer {
      text-align: center;
      padding: 20px;
      background-color: #222;
      color: #bbb;
      font-size: 0.9em;
      border-top: 1px solid #444;
      transform: translateZ(50px);
    }
    footer a {
      color: #00d4ff;
      text-decoration: none;
    }
    footer a:hover {
      text-decoration: underline;
      text-shadow: 0 0 10px rgba(0, 212, 255, 0.7);
    }
    /* Unique Holographic Showcase */
    #holographic-showcase {
      position: relative;
      height: 400px;
      margin: 50px 0;
      perspective: 2500px;
      transform-style: preserve-3d;
    }
    #holo-canvas {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      z-index: 0;
    }
    .holo-content {
      position: relative;
      z-index: 1;
      text-align: center;
      color: #00d4ff;
      font-size: 2.5em;
      font-weight: 700;
      animation: holoGlow 1.5s ease-in-out infinite alternate;
      transform: translateZ(200px);
      text-shadow: 0 0 30px rgba(0, 212, 255, 0.9);
    }
  </style>
  <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap" rel="stylesheet">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r134/three.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/vanilla-tilt/1.7.0/vanilla-tilt.min.js"></script>
</head>
<body>
  <header>
    <canvas id="hero-canvas"></canvas>
    <div class="header-content">
      <img src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYwIiBoZWlnaHQ9IjE2MCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8cGF0aCBkPSJNMTYwIDgwQzE2MCAxMjQuMTgzIDE5LjY5NiAxNjAgODAgMTYwQzM1LjgxNyAxNjAgMCAxMjQuMTgzIDAgODBDMCAzNS44MTcgMzUuODE3IDAgODAgMFMxNjAgMzUuODE3IDE2MCA4MFoiIGZpbGw9IiNmZmNjMDAiLz4KICA8cGF0aCBkPSJNODAgMjBDODAgMzEuMDQ2IDY5LjA0NiA0MCA2MCA0MFM0MCAzMS4wNDYgNDAgMjBTNDguOTU0IDEwIDYwIDEwVDgwIDIwWiIgZmlsbD0iIzExMSIvPgogIDx0ZXh0IHg9IjgwIiB5PSIxMDAiIGZvbnQtZmFtaWx5PSJSb2JvdG8sIEFyaWFsLCBzYW5zLXNlcmlmIiBmb250LXNpemU9IjU1IiBmb250LXdlaWdodD0iNzAwIiBmaWxsPSIjMTExIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj5UUzwvdGV4dD4KPC9zdmc+" alt="Tahir Sayyaf Portfolio Logo" class="logo">
      <div class="welcome">Welcome to Tahir Sayyaf Portfolio</div>
      <div class="welcome-sub">Showcasing world-class designs and innovations</div>
    </div>
  </header>

  <nav>
    <a href="#home">Home</a>
    <a href="#stickers">Why Me</a>
    <a href="#download">Download</a>
    <a href="#contact">Contact</a>
    <a href="#faqs">FAQs</a>
  </nav>

  <section id="home">
    <h2>Home</h2>
    <p>Welcome to my portfolio! I'm Tahir Sayyaf, a top-rated freelancer specializing in world-class web designs with lightning-fast turnaround. Explore my work and elevate your brand with a bespoke landing page crafted for impact.</p>
    <div id="holographic-showcase">
      <canvas id="holo-canvas"></canvas>
      <div class="holo-content">Tahir Sayyaf's Signature Designs</div>
    </div>
  </section>

  <section id="stickers">
    <h2>Why Choose Me?</h2>
    <div class="stickers">
      <div class="sticker" data-tilt data-tilt-max="25" data-tilt-speed="800" data-tilt-perspective="2000">
        🌟 100+ Successful Projects
        <img src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzAiIGhlaWdodD0iMzAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PGNpcmNsZSBjeD0iMTUiIGN5PSIxNSIgcj0iMTUiIGZpbGw9IiNmZmNjMDAiLz48dGV4dCB4PSIxNSIgeT0iMjAiIGZvbnQtZmFtaWx5PSJSb2JvdG8iIGZvbnQtc2l6ZT0iMTgiIGZpbGw9IiMxMTEiIHRleHQtYW5jaG9yPSJtaWRkbGUiPlRTPC90ZXh0Pjwvc3ZnPg==" alt="TS Logo" class="sticker-logo">
      </div>
      <div class="sticker" data-tilt data-tilt-max="25" data-tilt-speed="800" data-tilt-perspective="2000">
        ⚡ Lightning-Fast Delivery
        <img src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzAiIGhlaWdodD0iMzAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PGNpcmNsZSBjeD0iMTUiIGN5PSIxNSIgcj0iMTUiIGZpbGw9IiNmZmNjMDAiLz48dGV4dCB4PSIxNSIgeT0iMjAiIGZvbnQtZmFtaWx5PSJSb2JvdG8iIGZvbnQtc2l6ZT0iMTgiIGZpbGw9IiMxMTEiIHRleHQtYW5jaG9yPSJtaWRkbGUiPlRTPC90ZXh0Pjwvc3ZnPg==" alt="TS Logo" class="sticker-logo">
      </div>
      <div class="sticker" data-tilt data-tilt-max="25" data-tilt-speed="800" data-tilt-perspective="2000">
        🏆 5-Star Client Reviews
        <img src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzAiIGhlaWdodD0iMzAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PGNpcmNsZSBjeD0iMTUiIGN5PSIxNSIgcj0iMTUiIGZpbGw9IiNmZmNjMDAiLz48dGV4dCB4PSIxNSIgeT0iMjAiIGZvbnQtZmFtaWx5PSJSb2JvdG8iIGZvbnQtc2l6ZT0iMTgiIGZpbGw9IiMxMTEiIHRleHQtYW5jaG9yPSJtaWRkbGUiPlRTPC90ZXh0Pjwvc3ZnPg==" alt="TS Logo" class="sticker-logo">
      </div>
      <div class="sticker" data-tilt data-tilt-max="25" data-tilt-speed="800" data-tilt-perspective="2000">
        🔒 100% Satisfaction Guarantee
        <img src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzAiIGhlaWdodD0iMzAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PGNpcmNsZSBjeD0iMTUiIGN5PSIxNSIgcj0iMTUiIGZpbGw9IiNmZmNjMDAiLz48dGV4dCB4PSIxNSIgeT0iMjAiIGZvbnQtZmFtaWx5PSJSb2JvdG8iIGZvbnQtc2l6ZT0iMTgiIGZpbGw9IiMxMTEiIHRleHQtYW5jaG9yPSJtaWRkbGUiPlRTPC90ZXh0Pjwvc3ZnPg==" alt="TS Logo" class="sticker-logo">
      </div>
      <div class="sticker" data-tilt data-tilt-max="25" data-tilt-speed="800" data-tilt-perspective="2000">
        🎨 Bespoke Designs
        <img src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzAiIGhlaWdodD0iMzAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PGNpcmNsZSBjeD0iMTUiIGN5PSIxNSIgcj0iMTUiIGZpbGw9IiNmZmNjMDAiLz48dGV4dCB4PSIxNSIgeT0iMjAiIGZvbnQtZmFtaWx5PSJSb2JvdG8iIGZvbnQtc2l6ZT0iMTgiIGZpbGw9IiMxMTEiIHRleHQtYW5jaG9yPSJtaWRkbGUiPlRTPC90ZXh0Pjwvc3ZnPg==" alt="TS Logo" class="sticker-logo">
      </div>
      <div class="sticker" data-tilt data-tilt-max="25" data-tilt-speed="800" data-tilt-perspective="2000">
        🖥️ Interactive 3D Interfaces
        <img src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzAiIGhlaWdodD0iMzAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PGNpcmNsZSBjeD0iMTUiIGN5PSIxNSIgcj0iMTUiIGZpbGw9IiNmZmNjMDAiLz48dGV4dCB4PSIxNSIgeT0iMjAiIGZvbnQtZmFtaWx5PSJSb2JvdG8iIGZvbnQtc2l6ZT0iMTgiIGZpbGw9IiMxMTEiIHRleHQtYW5jaG9yPSJtaWRkbGUiPlRTPC90ZXh0Pjwvc3ZnPg==" alt="TS Logo" class="sticker-logo">
      </div>
    </div>
  </section>

  <section id="download">
    <h2>Download My Portfolio</h2>
    <div class="download-section">
      <p>Discover my premium services and projects through my curated portfolio brochure, showcasing stunning designs and exclusive offerings.</p>
      <a href="path/to/your/portfolio.pdf" download class="download-button">Download Now</a>
      <p class="download-counter">Downloaded 150+ times!</p>
    </div>
  </section>

  <section id="contact">
    <h2>Contact Me</h2>
    <div class="contact-form" data-tilt data-tilt-max="20" data-tilt-speed="800" data-tilt-perspective="2000">
      <form>
        <input type="text" placeholder="Your Name" required />
        <input type="email" placeholder="Your Email" required />
        <textarea placeholder="Your Message" rows="5" required></textarea>
        <button type="submit">Send Message</button>
      </form>
    </div>
  </section>

  <section id="faqs">
    <h2>FAQs</h2>
    <div id="faq-container"></div>
  </section>

  <!-- Chatbot -->
  <div class="chatbot-container" data-tilt data-tilt-max="25" data-tilt-speed="800" data-tilt-perspective="2000">
    <button class="chatbot-toggle"></button>
    <div class="chatbot-window">
      <div class="chatbot-messages">
        <!-- Messages will be added dynamically -->
      </div>
      <div class="chatbot-input">
        <input type="text" placeholder="Type your question..." />
        <button>Send</button>
      </div>
    </div>
  </div>

  <footer>
    <p>&copy; 2025 Tahir Sayyaf. All rights reserved. Unauthorized copying or reproduction of this portfolio's design, code, or content is strictly prohibited.</p>
    <p>Contact me at <a href="mailto:your.email@example.com">your.email@example.com</a> for inquiries.</p>
  </footer>

  <script>
    // Disable right-click and text selection
    document.addEventListener('contextmenu', (e) => {
      e.preventDefault();
      alert('Copying is disabled to protect my portfolio. Contact me for inquiries!');
    });
    document.addEventListener('selectstart', (e) => {
      e.preventDefault();
    });

    // Editable FAQs with Image/Video Support
    const faqs = [
      {
        question: "What services do you offer?",
        answer: "I specialize in premium web design, including landing pages, portfolio sites, and interactive features like 3D effects and chatbots.",
        media: { type: "image", src: "images/project1.jpg" }
      },
      {
        question: "How soon can you deliver a project?",
        answer: "Most projects are delivered within 24-48 hours, depending on complexity.",
        media: { type: "video", src: "videos/project1.mp4" }
      },
      {
        question: "Do you offer revisions?",
        answer: "Yes, I provide unlimited revisions until you're fully satisfied!"
      },
      {
        question: "Can you design in my preferred language?",
        answer: "Absolutely, I support multilingual projects. Just let me know your needs!",
        media: { type: "image", src: "images/project2.jpg" }
      }
    ];

    function renderFAQs() {
      const faqContainer = document.getElementById('faq-container');
      faqContainer.innerHTML = '';
      faqs.forEach(faq => {
        const faqDiv = document.createElement('div');
        faqDiv.classList.add('faq');
        faqDiv.setAttribute('data-tilt', '');
        faqDiv.setAttribute('data-tilt-max', '20');
        faqDiv.setAttribute('data-tilt-speed', '800');
        faqDiv.setAttribute('data-tilt-perspective', '2000');
        let mediaHTML = '';
        if (faq.media) {
          if (faq.media.type === 'image') {
            mediaHTML = `<img src="${faq.media.src}" alt="Project Media" class="faq-media">`;
          } else if (faq.media.type === 'video') {
            mediaHTML = `<video src="${faq.media.src}" controls class="faq-media" style="max-height: 200px;"></video>`;
          }
        }
        faqDiv.innerHTML = `
          <h4>${faq.question}</h4>
          <p>${faq.answer}</p>
          ${mediaHTML}
        `;
        faqContainer.appendChild(faqDiv);
      });

      VanillaTilt.init(document.querySelectorAll('.faq'), {
        max: 20,
        speed: 800,
        perspective: 2000,
        glare: true,
        'max-glare': 0.5
      });

      document.querySelectorAll('.faq').forEach(faq => {
        faq.addEventListener('click', () => {
          faq.classList.toggle('active');
        });
      });
    }

    renderFAQs();

    // Three.js for 3D Parallax Hero Section with Particles
    const heroScene = new THREE.Scene();
    const heroCamera = new THREE.PerspectiveCamera(75, window.innerWidth / 800, 0.1, 1000);
    const heroRenderer = new THREE.WebGLRenderer({ canvas: document.getElementById('hero-canvas'), alpha: true });
    heroRenderer.setSize(window.innerWidth, 800);

    const heroGeometry = new THREE.TorusKnotGeometry(4, 1.2, 100, 16);
    const heroMaterial = new THREE.ShaderMaterial({
      uniforms: {
        time: { value: 0 },
        color1: { value: new THREE.Color(0x00d4ff) },
        color2: { value: new THREE.Color(0xffcc00) }
      },
      vertexShader: `
        varying vec2 vUv;
        void main() {
          vUv = uv;
          gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
        }
      `,
      fragmentShader: `
        uniform float time;
        uniform vec3 color1;
        uniform vec3 color2;
        varying vec2 vUv;
        void main() {
          float t = sin(time * 0.5) * 0.5 + 0.5;
          vec3 color = mix(color1, color2, t);
          gl_FragColor = vec4(color, 0.8);
        }
      `,
      wireframe: true
    });
    const heroTorusKnot = new THREE.Mesh(heroGeometry, heroMaterial);
    heroScene.add(heroTorusKnot);

    const particleCount = 500;
    const particles = new THREE.BufferGeometry();
    const positions = new Float32Array(particleCount * 3);
    for (let i = 0; i < particleCount * 3; i += 3) {
      positions[i] = (Math.random() - 0.5) * 20;
      positions[i + 1] = (Math.random() - 0.5) * 20;
      positions[i + 2] = (Math.random() - 0.5) * 10;
    }
    particles.setAttribute('position', new THREE.BufferAttribute(positions, 3));
    const particleMaterial = new THREE.PointsMaterial({
      color: 0x00d4ff,
      size: 0.3,
      transparent: true,
      opacity: 0.9
    });
    const particleSystem = new THREE.Points(particles, particleMaterial);
    heroScene.add(particleSystem);

    heroCamera.position.z = 12;

    function animateHero() {
      requestAnimationFrame(animateHero);
      heroTorusKnot.rotation.x += 0.005;
      heroTorusKnot.rotation.y += 0.005;
      heroMaterial.uniforms.time.value += 0.02;
      const positions = particleSystem.geometry.attributes.position.array;
      for (let i = 0; i < particleCount * 3; i += 3) {
        positions[i + 2] += 0.02;
        if (positions[i + 2] > 10) positions[i + 2] -= 20;
      }
      particleSystem.geometry.attributes.position.needsUpdate = true;
      heroRenderer.render(heroScene, heroCamera);
    }
    animateHero();

    document.addEventListener('mousemove', (event) => {
      const mouseX = (event.clientX / window.innerWidth) * 2 - 1;
      const mouseY = -(event.clientY / 800) * 2 + 1;
      heroTorusKnot.position.x = mouseX * 3;
      heroTorusKnot.position.y = mouseY * 3;
      particleSystem.position.x = mouseX * 2;
      particleSystem.position.y = mouseY * 2;
    });

    // Unique Holographic Showcase
    const holoScene = new THREE.Scene();
    const holoCamera = new THREE.PerspectiveCamera(75, window.innerWidth / 400, 0.1, 1000);
    const holoRenderer = new THREE.WebGLRenderer({ canvas: document.getElementById('holo-canvas'), alpha: true });
    holoRenderer.setSize(window.innerWidth, 400);

    const holoGeometry = new THREE.DodecahedronGeometry(4, 0);
    const holoMaterial = new THREE.ShaderMaterial({
      uniforms: {
        time: { value: 0 },
        color1: { value: new THREE.Color(0x00d4ff) },
        color2: { value: new THREE.Color(0xffcc00) }
      },
      vertexShader: `
        varying vec2 vUv;
        void main() {
          vUv = uv;
          gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
        }
      `,
      fragmentShader: `
        uniform float time;
        uniform vec3 color1;
        uniform vec3 color2;
        varying vec2 vUv;
        void main() {
          float t = sin(time * 0.5) * 0.5 + 0.5;
          vec3 color = mix(color1, color2, t);
          gl_FragColor = vec4(color, 0.8);
        }
      `,
      wireframe: true
    });
    const holoDodecahedron = new THREE.Mesh(holoGeometry, holoMaterial);
    holoScene.add(holoDodecahedron);

    const holoParticleCount = 300;
    const holoParticles = new THREE.BufferGeometry();
    const holoPositions = new Float32Array(holoParticleCount * 3);
    for (let i = 0; i < holoParticleCount * 3; i += 3) {
      const theta = Math.random() * 2 * Math.PI;
      const phi = Math.random() * Math.PI;
      const r = 5 + Math.random() * 2;
      holoPositions[i] = r * Math.sin(phi) * Math.cos(theta);
      holoPositions[i + 1] = r * Math.sin(phi) * Math.sin(theta);
      holoPositions[i + 2] = r * Math.cos(phi);
    }
    holoParticles.setAttribute('position', new THREE.BufferAttribute(holoPositions, 3));
    const holoParticleMaterial = new THREE.PointsMaterial({
      color: 0x00d4ff,
      size: 0.2,
      transparent: true,
      opacity: 0.9
    });
    const holoParticleSystem = new THREE.Points(holoParticles, holoParticleMaterial);
    holoScene.add(holoParticleSystem);

    holoCamera.position.z = 12;

    function animateHolo() {
      requestAnimationFrame(animateHolo);
      holoDodecahedron.rotation.x += 0.01;
      holoDodecahedron.rotation.y += 0.01;
      holoMaterial.uniforms.time.value += 0.02;
      const holoPositions = holoParticleSystem.geometry.attributes.position.array;
      for (let i = 0; i < holoParticleCount * 3; i += 3) {
        const theta = 0.01 + i / holoParticleCount * 0.02;
        holoPositions[i] = 6 * Math.sin(theta + holoMaterial.uniforms.time.value);
        holoPositions[i + 1] = 6 * Math.cos(theta + holoMaterial.uniforms.time.value);
        holoPositions[i + 2] = 6 * Math.sin(theta + holoMaterial.uniforms.time.value);
      }
      holoParticleSystem.geometry.attributes.position.needsUpdate = true;
      holoRenderer.render(holoScene, holoCamera);
    }
    animateHolo();

    // Resize handler
    window.addEventListener('resize', () => {
      heroRenderer.setSize(window.innerWidth, 800);
      heroCamera.aspect = window.innerWidth / 800;
      heroCamera.updateProjectionMatrix();

      holoRenderer.setSize(window.innerWidth, 400);
      holoCamera.aspect = window.innerWidth / 400;
      holoCamera.updateProjectionMatrix();
    });

    // Vanilla Tilt for 3D effect on stickers, contact form, and chatbot
    VanillaTilt.init(document.querySelectorAll('.sticker, .contact-form, .chatbot-container'), {
      max: 25,
      speed: 800,
      perspective: 2000,
      glare: true,
      'max-glare': 0.5
    });

    // Download counter simulation
    document.querySelector('.download-button').addEventListener('click', () => {
      let counter = document.querySelector('.download-counter');
      let count = parseInt(counter.textContent.match(/\d+/)[0]) + 1;
      counter.textContent = `Downloaded ${count}+ times!`;
    });

    // Smooth scroll for nav links
    document.querySelectorAll('nav a').forEach(anchor => {
      anchor.addEventListener('click', function(e) {
        e.preventDefault();
        const section = document.querySelector(this.getAttribute('href'));
        section.scrollIntoView({ behavior: 'smooth' });
      });
    });

    // Chatbot functionality with multilingual support and visitor welcome
    const chatbotToggle = document.querySelector('.chatbot-toggle');
    const chatbotWindow = document.querySelector('.chatbot-window');
    const chatbotInput = document.querySelector('.chatbot-input input');
    const chatbotSend = document.querySelector('.chatbot-input button');
    const chatbotMessages = document.querySelector('.chatbot-messages');

    // Track if welcome message has been shown
    let welcomeShown = false;

    chatbotToggle.addEventListener('click', () => {
      chatbotWindow.classList.toggle('active');
      if (chatbotWindow.classList.contains('active') && !welcomeShown) {
        const userName = getUserName();
        const browserLang = navigator.language.split('-')[0];
        const lang = ['en', 'ur', 'ru', 'hi', 'de'].includes(browserLang) ? browserLang : 'en';
        addMessage(responses[lang].welcome.replace('{name}', userName), 'bot', lang);
        addMessage(responses[lang].prompt, 'bot', lang);
        welcomeShown = true;
      }
    });

    // Multilingual responses
    const responses = {
      en: {
        welcome: "Welcome to Tahir Sayyaf Portfolio, {name}! 😎 I'm your virtual assistant, here to answer any question about my work or services!",
        prompt: "Type your question below (e.g., 'What services do you offer?' or 'Aur sunao!') or use the Contact Me section. Let's get started! 🚀",
        services: "I specialize in premium web design, including landing pages, portfolio sites, and interactive features like 3D effects, chatbots, and holographic showcases.",
        delivery: "Most projects are delivered within 24-48 hours, depending on complexity.",
        revisions: "Yes, I provide unlimited revisions until you're fully satisfied!",
        language: "Absolutely, I support multilingual projects. Just let me know your needs!",
        contact: "Please fill out the contact form above, and I'll get back to you ASAP!",
        projects: "Explore my portfolio to see 100+ successful projects with 5-star client reviews! Check out the holographic showcase for a unique experience.",
        holographic: "The holographic showcase is a unique 3D feature I created to highlight my signature designs. It’s a spinning dodecahedron with a glowing effect. Cool, right? 😎",
        default: "Hmmm, that's an interesting question! 😄 Try asking about my services, projects, holographic showcase, or just say 'aur sunao' for a fun chat!"
      },
      ur: {
        welcome: "طاہر سیاف پورٹ فولیو میں خوش آمدید، {name}! 😎 میں آپ کا ورچوئل اسسٹنٹ ہوں، میرے کام یا خدمات کے بارے میں کوئی بھی سوال پوچھنے کے لیے تیار ہوں!",
        prompt: "نیچے اپنا سوال ٹائپ کریں (مثال کے طور پر، 'آپ کیا خدمات پیش کرتے ہیں؟' یا 'اور سناؤ!') یا رابطہ سیکشن استعمال کریں۔ چلیں شروع کریں! 🚀",
        services: "میں پریمیم ویب ڈیزائن میں مہارت رکھتا ہوں، بشمول لینڈنگ پیجز، پورٹ فولیو سائٹس، اور 3D ایفیکٹس، چیٹ بوٹس، اور ہولوگرافک شوکیس جیسے انٹرایکٹو فیچرز۔",
        delivery: "زیادہ تر پراجیکٹس پیچیدگی کے لحاظ سے 24-48 گھنٹوں میں ڈیلیور ہوتے ہیں۔",
        revisions: "جی ہاں، میں مکمل اطمینان تک لامحدود ترامیم فراہم کرتا ہوں!",
        language: "بالکل، میں کثیر لسانی پراجیکٹس کو سپورٹ کرتا ہوں۔ بس اپنی ضروریات بتائیں!",
        contact: "براہ کرم اوپر رابطہ فارم پُر کریں، میں جلد از جلد جواب دوں گا!",
        projects: "میرے پورٹ فولیو کو دیکھیں اور 100+ کامیاب پراجیکٹس اور 5 اسٹار کلائنٹ ریویوز چیک کریں! ہولوگرافک شوکیس ایک منفرد تجربے کے لیے دیکھیں۔",
        holographic: "ہولوگرافک شوکیس ایک منفرد 3D فیچر ہے جو میں نے اپنے سگنچر ڈیزائنز کو ہائی لائٹ کرنے کے لیے بنایا۔ یہ ایک گھومتا ہوا ڈوڈیکاہیڈرن ہے جو چمکتا ہے۔ ٹھنڈا، نا؟ 😎",
        default: "ہمم، یہ سوال تھوڑا مختلف ہے! 😄 میری خدمات، پراجیکٹس، ہولوگرافک شوکیس کے بارے میں پوچھیں یا بس 'اور سناؤ' کہیں مزے کے لیے!"
      },
      ru: {
        welcome: "Добро пожаловать в портфолио Тахира Сайяфа, {name}! 😎 Я ваш виртуальный помощник, готов ответить на любые вопросы о моей работе или услугах!",
        prompt: "Введите ваш вопрос ниже (например, 'Какие услуги вы предлагаете?' или 'Расскажи что-нибудь!') или используйте раздел 'Связаться со мной'. Начнем! 🚀",
        services: "Я специализируюсь на премиум веб-дизайне, включая лендинги, сайты-портфолио и интерактивные функции, такие как 3D-эффекты, чат-боты и голографические витрины.",
        delivery: "Большинство проектов доставляется в течение 24-48 часов в зависимости от сложности.",
        revisions: "Да, я предоставляю неограниченные правки, пока вы не будете полностью удовлетворены!",
        language: "Конечно, я поддерживаю многоязычные проекты. Просто сообщите о ваших потребностях!",
        contact: "Пожалуйста, заполните форму обратной связи выше, и я отвечу как можно скорее!",
        projects: "Ознакомьтесь с моим портфолио, чтобы увидеть более 100 успешных проектов с 5-звездочными отзывами клиентов! Посмотрите голографическую витрину для уникального опыта.",
        holographic: "Голографическая витрина — это уникальная 3D-функция, которую я создал для выделения моих фирменных дизайнов. Это вращающийся додекаэдр с эффектом свечения. Круто, правда? 😎",
        default: "Хм, интересный вопрос! 😄 Попробуйте спросить о моих услугах, проектах, голографической витрине или просто скажите 'расскажи что-нибудь' для веселья!"
      },
      hi: {
        welcome: "ताहिर सय्याफ पोर्टफोलियो में आपका स्वागत है, {name}! 😎 मैं आपका वर्चुअल असिस्टेंट हूँ, मेरे काम या सेवाओं के बारे में कोई भी सवाल पूछने के लिए तैयार हूँ!",
        prompt: "नीचे अपना सवाल टाइप करें (उदाहरण के लिए, 'आप कौन सी सेवाएँ देते हैं?' या 'और सुनाओ!') या कॉन्टैक्ट मी सेक्शन का उपयोग करें। चलो शुरू करें! 🚀",
        services: "मैं प्रीमियम वेब डिज़ाइन में विशेषज्ञ हूँ, जिसमें लैंडिंग पेज, पोर्टफोलियो साइट्स, और 3D इफेक्ट्स, चैटबॉट्स, और होलोग्राफिक शोकेस जैसे इंटरैक्टिव फीचर्स शामिल हैं।",
        delivery: "ज्यादातर प्रोजेक्ट्स जटिलता के आधार पर 24-48 घंटों में डिलीवर हो जाते हैं।",
        revisions: "हाँ, मैं पूरी तरह से संतुष्ट होने तक अनलिमिटेड रिवीज़न देता हूँ!",
        language: "बिल्कुल, मैं बहुभाषी प्रोजेक्ट्स को सपोर्ट करता हूँ। बस अपनी ज़रूरतें बताएँ!",
        contact: "कृपया ऊपर कॉन्टैक्ट फॉर्म भरें, मैं जल्द से जलद जवाब दूँगा!",
        projects: "मेरे पोर्टफोलियो को देखें और 100+ सफल प्रोजेक्ट्स और 5-स्टार क्लाइंट रिव्यूज़ देखें! होलोग्राफिक शोकेस एक अनोखे अनुभव के लिए देखें।",
        holographic: "होलोग्राफिक शोकेस एक अनोखा 3D फीचर है जिसे मैंने अपने सिग्नेचर डिज़ाइन्स को हाइलाइट करने के लिए बनाया है। यह एक घूमने वाला डोडेका हेड्रॉन है जो चमकता है। कूल, ना? 😎",
        default: "हम्म, ये सवाल थोड़ा अलग है! 😄 मेरी सेवाओं, प्रोजेक्ट्स, होलोग्राफिक शोकेस के बारे में पूछें या बस 'और सुनाओ' कहें मज़े के लिए!"
      },
      de: {
        welcome: "Willkommen im Portfolio von Tahir Sayyaf, {name}! 😎 Ich bin Ihr virtueller Assistent und beantworte gerne alle Fragen zu meiner Arbeit oder meinen Dienstleistungen!",
        prompt: "Geben Sie Ihre Frage unten ein (z.B. 'Welche Dienstleistungen bieten Sie an?' oder 'Erzähl mal was!') oder nutzen Sie den Kontaktbereich. Los geht’s! 🚀",
        services: "Ich bin spezialisiert auf Premium-Webdesign, einschließlich Landingpages, Portfolioseiten und interaktive Funktionen wie 3D-Effekte, Chatbots und holografische Schaufenster.",
        delivery: "Die meisten Projekte werden je nach Komplexität innerhalb von 24-48 Stunden geliefert.",
        revisions: "Ja, ich biete unbegrenzte Überarbeitungen, bis Sie vollkommen zufrieden sind!",
        language: "Absolut, ich unterstütze mehrsprachige Projekte. Teilen Sie mir einfach Ihre Bedürfnisse mit!",
        contact: "Bitte füllen Sie das Kontaktformular oben aus, ich melde mich so schnell wie möglich!",
        projects: "Schauen Sie sich mein Portfolio an, um über 100 erfolgreiche Projekte mit 5-Sterne-Kundenbewertungen zu sehen! Sehen Sie sich das holografische Schaufenster für ein einzigartiges Erlebnis an.",
        holographic: "Das holografische Schaufenster ist eine einzigartige 3D-Funktion, die ich entwickelt habe, um meine charakteristischen Designs hervorzuheben. Es ist ein rotierendes Dodekaeder mit Leuchteffekt. Cool, oder? 😎",
        default: "Hmm, das ist eine interessante Frage! 😄 Fragen Sie nach meinen Dienstleistungen, Projekten, dem holografischen Schaufenster oder sagen Sie einfach 'Erzähl mal was' für Spaß!"
      }
    };

    // Simple language detection based on keywords
    function detectLanguage(input) {
      input = input.toLowerCase();
      if (input.includes('salaam') || input.includes('aur sunao') || input.includes('kya hua')) return 'ur';
      if (input.includes('привет') || input.includes('расскажи')) return 'ru';
      if (input.includes('नमस्ते') || input.includes('और सुनाओ')) return 'hi';
      if (input.includes('hallo') || input.includes('erzähl')) return 'de';
      return 'en';
    }

    function addMessage(message, type, lang = 'en') {
      const msgDiv = document.createElement('div');
      msgDiv.classList.add('chatbot-message', type);
      msgDiv.textContent = message;
      chatbotMessages.appendChild(msgDiv);
      chatbotMessages.scrollTop = chatbotMessages.scrollHeight;
    }

    // Get user name for personalized welcome
    function getUserName() {
      let name = localStorage.getItem('userName');
      if (!name) {
        name = prompt('Please enter your name for a personalized experience:', 'Guest') || 'Guest';
        localStorage.setItem('userName', name);
      }
      return name;
    }

    // Multilingual chatbot responses
    chatbotSend.addEventListener('click', () => {
      const userInput = chatbotInput.value.trim();
      if (userInput) {
        const lang = detectLanguage(userInput);
        addMessage(userInput, 'user', lang);
        let response = responses[lang].default;
        const inputLower = userInput.toLowerCase();
        if (inputLower.includes('services') || inputLower.includes('خدمات') || inputLower.includes('услуги') || inputLower.includes('सेवाएँ') || inputLower.includes('dienstleistungen')) {
          response = responses[lang].services;
        } else if (inputLower.includes('how soon') || inputLower.includes('delivery') || inputLower.includes('کب تک') || inputLower.includes('доставка') || inputLower.includes('डिलीवरी') || inputLower.includes('lieferung')) {
          response = responses[lang].delivery;
        } else if (inputLower.includes('revisions') || inputLower.includes('ترامیم') || inputLower.includes('правки') || inputLower.includes('रिवीज़न') || inputLower.includes('überarbeitungen')) {
          response = responses[lang].revisions;
        } else if (inputLower.includes('language') || inputLower.includes('زبان') || inputLower.includes('язык') || inputLower.includes('भाषा') || inputLower.includes('sprache')) {
          response = responses[lang].language;
        } else if (inputLower.includes('contact') || inputLower.includes('رابطہ') || inputLower.includes('контакт') || inputLower.includes('संपर्क') || inputLower.includes('kontakt')) {
          response = responses[lang].contact;
        } else if (inputLower.includes('projects') || inputLower.includes('پراجیکٹس') || inputLower.includes('проекты') || inputLower.includes('प्रोजेक्ट्स') || inputLower.includes('projekte')) {
          response = responses[lang].projects;
        } else if (inputLower.includes('holographic') || inputLower.includes('ہولوگرافک') || inputLower.includes('голографический') || inputLower.includes('होलोग्राफिक') || inputLower.includes('holografisch')) {
          response = responses[lang].holographic;
        } else if (inputLower.includes('aur sunao') || inputLower.includes('kya hua') || inputLower.includes('расскажи') || inputLower.includes('और सुनाओ') || inputLower.includes('erzähl')) {
          response = responses[lang].default;
        }
        setTimeout(() => addMessage(response, 'bot', lang), 500);
        chatbotInput.value = '';
      }
    });

    chatbotInput.addEventListener('keypress', (e) => {
      if (e.key === 'Enter') chatbotSend.click();
    });
  </script>
</body>
</html>
