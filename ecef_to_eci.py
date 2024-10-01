# ecef_to_eci.py
#
# Usage: python3 ecef_to_eci.py year month day hour minute second ecef_x_km ecef_y_km ecef_z_km
# _o represents the ECEF origin of SEZ frame and the others are the ecef position
# Converts ECEF vector components to SEZ
#  See "Fundamentals of Astrodynamics and Applications, Fourth Edition" by
#  David A. Vallado, pages 172-173
# Parameters:
# year
# month
# day
# hour
# minute
# second
# ecef_x_km: x-component of ECI vector in km
# ecef_y_km: y-component of ECI vector in km
# ecef_z_km: z-component of ECI vector in km

# Output:
#  Prints ecef components x,y,z in km
#
# Written by Isha Aurora
# Other contributors: None
#
# This work is licensed under CC BY-SA 4.0

# import Python modules
import math # math module
import sys  # argv

# "constants"
w=7.292115*10**-5
# helper functions

## calculated denominator

# initialize script arguments
year = float('nan')  
mon = float('nan')  
day = float('nan')  
hour = float('nan')
min = float('nan')
sec = float('nan')
ecef_x_km = float('nan')  
ecef_y_km = float('nan')  
ecef_z_km = float('nan')  

# parse script arguments (always 1 more than the number of arguments)
if len(sys.argv) == 10:
    try:
        year = float(sys.argv[1])
        mon = float(sys.argv[2])
        day = float(sys.argv[3])
        hour = float(sys.argv[4])
        min = float(sys.argv[5])
        sec = float(sys.argv[6])
        ecef_x_km = float(sys.argv[7])
        ecef_y_km = float(sys.argv[8])
        ecef_z_km = float(sys.argv[9])

    except ValueError:
        print("Error: year month day hour minute second ecef_x_km ecef_y_km, and ecef_z_km must be numeric.")
        exit()
else:
    print(\
        'python3 eci_to_ecef.py year month day hour minute second ecef_x_km ecef_y_km ecef_z_km'\
            )
    exit()

# write script below this line

#fractional julian date

jd =  math.floor(day - 32075 + 1461* (year+4800+(mon-14)/12)/4 +367*(mon-2-(mon-14)/12*12)/12 -3*((year+4900+(mon-14)/12)/100)/4)
jd_midnight = jd - 0.5
dfrac = (sec+60*(min+60*hour))/86400
jdfrac = jd_midnight+dfrac
T_ut1 = (jdfrac-2451545)/36525
theta_GMST = 67310.54841 +(876600*60*60+8640184.812866)*T_ut1+0.093104*(T_ut1**2)-6.2*(10**-6)*(T_ut1**3)
rad_GMST = math.fmod(theta_GMST%86400*w+2*math.pi,2*math.pi)

#to ecef
eci_x_km = ecef_x_km*math.cos(-rad_GMST) + ecef_y_km*math.sin(-rad_GMST)
eci_y_km = -ecef_x_km*math.sin(-rad_GMST) + ecef_y_km*math.cos(-rad_GMST)
eci_z_km = ecef_z_km

print(eci_x_km)
print(eci_y_km)
print(eci_z_km)