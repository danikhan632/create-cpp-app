#ifndef helper_H
#define helper_H
//    the entire header file
#include <string>
#include <vector>
#include <iostream>
#include <cstdlib>
class helper
{
private :
     int priv_id;


public :
     helper(int id_);          
     int get_id();
     void set_id(int id_);

};

#endif