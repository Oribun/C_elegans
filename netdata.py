import numpy as np
import cellname

def set_neural:
    # NEURON[presynaps][postsynaps]
    net_size = len(SENSOR) + len(INTER) + len(MOTOR)
    matrix_weight =  np.array([[[0, 0] for i in range(net_size)]
                              for j in range(net_size)])
    
    matrix_weight = sensor(matrix_weight)
    matrix_weight = intor(matrix_weight)
