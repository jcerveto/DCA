import gettext
import os
from random import randint

def generar_mensaje():
    mensajes = {
        0: "Si estirem tots ella caurà",
        1: "T'estime, t'estimo, t'estim",
        2: "No hi havia a València dos amants com nosaltres",
        3: "Tinc un cel i un infern",
        4: "Cal la calor a la Safor bombeja el ritme"
    }

    random_index = randint(0, len(mensajes.keys()) - 1)
    return mensajes[random_index]

def configurar_idioma(idioma="ca"):
    current_dir = os.path.dirname(__file__)
    locale_dir = os.path.join(current_dir, "locale")
    try:
        lang = gettext.translation("m", localedir=locale_dir, languages=[idioma])
        lang.install()
        return lang.gettext
    except FileNotFoundError:
        # Si no se encuentra el idioma, usar por defecto
        gettext.install("m", localedir=locale_dir)
        return gettext.gettext

def main():
    idioma = os.getenv("LANG", "ca")[:2]
    t = configurar_idioma(idioma)

    print(t("Benvingut a la nostra aplicació!"))

    data = ''
    while data != 'q':
        data = input(f'{t("Escriu qualsevol cosa per a llegir un vers. Prem [q] per a eixir: ")}')
        print(t(generar_mensaje()))

    print(t('Salut!'))
if __name__ == "__main__":
    main()
