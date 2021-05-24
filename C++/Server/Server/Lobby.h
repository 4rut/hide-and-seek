#pragma once

#include <string>

#include "Maze.h"

#include <json/json.hpp>


using json = nlohmann::json;


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
	json data;

};

