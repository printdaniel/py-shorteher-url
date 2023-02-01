import pyshorteners

def shorten(url):
    """
    Esta función acorta una URL utilizando el servicio TinyURL.

    Args:
    url (str): La URL a acortar.

    Returns:
    str: La URL acortada o un mensaje de error si hubo un problema.
    """
    shortener = pyshorteners.Shortener()
    try:
        shortened_url = shortener.tinyurl.short(url)
    except Exception as e:
        return f"Error al acortar la URL: {e}"
    return shortened_url

if __name__ == "__main__":
    url = input("Ingrese el link que desea acortar: ")
    shortened = shorten(url)
    print(f"\n{shortened}")
