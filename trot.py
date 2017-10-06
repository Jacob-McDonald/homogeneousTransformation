from rotations import *

def trot2(t):
    T = rot2(t)
    T = np.concatenate((T,[0,0]))
    T = np.concatenate((T,np.array([[0,0,1]]).T),axis=1)
    return T

def trotx(t):
    T = rotx(t)
    T = np.concatenate((T,[0,0,0]))
    T = np.concatenate((T,np.array([[0,0,0,1]]).T),axis=1)
    return T

def troty(t):
    T = roty(t)
    T = np.concatenate((T,[0,0,0]))
    T = np.concatenate((T,np.array([[0,0,0,1]]).T),axis=1)
    return T

def trotz(t):
    T = rotz(t)
    T = np.concatenate((T,[0,0,0]))
    T = np.concatenate((T,np.array([[0,0,0,1]]).T),axis=1)
    return T