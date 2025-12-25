import tkinter as tk
import requests
from app.config import OPENWEATHER_API_KEY

def open_weather_window():
    win = tk.Toplevel()
    win.title("Weather App")
    win.geometry("420x320")
    win.configure(bg="#ecf0f1")

    # ---------- Header ----------
    title = tk.Label(
        win,
        text="🌦 Weather Information",
        font=("Helvetica", 16, "bold"),
        bg="#ecf0f1",
        fg="#2c3e50"
    )
    title.pack(pady=15)

    # ---------- Card ----------
    card = tk.Frame(
        win,
        bg="white",
        bd=0
    )
    card.pack(padx=30, pady=10, fill="both", expand=True)

    # ---------- City Input ----------
    tk.Label(
        card,
        text="Enter City",
        font=("Helvetica", 11),
        bg="white",
        fg="#34495e"
    ).pack(pady=(20, 5))

    city_entry = tk.Entry(
        card,
        font=("Helvetica", 12),
        justify="center"
    )
    city_entry.pack(pady=5)

    # ---------- Result ----------
    result = tk.Label(
        card,
        text="",
        font=("Helvetica", 14, "bold"),
        bg="white",
        fg="#2c3e50",
        justify="center"
    )
    result.pack(pady=20)

    # ---------- Button ----------
    def get_weather():
        city = city_entry.get().strip()
        if not city:
            result.config(text="⚠️ Please enter a city")
            return

        url = (
            f"https://api.weatherapi.com/v1/current.json"
            f"?key={OPENWEATHER_API_KEY}&q={city}"
        )

        try:
            response = requests.get(url, timeout=10)
            data = response.json()

            if "error" in data:
                result.config(text="❌ City not found")
                return

            temp = data["current"]["temp_c"]
            condition = data["current"]["condition"]["text"]

            result.config(
                text=f"🌡 {temp}°C\n☁️ {condition}"
            )

        except Exception:
            result.config(text="⚠️ Network error")

    tk.Button(
        card,
        text="Get Weather",
        font=("Helvetica", 12),
        bg="#3498db",
        fg="white",
        activebackground="#2980b9",
        activeforeground="white",
        relief="flat",
        padx=20,
        pady=8,
        command=get_weather
    ).pack(pady=10)

