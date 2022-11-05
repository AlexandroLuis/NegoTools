# Instructions how to use nego thompson-sampling

## start

ts = ThompsonSampling([element1_arm, element2_arm])

## draw a random arm

arm = ts.draw_arm()

## update arm 

result as bool (True or False)
ts.update_arm(result, arm)
