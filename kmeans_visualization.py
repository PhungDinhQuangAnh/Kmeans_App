import pygame
from math import sqrt
from random import randint
from sklearn.cluster import KMeans
def distance(p1,p2):
	return sqrt((p1[0]-p2[0]) * (p1[0]-p2[0]) + (p1[1] - p2[1]) * (p1[1] - p2[1]))
def draw_graphics():
	# Màu
	BG=(47, 49, 54)
	BORDER=(88, 89, 93)
	BLACK=(34, 35, 36)
	GREY=(151, 153, 154)
	WHITE=(191, 194, 199)
	RED=(222, 121, 121)
	BLACK1=(61, 57, 57)
	TEXT_COLOR = (255,255,255)
	GREEN = (114, 219, 130)
	
	# Phông chữ
	FONT = pygame.font.SysFont("Time New Romans",40)
	FONT_SMALL = pygame.font.SysFont("Time New Romans",33)
	FONT_BIG = pygame.font.SysFont("Time New Romans",50)
	FONT_SMALLER = pygame.font.SysFont("Time New Romans",23)

	# Chữ
	PLUS_TEXT = FONT_BIG.render("+",True,TEXT_COLOR)
	MINUS_TEXT = FONT_BIG.render("-",True,TEXT_COLOR)
	RUN_TEXT = FONT_SMALL.render("RUN",True,TEXT_COLOR)
	RANDOM_TEXT = FONT_SMALL.render("RANDOM",True,TEXT_COLOR)
	USE_ALGORITHM_TEXT = FONT_SMALL.render("ALGORITHM",True,TEXT_COLOR)
	RESET_TEXT = FONT.render("RESET",True,TEXT_COLOR)
	NUMBER_POINTS_TEXT = FONT_SMALLER.render("NUMBER OF POINTS",True,TEXT_COLOR)
	ERROR_TEXT = FONT_SMALLER.render("ERROR",True,TEXT_COLOR)
	k_text = FONT_SMALL.render("k = " + str(k),True,GREEN)
	if len(points)>0:
		NUMBER_POINTS_VALUE_TEXT = FONT_SMALL.render(str(len(points)),True,(128, 226, 221))
	else:
		NUMBER_POINTS_VALUE_TEXT = FONT_SMALL.render(str(0),True,(128, 226, 221))
	error_value_text = FONT_SMALL.render(str(int(error)),True,(128, 226, 221))

	# Nền
	screen.fill(BG)

	# Vẽ khung bảng
	pygame.draw.rect(screen,BORDER,(10,10,1280,480))
	pygame.draw.rect(screen,BLACK,(13,13,1274,474))

	# Vẽ nút reset
	pygame.draw.rect(screen,WHITE,(1146,528,104,44))
	pygame.draw.rect(screen,GREY,(1148,530,100,40))
	screen.blit(RESET_TEXT,(1153,537))

	# Vẽ nút thuật toán
	pygame.draw.rect(screen,WHITE,(942,528,154,44))
	pygame.draw.rect(screen,GREY,(944,530,150,40))
	screen.blit(USE_ALGORITHM_TEXT,(949,540))

	# Vẽ bảng
	pygame.draw.rect(screen,RED,(622,498,270,90))
		# NUMBER_POINTS
	pygame.draw.rect(screen,BLACK1,(624,500,170,42))
	screen.blit(NUMBER_POINTS_TEXT,(631,513))
		# ERROR
	pygame.draw.rect(screen,BLACK1,(624,544,170,42))
	screen.blit(ERROR_TEXT,(680,559))
		# NUMBER_POINTS_VALUE
	pygame.draw.rect(screen,BLACK1,(796,500,94,42))
	NUMBER_POINTS_VALUE_POS = NUMBER_POINTS_VALUE_TEXT.get_rect(center=(842,521))
	screen.blit(NUMBER_POINTS_VALUE_TEXT,NUMBER_POINTS_VALUE_POS)
		# ERROR_VALUE
	pygame.draw.rect(screen,BLACK1,(796,544,94,42))
	error_value_pos = error_value_text.get_rect(center=(842,566))
	screen.blit(error_value_text,error_value_pos)

	# Vẽ nút random
	pygame.draw.rect(screen,WHITE,(344,528,114,44))
	pygame.draw.rect(screen,GREY,(346,530,110,40))
	screen.blit(RANDOM_TEXT,(349,540))

	# Vẽ nút run
	pygame.draw.rect(screen,WHITE,(508,528,64,44))
	pygame.draw.rect(screen,GREY,(510,530,60,40))
	screen.blit(RUN_TEXT,(515,540))

	# Vẽ K
		# "+""
	pygame.draw.rect(screen,GREY,(50,528,44,44))
	screen.blit(PLUS_TEXT,(62,529))
		# "-"
	pygame.draw.rect(screen,GREY,(250,528,44,44))
	screen.blit(MINUS_TEXT,(264,531))
		# k_value
	pygame.draw.rect(screen,WHITE,(94,528,156,44))
	pygame.draw.rect(screen,BLACK1,(96,530,152,40))
	screen.blit(k_text,(144,540))

	# Vẽ các điểm
	for i in range(len(points)):
		try:
			pygame.draw.circle(screen,(255,255,255),(points[i][0],points[i][1]),8)
			pygame.draw.circle(screen,COLORS[clusters[i]],(points[i][0],points[i][1]),6)
		except:
			pygame.draw.circle(screen,(255,255,255),(points[i][0],points[i][1]),8)
			pygame.draw.circle(screen,(50,50,50),(points[i][0],points[i][1]),6)

	# Vẽ các nhãn
	for i in range(len(labels)):
		try:
			pygame.draw.circle(screen,COLORS[i],(labels[i][0],labels[i][1]),12)
		except:
			COLORS.append((randint(0,255),randint(0,255),randint(0,255)))

	# Vẽ vị trí chuột
	if 22<mouse_x<1278 and 22<mouse_y<478:
		mouse_text = pygame.font.SysFont("sans",15).render("("+str(mouse_x)+","+str(mouse_y)+")",True,(248, 217, 110))
		screen.blit(mouse_text,(mouse_x+10,mouse_y+10))

