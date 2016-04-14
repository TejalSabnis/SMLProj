__author__ = 'Tejal'

from sklearn import cross_validation
from sklearn import metrics
from sklearn.naive_bayes import GaussianNB

def fun():
    print "hello tejal"

if __name__ == '__main__':

    data = []
    target = []

    f = open("C:\\Users\\Tejal\\Documents\\ASU\\2_Spring 2016\\CSE 572 Data Mining\\Project\\Scikit\\train_data(1).txt",'r')
    for line in f:
        linestrlist = line.strip().split(',')
        linenumlist = []
        for str in linestrlist:
            if '.' in str:
                linenumlist.append(float(str))
            else:
                linenumlist.append(int(str))
        data.append(linenumlist)
    f.close()

    f = open("C:\\Users\\Tejal\\Documents\\ASU\\2_Spring 2016\\CSE 572 Data Mining\\Project\\Scikit\\train_label(1).txt",'r')
    for line in f:
        target.append(int(line.strip()))
    f.close()

    #print data
    #print target

    # fit a SVM model to the data
    model = GaussianNB()
    #model.fit(data, target)
    print(model)
    # make predictions
    #expected = target
    #predicted = model.predict(data)

    # X_train, X_test, y_train, y_test = cross_validation.train_test_split(data, target, test_size=0.1, random_state=0)
    # clf = model.fit(X_train, y_train)
    # print clf.score(X_test, y_test)

    cv = cross_validation.ShuffleSplit(920, n_iter=10, test_size=0.1, random_state=0)

    scores = cross_validation.cross_val_score(model, data, target, cv=cv)
    print scores
    print scores.mean()
    # summarize the fit of the model
    #print(metrics.classification_report(expected, predicted))
    #print(metrics.confusion_matrix(expected, predicted))