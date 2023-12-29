class Moving_Average:

    def __init__(self, slot, df):
        self.slot = slot
        self.df = df

    def calculate(self):
        try:
            self.df['moving_average_{}'.format(self.slot)] = self.df['close'].rolling(window=int(self.slot),
                                                                                      min_periods=1).mean()
            return self.df

        except Exception as e:
            print(str(e) + 'has occurred')
            return

class Stochastic:

    def __init__(self, df):
        self.df = df

    def calculate(self):
        try:
            self.df['%K'] = (self.df['close'] - self.df['low'].rolling(window=14).min()) / (
                    self.df['high'].rolling(window=14).max() - self.df['low'].rolling(window=14).min()) * 100

            self.df['%D'] = self.df['%K'].rolling(window=3).mean()

            self.df.dropna(inplace=True)
            self.df.fillna(value=0, inplace=True)

            return self.df

        except Exception as e:
            print(str(e) + ' has occurred')
            return
