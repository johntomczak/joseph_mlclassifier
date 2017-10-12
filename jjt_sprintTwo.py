import csv
import numpy as np
import scipy.stats
from sklearn.linear_model import SGDClassifier
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

i = 0
ust = []
cpi = []
unemp = []
suggest = []
data = []

#import data
with open( 'sprint2_data_x.csv') as fl:
        rdr = csv.reader( fl, dialect=csv.excel_tab, delimiter = ',' )
        # rdr = csv.reader( fl, delimiter = ',' )
        for row in rdr:
            if( i != 0 ):
                ust.append( row[1] )
                cpi.append( row[2] )
                unemp.append( row[3] )
                suggest.append( row[4] )
                i = 1
            else:
                i = 1

# remove #N/A values
i = 0
# print( "initial", len( ust ), len(unemp) )
while i < len( ust ):
    # print( ust[i] )
    if suggest[i] == "N/A" or ust[i] == "#N/A":
        del ust[i]
        del unemp[i]
        del cpi[i]
        del suggest[i]

    i += 1

del ust[len(ust)-1]
del unemp[len(unemp)-1]
del cpi[len(ust)-1]
del suggest[len(unemp)-1]

# print( "now", len( ust ), len(unemp) )

for i in range( 0, len(ust) ):
    data.append( [ ust[i], unemp[i], cpi[i] ] )

# print suggest

data_np = np.array( data )
# suggest_np = np.array( suggest )
suggest = map( int, suggest )

x_train, x_test, y_train, y_test = data_np[:11000], data_np[11000:], suggest[:11000], suggest[11000:]
sgd_clf = SGDClassifier( random_state=42 )
sgd_clf.fit( x_train, y_train )

print "\nHello, World"

print data[0]
# sgd_clf.predict(  [np.array['4.06', '5.8', '30.04']] )

from sklearn.model_selection import cross_val_score
cross_val_score(sgd_clf, x_train, y_train, cv=3, scoring="accuracy")

fl.close()
