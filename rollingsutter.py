import numpy as np

class Blade:
	def __init__(self, x, y, ang_pos, ang_vel, ang_size, length):
		self.x_centre = x
		self.y_centre = y
		self.ang_pos  = np.deg2rad(ang_pos)
		self.ang_vel  = np.deg2rad(ang_vel)
		self.ang_size = np.deg2rad(ang_size)
		self.length   = length**2
	
	def rotate(time):
		self.ang_pos += ang_vel * time
		self.ang_pos = ang_pos % (2 * np.py)
	
	def test(x, y):
		x -= x_centre
		y -= y_centre
		r_squared = x**2 + y**2
		if r_squared > self.length:
			return False
		theta = np.arctan(x/y)
		if theta > ang_pos and theta < ang_pos + ang_size:
			return True
		else:
			return False
	
