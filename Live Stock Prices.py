
# The program uses Yahoo Finance to fetch live stock market data of Microsoft and Apple stocks. The output produces two animated graphs using Matplotlib FuncAnimation that updates itself automatically showing all the ups and down in the stock prices--live.


from matplotlib.animation import FuncAnimation


import matplotlib.pyplot as plt

import yfinance as yf

import pandas as pd


plt.style.use('ggplot')


# Producing two plots:
              
fig, (ax1, ax2) = plt.subplots(nrows= 2, ncols= 1, sharex= True, constrained_layout= True)
    

# Creating a function for Matplotlib FuncAnimation:
                       
def animate(self):


# Fetching data from Yahoo Finance:
    
    apple_finance_data = yf.download(tickers= 'AAPL',
                                    period= '1d',
                                    interval= '1m',
                                    progress= False)
                                    
    microsoft_finance_data = yf.download(tickers= 'MSFT',
                                    period= '1d',
                                    interval= '1m',
                                    progress= False)
                                    

# Getting closing prices for the two graphs:
                                         
    apple_closing_prices = apple_finance_data['Close']
    
    microsoft_closing_prices = microsoft_finance_data['Close']

    
# PLotting the graphs:
        
    ax1.cla()
    
    ax2.cla()
    
    
    ax1.plot(apple_closing_prices, label= 'Apple', color= 'red')
    
    ax2.plot(microsoft_closing_prices, label= 'Microsoft', color= 'green')
    
        
# Labeling the plots :
    
    ax1.legend(loc= 'lower left', fontsize= 5)
    
    ax2.legend(loc= 'lower left', fontsize= 5)    
    
    
    ax1.set_title('Live Stock Prices :', fontsize = 9, fontweight = 'bold')
    
    ax1.set_ylabel('USD ($) >', fontsize = 7, fontweight= 'bold')
    
    ax2.set_xlabel('Time (Month-Day Hours) >', fontsize = 7, fontweight= 'bold')
    
    ax2.set_ylabel('USD ($) >', fontsize = 7, fontweight= 'bold')
    
    
    ax1.tick_params(axis= 'y', labelsize= 6)
    
    ax2.tick_params(axis= 'x', rotation= 30, labelsize= 6)
    
    ax2.tick_params(axis= 'y', labelsize= 6)


# Animating the plots for live updates:

animation = FuncAnimation(fig, animate, interval= 1000, repeat= False)
        
plt.show()
    
                                                       
''' Created By Sourin Das '''