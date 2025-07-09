from app import app
import webbrowser
from threading import Timer


def open_browser():
    webbrowser.open_new_tab("http://127.0.0.1:5001")

if __name__ == "__main__":
    Timer(1, open_browser).start()
    app.run(host="0.0.0.0", port=5001, debug=True)
