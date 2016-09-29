TARGETS := main

all: $(TARGETS)
	
main: main.o julia.o julia.h
	g++ -o $(TARGETS) main.o julia.o

main.o: main.cpp
	g++ -c main.cpp

julia.o: julia.cpp julia.h extra.o 
	g++ -c julia.cpp

extra.o: extra.cpp extra.h
	g++ -c extra.cpp

clean:
	rm -f *.o
	rm -f $(TARGETS)
