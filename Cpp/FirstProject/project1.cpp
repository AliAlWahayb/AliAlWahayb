#include <iostream>
#include <cstdlib>
#include <cmath>
#include <string>
#include <fstream>
using namespace std;

void start()
{
    cout << "chose a number" << endl;
    cout << "1. new order" << endl;
    cout << "2. display order" << endl;
    cout << "3. edit order" << endl;
    cout << "4. search order" << endl;
    cout << "5. " << endl;
    cout << "6. Exit" << endl;
}

struct menu_items
{
    string name;
    double price;
    int place_number;
};

menu_items menu[20];
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
            menufile>>menu[counter].name;
            menufile>>menu[counter].price;
            menu[counter].place_number = counter + 1;
            counter++;
        }
        menu_item_counter = counter - 1;
    }
    else
    {
        cout << "menu not found\n";
    }
    menufile.close();
}

void the_menu()
{
    for (int i = 0; i < menu_item_counter; i++)
    {
        cout << menu[i].place_number << ".";
        cout << menu[i].name << " ";
        cout << menu[i].price << endl;
    }
}

void the_order()
{
    the_menu();
    int order_answer;
    ofstream order;
    order.open("order.txt", ios::out);
    cout << "place your order by entring the number" << endl;
    cout << "to end the order press 0" << endl;

    while (order_answer != 0){
        cin >> order_answer;
        if (order_answer >= 1 && order_answer < menu_item_counter + 1)
        {
            order << order_answer << endl;
        }
        else if (order_answer !=0)
        {
            cout << "item not found" << endl;
        }
    }
}

void the_edit()
{
    the_menu();
    int order_answer;
    ofstream order;
    order.open("order.txt", ios::app);
    cout << "place your order by entring the number" << endl;
    cout << "to end the order press 0" << endl;
    while (order_answer != 0){
        cin >> order_answer;
        if (order_answer >= 1 && order_answer < menu_item_counter + 1)
        {
            order << order_answer << endl;
        }
        else if (order_answer !=0)
        {
            cout << "item not found" << endl;
        }
    }
}

void the_search()
{
    string search_answer;
    do
    {
        cout << "search by name" << endl;
        cout << "0 to exit" << endl;
        cin >> search_answer;

        bool found= false;
        for (int i = 0; i < menu_item_counter; i++)
        {
            if (search_answer == menu[i].name)
            {
                cout << "item found" << endl;
                cout << menu[i].place_number << ".";
                cout << menu[i].name << " ";
                cout << menu[i].price << endl;
                found=true;
                break;
            }
                
        }
        if (found==false && search_answer != "0")
        {
            cout<<"item not found"<<endl;
        }
        
        

        
    } while (search_answer != "0");
    
    return;
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
            cout << "2";
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
            cout << "5";
        }
        else if (navigator_number == 6)
        {
            cout << "good bye";
        }
    }

    return 0;
}