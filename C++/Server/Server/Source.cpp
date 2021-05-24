#include <iostream>
#include <string>
#include <vector>

#include <fstream>

#include <json/json.hpp>
#include "include/cpp_httplib/httplib.h"

#include "Lobby.h"
#include "Maze.h"

using json = nlohmann::json;
using namespace httplib;

void gen_response(const Request& req, Response& res) 
{
	res.set_content("test", "text/plain; charset=UTF-8");
}

int main()
{
	Server svr;
	svr.Get("/", gen_response);

	std::cout << "Start server... OK\n";
	svr.listen("localhost", 1234);
	return 0;
}