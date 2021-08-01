import math

def windmill(pts):
    pvt = (0,0) #intial Pivot
    La = math.tan(math.radians(90)) #Line's Intial Angle Of Rotation.
    minA = math.radians(361)
    pas = False
    count=0
    potPvt = []
    comAngle = 0
    prevpvt = ()
    while(comAngle <= math.radians(360)):
        for pt in pts:
            if(pvt == pt or (pt == prevpvt and len(pts) > 2)):
                pas = True
                continue
            radius = math.sqrt( (pvt[0]-pt[0])**2 + (pvt[1]-pt[1])**2 ) 
            if(comAngle == math.radians(0) or comAngle == math.pi):
                A = 1
                B = -2*pvt[1]
                C = (pvt[1]**2)-(radius**2) 
                intrY1 = -(B/(2*A)) + math.sqrt(B**2 - 4*A*C)/(2*A)
                intrY2 = -(B/(2*A)) - math.sqrt(B**2 - 4*A*C)/(2*A)

                intrX1 = ((intrY1 - pvt[1])/La) + pvt[0]
                intrX2 = ((intrY2 - pvt[1])/La) + pvt[0]

            else:
                A = La**2 + 1
                B = -2*(pvt[0]+(La**2)*pvt[0])
                C = (pvt[0]**2) + (pvt[0]**2)*(La**2) - (radius**2)
                
                intrX1 = -(B/(2*A)) + math.sqrt(B**2 - 4*A*C)/(2*A)
                intrX2 = -(B/(2*A)) - math.sqrt(B**2 - 4*A*C)/(2*A)

                intrY1 = La*(intrX1-pvt[0]) + pvt[1]
                intrY2 = La*(intrX2-pvt[0]) + pvt[1]
            
            angle1 = math.atan2(intrY1-pvt[1],intrX1-pvt[0])-math.atan2(pt[1]-pvt[1],pt[0]-pvt[0])
            if(angle1 > math.pi):
                angle1 -= 2*math.pi
            elif(angle1 <= -math.pi):
                angle1 += 2*math.pi
            
            angle2 = math.atan2(intrY2-pvt[1],intrX2-pvt[0])-math.atan2(pt[1]-pvt[1],pt[0]-pvt[0])
            if(angle2 > math.pi):
                angle2 -= 2*math.pi
            elif(angle2 <= -math.pi):
                angle2 += 2*math.pi
            
            if(angle1 > 0):
                angle = abs(angle1)
            else:
                angle = abs(angle2)
            
            if(angle < minA):
                minA = angle
                potPvt = pt
        
        
        if(~pas):
            if(comAngle+minA < math.pi*2):
                count+=1
                comAngle += (minA+0.001)
                La = math.tan((math.pi/2)-comAngle)
                prevpvt = pvt
                pvt = potPvt
                minA = math.radians(361)
                pas = False
            else:
                break
    return count
