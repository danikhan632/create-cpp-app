#include "../include/node.h"
Node::Node(std::string* data_){
    data=data_;
    next=nullptr;
}
std::string* Node::getData(){
    return data;
}
void Node::setData(std::string* data_){
    data=data_;
}

Node* Node::getNext(){
    return next;
}
void Node::setNext(Node* next_){
    next=next_;
}
Node::~Node(){
    delete data;
}