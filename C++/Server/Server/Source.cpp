#include <iostream>
#include <vector>

#include <json/json.hpp>
#include <cpp_httplib/httplib.h>

#include "Lobby.h"
#include "Maze.h"

using json = nlohmann::json;

int main()
{
	Lobby a;

	Maze maze;
	maze.PrintGrid();

	for (int i = 0; i < 15; i++) {
		for (int j = 0; j < 20; j++)
			std::cout << maze.gridInt[i][j] << ' ';
		std::cout << '\n';
	}

	return 0;
}