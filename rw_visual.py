import matplotlib.pyplot as plt
from random_walk import RandomWalk

# 랜덤 워크를 생성합니다
while True:
    rw = RandomWalk(50_000)
    rw.fill_walk()

    plt.style.use('classic')
    # fig, ax = plt.subplots() 
    # fig, ax = plt.subplots(figsize=(15,9)) #크기 조정해 화면 채우기 
    fig, ax = plt.subplots(figsize=(10,6),dpi=128) #크기 조정해 화면 채우기
    point_numbers = range(rw.num_points) # # 너무크다 화면이 ㄷㄷ 

    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none',s=1)
    #ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,edgecolors='none',s=15)
    #ax.scatter(rw.x_values, rw.y_values, s=15)
    ax.set_aspect('equal')

    #시작점과 끝점을 강조합니다.
    ax.scatter(0,0,c='green', edgecolors='none',s=100)
    ax.scatter(rw.x_values[-1],rw.y_values[-1], c='red', edgecolors='none',s=100)

    # 축을 제거합니다
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    #시각화를 하다보면 이런식으로 메서드체인을 만들어 설정하는 경우도 자주있다네.

    #plt.show()
    
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break

    plt.show()  # 창을 닫고 다른걸 보고싶을떄 y를 누르면 새거 나오게 show를 내림