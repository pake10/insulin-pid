# Quickly simulating the PID algorithm for automated insulin delivery.

sg = [120] # Setting an initial BG of 120 mg/dl.
i = 1.6 # Initial basal rate set to 1.6 U/h.

while True:
    current = float(input("Verensokeri: "))
    sg.append(current)
    
    p = 1/135 * (current - 120)
    i += (1/135) / 450 * (current - 120)

    if i > 3: # Limiting the basal delivery.
        i = 3
    elif i < 0:
        i = 0
        
    d = (1/135) * 90 * (sg[-1] - sg[-2])

    pid = p + i + d

    print("PID: {}".format(pid))
