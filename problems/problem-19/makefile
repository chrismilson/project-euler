FILES = count-sundays.cpp
CXX = g++
CXXFLAGS =
OBJECTS = $(FILES:%.cpp=%.o)

.PHONY : all
all : $(OBJECTS)
	@ $(CXX) $(CXXFLAGS) $(OBJECTS) -o app
	@ ./app
	@ rm -rf $(OBJECTS) app

.SILENT : $(OBJECTS)
$(OBJECTS) :
