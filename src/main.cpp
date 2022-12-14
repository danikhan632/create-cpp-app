#include "../include/Helper.h"
#include "../include/LinkedList.h"
#include "../include/Node.h"

#include <stdlib.h>

//------------------------------------------------------------------------------------
// Program main entry point
//------------------------------------------------------------------------------------


int main(void)
{
  std::string* name= new std::string("bob");
  std::string* name2= new std::string("sally");
  std::string* name3= new std::string("joe");
  std::string* name4= new std::string("james");
  std::cout<<"Hello World!\nThis is an example of a custom LinkedList in C++\n\n"<<std::endl;

  LinkedList* list = new LinkedList(name);
  list->addToFront(name2);
  list->addToFront(name3);
  list->addToFront(name4);
  // list->~LinkedList();
  // free(list);

 list->print();
 std::cout<<"Looks like it has a seg fault, yikes!\nrun \"cpx\" in the terminal to see options such as \"cpx dev\"to build and run\n\n"<<std::endl;

  list->~LinkedList();
  list->print();

    return 0;
  }
