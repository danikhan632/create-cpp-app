#ifndef Node_H
#define Node_H
//    the entire header file
#include <string>
#include <vector>
#include <iostream>
#include <cstdlib>
class Node
{
private :
    std::string* data;
    Node* next;


public :
     Node(std::string* data_);
     Node(std::string* data_, Node* next_); 
     ~Node();         
     std::string* getData();
     Node* getNext();
     void setNext(Node* next_);
     void setData(std::string* data_);
     

};

#endif