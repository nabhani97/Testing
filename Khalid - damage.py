print ("Start")

# what if there were 12 enemies? How would you *model* that?
x_dist = 10
y_dist = 10
z_dist = 10

mx_dist = 20
my_dist = 20
mz_dist = 20


distance = 10 # distance in metres
damage = "";

if distance > 0 and distance <= 10:
        print ("Very near")
        damage = "Dead"
elif distance > 10 and distance < 20:
        print ("Close")
        damage = "Moderate"
else:
        print ("Far away")
        damage = "none"

print("The damage is: %s \nAt distance: %s" % (damage, distance))        # string interpolation
print ("End")