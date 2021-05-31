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
	std::cout << lobby.data["number_of_players"] << "\n";


	res.set_content(lobby.data.dump(), "application/json; charset=UTF-8");
	lobby.try_to_connect = 1;

	//std::cout << "number_of_players: " << (int)lobby.data["number_of_players"] << '\n';
}

int main()
{
	Server svr;
	svr.Get("/", gen_response);

	std::cout << lobby.roomId << std::endl;
	
	std::thread th1([&]() {
		lobby.ddos_cli();
		});

	std::cout << "Start server... OK\n";
	svr.listen("localhost", 1234);
	
	th1.detach();
	return 0;
}