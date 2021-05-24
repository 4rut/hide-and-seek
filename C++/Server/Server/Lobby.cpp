#include <iostream>
#include <string>
#include <cstdlib>

#include "Lobby.h"


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
}