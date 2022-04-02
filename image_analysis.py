import cv2
import numpy as np
from scipy.stats import kurtosis, skew

class ImageData():

    def __init__(self, image):
        self.image = image
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

    def entropy_fn(self, signal):
        '''
        function returns entropy of a signal
        signal must be a 1-D numpy array
        '''
        lensig=signal.size
        symset=list(set(signal))
        numsym=len(symset)
        propab=[np.size(signal[signal==i])/(1.0*lensig) for i in symset]
        ent=np.sum([p*np.log2(1.0/p) for p in propab])
        
        return ent.round(4)

    def meanStd(self):
        mean, std = cv2.meanStdDev(self.image)
        mean = mean[0][0].round(4)
        std = std[0][0].round(4)

        return(mean, std)

    def skewness(self):
        skewness = skew(self.image, axis=None)

        return(skewness)

    def kurtosis(self):
        curtosis = kurtosis(self.image, axis=None)

        return(curtosis)

    def entropy(self):
        arr = np.array(self.image).ravel()
        entr = self.entropy_fn(arr)

        return(entr)