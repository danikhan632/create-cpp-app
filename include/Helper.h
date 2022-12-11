#ifndef Helper_H
#define Helper_H
//    the entire header file
#include <string>
#include <vector>
#include <iostream>
#include <cstdlib>
class Helper
{
private :
     int priv_id;


public :
     Helper(int id_);          
     int get_id();
     void set_id(int id_);

};

#endif