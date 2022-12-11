#include "../include/LinkedList.h"

 LinkedList::LinkedList(std::string* data_){
    Node* temp = new Node(data_);
    size=0;
    head=temp;
 }


 LinkedList::~LinkedList(){
    Node* curr = head;
    while(curr->getNext() != nullptr){
        Node* temp =curr->getNext();
        curr->~Node();
        free(curr);
        curr = temp;
    }
 }        
 void LinkedList::addToFront(std::string* data_){
    Node* temp = head;
    Node* new_head= new Node(data_);
    new_head->setNext(temp);
    head=new_head;
    size++;
 }

 void LinkedList::addToBack(std::string* data_){
    Node* curr = head;
    while(curr->getNext() != nullptr){
        curr = curr->getNext();
    }
    curr->setNext(new Node(data_));
    size++;
 }
 void LinkedList::addAtIndex(std::string* data_, unsigned int idx_){
   if(idx_ > size){return;}
   Node* curr = head;
   for(int i =0; i < idx_; i++){
      curr = curr->getNext();
   }
      Node* temp_next = curr->getNext();
      Node* temp = new Node(data_);
      curr->setNext(temp);
      temp->setNext(temp_next);
      size++;
 }
 Node* LinkedList::getFront(){
   return head;
 }
 Node* LinkedList::getBack(){
    Node* curr = head;
    while(curr->getNext() != nullptr){
        curr = curr->getNext();
    }
    return curr;
 }


 Node* LinkedList::getAtIndex(unsigned int idx_){
   if(idx_ > size){return nullptr;}
   Node* curr = head;
   for(int i =0; i < idx_; i++){
      curr = curr->getNext();
   }
   return curr;
 
 }
Node* LinkedList::removeFront(){
    Node* temp = head->getNext();
    Node* old_head=head;
    head=temp;
   //  old_head->~Node();
   //  free(old_head);
    size--;
   return old_head;
}
   Node* LinkedList::removeBack(){
      Node* curr = head;
      while(curr->getNext()->getNext() != nullptr){
         curr = curr->getNext();
      }
    Node* old_node=curr->getNext();
    curr->setNext(nullptr);
    size--;
    return old_node;
   }
 Node* LinkedList::removeAtIndex(unsigned int idx_){
   if(idx_ > size){return nullptr;}
   Node* curr = head;
   for(int i =0; i < idx_-1; i++){
      curr = curr->getNext();
   }
   Node* old_node=curr->getNext();
    curr->setNext(curr->getNext()->getNext());
    size--;
    return old_node;
 }
unsigned int LinkedList::getSize(){return size;}

 void LinkedList::print(){
    Node* curr = head;
    while(curr->getNext() != nullptr){
        std::cout << curr->getData()->c_str() <<std::endl;
        curr = curr->getNext();
    }
 }
 Node* LinkedList::toArray(){
   Node* curr = head;
   Node* array_ptr; if (!(array_ptr = (Node *) malloc(sizeof(Node) * size))) return nullptr;
   for(int i=0; i< size; i++){
      array_ptr[i] = *curr;
      curr=curr->getNext();
   }
   return array_ptr;
 }

