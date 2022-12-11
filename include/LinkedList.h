#ifndef LinkedList_H
#define LinkedList_H
//    the entire header file
#include <string>
#include <vector>
#include <iostream>
#include <cstdlib>
#include "Node.h"

class LinkedList
{
private :
    unsigned int size;
    Node* head;



public :
     LinkedList(std::string* data_);
     ~LinkedList();         
     void addToFront(std::string* data_);
     void addToBack(std::string* data_);
     void addAtIndex(std::string* data_, unsigned int idx_);
     Node* getFront();
     Node* getBack();
     Node* getAtIndex(unsigned int idx_);
    Node* removeFront();
     Node* removeBack();
     Node* removeAtIndex(unsigned int idx_);
     void print();
     unsigned int getSize();
     Node* toArray(); //array


};


#endif