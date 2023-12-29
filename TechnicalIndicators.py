class Moving_Average:

    def __init__(self, slot, df):
        self.slot = slot  # El periodo de la media móvil
        self.df = df  # DataFrame con los datos de precios

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
            # Calcular %K
            self.df['%K'] = (self.df['close'] - self.df['low'].rolling(window=14).min()) / (
                    self.df['high'].rolling(window=14).max() - self.df['low'].rolling(window=14).min()) * 100

            # Calcular %D (media móvil de %K)
            self.df['%D'] = self.df['%K'].rolling(window=3).mean()

            # Eliminar filas con valores NaN generados por las ventanas de las medias móviles
            self.df.dropna(inplace=True)
            self.df.fillna(value=0, inplace=True)

            return self.df

        except Exception as e:
            print(str(e) + ' has occurred')
            return
