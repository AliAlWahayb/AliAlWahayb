#include <iostream>
#include <cstdlib>
#include <cmath>
#include <string>
#include <fstream>
#include <ctime>
using namespace std;

/**
 * This function displays the menu for the user to choose from.
 */
void start()
{
    cout << "Please choose an operation  \n";
    cout << "1. New Order" << endl
         << endl;
    cout << "2. Display Order" << endl
         << endl;
    cout << "3. Edit Order" << endl
         << endl;
    cout << "4. Search Order" << endl
         << endl;
    cout << "5. Report" << endl
         << endl;
    cout << "6. Exit" << endl;
}

/* Getting the current time and date. */
time_t now = time(0);
char *dt = ctime(&now);

struct menu_items
{
    string name;
    double price;
    int place_number;
};

menu_items menu[50];
/* A counter for the number of items in the menu. */
int menu_item_counter = 0;

/* Opening the menu.txt file and reading the data from it. */
void menu_input()
{
    
    
    ifstream menufile;
    menufile.open("menu.txt", ios::in);
    if (menufile.is_open() == true || menufile.is_open())
    {
        int counter = 0;
        while (!menufile.eof())
        {
            menufile >> menu[counter].name;
            menufile >> menu[counter].price;
            menu[counter].place_number = counter + 1;
            ++counter;
        }
        menu_item_counter = counter;
    }
    else
    {
        cout << "Menu not found\n";
        cout << "Make a menu.txt file and add the menu" << endl;
    }
    menufile.close();
}

/**
 * This function prints out the menu items in a formatted way
 */
void the_menu()
{
    cout << "::::::::::::XXX:::::::MENU::::::XXX:::::::::::::\n";
    for (int i = 0; i < menu_item_counter; i++)
    {
        cout << "\n Item[" << menu[i].place_number << "] " << menu[i].name << " $" << menu[i].price << '\n';
    }
    cout << endl
         << "::::::::::::XXX:::::::MENU::::::XXX:::::::::::::\n";
}

double total;

/**
 * It takes the user's order and writes it to a file.
 */
void the_order()
{
    the_menu();
    int order_answer;
    ofstream order;
    order.open("order.txt", ios::out);
    cout << "Place your order by entring the number" << endl;
    cout << "To end the order press 0" << endl;

    while (order_answer != 0)
    {
        cin >> order_answer;
        if (order_answer >= 1 && order_answer < menu_item_counter + 1)
        {
            int x = 0;
            for (int i = 0; i < menu_item_counter; i++)
            {
                if (order_answer == menu[i].place_number)
                {
                    x = i;
                }
            }

            order << menu[x].name << " " << menu[x].price << endl;
            total += menu[x].price;
        }
        else if (order_answer != 0)
        {
            cout << "Item not found" << endl;
        }
    }
}

struct order_data
{
    string name;
    double price;
    int place_number;
};
order_data order_save[50];
/* A counter for the number of items in the order. */
int order_item_counter = 0;

/**
 * It reads the order.txt file and saves the data into an array of structs.
 */
void order_input()
{
    ifstream order;
    order.open("order.txt", ios::in);
    if (order.is_open() == true || order.is_open())
    {
        int counter = 0;
        while (!order.eof())
        {
            order >> order_save[counter].name;
            order >> order_save[counter].price;
            order_save[counter].place_number = counter + 1;
            counter++;
        }
        order_item_counter = counter;
    }
    else
    {
        cout << "Order not found\n";
    }
    order.close();
}

/**
 * It takes the order_input() function and displays the order_save array
 */
void display_order()
{
    order_input();
    cout << "::::::::::::XXX:::::::Order::::::XXX:::::::::::::\n";
    for (int i = 0; i < order_item_counter - 1; i++)
    {
        cout << "\n Item[" << order_save[i].place_number << "] " << order_save[i].name << " $" << order_save[i].price << '\n';
    }
    cout << endl
         << "::::::::::::XXX:::::::Order::::::XXX:::::::::::::\n";
}

/**
 * It's a function that allows the user to add or delete items from the order
 */
