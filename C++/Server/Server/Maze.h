#pragma once

#define GRID_WIDTH 20
#define GRID_HEIGHT 15
#define NORTH 0
#define EAST 1
#define SOUTH 2
#define WEST 3

class Maze
{
private:
	char gridChar[GRID_WIDTH * GRID_HEIGHT];

	void ResetGrid();
	int XYToIndex(int x, int y);
	int IsInBounds(int x, int y);
	void Visit(int x, int y);

public:
	void PrintGrid();
	int gridInt[GRID_WIDTH][GRID_HEIGHT];

	Maze();

};

