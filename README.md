# ⚡ Modern URL Shortener

A lightning-fast, full-stack URL shortening service built with **FastAPI**, **MongoDB**, and a completely custom, premium "AI-startup" aesthetic frontend (Vanilla JS/CSS). 

Designed to be lightweight, incredibly responsive, and deploy-ready for Serverless environments like **Vercel**.

## ✨ Features
* **Premium UI:** A custom-built, dark-mode interface featuring atmospheric overlapping radial gradients, pill-shaped UI components, and fluid micro-animations.
* **Instant Redirection:** FastAPI backend ensures sub-millisecond route matching and redirection.
* **Robust URL Validation:** Automatically cleans and formats missing HTTP schemes before insertion to prevent relative-path breaking.
* **Vercel Ready:** Pre-configured `vercel.json` routing maps the Python backend and static frontend together on a single domain.

## 🛠️ Tech Stack
* **Backend:** Python, FastAPI, Uvicorn
* **Database:** MongoDB (`pymongo`)
* **Frontend:** HTML5, Modern CSS (Flexbox), Vanilla JavaScript

## 🚀 Running Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/mohsinn1/url-shortener.git
   cd url-shortener
