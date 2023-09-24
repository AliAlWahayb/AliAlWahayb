#include <iostream>
#include <fstream>
using namespace std;


int main() {
    int navigator_number;

    

    do
    {
        cout<<"chose a number"<<endl;
        cout<<"1. Display Statistics"<<endl;
        cout<<"2. List Products"<<endl;
        cout<<"3. Add New Product"<<endl;
        cout<<"4. Remove Product"<<endl;
        cout<<"5. Edit Product"<<endl;
        cout<<"6. Exit"<<endl;
        cin>>navigator_number;

        cout<<"test";
    } while (navigator_number!=6);
    
	return 0;
}