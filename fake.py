import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import messagebox

class FakeNewsDetectorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Detector de Fake News")

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Insira a URL da notícia:")
        self.label.pack(pady=10)

        self.url_entry = tk.Entry(self.root, width=50)
        self.url_entry.pack(pady=5)

        self.check_button = tk.Button(self.root, text="Verificar Notícia", command=self.check_news)
        self.check_button.pack(pady=10)

    def check_news(self):
        url = self.url_entry.get()
        result = self.detect_fake_news(url)
        messagebox.showinfo("Resultado", result)

    def detect_fake_news(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, 'html.parser')
            titles = soup.find_all('h2')

            suspicious_keywords = ['falso', 'fake', 'enganoso', 'desmentido', 'mentira']

            for title in titles:
                title_text = title.get_text().lower()
                for keyword in suspicious_keywords:
                    if keyword in title_text:
                        return "Esta notícia é suspeita!"
            return "Esta notícia parece genuína."

        except requests.exceptions.RequestException as e:
            return "Erro de requisição: " + str(e)
        except Exception as e:
            return "Erro: " + str(e)

if __name__ == "__main__":
    root = tk.Tk()
    app = FakeNewsDetectorApp(root)
    root.mainloop()

