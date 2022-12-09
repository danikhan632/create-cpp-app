#ifndef Adv_H
#define Adv_H
//    the entire header file
#include <string>
#include <vector>
#include <iostream>
#include <cstdlib>

class Adv
{
private :
     int priv_id;


public :
     Adv(int id_);          
     int get_id();
     std::string makeGoogleReq();

     void set_id(int id_);

};

#endif