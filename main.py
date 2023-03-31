import requests
import sys

ip = "51.83.180.219"

def text_to_tokens(text):
    text = text.replace("maxq1hash", "#")
    text = text.replace("maxq1procent", "%")
    text = text.replace("maxq1ampersand", "&")
    text = text.replace("maxq1plus", "+")
    text = text.replace("maxq1equal", "=")
    text = text.replace("maxq1quest", "?")
    text = text.replace("maxq1space", " ")
    text = text.replace("maxq1tab", "\t")
    text = text.replace("maxq1newline", "\n")
    text = text.replace("maxq1left", "<")
    text = text.replace("maxq1right", ">")
    text = removeAccents(text)
    return text

def tokens_to_text(text):
    text = text.replace("#", "maxq1hash")
    text = text.replace("%", "maxq1procent")
    text = text.replace("&", "maxq1ampersand")
    text = text.replace("+", "maxq1plus")
    text = text.replace("=", "maxq1equal")
    text = text.replace("?", "maxq1quest")
    text = text.replace(" ", "maxq1space")
    text = text.replace("\t", "maxq1tab")
    text = text.replace("\n", "maxq1newline")
    text = text.replace("<", "maxq1left")
    text = text.replace(">", "maxq1right")
    text = removeAccents(text)
    return text

def ask(code):
    code = text_to_tokens(code)
    response = requests.get(f"http://{ip}:3567/karix/?text={code}&new_tokens=100")
    return tokens_to_text(responce.txt)

if __name__ == "__main__":
    ask(sys.argv[1])
