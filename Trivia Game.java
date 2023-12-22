// The "Culminating" class.

// Who Wants to be a Millionare

// Name: Abdelrahman Abdelaal
// Date: November 8th, 2021

/*Rules of the game;

1. There will be 10 multiple choice questions that the YOU will have to answer.
2. Each time you get a question correct, you win $100,000.
3. In order to win $1,000,000 you would have to get all ten questions correct.
4. As you go along the questions, you will have the option to quit the game
   and keep the amount of money you've earned, or you can keep on going.
5. If you get just ONE question wrong, you will lose all of your money, and
   it'll be GAME OVER for you.
6. There will be lifelines to help you answer the questions, you will be able
   to use them only three times in the entire program, and once per question.

*/

import java.awt.*;
import hsa.Console;

public class Culminating
{
    static Console c;           // The output console

    public static void main (String[] args)
    {
	c = new Console ();

	// Decleration
	int money, count;
	money = 0;
	count = 0;

	String rules, quit;
	quit = "";          // Accessing variable

	char enterKey, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10;
	q1 = ' ';           // Accessing variables
	q2 = ' ';
	q3 = ' ';
	q4 = ' ';
	q5 = ' ';
	q6 = ' ';
	q7 = ' ';
	q8 = ' ';
	q9 = ' ';
	q10 = ' ';

	// Introduction

	c.setColour (Color.blue);           // Sets colour to blue
	for (int x = 0 ; x <= 639 ; x++)    // As long as x is less than or equal to 639, the loop will run
	{
	    c.drawLine (x, 0, x, 500);      // Draws a moving line (left to right)
	    delay (5);
	}

	Font Introduction = new Font ("Courier", Font.BOLD, 30);        // Sets font
	c.setColor (Color.green);                                       // Sets Colour
	c.setFont (Introduction);
	c.drawString ("WHO WANTS TO BE A MILLIONARE!", 60, 200);        // Introduction Text
	delay (3000);                                                   // Waits three seconds

	c.clear ();

	c.setColour (Color.yellow);             // Colour yellow
	for (int x = 639 ; x > 0 ; x--)         // If x is greater than zero, start the loop then subtract by 1 each iteration
	{
	    c.drawLine (x, 0, x, 500);          // Draws a moving line (right to left)
	    delay (5);
	}

	c.setColor (Color.blue);                // Sets colour to blue
	c.drawString ("By: Abdelrahman Abdelaal", 100, 200);
	delay (3000);
	c.clear ();

	c.setColor (Color.green);               // Sets colour to green

	do
	{
	    c.println ("\t\tWould you like to know the rules (Yes), (No): ");       // If the user want's the rules of the game or not
	    rules = c.readString ();
	}
	while (!(rules.equals ("no")) && !(rules.equals ("No")) && !(rules.equals ("yes")) && !(rules.equals ("Yes"))); // Invalid input system

	// User chooses to go through the rules

	if (rules.equals ("Yes") || rules.equals ("yes"))
	{
	    c.clear ();

	    c.println ("\n\nThe rules are very simple: You must answer all ten questions correctly to get \nONE MIILION DOlLARS!");
	    c.println ();

	    c.println ("Each time you get a question correct, you win ONE HUNDRED THOUSAND DOLLARS!");
	    c.println ();

	    c.println ("You have the option to quit the game anytime you want, and keep\nthe money you've earned so far.");
	    c.println ();

	    c.println ("But if you choose to go on, I must caution you, if you get ONE question wrong, \nyou will lose all your money.");
	    c.println ();

	    c.println ("If this happens, it's GAME OVER for you.");
	    c.println ();

	    c.println ("Also, if you're having difficulty with your questions there are lifelines \nto help you answer the question, you get to use them three times in the");
	    c.println ("game, and once per question.");
	    c.println ();

	    c.println ("To access the lifelines, enter \'h\' when asked a question.");
	    c.println ();

	    c.println ("Enter a key to continue: ");
	    enterKey = c.getChar ();                // Waits to input a key

	    c.clear ();                              // Clears the screen
	}

	// User chooses to not go through the rules

	else if (rules.equals ("No") || rules.equals ("no"))
	{
	    c.clear ();
	    c.println ("Ok, hope you're ready!");
	    delay (3000);                           // Waits three seconds
	    c.clear ();                             // Clears the screen
	}


	// The start of the game

	c.setColour (Color.green);               // Sets colour to green
	for (int x = 639 ; x > 0 ; x--)          // If x is greater than zero, start the loop then subtract by 1 each iteration
	{
	    c.drawLine (x, 0, x, 500);           // Draws a moving line (right to left)
	    delay (5);
	}

	c.setColor (Color.red);                 // Sets colour to red
	c.drawString ("LETS GET STARTED!!", 180, 200);
	delay (3000);
	c.clear ();

	c.setColor (Color.green);               // Sets colour to green

	// Question 1

	c.println ("\n\tHere is the first question, we'll go easy on you for this question.");

	c.drawString ("Who Created Starwars?", 155, 200);       // Displays question
	delay (5000);                                           // Five seconds to read the question
	c.clear ();

	c.println ("\n\n\ta) Barack Obama\t\t\t\t\tb) Michael Jackson");        // Displays the options
	c.println ("\n\n\tc) George Lucas\t\t\t\t\td) Abdelrahman Abdelaal");

	q1 = repeatQuestion (q1);       // Invalid input checking system

	if (count < 3 && q1 == 'h')     // Tracks how many times the lifeines were used
	{
	    q1 = lifeline (q1, 0);
	    count++;                    // If a lifeline was used add one to count
	}

	q1 = noLifeline (q1, count);    // If the user used the lifelines three times, the question will repeat and the lifelines will be permanatly closed

	if (q1 == 'c')                  // If you inputted the correct answer for question 1
	{
	    money = correct (money);    // Adds 100,000 to the total money earned
	    c.println ("Money earned so far: $" + money);

	    quit = quit1 (quit);        // Asks user if they want to quit the program or not


	    // Question 2

	    if ((quit.equals ("No") || quit.equals ("no")))         // If the user chooses not to quit
	    {
		c.println ("Welcome to the next level");
		delay (3000);
		c.println ("\n\t\t\tHere is the second question.");
		c.drawString ("What is ten to the power of 5?", 50, 200);     // Displays question
		delay (5000);                                                 // Five seconds to read the question
		c.clear ();
		c.println ("\n\n\ta) 100\t\t\t\t\tb) 1000");        // Displays the options
		c.println ("\n\n\tc) 10\t\t\t\t\td) 100000");

		q2 = repeatQuestion (q2);           // Invalid input system

		if (count < 3 && q2 == 'h')         // Tracks how many times the user used the lifelines
		{
		    q2 = lifeline (q2, 1);
		    count++;                        // If the user used a lifeline add one to count
		}

		// If the user used the lifelines three times, the question will repeat and the lifelines will be permanatly closed

		q2 = noLifeline (q2, count);

		if (q2 == 'd')                  // If the user inputted the correct answer
		{
		    money = correct (money);    // Adds 100,000 to the total money earned
		    c.println ("Money earned so far: $" + money);

		    quit = quit1 (quit);        // Asks the user if the want to quit
		}

		else                            // If the user didn't input the correct answer
		{
		    delay (3000);
		    c.clear ();
		    c.println ("You've put in the wrong answer, GAME OVER.");
		}


		// Question 3

		if ((quit.equals ("no") || quit.equals ("No")) && q2 == 'd')        // If the user chooses not to quit
		{
		    c.println ("Welcome to the next level.");
		    delay (3000);
		    c.println ("\n\t\t\tHere is the third question.");
		    Font adjusted = new Font ("Courier", Font.BOLD, 25);        // Adjusted font
		    c.setFont (adjusted);        // Sets new font

		    c.drawString ("What can be touched, but can't be seen?", 26, 200);      // Displays the question
		    delay (5000);           // Five seconds to read the question
		    c.clear ();
		    c.println ("\n\n\ta) Air\t\t\t\t\tb) John Cena");               // Displays the options
		    c.println ("\n\n\tc) Heart\t\t\t\td) Back of your head");

		    q3 = repeatQuestion (q3);       // Invalid input sysstem

		    if (count < 3 && q3 == 'h')     // Tracks how many times the lifelines were used
		    {
			q3 = lifeline (q3, 2);
			count++;                    // If a lifeline was used add one to the count
		    }

		    // If the user used the lifelines three times, the question will repeat and the lifelines will be permanatly closed

		    q3 = noLifeline (q3, count);

		    if (q3 == 'c')                  // If the user inputted the correct answer
		    {
			money = correct (money);    // Adds 100,000 to the total
			c.println ("Money earned so far: $" + money);

			quit = quit1 (quit);        // Asks the user if they want to quit the program
		    }

		    else                            // If the user use didn't input the correct answer
		    {
			delay (3000);
			c.clear ();
			c.println ("You've put in the wrong answer, GAME OVER.");
		    }

		    // Question 4

		    if ((quit.equals ("no") || quit.equals ("No")) && q3 == 'c')        // If the user chooses not to quit
		    {
			c.println ("Welcome to the next level.");
			delay (3000);
			c.println ("\n\t\t\tHere is the fourth question.");
			c.drawString ("Who is the first President of America", 45, 200);    // Displays the question
			delay (5000);           // Five seconds to read the question
			c.clear ();

			c.println ("\n\n\ta) George Clooney\t\t\tb) George Washington");        // Displays the options
			c.println ("\n\n\tc) George Stewart\t\t\td) Joe Biden");

			q4 = repeatQuestion (q4);       // Invalid input system

			if (count < 3 && q4 == 'h')     // Keeps track of how many times the lifelines were used
			{
			    q4 = lifeline (q4, 3);
			    count++;                    // If a lifeline was used add one to the count
			}

			// If the user used the lifelines three times, the question will repeat and the lifelines will be permanatly closed

			q4 = noLifeline (q4, count);

			if (q4 == 'b')                  // If the user inputted the correct answer
			{
			    money = correct (money);    // Adds 100,000 to the total earned money
			    c.println ("Money earned so far: $" + money);

			    quit = quit1 (quit);        // Asks the user if they want to quit the program
			}

			else                            // If the user inputted the incorrect answer
			{
			    delay (3000);
			    c.clear ();
			    c.println ("You've inputted the wrong answer, GAME OVER.");
			}

			// Question 5

			if ((quit.equals ("no") || quit.equals ("No")) && q4 == 'b')        // If the user chooses not to quit the program
			{
			    c.println ("Welcome to the next level.");
			    c.println ("\n\t\t\tHere is the fifth question.");
			    c.drawString ("How many bones does a shark have?", 80, 200);          // Displays the question
			    delay (5000);               // Five seconds to read the question
			    c.clear ();

			    c.println ("\n\n\ta) None\t\t\t\t\tb) 128");        // Displays the options
			    c.println ("\n\n\tc) 314\t\t\t\t\td) 91 ");

			    q5 = repeatQuestion (q5);   // Invalid input system

			    if (count < 3 && q5 == 'h') // Keeps track of how many times the lifelines were used
			    {
				q5 = lifeline (q5, 4);
				count++;                // If a lifeline was used add one to the count
			    }

			    // If the user used the lifelines three times, the question will repeat and the lifelines will be permanatly closed

			    q5 = noLifeline (q5, count);

			    if (q5 == 'a')                  // If the user gets the correct answer
			    {
				money = correct (money);    // Adds 100,000 to the total earned money
				c.println ("Money earned so far: $" + money);

				quit = quit1 (quit);        // Asks the user if they want to quit the program
			    }

			    else                            // If the user inputted the incorrect answer
			    {
				delay (3000);
				c.clear ();
				c.println ("You've inputted the wrong answer, GAME OVER.");
			    }


			    // Question 6

			    if ((quit.equals ("no") || quit.equals ("No")) && q5 == 'a')        // If the user chooses not to quit the program
			    {
				c.println ("Welcome to the new level.");
				c.println ("\n\t\t\tHere is the sixth question.");
				c.drawString ("When was St. Ignatius of Loyola founded?", 30, 200);        // Displays the question
				delay (5000);               // Five seconds to read the question
				c.clear ();

				c.println ("\n\n\ta) 1980\t\t\t\t\tb) 1984");       // Displays the options
				c.println ("\n\n\tc) 1982\t\t\t\t\td) 1995");

				q6 = repeatQuestion (q6);   // Invalid input system

				if (count < 3 && q6 == 'h') // Keeps track of how many times the lifelines were used
				{
				    q6 = lifeline (q6, 5);
				    count++;                // If a lifeline was used add one to count
				}


				/*If the user used the lifelines three times, the question will repeat and the lifelines will be permanatly
				 closed*/

				q6 = noLifeline (q6, count);

				if (q6 == 'c')                  // If the user entered the correct answer
				{
				    money = correct (money);    // Adds 100,000 to the total
				    c.println ("Money earned so far: $" + money);

				    quit = quit1 (quit);        // Asks the user if they want to quit
				}

				else                            // If the user didn't input the correct answer
				{
				    delay (3000);
				    c.clear ();
				    c.println ("You've inputted the wrong answer, GAME OVER.");
				}

				// Question 7

				if ((quit.equals ("no") || quit.equals ("No")) && q6 == 'c')        // If the user chooses not to quit
				{
				    c.println ("Welcome to the next level.");
				    c.println ("\n\t\t\tHere is the seventh question.");
				    c.drawString ("What is the rarest m & m colour?", 75, 200);     // Displays the question
				    delay (5000);           // Five seconds to read the question
				    c.clear ();

				    c.println ("\n\n\ta) Orange\t\t\t\t\tb) Yellow");       // Displays the options
				    c.println ("\n\n\tc) Brown\t\t\t\t\td) blue");

				    q7 = repeatQuestion (q7);       // Invalid input system

				    if (count < 3 && q7 == 'h')     // Keeps track of how many times the lifelines were used
				    {
					q7 = lifeline (q7, 6);
					count++;                    // Adds one to count each time a lifeline was used
				    }

				    /* If the user used the lifelines three times, the question will repeat and the lifelines will be permanatly
				    closed */

				    q7 = noLifeline (q7, count);

				    if (q7 == 'c')                  // If the user inputted the correct answer
				    {
					money = correct (money);    // Adds 100,000 to the total money earned
					c.println ("Money earned so far: $" + money);

					quit = quit1 (quit);        // Asks the user if they want to quit
				    }

				    else                            // If the user didn't input the correct answer
				    {
					delay (3000);
					c.clear ();
					c.println ("You've inputted the wrong answer, GAME OVER.");
				    }


				    // Question 8

				    if ((quit.equals ("no") || quit.equals ("No")) && q7 == 'c')        // If the user chooses not to quit
				    {
					c.println ("Welcome to the next level.");
					c.println ("\n\t\t\tHere is the eigth question.");
					c.drawString ("What is Earth's largest ocean?", 85, 200);       // Displays the question
					delay (5000);       // Five seconds to read the question
					c.clear ();

					c.println ("\n\n\ta) Atlantic\t\t\t\tb) Pacific");      // Displays the options
					c.println ("\n\n\tc) Indian\t\t\t\td) Arctic");

					q8 = repeatQuestion (q8);       // Invalid input system

					if (count < 3 && q8 == 'h')     // Keeps track of how many times the lifelines were used
					{
					    q8 = lifeline (q8, 7);
					    count++;                    // Adds one to count each time a lifeline was used
					}

					/* If the user used the lifelines three times, the question will repeat and the lifelines will be
					permanatly closed */

					q8 = noLifeline (q8, count);

					if (q8 == 'b')                  // If the user inputted the correct answer
					{
					    money = correct (money);    // Adds 100,000 to the total money earned
					    c.println ("Money earned so far: $" + money);

					    quit = quit1 (quit);        // Asks the user if they would like to quit the program
					}

					else                            // If the user inputted the wrong answer
					{
					    delay (3000);
					    c.clear ();
					    c.println ("You've inputted the wrong answer, GAME OVER.");
					}

					// Question 9

					if ((quit.equals ("no") || quit.equals ("No")) && q8 == 'b')        // If the user chooses not to quit
					{
					    c.println ("Welcome to the next level.");
					    c.println ("\n\t\t\tHere is the ninth question.");
					    c.drawString ("Which desert is the largest in the world?", 20, 200);    // Displays the question
					    delay (5000);       // Five seconds to read the question
					    c.clear ();

					    c.println ("\n\n\ta) Namib Desert\t\t\tb) Gobi Desert");        // Displays the options
					    c.println ("\n\n\tc) Mojave Desert\t\td) Antarctic Desert");

					    q9 = repeatQuestion (q9);       // Invalid input system

					    if (count < 3 && q9 == 'h')     // Keeps track of how many times the lifelines were used
					    {
						q9 = lifeline (q9, 8);
						count++;                    // Adds one to count each time a lifeline was used
					    }

					    /* If the user used the lifelines three times, the question will repeat and the lifelines
					    will be permanatly closed*/

					    q9 = noLifeline (q9, count);

					    if (q9 == 'd')                  // If the user inputted the correct answer
					    {
						money = correct (money);    // Adds 100,000 to the total money earned
						c.println ("Money earned so far: $" + money);

						quit = quit1 (quit);        // Asks the user if they want to quit the program
					    }

					    else                            // If the user inputted the wrong answer
					    {
						delay (3000);
						c.clear ();
						c.println ("You've inputted the wrong answer, GAME OVER.");
					    }

					    // FINAL QUESTION

					    if ((quit.equals ("no") || quit.equals ("No")) && q9 == 'd')        // If the user chooses not to quit
					    {
						c.println ("WELCOME TO THE FINAL LEVEL!!!!!");
						delay (3000);
						c.println ("\nThe MOMENT you've all been waiting for!");        // Dramatic effect...
						delay (3000);
						c.println ("\nThe HARDEST QUESTION you've ever faced!");        // Some more dramatic effect...
						delay (3000);
						c.println ("\nFor ONE MILLION DOLLARS....");                    // More dramatic effect...
						delay (3000);
						c.println ("\nThe question is.......");                         // Just a little bit more dramatic effect...
						delay (5000);
						c.clear ();

						c.drawString ("What month is it?", 200, 200);        // Displays the question
						delay (5000);           // Five seconds to read the question
						c.clear ();

						c.println ("\n\n\ta) December\t\t\tb) November");       // Displays the options
						c.println ("\n\n\tc) June\t\t\t\td) March");

						q10 = repeatQuestion (q10);         // Invalid input system

						if (count < 3 && q10 == 'h')        // Keeps track of how many times the lifelines were used
						{
						    q10 = lifeline (q10, 9);
						    count++;                        // If a lifeline was used add one to count
						}

						/* If the user used the lifelines three times, the question will repeat and the lifelines
						will be permanatly closed*/

						q10 = noLifeline (q10, count);

						if (q10 == 'b')                 // If the user inputted the correct answer
						{
						    delay (3000);
						    c.clear ();


						    c.setColour (Color.blue);           // Sets colour to blue
						    for (int x = 0 ; x <= 639 ; x++)    // As long as x is less than or equal to 639, the loop will run
						    {
							c.drawLine (x, 0, x, 500);      // Draws a moving line (left to right)
							delay (2);
						    }


						    c.setColour (Color.red);                 // Sets colour to red

						    // if x is greater than zero, start the loop and subtract one each iteration

						    for (int x = 639 ; x > 0 ; x--)
						    {
							c.drawLine (x, 0, x, 500);           // Draws a moving line (right to left)
							delay (2);
						    }


						    c.setColour (Color.yellow);           // Colour yellow

						    // If y is less than or equal to 500, start the lopp then add 1 each iteration

						    for (int y = 0 ; y <= 500 ; y++)
						    {
							c.drawLine (0, y, 640, y);
							delay (2);
						    }

						    c.setColor (Color.green);

						    c.drawString ("YOU JUST WON ONE MILLION DOLLARS!!", 60, 200);
						    delay (5000);
						    c.clear ();
						    c.drawString ("Thank you for playing!", 160, 200);
						}

						else                            // If the user inputted the wrong answer
						{
						    delay (3000);
						    c.clear ();
						    c.println ("...You got the question wrong?");
						    delay (3000);
						    c.println ("\nHow? How is this possible?");
						    delay (3000);
						    c.println ("\nYou just lost yourself $" + money);
						    delay (3000);
						    c.println ("Wow....Thanks for playing, I guess?");
						}

					    }

					}
				    }
				}
			    }
			}
		    }
		}
	    }
	}

	else                            // If you inputted the incorrect answer for question 1
	{
	    delay (3000);
	    c.clear ();
	    c.println ("You've put in the wrong answer, GAME OVER.");
	}


	// Place your program here.  'c' is the output console
    } // main method


