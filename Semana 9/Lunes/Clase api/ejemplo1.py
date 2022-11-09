import requests

def main():
    url = "https://google.com"
    response = requests.get("http://localhost:8000/api/countries/")
    print(response)
    

    if response.status_code == 200:
        content = response.content
        print(content)
        file = open("google.html", "wb")
        file.write(content)
        file.close()


main()