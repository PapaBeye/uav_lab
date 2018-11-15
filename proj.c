#include<stdio.h>

#include<stdlib.h>

// Defines maximum row and column size

#define MAX 25

// main function definition

int main()

{

     // Loop variable

     int r, c;

     // Declares an matrix

     int floor[MAX][MAX];

     // To store the commands entered by the user

     int command, command1;

     // To store the current position

     int posx, posy;

     // Initializes the current position to zero

     posx = posy = 0;

     // Initializes the move to zero

     int move = 0;

     // Loops till number of rows

     for (r = 0; r < MAX; r++)

          // Loops till number of columns

          for (c = 0; c < MAX; c++)

              // Initializes each cell to zero

              floor[r][c] = 0;

     // Loops till user command is not 9

     do

     {

          // Accepts the command from the user

          scanf("%d", &command);

          // Checks if the command is 5

          if (command == 5)

              // Accept the number after the comma symbol

              scanf(",%d", &command1);

          // Otherwise set the move value to command

          else

              move = command;

          // Checks if the command is 5

          if (command == 5)

          {

              // Checks if the move is 1

              if (move == 1)

              {

                   // Checks if the position of x coordinate is 0 then cannot move up

                   // Because x coordinate cannot be negative

                   if (posx == 0)

                   {

                        // Display error message and exit the program

                        printf("Cannot Move UP");

                        exit(0);

                   }// End of if condition

                   // Otherwise move up

                   else

                   {

                        // Loops from current x coordinate position to current x coordinate position minus command1 value,

                        // which is number of position to move

                        for (r = posx; r >= posx - command1; r--)

                             // Set the floor array row index r and column index position posy to '.'

                             floor[r][posy] = '.';

                        // Update the current x coordinate position to r value

                        posx = r;

                   }// End of else

              }// End of outer if condition

              // Otherwise, checks if the move is 2

              else if (move == 2)

              {

                   // Checks if the position of x coordinate is MAX then cannot move down

                   // Because x coordinate cannot be more than MAX

                   if (posx == MAX)

                   {

                        // Display error message and exit the program

                        printf("Cannot Move DOWN");

                        exit(0);

                   }// End of if condition

                   // Otherwise move down

                   else

                   {

                        // Loops from current x coordinate position to current x coordinate position plus command1 value,

                        // which is number of position to move

                        for (r = posx; r < posx + command1; r++)

                             // Set the floor array row index r and column index position posy to '.'

                             floor[r][posy] = '.';

                        // Update the current x coordinate position to r value

                        posx = r;

                   }// End of else

              }// End of outer if conditionEnd of else if condition

              // Otherwise, checks if the move is 3

              else if (move == 3)

              {

                   // Checks if the position of y coordinate is MAX then cannot move right

                   // Because y coordinate cannot be more than MAX

                   if (posy == MAX)

                   {

                        // Display error message and exit the program

                        printf("Cannot Turn Right");

                        exit(0);

                   }// End of if condition

                   // Otherwise move right

                   else

                   {

                        // Loops from current y coordinate position to current y coordinate position plus command1 value,

                        // which is number of position to move

                        for (r = posy; r < posy + command1; r++)

                             // Set the floor array row index r and column index position posy to '.'

                             floor[posx][r] = '.';

                        // Update the current y coordinate position to r value

                        posy = r;

                   }// End of else

              }// End of else if condition

              // Otherwise, checks if the move is 4

              else if (move == 4)

              {

                   // Checks if the position of y coordinate is 0then cannot move left

                   // Because y coordinate cannot be less than zero

                   if (posy == 0)

                   {

                        // Display error message and exit the program

                        printf("Cannot Turn Left");

                        exit(0);

                   }// End of if condition

                   // Otherwise move right

                   else

                   {

                        // Loops from current y coordinate position to current y coordinate position minus command1 value,

                        // which is number of position to move

                        for (r = posy; r >= posy - command1; r--)

                             // Set the floor array row index r and column index position posy to '.'

                             floor[posx][r] = '.';

                        posy = r;

                        // Update the current y coordinate position to r value

                        posy = r;

                   }// End of else

              }// End of else if condition

          }

          // Otherwise, checks if the command is 6

          else if (command == 6)

          {

              // Loops up to number of rows

              for (r = 0; r < MAX; r++)

              {

                   // Loops up to number of columns

                   for (c = 0; c < MAX; c++)

                        // Displays each cell value

                        printf("%c", floor[r][c]);

                   // Displays new line

                   printf("\n");

              }// End of for loop

          }// End of else if

     } while (command != 9);
     return 0;

}