    // Delay Method

    public static void delay (int millisecs)
    {
	try
	{
	    Thread.currentThread ().sleep (millisecs);
	}


	catch (InterruptedException e)
	{
	}
    }


    // Correct answer method

    public static int correct (int money)
    {
	delay (3000);                   // Waits three seconds
	c.clear ();                     // Clears the screen

	c.drawString ("C", 210, 200);
	delay (500);
	c.drawString ("O", 245, 200);
	delay (500);
	c.drawString ("R", 275, 200);
	delay (500);
	c.drawString ("R", 305, 200);
	delay (500);
	c.drawString ("E", 335, 200);
	delay (500);
	c.drawString ("C", 365, 200);
	delay (500);
	c.drawString ("T", 395, 200);
	delay (3000);
	c.clear ();

	money += 100000;                // Adds one hundred thousand dollars to total money

	c.println ();
	c.println ("You have won yourself ONE HUNDRED THOUSAND DOLLARS to your total!");
	c.println ("\n\n");
	return (money);                 // Returns money
    }


    // If the user wants to quit method

    public static String quit1 (String quit)
    {

	do
	{
	    c.println ();
	    c.println ("Would you like to quit and keep your hard earned money (Yes) (No): ");      // Asks the user
	    quit = c.readString ();
	}
	while (!(quit.equals ("no")) && !(quit.equals ("No")) && !(quit.equals ("yes")) && !(quit.equals ("Yes")));     // Invalid input system

	// If the user doesn't want to quit
	if (quit.equals ("No") || quit.equals ("no"))
	{
	    c.println ("Ok, here we go!");
	    delay (3000);
	    c.clear ();
	    return (quit);      // Returns quit
	}

	// If the user wants to quit
	else
	{
	    c.println ("Well, everyone goes home happy. Thanks for playing!");
	    return (quit);      // Returns quit
	}
    }


