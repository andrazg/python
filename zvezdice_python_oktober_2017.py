#python 2.7.12
import math
dado = '*'
counter = 20
count = 19
steje = 1
for i in range(1,counter):
    counter-=1
    print counter * " " + dado
    steje += dado.count("*")
    dado = dado + "**"
steje = steje -1
steje = int(math.sqrt(steje))
for i in range(1,10):
    print steje * " " + "**"




   *
                  ***
                 *****
                *******
               *********
              ***********
             *************
            ***************
           *****************
          *******************
         *********************
        ***********************
       *************************
      ***************************
     *****************************
    *******************************
   *********************************
  ***********************************
 *************************************
                   **
                   **
                   **
                   **
                   **
                   **
                   **
                   **
                   **