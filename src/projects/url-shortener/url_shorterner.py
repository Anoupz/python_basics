from typing import Final
import requests

API_KEY: Final[str] = "6ee2380ec32a0c2de6b9d425784a18437a127"
BASE_URL: Final[str] = "https://cutt.ly/api/api.php"


def shorten_link(full_link: str):
    payload: dict = {"key": API_KEY, "short": full_link}
    request = requests.get(BASE_URL, params=payload)
    data: dict = request.json()

    if url_data := data.get("url"):
        if url_data["status"] == 7:
            short_link: str = url_data["shortLink"]
            print("Link shortened successfully:", short_link)
        else:
            print("Error:", url_data["status"])


def main():
    full_link: str = input("Enter the link to shorten: ")
    shorten_link(full_link)


if __name__ == "__main__":
    main()
