import numpy as np
import matplotlib.pyplot as plt

def grad(color_1, color_2, r_squared, max_grad):
	max_grad = max_grad**2
	color_diff = np.subtract(color_1,color_2)
	ratio = r_squared/max_grad
	color_add = ratio*color_diff
	color_add_int = color_add.astype("int16")
	result = np.add(color_2, color_add_int)
	return result
	

class Blade:
	def __init__(self, x, y, ang_pos, ang_vel, ang_size, length):
		self.x_centre = x
		self.y_centre = y
		self.ang_pos  = np.deg2rad(ang_pos)
		self.ang_vel  = np.deg2rad(ang_vel)
		self.ang_size = np.deg2rad(ang_size)
		self.length   = length**2
	
	def rotate(self, time):
		self.ang_pos += self.ang_vel * time
		self.ang_pos = self.ang_pos % (2 * np.pi)
	
	def distance(self, x, y):
		x -= self.x_centre
		y -= self.y_centre
		return (x, y, x**2 + y**2)
	
	def test(self, x, y):
		x, y, r_squared = self.distance(x,y)
		if r_squared > self.length:
			return False
		theta = np.arccos(x/np.sqrt(r_squared))
		if y < 0:
			theta = 2*np.pi - theta
		
		if theta >= self.ang_pos and theta <= (self.ang_pos + self.ang_size) % (2*np.pi):
			return True
		else:
			return False


blade1 = Blade(540,540,  0,30,20,300)
blade2 = Blade(540,540, 90,30,20,300)
blade3 = Blade(540,540,180,30,20,300)
blade4 = Blade(540,540,270,30,20,300)
x_size = 1080
y_size = 1080
image = np.zeros(shape=(x_size, y_size, 3), dtype="uint8")
color_2 = np.array((  0,250,240))
color_1 = np.array((255,  0,  0))

shutter_speed = 0.3

for row in range(0,x_size):
	for col in range(0,y_size):
		if blade1.test(row, col) == True:
		#	image[row][col] = grad(color_1,color_2,blade1.distance(row, col)[2], 300)
		#elif blade2.test(row, col) == True:
			image[row][col] = grad(color_1,color_2,blade1.distance(row, col)[2], 300)
		elif blade3.test(row, col) == True:
			image[row][col] = grad(color_1,color_2,blade1.distance(row, col)[2], 300)
		#elif blade4.test(row, col) == True:
			image[row][col] = grad(color_1,color_2,blade1.distance(row, col)[2], 300)
		else:
			image[row][col] = (255,255,255)
	blade1.rotate(shutter_speed)
	#blade2.rotate(shutter_speed)
	blade3.rotate(shutter_speed)
	#blade4.rotate(shutter_speed)
	
plt.imshow(image)
plt.show()
