from base import BaseAlgo

class HelloWorld(BaseAlgo):
    def __init__(self, options):
        pass

    def fit(self, df, options):
        df['message'] = "Hello World!"
        return df
