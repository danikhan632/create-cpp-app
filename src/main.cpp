#include "../include/helper.h"
#include "../include/adv.h"
#include <stdlib.h>

//------------------------------------------------------------------------------------
// Program main entry point
//------------------------------------------------------------------------------------


int main(void)
{

	helper anna = helper(65);
	std::cout << (anna.get_id()) << std::endl;
	std::string hello = "hello world";
	std::cout << (hello) << std::endl;
  Adv goog = Adv(16);

  std::cout << (goog.makeGoogleReq()) << std::endl;

    return 0;
  }