pygame.init()

# Khởi tạo
screen = pygame.display.set_mode((1300,600))
caption = pygame.display.set_caption("KMeans Visualization")
FPS = pygame.time.Clock()

# Biến
k,error = 0,0
points = []
labels = []
clusters = []
COLORS = [(125, 218, 88),(93, 226, 231),(250,1,1),(254,153,0),(255, 222, 89),(204, 108, 231)]

running=True
while running:
	mouse_x,mouse_y=pygame.mouse.get_pos()	
	draw_graphics()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			# Thay đổi k
			if 50<mouse_x<94 and 528<mouse_y<572:
				k+=1
			if 250<mouse_x<294 and 528<mouse_y<572:
				if k>0:
					k-=1
				else:
					k=0

			# Tạo các điểm trên khung bảng
			if 22<mouse_x<1278 and 22<mouse_y<478:
				point = [mouse_x,mouse_y]
				points.append(point)

			# Tạo ngẫu nhiên các nhãn
			if 344<mouse_x<458 and 528<mouse_y<572:
				labels = []
				clusters = []
				for i in range(k):
					label = [randint(22,1278),randint(22,478)]
					labels.append(label)

			# Chạy
			if 508<mouse_x<572 and 528<mouse_y<572:
				try:
					if labels != []:
						clusters = []
						x = 0
						error = 0
						for i in range(len(points)):
							minn = float('inf')
							for j in range(len(labels)):
								if minn > distance(points[i],labels[j]):
									minn = distance(points[i],labels[j])
									x = j
							error += minn
							clusters.append(x)
				except:
					continue
				# Di chuyển các nhãn vào các cụm
				for i in range(len(labels)):
					dem = 1
					for j in range(len(clusters)):
						if clusters[j] == i:
							labels[i][0]+=points[j][0]
							labels[i][1]+=points[j][1]
							dem+=1
					labels[i][0]/=dem
					labels[i][1]/=dem
			# Khởi tạo lại
			if 1146<mouse_x<1250 and 528<mouse_y<572:
				k,error = 0,0
				points = []
				labels = []
				clusters = []

			# Thuật toán
			if 942<mouse_x<1096 and 528<mouse_y<572:
				try:
					kmeans = KMeans(n_clusters=k).fit(points)
					labels = kmeans.cluster_centers_
					clusters = kmeans.predict(points)
					error = 0
					for i in range(len(points)):
							minn = float('inf')
							for j in range(len(labels)):
								if minn > distance(points[i],labels[j]):
									minn = distance(points[i],labels[j])
							error += minn
				except:
					pass
				
	pygame.display.flip()
	FPS.tick(30)
pygame.quit()



