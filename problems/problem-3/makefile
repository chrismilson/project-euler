CC = gcc
CFLAGS =
FILES = largest-pfactor.c
OBJECTS = $(FILES:%.c=%.o)

.PHONY : all
all : $(OBJECTS)
	@ $(CC) $(CFLAGS) $(OBJECTS) -o app
	@ ./app 600851475143
	@ rm -rf $(OBJECTS) app

.SILENT : $(OBJECTS)
$(OBJECTS) :
