#include "../include/adv.h"
// #include <curl/curl.h>


Adv::Adv(int id_){
    priv_id=id_;
}

static size_t WriteCallback(void *contents, size_t size, size_t nmemb, void *userp)
{
    ((std::string*)userp)->append((char*)contents, size * nmemb);
    return size * nmemb;
}

std::string Adv::makeGoogleReq(){
//  CURL *curl;
//   CURLcode res;
//   std::string readBuffer;

//   curl = curl_easy_init();
//   if(curl) {
//     curl_easy_setopt(curl, CURLOPT_URL, "http://www.google.com");
//     curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, WriteCallback);
//     curl_easy_setopt(curl, CURLOPT_WRITEDATA, &readBuffer);
//     res = curl_easy_perform(curl);
//     curl_easy_cleanup(curl);

//    return readBuffer.substr(0,300);
//   }
  return "uncomment code in src/adv.cpp and in conanfile.txt\n add the following line under [requires]: libcurl/7.86.0";
}