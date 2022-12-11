#include "../include/Helper.h"


Helper::Helper(int id_){
    priv_id = id_;
}

int Helper::get_id(){
    return priv_id;
}

void Helper::set_id(int id_){
    priv_id = id_;
}
