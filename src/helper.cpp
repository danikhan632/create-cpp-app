#include "../include/helper.h"
#include <string>
#include <vector>
#include <iostream>

helper::helper(int id_){
    priv_id = id_;
}

int helper::get_id(){
    return priv_id;
}

void helper::set_id(int id_){
    priv_id = id_;
}
