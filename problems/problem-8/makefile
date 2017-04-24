CC = gcc
CFLAGS =
FILES = greatest-product.c
OBJECTS = $(FILES:%.c=%.o)

.PHONY : all
all : $(OBJECTS)
	@ $(CC) $(CFLAGS) $(OBJECTS) -o app
	@ ./app
	@ rm -rf $(OBJECTS) app

.SILENT : $(OBJECTS)
$(OBJECTS) :