    // Life line "Ask A Audience Member" Method

    public static void audience ()
    {
	int num;

	num = (int) (Math.random () * 4) + 1;                         // Random number from 1 - 4

	if (num == 1)
	{
	    c.println ("\tAudience member: I think it's \'a\'.");     // Audience member picks 'a'
	}

	else if (num == 2)
	{
	    c.println ("\tAudience member: I think it's \'b\'.");     // Audience member picks 'b'
	}

	else if (num == 3)
	{
	    c.println ("\tAudience member: I think it's \'c\'.");     // Audience member picks 'c'
	}

	else if (num == 4)
	{
	    c.println ("\tAudience member: I think it's \'d\'.");     // Audience member picks 'd'
	}
    }


    // Life line "Reveals one incorrect answer" Method

    public static void revealQ (int row)
    {
	char[] [] questions = {{'a', 'b', 'c', 'd', 'c'},           // The first four cells are the options and the fifth is the answer
		{'a', 'b', 'c', 'd', 'd'},
		{'a', 'b', 'c', 'd', 'c'},
		{'a', 'b', 'c', 'd', 'b'},
		{'a', 'b', 'c', 'd', 'a'},
		{'a', 'b', 'c', 'd', 'c'},
		{'a', 'b', 'c', 'd', 'c'},
		{'a', 'b', 'c', 'd', 'b'},
		{'a', 'b', 'c', 'd', 'd'},
		{'a', 'b', 'c', 'd', 'b'},
	    };
	int column;

	do
	{
	    column = (int) (Math.random () * 4);                    // Chooses a random column from 1 - 4
	}
	while (questions [row] [column] == questions [row] [4]);           // Repeat the code if the option chosen is the answer

	c.println ("\t" + questions [row] [column] + " is one of the wrong answers.");      // Displays one of the wrong answers
    }


