import numpy as np
import cellname

def sensor(weight):
    # A -> B
    # NEURON['A']['B']
    # FLAG
    #     [S, G]: ['Chemical synapse', 'Gap junction']
    #
    ## SONSOR
    weight['ALML']['PVCL'] = [ 9, 0]
    weight['ALML']['AVDL'] = [ 1, 0]
    weight['ALML']['AVEL'] = [ 1, 0]
    weight['ALML']['AVM']  = [ 0, 2]
    
    weight['AVM']['PVCL']  = [ 9, 0]
    weight['AVM']['AVBL']  = [12, 0]
    weight['AVM']['AVDL']  = [ 0, 2]
    weight['AVM']['ALML']  = [ 0, 2]
    
    weight['PLML']['PVCL'] = [ 2, 2]
    weight['PLML']['AVAL'] = [ 5, 0]
    weight['PLML']['AVDL'] = [ 5, 0]
    weight['PLML']['LUAL'] = [ 0, 2]

    
