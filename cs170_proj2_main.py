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
def cross_valid_demo(data, curr_set, feature_to_add):
    return random.random()

def feature_search_demo(data):
    curr_set_of_feat = []
    list_of_acc = []
    #i for index val, x for the actual row
    data_feat = data.columns[1:].values
    for i in data_feat:
        #col for actual col val
        #print(type(row))
        #[1:] to ignore class
        #print('on the ' + str(i) + 'th level of the search tree')
        feature_to_add_at_lvl = []
        best_curr_acc = 0.0

        
        for j in data_feat:
            #print(col)
            #print(type(j))
            #print('j=' + str(j))
            #k = j
            if int(j) not in curr_set_of_feat:
                print('considering adding feature: ' + str(j))# + ' = ' + str(col))
                #for some reason ++j doesnt work
                #k = j + 1
                #print(j)
                accuracy = cross_valid_demo(small_df, curr_set_of_feat, j)
                #print('ditto ' + str(j))
                if (accuracy - best_curr_acc) > 0.01: #new accuracy is greater than curr
                    best_curr_acc = accuracy
                    #print(type(best_curr_acc))
                    #print(type(accuracy))
                    #print(j)
                    feature_to_add_at_lvl.append(j)
                    print('using feature ' + str(feature_to_add_at_lvl) + ' our new best accuracy is ' + str(best_curr_acc))
                    #print(type(k))
                    #print(type(feature_to_add_at_lvl))
            #print(j)
            #else:
                #print('ditto')
            #j+=1 #incr index for print
        #if(feature_to_add_at_lvl):
        curr_set_of_feat.append(feature_to_add_at_lvl)
        list_of_acc.append(best_curr_acc)
        #print(type(curr_set_of_feat[0]))
        #print(curr_set_of_feat)
        #print('on level ' + str(i) + ', feature ' + str(feature_to_add_at_lvl) + ' was added to current set')
#            print(f"Index: {i}")
#        print(f"contents:\n{row}\n")
#    for row in small_df.itertuples():
#        print(row.Index + row._1)
    #print(curr_set_of_feat)
    print('feature set with largest accuracy is: ' + str(max(list_of_acc)) + ' using feature set ' + str(curr_set_of_feat[list_of_acc.index(max(list_of_acc))]))
    #print('our best set of features are ' + str(curr_set_of_feat) + ' with an accuracy of ' + str(best_curr_acc))
    #print('finished: ' + str(curr_set_of_feat))
#, curr_set, feature_to_add)
def cross_valid(data, curr_set, feature_to_add):
    num_correct_class = 0
    temp_data = data.copy()

    #create a temp list of features to focus on, including the feature at hand
    temp_set = curr_set
    temp_set.append(feature_to_add)
    #print('temp set ' + str(temp_set))
#    for x in range(1,11):
#        if x not in temp_set:
    for col in temp_data.columns[1:]:
        if col not in temp_set:
            temp_data[col].values[:] = 0
    #print(temp_data)

    for i, row in temp_data.iterrows():
        obj_to_classify = row[1:]
        #print(obj_to_classify)

        nearest_neighbor_dist = 1000000000.0
        nearest_neighbor_loc = 1000000000.0

        label_obj_to_class = row[0]
        #print('label='+str(label_obj_to_class))

        for k, subrow in temp_data.iterrows():
            #print('subraow='+str(subrow))
            #make sure we're not comparing a row to itself
            if k != i:
                #print('ask if ' + str(i) + ' is nearest neighbor with ' + str(k))
                #print(subrow)
                distance = math.sqrt(sum((obj_to_classify - subrow[1:]))**2.0)
                #print(distance)

                if (distance - nearest_neighbor_dist) < 0.001:
                    nearest_neighbor_dist = distance
                    nearest_neighbor_loc = k
                    #print(data[nearest_neighbor_loc][0])
                    nearest_neighbor_label = data.iloc[nearest_neighbor_loc][0]
                    #print(nearest_neighbor_label)
        #print('object ' + str(i) + ' is class: ' + str(label_obj_to_class))
        #print('its nearest neighbor is ' + str(nearest_neighbor_loc) + ', which is: ' + str(nearest_neighbor_label))

        if label_obj_to_class == nearest_neighbor_label:
            num_correct_class+=1
        
    accuracy = num_correct_class/len(data.index)
    print('with features ' + str(temp_set) + ', we have an accuracy of ' + str(accuracy))
    return accuracy



#the data files are split "__", two blank spaces
small_df = pandas.read_csv('CS170_SMALLtestdata__70.txt', sep = '  ', header = None)
feature_search_demo(small_df)
#cross_valid(small_df, [1,9], 5)

#temp_arr = [[3,4,5], [1,2]]
#temp_arr2 = [7,8,10]
#temp_arr.append(temp_arr2)
#print(temp_arr)
#temp = pandas.DataFrame(
#    [[1,2,3],
#    [4,5,6],
#    [7,8,9]]
#)

#print(temp)
#temp.loc[0:][0] = 0
#print(temp)
#cross_valid(small_df)
#print(random.randint(1,10))
