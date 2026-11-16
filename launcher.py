"""Локальний запуск записника з постійною адресою http://127.0.0.1:8765/ ."""
from functools import partial
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from threading import Timer
import webbrowser

PORT = 8765


def main():
    folder = Path(__file__).resolve().parent
    handler = partial(SimpleHTTPRequestHandler, directory=str(folder))
    try:
        server = ThreadingHTTPServer(("127.0.0.1", PORT), handler)
    except OSError as exc:
        print(f"Не вдалося запустити локальний сервер на порту {PORT}: {exc}")
        print("Можливо, застосунок уже запущено. Перевірте http://127.0.0.1:8765/")
        return
    url = f"http://127.0.0.1:{PORT}/"
    print("День за днем — планувальник")
    print("Відкрийте", url)
    print("Щоб зупинити сервер, натисніть Ctrl+C або закрийте це вікно.")
    Timer(0.7, lambda: webbrowser.open(url)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()