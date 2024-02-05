import matplotlib.pyplot as plt

# x_values = [1,2,3,4,5]
x_values = range(1,1001) #

# y_values = [1,4,9,16,25]
y_values = [x**2 for x in x_values]

plt.style.use('seaborn-v0_8')#
fig, ax = plt.subplots()
# ax.scatter(x_values,y_values,s=10)
ax.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues, s=10)

#그래프 타이틀을 지정하고 축에 이름표를 붙입니다.
ax.set_title("Square Numbers", fontsize=24) #
ax.set_xlabel("Value", fontsize =14)
ax.set_ylabel("Square of Value", fontsize=14)

# 틱 이름표 크기를 지정합니다.
ax.tick_params(labelsize=14)
ax.axis([ 0,1100,0,1_100_000 ]) #
ax.ticklabel_format(style='plain')

plt.savefig('squares_plot.png',bbox_inches='tight')
#이미지로 저장

plt.show() #현재까지의 그림을 보여주고 내부 그림 버퍼를 클리어함
