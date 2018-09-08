Pretty simple linear regression calculator I made during a really slow day at a summer job.

Really limited as far as its scope of actual applications, but pretty smooth for an introductory statistics or linear algebra course.

Uses pandas and numpy for the data handling side (pandas for dataframes/series, numpy for linear algebra).

Uses tkinter for a really bare-bones GUI; users can quit (exit) the application or submit their data with, obviously, submit.

<img width="595" alt="screen shot 2018-09-07 at 10 21 10 pm" src="https://user-images.githubusercontent.com/37029617/45249474-e5abc400-b2ee-11e8-96e1-d0f1c7041bca.png">

Unfortunately, right now, the calculator only supports complete data and wont make the computation if the number of x-values =/= the number of y-values. Ill probably add support for incomplete data eventually.

<img width="796" alt="screen shot 2018-09-07 at 10 33 04 pm" src="https://user-images.githubusercontent.com/37029617/45249476-f2c8b300-b2ee-11e8-88b5-b29f824c546e.png">

Upon making a computation, the window prompts users to press the input new data button if they want to compute a new regression line. If the user just enters new data without pressing input new data, the computation will still be correct, but other things can potentially get a little wacky, still have to work on that. The input new data button simply restarts the application. 

Also, user's are now surprised with a graph me button, which allows the user to choose to view a plot of their regression line and input data.

<img width="697" alt="screen shot 2018-09-07 at 10 34 34 pm" src="https://user-images.githubusercontent.com/37029617/45249479-04aa5600-b2ef-11e8-9288-cc4aafa8e8d2.png">

If the user presses graph me, a plot is generated via matplotlib's pyplot, with the data as a scatter plot against the regression line generated in the previous step.

<img width="1276" alt="screen shot 2018-09-07 at 10 35 07 pm" src="https://user-images.githubusercontent.com/37029617/45249482-11c74500-b2ef-11e8-9fab-c98fa8849830.png">

Overall, still a work in progress. In the future ill address the issues mentioned above and hopefully add support for multiple regression and (maybe?) other regression methods, curvature (i.e. parabolic fitting), a prediction option and, of course, a nicer GUI.