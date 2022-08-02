import pandas as pd

carsDataset = {
  'Manufacturer': ["BMW", "Volvo", "Ford"],
  'Model': ["X5 Sport", "XC90 Inscription", "Expedition"],
  'Price': [90.820, 80.900, 50.100],
  'Type': ["SUV", "SUV", "SUV"],
  'Mileage': ["11.24 KM/L",	"16.60 KM/L", "18.60 KM/L"]
}

df = pd.DataFrame(carsDataset)

print(df) 