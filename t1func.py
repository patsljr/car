from vec import Vector, substract, pdiv
import math
## DO NOT HAVE MOVEMENT VECTORS WITH 0 as a component, it will crash this 
def on_road(margin, pos_vec, vlis):
    if(pdiv(pos_vec, vlis[0].unit_vector()).nominal(margin) == True):
        return [True, vlis[0].unit_vector()]
    else:
        for i in range(len(vlis) - 2):
            pos_vec = substract(pos_vec, vlis[i])
            if(pdiv(pos_vec, vlis[i + 1].unit_vector()).nominal(margin) == True):
                if(pdiv(substract(pos_vec, vlis[i + 1]), vlis[i + 2].unit_vector()).nominal(margin)):
                    return [True, vlis[i + 2]]
                return [True, vlis[i + 1]]
        return False


print(on_road(0.5, Vector(3, 7), [Vector(2, 4), Vector(1, 3), Vector(-3, 3)])[1].x,on_road(0.5, Vector(2.5, 5.4), [Vector(2, 4), Vector(1, 3), Vector(-1, 3)])[1].y )







## DO NOT HAVE MOVEMENT VECTORS WITH 0 as a component, it will crash this





##Note for today:
##Don't know what is going to happen if pos-vec is the intersection point of two vector
#This needs to be done to figure out what it's velocity vector should look like in order to turn
#Solution is to test next vector on succesful solution, then we know to use the next one instead
def get_vec_sol(margin, pos_vec, vlis):
    return on_road(margin, pos_vec, vlis)[1].angle()

def get_solution(margin, pos_vec, vlis):
    v = on_road(margin, pos_vec, vlis)
    if(v[0] ==  True):
        return v[1]
    else:
        return substract(v[1], pos_vec)

## return values for motors function
def rvm(goal_vector, current_vector, radi, factor,dv):
    diff = (goal_vector.angle() - current_vector.angle())/(radi)*(math.pi())
    if(-1 * math.pi()/12 < goal_vector.angle() - current_vector.angle() < math.pi()/12):
        return [dv, dv]
    elif(goal_vector.angle() - current_vector.angle() > 0):
        return [factor/diff**2, diff + factor/diff**2]
    else:
        return [diff + factor/diff**2, factor/diff**2]
    

#classic goes as follows 
# m = [0, 0], motor speeds left and right
# current_pos = 0
# course_data = current position (updated by thread 2)
# current_vector = current vector (updated by thread 2) 
# 
# m = rvm(get_solution(margin, current_pos, course_data), current_vector, radi, factor, dv)
#        
    