    // Lifeline "Hint"

    public static void hint (int row)
    {
	String[] [] questions = {{"\tThis person wears glasses."},            // Each row in the 2D array represents a question
		{"\tYour calculator can help you answer this."},
		{"\tLove is in the air."},
		{"\tHis name starts with a G."},
		{"\tThe number is suprisingly low!"},
		{"\tThe answer is in the 80s."},
		{"\tThe only hint I can give you is that it's definitely not red."},
		{"\tIt is between the continets of Asia and Australia."},
		{"\tThe answer has an \'a\' in it."},
		{"\tCheck your calendar."},
	    };

	c.println (questions [row] [0]);            // Prints the hint coresponding to the question / row
    }


    // Choose a lifeline method

    public static char lifeline (char question, int row)
    {
	if (question == 'h')        // If user chooses 'h'
	{
	    char lifeline2;

	    c.println ("\n\tHi there! I heard you need help with a question.");

	    // Invalid input system

	    do
	    {
		c.println ("\n\tChoose a lifeline (a) Ask a audience member\n\t(b) Take a hint (c) Reveal one incorrect answer: ");     // Asks the user which for lifeline
		lifeline2 = c.getChar ();
		c.println ("\n\tYou have chosen lifeline " + lifeline2);
	    }
	    while (lifeline2 != 'a' && lifeline2 != 'b' && lifeline2 != 'c');       // Invalid input system

	    if (lifeline2 == 'a')       // If the user wants to ask a audience member
	    {
		c.println ();
		audience ();
	    }

	    if (lifeline2 == 'b')       // If the user would like a hint
	    {
		c.println ();
		hint (row);
	    }

	    if (lifeline2 == 'c')       // If the user wants one incorrect answer to be revealed
	    {
		c.println ();
		revealQ (row);
	    }

	    // Gives the options again for the question after the lifeline was given

	    do
	    {
		c.println ("\n\n\tEnter your answer (a) (b) (c) (d): ");
		question = c.getChar ();
		c.println ("\tYou have chosen " + question);
	    }
	    while (question != 'a' && question != 'b' && question != 'c' && question != 'd');       // Invalid input system

	}

	return (question);      // Returns question
    }


    // do-while loop for questions method

    public static char repeatQuestion (char question)
    {
	do
	{
	    c.println ("\n\n\tEnter your answer (a) (b) (c) (d) (h): ");
	    question = c.getChar ();
	    c.println ("\tYou have chosen " + question);
	}
	while (question != 'a' && question != 'b' && question != 'c' && question != 'd' && question != 'h');        // While the answer isn't one of the options

	return (question);      // Returns question
    }


    // If the user tires to use the lifeline again after having used it three times before

    public static char noLifeline (char questions, int count)
    {
	while (count >= 3 && questions == 'h')      // If the count is greater than or equal to three and if the user chose 'h'
	{
	    c.println ("\tYou've used the lifelines three times already!");
	    c.println ();

	    do              // Displays the options again for the question
	    {
		c.println ("\n\n\tEnter your answer (a) (b) (c) (d): ");
		questions = c.getChar ();
		c.println ("\tYou have chosen " + questions);
	    }
	    while (questions != 'a' && questions != 'b' && questions != 'c' && questions != 'd' && questions != 'h');       // Invalid input system
	}

	return (questions);     // Returns question
    }
} // Culminating class
