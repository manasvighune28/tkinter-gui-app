import tkinter as tk
import requests
import feedparser

def open_news_window():
    win = tk.Toplevel()
    win.title("Latest Indian News")
    win.geometry("900x550")
    win.configure(bg="#f4f6f8")

    header = tk.Label(
        win,
        text="📰 Latest Indian News (India)",
        font=("Helvetica", 18, "bold"),
        bg="#f4f6f8",
        fg="#2c3e50"
    )
    header.pack(pady=15)

    container = tk.Frame(win, bg="#f4f6f8")
    container.pack(fill="both", expand=True)

    canvas = tk.Canvas(container, bg="#f4f6f8", highlightthickness=0)
    scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)

    scroll_frame = tk.Frame(canvas, bg="#f4f6f8")
    canvas.create_window((0, 0), window=scroll_frame, anchor="nw")

    scroll_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    # ✅ FETCH RSS WITH HEADERS (CRITICAL FIX)
    feed_url = "https://timesofindia.indiatimes.com/rssfeeds/-2128936835.cms"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(feed_url, headers=headers, timeout=10)
        feed = feedparser.parse(response.text)
    except Exception as e:
        tk.Label(
            scroll_frame,
            text="❌ Failed to load news",
            font=("Helvetica", 14),
            fg="red",
            bg="#f4f6f8"
        ).pack(pady=20)
        return

    if not feed.entries:
        tk.Label(
            scroll_frame,
            text="❌ RSS blocked by network",
            font=("Helvetica", 14),
            fg="red",
            bg="#f4f6f8"
        ).pack(pady=20)
        return

    # ✅ DISPLAY NEWS
    for entry in feed.entries[:20]:
        card = tk.Frame(scroll_frame, bg="white")
        card.pack(fill="x", padx=30, pady=10)

        tk.Label(
            card,
            text=entry.title,
            font=("Helvetica", 13, "bold"),
            bg="white",
            fg="#2c3e50",
            wraplength=800,
            justify="left"
        ).pack(anchor="w", padx=15, pady=(10, 5))

        if hasattr(entry, "summary"):
            tk.Label(
                card,
                text=entry.summary[:150] + "...",
                font=("Helvetica", 10),
                bg="white",
                fg="#7f8c8d",
                wraplength=800,
                justify="left"
            ).pack(anchor="w", padx=15, pady=(0, 10))
