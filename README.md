# pandas L&L
Introduction to Pandas

Reference book: https://pandas.pydata.org/docs/pandas.pdf


**1. Recommended Python IDE:**

- https://www.jetbrains.com/pycharm/download/
- https://code.visualstudio.com/download


**2. Python and Pandas Installation:**

```console
$ python --version
$ brew install python3

$ pip install pandas

$ pip list
$ pip list | grep pandas
$ pip show pandas
```

### 3. Let's code!!

```python
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
```
