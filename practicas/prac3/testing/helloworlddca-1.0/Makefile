# Makefile

DESTDIR=.
PROG=hw

all: $(PROG)

$(PROG): $(PROG).c
	gcc $(PROG).c -o $@

install: $(PROG)
	mkdir -p $(DESTDIR)/usr/bin
	cp $(PROG) $(DESTDIR)/usr/bin/

clean:
	rm -f *~ $(PROG) *.o

.PHONY: clean install all
