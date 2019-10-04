import numpy as np

class Meticas:
    
    def mae(self, y_true, y_pred):
        return np.mean(np.absolute(y_true - y_pred))
    
    def mse(self, y_true, y_pred):
        return np.mean((y_true - y_pred) ** 2)

    def rmse(self, y_true, y_pred):
        return np.sqrt(np.mean((y_true - y_pred) ** 2))
    
    def msle(self, y_true, y_pred):
        return np.mean((np.log(y_true + 1) - np.log(y_pred + 1)) ** 2)
   
    def rmsle(self, y_true, y_pred):
        return np.sqrt(np.mean((np.log(y_true + 1) - np.log(y_pred + 1)) ** 2))
    
    def ssr(self, y_true, y_pred):
        return np.sum((_true - y_pred) ** 2)

    def sst(slef, y_true, y_pred):
        return np.sum()

    def r2(self, y_true, y_pred):
        return 1 - (ssr(y_true, y_pred)/sst(y_true, y_pred))