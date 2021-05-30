#include <iostream>
#include <string>
#include <cstdlib>
#include <vector>

#include <json/json.hpp>
#include "include/cpp_httplib/httplib.h"

#include "Lobby.h"

using json = nlohmann::json;
using namespace httplib;


void Lobby::generateRoomId()
{
	srand(time(NULL));

	std::string tmp;
	for (int i = 0; i < ROOM_ID_LENGTH; i++)
		tmp += charactersToGenerateId[rand() * sizeof(charactersToGenerateId) / RAND_MAX];
	roomId = tmp;
}


Lobby::Lobby()
{
	generateRoomId();
	data["roomId"] = roomId;

	for (int i = 0; i < 15; i++)
		for (int j = 0; j < 20; j++)
			data["maze"][i][j] = maze.gridInt[i][j];

	data["number_of_players"] = 0;
	data["players"] = {};

}
	
void Lobby::ddos_cli() 
{
		
}

void Lobby::connect_to_players()
{
	for (int i = 1; i <= 5; i++)
	{
		try
		{
			Client cli(("http://localhost:" + std::to_string(1234 + i)).c_str());
			players.push_back(cli);

			std::cout << "Connected to " << "http://localhost:" << std::to_string(1234 + i);
		}
		catch (int)
		{
			std::cerr << "Connection failed to " << "http://localhost:" << std::to_string(1234 + i);
		}
	}
}
