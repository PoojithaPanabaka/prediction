from sklearn import tree
x=[[6,66,9],[5,50,7],[5.5,50,5],[5,51,6],[6,70,10],[5.7,75,8],[6,80,9]]
y=["male","male","female","female","male","female","male"]
clf=tree.DecisionTreeClassifier()
clf=clf.fit(x,y)
pre=clf.predict([[5.5,60,8]])
print(pre)
