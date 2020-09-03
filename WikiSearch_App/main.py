import eel
import wikipedia


@eel.expose
def get_info(question):
    answer = wikipedia.summary(question)
    return answer

eel.init("web")

eel.start("index.html", size=(850, 850))