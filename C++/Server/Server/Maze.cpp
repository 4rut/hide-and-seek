#include <iostream>
#include <cstdlib>

#include "Maze.h"


void Maze::ResetGrid()
{
	for (int i = 0; i < GRID_WIDTH * GRID_HEIGHT; ++i)
	{
		gridChar[i] = '#';
	}
}

int Maze::XYToIndex(int x, int y)
{
	return y * GRID_WIDTH + x;
}

int Maze::IsInBounds(int x, int y)
{
	if (x < 0 || x >= GRID_WIDTH) return false;
	if (y < 0 || y >= GRID_HEIGHT) return false;
	return true;
}

void Maze::Visit(int x, int y)
{
	gridChar[XYToIndex(x, y)] = ' ';
	
	int dirs[4];
	dirs[0] = NORTH;
	dirs[1] = EAST;
	dirs[2] = SOUTH;
	dirs[3] = WEST;

	for (int i = 0; i < 4; ++i)
	{
		int r = rand() & 3;
		int temp = dirs[r];
		dirs[r] = dirs[i];
		dirs[i] = temp;
	}

	for (int i = 0; i < 4; ++i)
	{
		int dx = 0, dy = 0;
		switch (dirs[i])
		{
		case NORTH: dy = -1; break;
		case SOUTH: dy = 1; break;
		case EAST: dx = 1; break;
		case WEST: dx = -1; break;
		}
	
		int x2 = x + (dx << 1);
		int y2 = y + (dy << 1);
		if (IsInBounds(x2, y2))
		{
			if (gridChar[XYToIndex(x2, y2)] == '#')
			{
				gridChar[XYToIndex(x2 - dx, y2 - dy)] = ' ';
		
				Visit(x2, y2);
			}
		}
	}
}

void Maze::PrintGrid()
{
	for (int y = 0; y < GRID_HEIGHT; ++y)
	{
		for (int x = 0; x < GRID_WIDTH; ++x)
		{
			std::cout << gridChar[XYToIndex(x, y)];
		}
		std::cout << std::endl;
	}
}

Maze::Maze() 
{
	srand(time(0));
	ResetGrid();
	Visit(1, 1);

	for (int y = 0; y < GRID_HEIGHT; ++y)
		for (int x = 0; x < GRID_WIDTH; ++x)
			if(gridChar[XYToIndex(x, y)] == '#')
				gridInt[y][x] = 1;
			else
				gridInt[y][x] = 0;
}