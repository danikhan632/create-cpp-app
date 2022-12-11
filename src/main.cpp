#include "../include/helper.h"
#include "../include/linkedlist.h"
#include "../include/node.h"

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

  LinkedList* list = new LinkedList(name);
  list->addToFront(name2);
  list->addToFront(name3);
  list->addToFront(name4);
  // list->~LinkedList();
  // free(list);

 list->print();
  list->~LinkedList();

  list->print();


    return 0;
  }
