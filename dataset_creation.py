from scipy.stats.stats import skew
from image_analysis import ImageData
import cv2
import os

def get_image_info(path):

    img = cv2.imread(path)
    img_data = ImageData(img)
    mean, std = img_data.meanStd()
    skewness = img_data.skewness()
    kurtosis = img_data.kurtosis()
    entropy = img_data.entropy()

    return([mean, std, skewness, kurtosis, entropy])

def make_csv():
    
    file_name = open('apple_orange_dataset.csv', 'a')

    for each_class in os.listdir('dataset'):

        if each_class == '.DS_Store':
            continue

        else:
            for each_img in os.listdir(os.path.join('dataset', each_class)):
                if each_img == '.DS_Store':
                    continue

                else:
                    lt = get_image_info(os.path.join('dataset', each_class, each_img))
                    
                    file_name.write(each_img)
                    file_name.write(',')

                    for i in lt:
                        file_name.write(str(i))
                        file_name.write(',')

                    file_name.write(each_class)
                    file_name.write('\n')

    file_name.close()
    print('Dataset Created')

if __name__ == '__main__':
    make_csv()