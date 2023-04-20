#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



# In[3]:


gas = pd.read_csv('gas_prices.csv')
gas


# In[4]:


gas = pd.read_csv('gas_prices.csv')
plt.plot(gas.Year, gas.USA, label="USA")
plt.plot(gas.Year, gas.Canada, label="Canada")
plt.title("USA Gas Prices")
plt.xlabel("Year")
plt.ylabel("Prices in Dollars")

plt.legend()
plt.show()


# In[54]:


gas = pd.read_csv('gas_prices.csv')

plt.figure(figsize=(6,4))
plt.plot(gas.Year, gas.USA, label="USA", color="blue", linestyle="-", marker=".", markersize="8")
plt.plot(gas.Year, gas.Canada, label="Canada", color="red", linestyle="-", marker=".", markersize="8")
plt.plot (gas.Year, gas["South Korea"], label="South Korea", color="green", linestyle="-", marker=".", markersize="8")


plt.xticks(gas.Year[::3])
plt.title("Gas Prices(in USD)")
plt.xlabel("Year")
plt.ylabel("Prices in Dollars")

plt.legend()
plt.show()


# In[101]:


gas = pd.read_csv('gas_prices.csv')

plt.figure(figsize=(6,4))
plt.plot(gas.Year, gas.USA, label="USA", color="blue", linestyle="-", marker=".", markersize="8")
plt.plot(gas.Year, gas.Canada, label="Canada", color="red", linestyle="-", marker=".", markersize="8")
plt.plot (gas.Year, gas["South Korea"], label="South Korea", color="green", linestyle="-", marker=".", markersize="8")
plt.plot (gas.Year, gas.Australia, label="Australia", color="magenta", linestyle="-", marker=".", markersize="8")

plt.xticks(gas.Year[::3])
plt.title("Gas Prices(in USD)", fontweight="bold")
plt.xlabel("Year")
plt.ylabel("Prices (in USD)")

plt.legend()
plt.show()


# In[104]:


gas = pd.read_csv('gas_prices.csv')

plt.figure(figsize=(6,4))
plt.plot(gas.Year, gas.USA, label="USA", color="blue", linestyle="-", marker=".", markersize="8")
plt.plot(gas.Year, gas.Canada, label="Canada", color="red", linestyle="-", marker=".", markersize="8")
plt.plot (gas.Year, gas["South Korea"], label="South Korea", color="green", linestyle="-", marker=".", markersize="8")
plt.plot (gas.Year, gas.Australia, label="Australia", color="magenta", linestyle="-", marker=".", markersize="8")

plt.xticks(gas.Year[::3].tolist()+[2011])
plt.title("Gas Prices(in USD)", fontweight="bold")
plt.xlabel("Year")
plt.ylabel("Prices (in USD)")

plt.legend()
plt.show()


# In[107]:


gas = pd.read_csv('gas_prices.csv')

plt.figure(figsize=(6,4))
plt.plot(gas.Year, gas.USA, label="USA", color="blue", linestyle="-", marker=".", markersize="8")
plt.plot(gas.Year, gas.Canada, label="Canada", color="red", linestyle="-", marker=".", markersize="8")
plt.plot (gas.Year, gas["South Korea"], label="South Korea", color="green", linestyle="-", marker=".", markersize="8")
plt.plot (gas.Year, gas.Australia, label="Australia", color="magenta", linestyle="-", marker=".", markersize="8")

plt.xticks(gas.Year[::3].tolist()+[2011])
plt.title("Gas Prices(in USD)", fontweight="bold")
plt.xlabel("Year")
plt.ylabel("Prices (in USD)")

plt.savefig("Gas_Price_Figure.png", dpi=300)
plt.legend()
plt.show()


# In[111]:


gas = pd.read_csv('gas_prices.csv')

plt.figure(figsize=(6,4))
plt.plot(gas.Year, gas.USA, label="USA", color="blue", linestyle="-", marker=".", markersize="8")
plt.plot(gas.Year, gas.Canada, label="Canada", color="red", linestyle="-", marker=".", markersize="8")
plt.plot (gas.Year, gas["South Korea"], label="South Korea", color="green", linestyle="-", marker=".", markersize="8")
plt.plot (gas.Year, gas.Australia, label="Australia", color="magenta", linestyle="-", marker=".", markersize="8")
plt.plot (gas.Year, gas.Japan, label="Japan", color="black", linestyle="-", marker=".", markersize="8")
plt.xticks(gas.Year[::3].tolist()+[2011])
plt.title("Gas Prices(in USD)", fontweight="bold")
plt.xlabel("Year")
plt.ylabel("Prices (in USD)")

plt.savefig("Gas_Price_Figure.png", dpi=300)
plt.legend()
plt.show()


# In[ ]:




