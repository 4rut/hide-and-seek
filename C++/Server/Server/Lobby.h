#pragma once

#include <string>

#include "Maze.h"

#include <json/json.hpp>

#include "include/cpp_httplib/httplib.h"


using json = nlohmann::json;
using namespace httplib;


#define ROOM_ID_LENGTH 6

class Lobby : private Maze
{

private:
	Maze maze;

	char charactersToGenerateId[62] = { 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
									  'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 
									  'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 
									  'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' };
	void generateRoomId();
	




public:
	Lobby();
	
	std::string roomId;
	json data = {};
	int try_to_connect = 0;
	void ddos_cli();

	// Clients
	// 1. Arrays does no working
	// 2. The constructor does not work with an equal sign
	// 3. The parenthesized declaration creates a function
	// 4. I love cpp <3

	Client player1{ "http://localhost:1235" };
	Client player2{ "http://localhost:1236" };
	Client player3{ "http://localhost:1237" };
	Client player4{ "http://localhost:1238" };
	Client player5{ "http://localhost:1239" };
};

