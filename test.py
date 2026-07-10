import numpy as np
b = 20
s = 16.5
a = 4
slotted_level_max_length = np.sqrt(a**2 - ((b-s)/2)**2)

print("Slotted Level Max Length:", slotted_level_max_length)


cos_theta = (b**2+(s+a)**2-a**2)/(2*b*(s+a))
slotted_level_min_length=np.sqrt((b/2)**2 + ((s/2)+a)**2 - 2*(b/2)*((s/2)+a)*cos_theta)
print("Slotted Level Min Length:", slotted_level_min_length)


max_steering_angle = ( np.arccos(((b/2)**2+slotted_level_min_length**2-((s/2)+a)**2)/(2*(b/2)*slotted_level_min_length)))*180/np.pi -90
print("Max Steering Angle:", max_steering_angle)

vehicle_length=(a*b)/(b-s)
print("Vehicle Length:", vehicle_length)   


w_s_angle_acute= np.arccos((b-s)/(2*a))*180/np.pi
print("W-S Angle Acute:", w_s_angle_acute)
w_s_angle= 180-w_s_angle_acute
print("W-S Angle:",w_s_angle)



theta=np.arccos(cos_theta)*180/np.pi
print("Theta:", theta)
range_in =w_s_angle_acute-theta
print("R-in:", range_in)

alpha = np.arccos((b**2-(s+a)**2+a**2)/(2*b*a))*180/np.pi
print("Alpha:", alpha)
range_out = alpha - w_s_angle_acute
print("R-out:", range_out)



r_out_horizontal= (vehicle_length/np.tan(np.radians(range_out)))-b/2
print("R-out Horizontal L-F:", r_out_horizontal)




r_in_horizontal= (vehicle_length/np.tan(np.radians(range_in)))+b/2
print("R-in Horizontal L-F:", r_in_horizontal)

print("Avg", (r_out_horizontal+r_in_horizontal)/2)

difference= r_out_horizontal-r_in_horizontal
print("Difference:", difference)
print("Percentage difference:", difference*100/b)

# A=91.522*np.pi/180
# L=(s**2) -2*(a**2)-(b**2) + 2*b*a*np.cos(A)

# M=2*(a**2)*np.cos(A)-2*b*a

# N=2*(a**2)*np.sin(A)

# C = np.acos(L/((M**2)+(N**2))**(0.5))-np.acos(M/((M**2)+(N**2))**(0.5))
# print("C:", C*180/np.pi)