void the_edit()
{
    int number_navigator = 5;

    while (number_navigator != 0)
    {
        cout << "1. To add to the order " << endl;
        cout << "2. To delete from the order" << endl;
        cout << "0. To exit" << endl;
        cin >> number_navigator;

        if (number_navigator == 1)
        {
            the_menu();
            int order_answer;
            ofstream order;
            order.open("order.txt", ios::app);
            cout << "Place your order by entring the number" << endl;
            cout << "To end the order press 0" << endl;

            cin >> order_answer;
            if (order_answer >= 1 && order_answer < menu_item_counter + 1)
            {
                int x = 0;
                for (int i = 0; i < menu_item_counter; i++)
                {
                    if (order_answer == menu[i].place_number)
                    {
                        x = i;
                    }
                }

                order << menu[x].name << " " << menu[x].price << endl;
                total += menu[x].price;
            }
            else
            {
                cout << "Item not found" << endl;
            }
        }
        else if (number_navigator == 2)
        {
            display_order();
            int item_number;
            cout << "Choose item number to delete" << endl;
            cin >> item_number;
            if (item_number > 0 && item_number < order_item_counter)
            {
                ofstream order;
                order.open("order.txt", ios::out);
                for (int i = 0; i < order_item_counter - 1; i++)
                {
                    if (order_save[i].place_number != item_number)
                    {
                        order << order_save[i].name << " " << order_save[i].price << endl;
                        order_save[i].place_number = i;
                    }
                }
                order.close();
                total -= order_save[item_number].price;
                order_input();
            }
        }
    }
}

void total_price()
{
    ofstream order;
    order.open("order.txt", ios::app);
    order << endl
          << "Total $" << total << endl;
    order << endl
          << dt;
}

/**
 * The function asks the user to enter a name of a menu item, and if the name is found, the function
 * will display the menu item's place number, name, and price
 * 
 * @return Nothing
 */
void the_search()
{
    string search_answer;
    do
    {
        cout << "Search by name" << endl;
        cout << "0 To exit" << endl;
        cin >> search_answer;

        bool found = false;
        for (int i = 0; i < menu_item_counter; i++)
        {
            if (search_answer == menu[i].name)
            {
                cout << "Item found" << endl;
                cout << menu[i].place_number << ".";
                cout << menu[i].name << " $";
                cout << menu[i].price << endl;
                found = true;
                break;
            }
        }
        if (found == false && search_answer != "0")
        {
            cout << "Item not found" << endl;
        }

    } while (search_answer != "0");

    return;
}
/**
 * The function the_report() is used to display the details of the products in the inventory
 */
void the_report()
{
    double pProduct;
    double mExpensive;
    double Total = menu_item_counter;
    mExpensive = menu[0].price;
    for (int i = 1; i < menu_item_counter; i++)
    {
        pProduct = menu[i].price;
        if (pProduct > mExpensive)
        {
            mExpensive = pProduct;
        }
    }
    double lExpensive;
    lExpensive = menu[0].price;
    for (int i = 1; i < menu_item_counter; i++)
    {
        pProduct = menu[i].price;
        if (pProduct < lExpensive)
        {
            lExpensive = pProduct;
        }
    }

    cout << "\n\n\n\t\t*********************************************";
    cout << "\n\t\t                 DETAILS                  ";
    cout << "\n\t\t*********************************************";
    cout << "\n\n\t\tTOTAL PRODUCT                    :" << Total;
    cout << "\n\n\t\tMOST EXPENSIVE PRODUCT           :" << mExpensive;
    cout << "\n\t\tLEAST EXPENSIVE PRODUCT            :" << lExpensive;
    cout << "\n\t\t*********************************************\n";

    ofstream report;
    report.open("report.txt", ios::out);
    report << "TOTAL PRODUCT :" << Total << endl;
    report << "MOST EXPENSIVE PRODUCT :" << mExpensive << endl;
    report << "LEAST EXPENSIVE PRODUCT :" << lExpensive;
    report << endl
           << dt;
}

int navigator_number = 0;

int main()
{

    while (navigator_number != 6)
    {
        start();
        menu_input();

        cin >> navigator_number;

        if (navigator_number == 1)
        {
            the_order();
        }
        else if (navigator_number == 2)
        {
            display_order();
        }
        else if (navigator_number == 3)
        {
            the_edit();
        }
        else if (navigator_number == 4)
        {
            the_search();
        }
        else if (navigator_number == 5)
        {
            the_report();
        }
        else if (navigator_number == 6)
        {
            total_price();
            cout << "Good Bye";
        }
    }

    return 0;
}
