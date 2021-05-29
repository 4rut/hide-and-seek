#include <iostream>
#include <string>
#include <vector>
#include <thread>
#include <chrono>

#include <fstream>

#include <json/json.hpp>
#include "include/cpp_httplib/httplib.h"

#include "Lobby.h"

#define NUMBER_OF_ROOMS 5

using json = nlohmann::json;
using namespace httplib;

Lobby lobby;

void gen_response(const Request& req, Response& res) 
{
	static int i = 0;
	std::cout << i++ << "\n";
	res.set_content(lobby.data.dump() ,"text/json; charset=UTF-8");
}

int main()
{

	Server svr;
	svr.Get("/", gen_response);

	std::cout << lobby.roomId << std::endl;
	
	svr.Get(("/")/* + lobby.roomId).c_str()*/, gen_response);


	std::cout << "Start server... OK\n";
	svr.listen("localhost", 1234);
	return 0;
}