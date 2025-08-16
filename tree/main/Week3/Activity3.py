import pandas as pd

csvFileName = 'online_shoppers_intention.csv'
parquetFileName = 'data.parquet'

class FileProcessing:
    def __init__(self, path):
        self.path = path

    def covertToParquet(self):
        csv = pd.read_csv(self.path)
        csv.to_parquet(parquetFileName, engine = 'pyarrow', index = False)

    def dataComputing(data):
        df = pd.DataFrame(data)
        for index, row in df.items():
            if data[index].dtypes == 'int64' or data[index].dtypes == 'float64':
                print(f'colomn name: {index}; avg: {data[index].mean()}; max: {data[index].max()}; min: {data[index].min()}')
    
    def readFile(self):
        file = pd.read_parquet(parquetFileName, engine = 'pyarrow')
        return pd.DataFrame(file)

def main():
    file = FileProcessing(csvFileName)
    FileProcessing.covertToParquet(file)
    FileProcessing.dataComputing(FileProcessing.readFile(file))

if __name__ == "__main__":
    main()