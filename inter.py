import numpy as np
import cellname

    
def intor(weight):
    # A -> B
    # NEURON['A']['B']
    # FLAG
    #     [S, G]: ['Chemical synapse', 'Gap junction']
    #
    ## INTOR
    weight['PVCL']['VB1']  = [19, 3]
    weight['PVCL']['DB1']  = [29, 0]
    weight['PVCL']['VA1']  = [ 0, 3]
    weight['PVCL']['DA1']  = [ 4, 0]
    weight['PVCL']['AS1']  = [ 2, 0]
    weight['PVCL']['AVAL'] = [20,10]
    weight['PVCL']['AVBL'] = [31, 0]
    weight['PVCL']['AVDL'] = [13, 0]
    weight['PVCL']['AVEL'] = [ 5, 0]
    weight['PVCL']['LUAL'] = [ 1, 0]
    
    weight['AVAL']['VA1']  = [84,62]
    weight['AVAL']['DB1']  = [10, 5]
    weight['AVAL']['DA1']  = [83,40]
    weight['AVAL']['PVCL'] = [28,10]
    weight['AVAL']['AVBL'] = [ 2, 0]
    weight['AVAL']['AVDL'] = [ 4, 0]
    weight['AVAL']['AVEL'] = [ 4, 0]
    weight['AVAL']['LUAL'] = [ 5, 0]

    weight['AVBL']['VB1']  = [ 1,39]
    weight['AVBL']['DB1']  = [ 0,16]
    weight['AVBL']['VA1']  = [ 5, 2]
    weight['AVBL']['DA1']  = [ 1, 0]
    weight['AVBL']['AS1']  = [13, 5]
    weight['AVBL']['AVAL'] = [27, 0]
    weight['AVBL']['AVDL'] = [ 3, 0]
    weight['AVBL']['AVEL'] = [ 3, 0]

    weight['AVDL']['DB1']  = [ 1, 0]
    weight['AVDL']['VA1']  = [ 7, 0]
    weight['AVDL']['DA1']  = [21, 0]
    weight['AVDL']['AS1']  = [ 8, 0]
    weight['AVDL']['PVCL'] = [ 1, 0]
    weight['AVDL']['AVAL'] = [63, 0]
    weight['AVDL']['AVBL'] = [ 1, 0]
    weight['AVDL']['LUAL'] = [ 3, 0]

    weight['LUAL']['PVCL'] = [ 3, 0]
    weight['LUAL']['AVAL'] = [21, 1]
    weight['LUAL']['AVDL'] = [10, 0]

    weight['AVEL']['DB1']  = [ 1, 0]
    weight['AVEL']['VA1']  = [14, 0]
    weight['AVEL']['DA1']  = [19, 0]
    weight['AVEL']['AS1']  = [ 7, 0]
    weight['AVEL']['PVCL'] = [ 1, 0]
    weight['AVEL']['AVAL'] = [42, 0]
    weight['AVEL']['AVDL'] = [ 1, 0]

