import datetime
import yfinance as yf
#functions from the yfinance doc
def getStock(stkInput, dayInput):
    dt = datetime.date.today()
    dtPast = dt + datetime.timedelta(days=-dayInput)
    # Call Yahoo finance to get stock data for the stock provided.
    dfStock = yf.download(stkInput, start=dtPast, end=dt)
    return dfStock

def removeTime(df):
    newDateList=[]
    dateList = list(df.index.values)
    # print(dateList)
    for i in range(0, len(dateList)):
        dateStr=str(dateList[i])
        itemList=dateStr.split("T")
        # print(itemList)
        newDateList.append(itemList[0])
    df["Date"] = newDateList
    df.set_index("Date", inplace=True)
    return df


while True:
    print('-' * 45)
    print('Stock Report Menu Options'.center(45))
    print('-' * 45)
    menu = input('1. Report changes for a stock \n2. Quit \n')
    if int(menu) == 2:
        print('Bye')
        break
    else:

        stockSymbol = input('Please enter the stock symbol: ')
        numDays = input('Please enter the number of the days for the analysis: ')
        try: #try and except in case the stock symbol is not founded the system still iterate
            df = getStock(stockSymbol.upper(),int(numDays))
            # print("Original Data\n", df)
            # print(df)
            df.columns = df.columns.droplevel(1)
            df.columns.name = None
            # print(f"Other\n {df}")
            # print("Cleaned Data\n")
            df = removeTime(df).reset_index()
            df = df[['Date', 'Close', 'Volume']]
            print('*' * 60)
            print(
                f'Daily Percent Changes - {df['Date'][0]} to {df['Date'][(len(df['Date'])) - 1]} *{stockSymbol.upper()}*'.center(
                    60))
            print('*' * 60)
            close_list = list(df['Close'])
            volume_list = list(df['Volume'])
            # calculating overall percentage change
            close_change = []
            for i in range(len(close_list)):
                if i == 0:  # first value in the list always start with 0.000
                    result = round(0.0000, 4)
                    close_change.append(result)
                else:
                    result = round((close_list[i] - close_list[i - 1]) / close_list[i - 1], 4)
                    close_change.append(result)  # adding to close_change list
            # print(close_change)
            # calculating volume % change
            volume_change = []
            for i in range(len(volume_list)):
                if i == 0:  # first value in the list always start with 0.000
                    result = round(0.0000, 4)
                    volume_change.append(result)  # adding to volume_change list
                else:
                    result = round((volume_list[i] - volume_list[i - 1]) / volume_list[i - 1], 4)
                    volume_change.append(result)
            df['Volume % Change'] = volume_change  # add list with calculations as a column in the dataframe
            df['Close % Change'] = close_change  # add list with calculations as a column in the dataframe
            print(df.to_string(index=False))
            print('-' * 60)
            print(f'Summary of cumulative changes for {stockSymbol.upper()}')
            print('-' * 60)
            print(f'{df['Date'][0]} to {df['Date'][(len(df['Date']) - 1)]}')
            volume_result = (volume_list[len(volume_list) - 1] - volume_list[0]) / volume_list[
                0]  # save result in variable to rounded
            print(f'% Volume Change: {round(volume_result, 4)}')
            close_result = (close_list[len(close_list) - 1] - close_list[0]) / close_list[
                0]  # save result in variable to rounded
            print(f'% Close Price Change: {round(close_result, 4)}')
        except:
            print("Stock Symbol was not founded")
