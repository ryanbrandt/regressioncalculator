import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("TKAgg")
from matplotlib import pyplot as plt
from tkinter import *
import sys
import os
from functools import partial


def leastSquares( ):
    
    # get regression line
    def myLine(x,x_vec):                                                       
        a = x_vec[1,0]
        return x_vec[0,0] + (x*a)
    
    # graph line against data
    def graphMe(x,y, x_vec):
        y_reg = y.astype(float) 
        # gaph y-vals                                                
        for i in range(len(y)):                                                 
            y_reg[i] = myLine(x[i], x_vec)
        
        # generate plot    
        plt.figure("Regression Plot")                                   
        plt.scatter(x, y, color = "blue")
        plt.plot(x, y_reg, color = "red")
        plt.xlabel('x-axis')
        plt.ylabel('y-axis')    
        plt.title("Regression line (red) vs Data (blue)")
        
        plt.show()                                                             
    
   	# hard reset app w system call
    def restartRegression():                                                    
        python = sys.executable
        os.execl(python, python, * sys.argv)
    
    # out computed line to UI
    def printMe(myLine):                                                        
        master.geometry("700x400")                                         
        Label(master, text = "Regression Line:", background = "bisque").grid(column = 0, row = 4)
        Label(master, text = myLine, background = "bisque").grid(column = 0, row = 5)
        Label(master, text = "Press input new data for a new regression line", background = "yellow").grid(column = 0, row = 6)
            
    # main computational method
    def computations(df,y):   
    	# need equal x and y          
        if len(df) != len(y):                                                   
            master.geometry("800x400")                                                                                                           
            L =  Label(master, text = "Need equal number of x and y-values, press input new data and restart", background = "red")
            L.grid(column = 0, row = 4)
            
            raise ValueError("User must input equal amount of x and y-values")
        
        
        # Simple least squares w/ linear algebra
        ones = pd.Series([1]*len(df))                                                   
        df_fix = pd.concat([ones, df], axis = 1)
        
        df_fix = df_fix.astype(int)
        y = y.astype(int)
        df = df.astype(int)   
                                                        
        df_trans = pd.DataFrame.transpose(df_fix)
        
        df_t_df = np.matmul(df_trans, df_fix)
                                                            
        df_t_y = np.matmul(df_trans, y)
    
        df_t_y.shape = (2,1)                    
    
        my_det = np.linalg.det(df_t_df) 
        df_t_df_a = df_t_df[0,0]
        df_t_df_d = df_t_df[df_t_df.shape[0]-1, df_t_df.shape[1]-1]        
        df_t_df[df_t_df.shape[0]-1, df_t_df.shape[1]-1] = df_t_df_a
        df_t_df[0,0] = df_t_df_d
        df_t_df[0,df_t_df.shape[0]-1] = -df_t_df[0,df_t_df.shape[0]-1]
        df_t_df[df_t_df.shape[1] - 1, 0] = -df_t_df[df_t_df.shape[1]-1, 0]
 
 		# solution vector   
        x_vec = (1/my_det)*np.matmul(df_t_df, df_t_y)                                 
        # get line, call print utility      
        myLine = "y = " + str(x_vec[0,0]) + " + x" + str(x_vec[1,0])
        printMe(myLine)
            
        command_with_args = partial(graphMe,df, y, x_vec)
        Button(master, text = "Graph Me", command = command_with_args , highlightbackground = "bisque").grid(row = 7, column = 0)
     
    # grab user input and pass to perform computations
    def getInt( ):                                                                       
        x_vals = pd.Series(e1.get( ).split(","))
        y_vals = pd.Series(e2.get( ).split(","))
        
        computations(x_vals, y_vals)
        
    # generate GUI
    master = Tk()                                                                                                      
    master.title("Regression Calculator")
    master.geometry("600x400")
    master.configure(background = "bisque")
    
    # label elements
    Label(master, text = "Enter values as comma-seperated", background = "bisque").grid(row = 0)
    Label(master, text = "x-values:", background = "bisque").grid(row = 1)
    Label(master, text = "y-values:", background = "bisque").grid(row = 2)
    
    # input elements
    e1 = Entry(master, background = "bisque", highlightthickness = 0)
    e2 = Entry(master, background = "bisque", highlightthickness = 0)
    e1.grid(row = 1, column = 1)
    e2.grid(row = 2, column = 1)
    
    # button elements
    Button(master, text = "Quit", command = master.quit, highlightbackground = "bisque").grid(row = 3, column = 0, sticky = W, pady = 4)
    Button(master, text = "Submit", command = getInt, highlightbackground = "bisque").grid(row = 3, column = 1, sticky = W, pady = 4)
    Button(master, text = "Input New Data", command = restartRegression, highlightbackground = "bisque").grid(row = 3, column = 2, sticky = W, pady = 4)
   
    master.call('wm', 'attributes', '.', '-topmost', '1')
    
    mainloop( )                                                                                                           
       
# run app
leastSquares( )                                                                                                                                                  #run app
