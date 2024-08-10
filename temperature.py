import requests
API_KEY = "8217898de424e5676fea3cd78406563e"  #Replace with your openweaterMap Api Key
CITY = str(input("Enter the City Name: "))
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}"

response = requests.get(URL)
data = response.json()
if data["cod"] == 200:
    main = data["main"]
    temperature = main["temp"]
    print(f"Current Temperature in {CITY}: {temperature}°C")
else:
    print("Error in the HTTP request")

