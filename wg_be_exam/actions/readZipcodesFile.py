import pandas as pd
import os


class ReadZipcodesFile:
    @staticmethod
    def handle(filename: str) -> pd.DataFrame:
        csv_file = os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            '../',
            filename)
        df = pd.read_csv(csv_file, sep=',', header=None, index_col=0)

        zipcodes = []
        for index, row in df.iterrows():
            if len(index) > 4:
                a_min = int(str(index).split('-')[0].strip())
                a_max = int(str(index).split('-')[1].strip())
                for zipcode in range(a_min, a_max+1):
                    zipcodes.append([zipcode, row.values[0]])
            else:
                zipcodes.append([int(index), row.values[0]])

        df_zipcodes = pd.DataFrame(zipcodes)
        df_zipcodes.columns = ['zipcode', 'risk_factor']
        df_zipcodes.set_index('zipcode', inplace=True)

        return df_zipcodes
