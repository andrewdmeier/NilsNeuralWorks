# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 08:21:27 2018

@author: NILSMUE
"""

import numpy as np


class Norm():       
    def minmax(X, rescale=False, raw=[0], axis=1):
        ''' Scales Data in Range between 0 and 1. Input can be a single- 
        or multidimenional np.array
        
        Keyword arguments:
            X       -- Input 1D or nD Array
            rescale -- False: scale, True: rescale
            raw     -- Raw Data (only for rescaling)
            axis    -- 0=row, 1=column, 2=all'''
            
        if not rescale:
            if len(X.shape) == 1:                            # check if 1D array
                return (X - np.min(X)) / (np.max(X) - np.min(X))
            elif len(X.shape) > 1:                          # check if nD array
                normed = np.zeros(X.shape)
                                                                
                if axis == 0:                                       
                    for i in range(0, X.shape[0]):
                        for j in range(0, X.shape[1]):
                            normed[i,j] = (X[i,j] - np.min(X[i,:])) / (np.max(X[i,:]) - np.min(X[i,:]))                                                            
                
                elif axis == 1:                                       
                    for i in range(0, X.shape[0]):
                        for j in range(0, X.shape[1]):
                            normed[i,j] = (X[i,j] - np.min(X[:,j])) / (np.max(X[:,j]) - np.min(X[:,j]))
                                           
                elif axis == 2:                                     
                    for i in range(0, X.shape[0]):
                        for j in range(0, X.shape[1]):
                            normed[i,j] = (X[i,j] - np.min(X)) / (np.max(X) - np.min(X))
                assert axis >= 0 and axis <= 2, '\naxis values should be:\n0 - for row\n1 - for column\n2 - for row and column'
                return normed
            else:
                print('DataType not understood! keep thinkin...')     
            
            
        if rescale == True:
            if len(X.shape) == 1:
                return X * (np.max(raw)-np.min(raw)) + np.min(raw)
            elif len(X.shape) > 1:
                denormed = np.zeros(X.shape)
                
                if axis == 0:
                    for i in range(0, X.shape[0]):
                        for j in range(0, X.shape[1]):
                            denormed[i,j] = X[i,j] * (np.max(raw[i,:])-np.min(raw[i,:])) + np.min(raw[i,:])
                        
                elif axis == 1:
                    for i in range(0, X.shape[0]):
                        for j in range(0, X.shape[1]):
                            denormed[i,j] = X[i,j] * (np.max(raw[:,j])-np.min(raw[:,j])) + np.min(raw[:,j])
                    
                elif axis == 2:        
                    for i in range(0, X.shape[0]):
                        for j in range(0, X.shape[1]):
                            denormed[i,j] = X[i,j] * (np.max(raw)-np.min(raw)) + np.min(raw)
                assert axis >= 0 and axis <= 2, '\naxis values should be:\n0 - for row\n1 - for column\n2 - for row and column'
                return denormed
            else:
                print('DataType not understood! keep thinkin...')
            
            
       
         
    def standardization(X, rescale=False, raw=[0], axis=1):
        ''' Mean is set as 0, wheras 1 represents the Standard Deviation of the
        Input Array. Input can be a single- or multidimenional np.array
        
        Keyword arguments:
            X       -- Input 1D or nD Array
            rescale -- False: scale, True: rescale
            raw     -- Raw Data (only for rescaling)
            axis    -- 0=row, 1=column, 2=all'''
            
        if not rescale:
            if len(X.shape) == 1:                            # check if 1D array
                return (X - np.mean(X)) / np.std(X)
            
            elif len(X.shape) > 1:                          # check if nD array
                normed = np.zeros(X.shape)
                
                if axis == 0:
                    for i in range(0, X.shape[0]):
                        for j in range(0, X.shape[1]):
                            normed[i,j] = (X[i,j] - np.mean(X[i,:])) / np.std(X[i,:])
                            
                elif axis == 1:
                    for i in range(0, X.shape[0]):
                        for j in range(0, X.shape[1]):
                            normed[i,j] = (X[i,j] - np.mean(X[:,j])) / np.std(X[:,j])
                
                elif axis == 2:
                    for i in range(0, X.shape[0]):
                        for j in range(0, X.shape[1]):
                            normed[i,j] = (X[i,j] - np.mean(X)) / np.std(X)
                assert axis >= 0 and axis <= 2, '\naxis values should be:\n0 - for row\n1 - for column\n2 - for row and column'
                return normed
            else:
                print('DataType not understood! keep thinkin...')     
            
  
        if rescale == True:
            if len(X.shape) == 1:
                return X * np.std(raw) + np.mean(raw)
            elif len(X.shape) > 1:
                denormed = np.zeros(X.shape)
                
                if axis == 0:
                    for i in range(0, X.shape[0]):
                        for j in range(0, X.shape[1]):
                            denormed[i,j] = X[i,j] * np.std(raw[i,:]) + np.mean(raw[i,:])
                            
                elif axis == 1:
                    for i in range(0, X.shape[0]):
                        for j in range(0, X.shape[1]):
                            denormed[i,j] = X[i,j] * np.std(raw[:,j]) + np.mean(raw[:,j])

                elif axis == 2:   
                    for i in range(0, X.shape[0]):
                        for j in range(0, X.shape[1]):
                            denormed[i,j] = X[i,j] * np.std(raw) + np.mean(raw)
                assert axis >= 0 and axis <= 2, '\naxis values should be:\n0 - for row\n1 - for column\n2 - for row and column'
                return denormed
            else:
                print('DataType not understood! keep thinkin...')
                
       
            
            
    def mean(X, rescale=False, raw=[0], axis=1):
        ''' Scales Data in Range between 0 and 1. Input can be a single- 
        or multidimenional np.array
        
        Keyword arguments:
            X       -- Input 1D or nD Array
            rescale -- False: scale, True: rescale
            raw     -- Raw Data (only for rescaling)
            axis    -- 0=row, 1=column, 2=all'''
            
        if not rescale:
            if len(X.shape) == 1:                            # check if 1D array
                return (X - np.average(X)) / (np.max(X) - np.min(X))
            elif len(X.shape) > 1:                          # check if nD array
                normed = np.zeros(X.shape)
                
                if axis == 0:
                    for i in range(0, X.shape[0]):
                        for j in range(0, X.shape[1]):
                            normed[i,j] = (X[i,j] - np.average(X[i,:])) / (np.max(X[i,:]) - np.min(X[i,:]))
                            
                elif axis == 1:
                    for i in range(0, X.shape[0]):
                        for j in range(0, X.shape[1]):
                            normed[i,j] = (X[i,j] - np.average(X[:,j])) / (np.max(X[:,j]) - np.min(X[:,j]))
                
                elif axis == 2:
                    for i in range(0, X.shape[0]):
                        for j in range(0, X.shape[1]):
                            normed[i,j] = (X[i,j] - np.average(X)) / (np.max(X) - np.min(X))
                assert axis >= 0 and axis <= 2, '\naxis values should be:\n0 - for row\n1 - for column\n2 - for row and column'
                return normed
            else:
                print('DataType not understood! keep thinkin...')     



            
        if rescale == True:
            if len(X.shape) == 1:
                return X * (np.max(raw)-np.min(raw)) + np.average(raw)
            elif len(X.shape) > 1:
                denormed = np.zeros(X.shape)
                if axis == 0:
                    for i in range(0, X.shape[0]):
                        for j in range(0, X.shape[1]):
                            denormed[i,j] = X[i,j] * (np.max(raw[i,:])-np.min(raw[i,:])) + np.average(raw[i,:])
                        
                elif axis == 1:
                    for i in range(0, X.shape[0]):
                        for j in range(0, X.shape[1]):
                            denormed[i,j] = X[i,j] * (np.max(raw[:,j])-np.min(raw[:,j])) + np.average(raw[:,j])
                        
                elif axis == 2:
                    for i in range(0, X.shape[0]):
                        for j in range(0, X.shape[1]):
                            denormed[i,j] = X[i,j] * (np.max(raw)-np.min(raw)) + np.average(raw)
                assert axis >= 0 and axis <= 2, '\naxis values should be:\n0 - for row\n1 - for column\n2 - for row and column'
                return denormed
            else:
                print('DataType not understood! keep thinkin...')
                
        

        
    def constant(X, rescale=False, const=10):
        if not rescale:
            return X / const
        if rescale == True:
            return X * const
        
        


        
    def ranged(X, rng=(0.1, 0.9), rescale=False, raw=[0], axis=1):
        if not rescale:
            if len(X.shape) == 1:                            # check if 1D array
                return (((rng[1] - rng[0]) * (X - np.min(X))) / (np.max(X) - np.min(X))) + rng[0]
            elif len(X.shape) > 1: 
                normed = np.zeros(X.shape)
                
                if axis == 0:
                    for i in range(0, X.shape[0]):
                        for j in range(0, X.shape[1]):
                            normed[i,j] = (((rng[1] - rng[0]) * (X[i,j] - np.min(X[i,:]))) / (np.max(X[i,:]) - np.min(X[i,:]))) + rng[0]
                        
                elif axis == 1:
                    for i in range(0, X.shape[0]):
                        for j in range(0, X.shape[1]):
                            normed[i,j] = (((rng[1] - rng[0]) * (X[i,j] - np.min(X[:,j]))) / (np.max(X[:,j]) - np.min(X[:,j]))) + rng[0]
                    
                elif axis == 2:
                    for i in range(0, X.shape[0]):
                        for j in range(0, X.shape[1]):
                            normed[i,j] = (((rng[1] - rng[0]) * (X[i,j] - np.min(X))) / (np.max(X) - np.min(X))) + rng[0]
                
                assert axis >= 0 and axis <= 2, '\naxis values should be:\n0 - for row\n1 - for column\n2 - for row and column'
                return normed
            else:
                print('Datatype not understood. Input must be of type 1D or 2D numpy.ndarray')



            
        if rescale == True:
            if len(X.shape) == 1:                            # check if 1D array
                return (((X - rng[0])*(np.max(raw)-np.min(raw)))/(rng[1] - rng[0])) + np.min(raw)
            elif len(X.shape) > 1:                          # check if nD array
                normed = np.zeros(X.shape)
                if axis == 0:
                    for i in range(0, X.shape[0]):
                        for j in range(0, X.shape[1]):
                            normed[i,j] = (((X[i,j] - rng[0])*(np.max(raw[i,:])-np.min(raw[i,:])))/(rng[1] - rng[0])) + np.min(raw[i,:])
                     
                elif axis == 1:
                    for i in range(0, X.shape[0]):
                        for j in range(0, X.shape[1]):
                            normed[i,j] = (((X[i,j] - rng[0])*(np.max(raw[:,j])-np.min(raw[:,j])))/(rng[1] - rng[0])) + np.min(raw[:,j])                     
            
                elif axis == 2:
                    for i in range(0, X.shape[0]):
                        for j in range(0, X.shape[1]):
                            normed[i,j] = (((X[i,j] - rng[0])*(np.max(raw)-np.min(raw)))/(rng[1] - rng[0])) + np.min(raw)
                
                assert axis >= 0 and axis <= 2, '\naxis values should be:\n0 - for row\n1 - for column\n2 - for row and column'
                return normed
            else:
                print('Datatype not understood. Input must be of type 1D or 2D numpy.ndarray')
            