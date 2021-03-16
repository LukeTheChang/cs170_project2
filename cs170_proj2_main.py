import pandas
import numpy
import random
from itertools import islice

#check if dependencies were installed
#print(numpy.__version__)
#print(pandas.__version__)

#stub function for random number
#n = random.randint(0, 9)
#print(n)

#the data files are split "__", two blank spaces
small_df = pandas.read_csv('CS170_SMALLtestdata__70.txt', sep = '  ', header = None)
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
    for i, row in small_df.iterrows():
        #col for actual col val
        #print(type(row))
        #[1:] to ignore class
        print('on the ' + str(i) + 'th level of the search tree')
        feature_to_add_at_lvl =[]
        best_curr_acc = 0

        j = 1
        for col in row[1:]:
#            print(type(col))
            print('considering adding feature: ' + str(j) + ' = ' + str(col))
             #for some reason ++j doesnt work
            k = j + 1
            accuracy = leave_one_out_cross_valid(small_df, curr_set_of_feat, k)

            if accuracy > best_curr_acc:
                best_curr_acc = accuracy
                feature_to_add_at_lvl = k
            
            j+=1 #incr index for print
        curr_set_of_feat.append(feature_to_add_at_lvl)
        print('on level ' + str(i) + ', feature ' + str(feature_to_add_at_lvl) + ' was added to current set')
#            print(f"Index: {i}")
#        print(f"contents:\n{row}\n")
#    for row in small_df.itertuples():
#        print(row.Index + row._1)


feature_search_demo(small_df)
#print(random.randint(1,10))
