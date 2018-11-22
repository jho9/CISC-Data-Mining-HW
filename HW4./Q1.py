import numpy as np
import pandas as pd
import math
from scipy.io import arff
import matplotlib.pyplot as plt

def get_distances(X_train, indices):
    return (np.linalg.norm(X_train - indices, axis = 1))
def K_means_centroid(list_of_Ks,k, data, X_train):
    start = 0
    stop = k
    list_of_total_acc = []
    for j in range(25):
        #df = pd.DataFrame()
        print("This is j of: ", j, "out of 24")
        print("Start is: ", start)
        print("Stop is:  ", stop)
        counter = 1
        temp = []
        indices = data.iloc[list_of_Ks[start:stop],:].index
        centroid = pd.DataFrame(temp)
        centroid = X_train.iloc[indices]
        prev_centroid = pd.DataFrame(temp)

        #print(centroid)
        while ((prev_centroid.equals(centroid)) == False) and counter < 50:
            list_of_distances = []
            difference_of_start_stop = stop - start
            print("Counter is going through this: ", counter)
            for i in range(difference_of_start_stop):
            #Distnace Function: 
                #get_distances(X_train,centroid.iloc[i])
                list_of_distances.append(get_distances(X_train,centroid.iloc[i]))

            distances_df = pd.DataFrame(list_of_distances).T

            #print(distances_df)

            list_of_labels = []
            #print(distances_df.shape)
            for i in range(distances_df.shape[0]):
                #print(i)
                #print("Checking_idxmin")
                #print(distances_df.iloc[i])
                #print("Checked Iloc")
                #print(distances_df.iloc[i].idxmin())
                list_of_labels.append(distances_df.iloc[i].idxmin())
            #print(list_of_labels)
            distances_df['Label'] = list_of_labels
            #val1 = (distances_df['Label'][distances_df['Label'] == 0]).count()
            #val2 = (distances_df['Label'][distances_df['Label'] == 1]).count()
            #val3 = (distances_df['Label'][distances_df['Label'] == 2]).count()
            #print(val1)
            #print(val2)
            #print(val3)
            #print(val1+val2+val3)

            list_of_new_centroids = []
            for i in range(difference_of_start_stop):
                list_of_new_centroids.append(X_train.iloc[distances_df[distances_df['Label'] == i].index].mean())

            prev_centroid = centroid
            #print(list_of_new_centroids)
            #print(centroid)
            #print(list_of_new_centroids)
            centroid = pd.DataFrame(temp)
            centroid = pd.DataFrame(list_of_new_centroids)
            #print(prev_centroid)
            #print(centroid)
            counter = counter + 1

        #print(centroid)

        #get_distances(df[], centroid)
        list_of_vals =[]
        for i in range(difference_of_start_stop):
            list_of_vals.append(((get_distances(X_train.iloc[distances_df[distances_df['Label'] == i].index], centroid.iloc[i]))**2).sum())

        total =sum(list_of_vals)
        print("This is the individual distance value: ")
        print(total)

        start = start + k
        stop = stop + k
        list_of_total_acc.append(total)
    avg_accur = sum(list_of_total_acc)/len(list_of_total_acc)
    print("This is the avg:")
    print(avg_accur)
    sum_of_acc = 0
    std = 0
    print("This is the std")
    for i in range(len(list_of_total_acc)):
        sum_of_acc = sum_of_acc +(list_of_total_acc[i] - avg_accur)**2
    std = math.sqrt((sum_of_acc)/len(list_of_total_acc))
    print(std)
    return avg_accur, std

list_of_Ks = [775, 1020, 200, 127, 329, 1626, 1515, 651, 658, 328, 1160, 108, 422, 88, 105, 261, 212,
1941, 1724, 704, 1469, 635, 867, 1187, 445, 222, 1283, 1288, 1766, 1168, 566, 1812, 214,
53, 423, 50, 705, 1284, 1356, 996, 1084, 1956, 254, 711, 1997, 1378, 827, 1875, 424,
1790, 633, 208, 1670, 1517, 1902, 1476, 1716, 1709, 264, 1, 371, 758, 332, 542, 672, 483,
65, 92, 400, 1079, 1281, 145, 1410, 664, 155, 166, 1900, 1134, 1462, 954, 1818, 1679,
832, 1627, 1760, 1330, 913, 234, 1635, 1078, 640, 833, 392, 1425, 610, 1353, 1772, 908,
1964, 1260, 784, 520, 1363, 544, 426, 1146, 987, 612, 1685, 1121, 1740, 287, 1383, 1923,
1665, 19, 1239, 251, 309, 245, 384, 1306, 786, 1814, 7, 1203, 1068, 1493, 859, 233, 1846,
1119, 469, 1869, 609, 385, 1182, 1949, 1622, 719, 643, 1692, 1389, 120, 1034, 805, 266,
339, 826, 530, 1173, 802, 1495, 504, 1241, 427, 1555, 1597, 692, 178, 774, 1623, 1641,
661, 1242, 1757, 553, 1377, 1419, 306, 1838, 211, 356, 541, 1455, 741, 583, 1464, 209,
1615, 475, 1903, 555, 1046, 379, 1938, 417, 1747, 342, 1148, 1697, 1785, 298, 1485,
945, 1097, 207, 857, 1758, 1390, 172, 587, 455, 1690, 1277, 345, 1166, 1367, 1858, 1427,
1434, 953, 1992, 1140, 137, 64, 1448, 991, 1312, 1628, 167, 1042, 1887, 1825, 249, 240,
524, 1098, 311, 337, 220, 1913, 727, 1659, 1321, 130, 1904, 561, 1270, 1250, 613, 152,
1440, 473, 1834, 1387, 1656, 1028, 1106, 829, 1591, 1699, 1674, 947, 77, 468, 997, 611,
1776, 123, 979, 1471, 1300, 1007, 1443, 164, 1881, 1935, 280, 442, 1588, 1033, 79, 1686,
854, 257, 1460, 1380, 495, 1701, 1611, 804, 1609, 975, 1181, 582, 816, 1770, 663, 737,
1810, 523, 1243, 944, 1959, 78, 675, 135, 1381, 1472]

def main():
    path = ('segment.arff')
    rawdata = arff.loadarff(path)
    data = pd.DataFrame(rawdata[0])
    X_values = data.iloc[:,:19]
    X_train = (X_values- X_values.mean())/(X_values.std())
    X_train = X_train.dropna(axis = 1)
    list_of_acc = []
    for k in range(1, 13):
        list_of_acc.append(K_means_centroid(list_of_Ks, k, data, X_train))
    results = pd.DataFrame(list_of_acc)
    results.columns = ['Mean', 'std']
    results['+/- Confidence'] = results['std'] * 2
    results['+ Confidence'] = results['Mean'] + results['+/- Confidence']
    results['- Confidence'] = results['Mean'] - results['+/- Confidence']
    results['k'] = range(1,13)
    order = ['k', 'Mean', '- Confidence', '+ Confidence']
    print(results[order])
    #plt.plot(range(1,13), results['Acc'])
    #plt.plot(range(1,13), results['+ Confidence'])
    #plt.plot(range(1,13), results['- Confidence'])

    #plt.errorbar(range(1,13), results['Acc'], yerr=results['+/- Confidence'], fmt='--o')
    #axes = plt.gca()
    #axes.set_ylim([0,80000])
    #plt.errorbar(range(1,13), results['Acc'], yerr=results['+/- Confidence'], fmt='--o')
    #axes = plt.gca()
    #axes.set_ylim([0,60000])

if __name__ == '__main__':
    main()
