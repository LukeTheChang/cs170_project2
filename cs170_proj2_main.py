import pandas
import numpy
import random
import math
from itertools import islice

#check if dependencies were installed
#print(numpy.__version__)
#print(pandas.__version__)

#stub function for random number
#n = random.randint(0, 9)
#print(n)


#small_df.index+=1
#small_df.index = numpy.arange(1, len(small_df)+1)
#print(small_df)
#print(small_df.size)
#print(len(small_df.index)) #num of rows; same as len(small_df.index))

#functions to get aquainted with pandas dataframe traversal
#print(small_df.tail(5))
#print(small_df.iloc[200][5])
def leave_one_out_cross_valid(data, curr_set, feature_to_add):
    return random.randint(1,10)

def feature_search_demo(data):
    curr_set_of_feat = []
    #i for index val, x for the actual row
    for i, row in data.iterrows():
        #col for actual col val
        #print(type(row))
        #[1:] to ignore class
        print('on the ' + str(i) + 'th level of the search tree')
        feature_to_add_at_lvl =[]
        best_curr_acc = 0

        j = 1
        for col in row[1:]:
#            print(type(col))
            if j not in curr_set_of_feat:
                print('considering adding feature: ' + str(j) + ' = ' + str(col))
                #for some reason ++j doesnt work
                k = j + 1
                accuracy = leave_one_out_cross_valid(small_df, curr_set_of_feat, k)

                if accuracy > best_curr_acc:
                    best_curr_acc = accuracy
                    feature_to_add_at_lvl = k
            
            j+=1 #incr index for print
        curr_set_of_feat.append(feature_to_add_at_lvl)
        #print(curr_set_of_feat)
        print('on level ' + str(i) + ', feature ' + str(feature_to_add_at_lvl) + ' was added to current set')
#            print(f"Index: {i}")
#        print(f"contents:\n{row}\n")
#    for row in small_df.itertuples():
#        print(row.Index + row._1)

def cross_valid(data):
    num_correct_class = 0

    for i, row in data.iterrows():
        obj_to_classify = row[1:]
        #print(obj_to_classify)

        nearest_neighbor_dist = 1000000000.0
        nearest_neighbor_loc = 1000000000.0

        label_obj_to_class = row[0]
        #print(label_obj_to_class)

        for k, subrow in data.iterrows():
            if k != i:
                #print('ask if ' + str(i) + ' is nearest neighbor with ' + str(k))
                #print(subrow)
                distance = math.sqrt(sum((obj_to_classify - subrow[1:]))**2.0)
                #print(distance)

                if (distance - nearest_neighbor_dist) < 0.0000001:
                    nearest_neighbor_dist = distance
                    nearest_neighbor_loc = k
                    #print(data[nearest_neighbor_loc][0])
                    nearest_neighbor_label = data.iloc[nearest_neighbor_loc][0]
                    #print(nearest_neighbor_label)
        print('object ' + str(i) + ' is class: ' + str(label_obj_to_class))
        print('its nearest neighbor is ' + str(nearest_neighbor_loc) + ', which is: ' + str(nearest_neighbor_label))

        if label_obj_to_class == nearest_neighbor_label:
            num_correct_class+=1
        
    accuracy = num_correct_class/len(data.index)
    print('accuracy = ' + str(accuracy))
#the data files are split "__", two blank spaces
small_df = pandas.read_csv('CS170_SMALLtestdata__70.txt', sep = '  ', header = None)

#feature_search_demo(small_df)
cross_valid(small_df)
#print(random.randint(1,10))
