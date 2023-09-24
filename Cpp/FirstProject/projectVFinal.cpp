#include <iostream>
#include <cstdlib>
#include <cmath>
#include <string>
#include <fstream>
#include <ctime>
using namespace std;

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

time_t now = time(0);
char *dt = ctime(&now);

struct menu_items
{
    string name;
    double price;
    int place_number;
};

menu_items menu[50];
int menu_item_counter = 0;

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
int order_item_counter = 0;

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
