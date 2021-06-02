#include <iostream>
#include <thread>
#include <chrono>
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
	data["number_of_players_now"] = 0;
	data["players"] = {};
}

void Lobby::ddos_cli()
{
	bool first_run = true;

	while (true)
	{
		if (first_run) {
			std::this_thread::sleep_for(std::chrono::milliseconds(3000));
			first_run = false;
		}

			if (try_to_connect) {
			if (try_to_connect <= 1) 
			{
				try {
					auto res = player1.Get("/");
					std::cout << res->body << '\n';

					if (res->status == 200)
					{
						std::string tmp_str = res->body;

						json tmp_json = json::parse(tmp_str);

						data["players"]["player1"] = tmp_json;
						data["number_of_players_now"] = tmp_json["number_of_players_now"];

						if (tmp_json["number_of_players"] > 1)
							try_to_connect = tmp_json["number_of_players"];
					}
				}
				catch (int x) {}
			}

			if (try_to_connect >= 2)
			{
				try {
					auto res = player2.Get("/");

					if (res->status == 200)
					{
						std::string tmp_str = res->body;

						json tmp_json = json::parse(tmp_str);

						data["players"]["player2"] = tmp_json;
						data["number_of_players_now"] = tmp_json["number_of_players_now"];

						if (tmp_json["number_of_players"] > 2)
							try_to_connect = tmp_json["number_of_players"];

					}
					else
						std::cout << "321321321321";
				}
			catch (int x) {}
			}

			if (try_to_connect >= 3)
			{
				try {
					auto res = player3.Get("/");
	
					if (res->status == 200)
					{
						std::string tmp_str = res->body;

						json tmp_json = json::parse(tmp_str);

						data["players"]["player3"] = tmp_json;
						data["number_of_players_now"] = tmp_json["number_of_players_now"];

						if (tmp_json["number_of_players"] > 3)
							try_to_connect = tmp_json["number_of_players"];

					}
				}
				catch (int x) {}
			}

			if (try_to_connect >= 4) 
			{
				try {
					auto res = player4.Get("/");
						
					if (res->status == 200)
					{
						std::string tmp_str = res->body;

						json tmp_json = json::parse(tmp_str);

						data["players"]["player4"] = tmp_json;
						data["number_of_players_now"] = tmp_json["number_of_players_now"];

						if (tmp_json["number_of_players"] > 4)
							try_to_connect = tmp_json["number_of_players"];

					}
				}
				catch (int x) {}
			}

			if (try_to_connect >= 5) 
			{
				try {
					auto res = player5.Get("/");

					if (res->status == 200)
					{
						std::string tmp_str = res->body;

						json tmp_json = json::parse(tmp_str);

						data["players"]["player5"] = tmp_json;
						data["number_of_players_now"] = tmp_json["number_of_players_now"];

						if (tmp_json["number_of_players"] > 5)
							try_to_connect = tmp_json["number_of_players"];

					}
				}
				catch (int x) {}
			}
		}
	}
}

