#include <iostream>
#include <string>
#include <vector>

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
	lobby.data["number_of_players"] = lobby.data["number_of_players"] + 1;
	std::cout << lobby.data["number_of_players"] << "\n";
	res.set_content(lobby.data.dump() ,"application/json; charset=UTF-8");
}

int main()
{
	Server svr;
	svr.Get("/", gen_response);

	std::cout << lobby.roomId << std::endl;
	
	svr.Get(("/")/* + lobby.roomId).c_str()*/, gen_response);

	lobby.ddos_cli();

	std::cout << "Start server... OK\n";
	svr.listen("localhost", 1234);
	return 0;
}