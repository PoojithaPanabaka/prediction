# prediction
To predict whether its male or Female by taking some dataset which contains height,weight,shoe size as labels.

from sklearn import tree
x=[[6,66,9],[5,50,7],[5.5,50,5],[5,51,6],[6,70,10],[5.11,75,8],[5.9,84,7]]
y=["male","male","female","female","male","male","female"]
clf=tree.DecisionTreeClassifier()
clf=clf.fit(x,y)
pre=clf.predict([[5.5,60,8]])
print(pre)
