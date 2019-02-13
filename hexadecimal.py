def clamp(x):
    return max(0,min(x,255))

print('#{0:02x}{1:02x}{2:02x}'.format(clamp(-20),clamp(275),clamp(125)))
