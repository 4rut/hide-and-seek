#include <iostream>
#include <thread>
#include <string>
#include <cstdlib>

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

	data["number_of_players"] = 1;
	data["is_room_empty"] = true;
	data["players"] = {};
}

void Lobby::ddos_cli() 
{
	while (true)
	{
		if (try_to_connect)
			try 
			{
				auto res = player1.Get("/");
				std::cout << res->status;
				if (res->status == 200) 
				{
					std::string tmp_str = res->body;
					std::string tmp_str_clear;
					
					// Json has extra '/' characters. This crutch removes them and saves them to a new variable
					for(int i = 0; i < tmp_str.length(); i++)
					if (tmp_str[i] != char(34) && tmp_str[i] != '\\')
						tmp_str_clear += tmp_str[i];
					
					json tmp_json = tmp_str_clear;

					data["players"]["player1"] = tmp_json;
				}
			}
			catch (int x) {}
	}

}

