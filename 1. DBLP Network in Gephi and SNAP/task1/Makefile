
#Data generation:
#1. Download and install snap and Gephi, see the README.txt file in the root directory

#2. In case the file "z7" is unavailable, or the latest snapshot of
#the DBLP database is desired, run "make json" to generate this file.

#3. Edit the session1_task1.cpp program to add seeds as desired

#4. Compile the DBLP lab program: make session1_task1

#5. Run the DBLP lab program: ./session1_task1

# Note: compilation warning messages can be ignored, SNAP generates
# lots of those

# Note: DBLP2graph (and make json) take a long time to run. "make
# json" requires the unix packages ascii2uni and uni2ascii.

CC = g++
CXXFLAGS += -std=c++98 -Wall
CXXFLAGS += -O3 -DNDEBUG
# turn on for crash debugging, get symbols with <prog> 2>&1 | c++filt
#CXXFLAGS += -g -rdynamic
CXXOPENMP = -fopenmp
LDFLAGS +=
LIBS += -lrt

TPATH = /courses/TSKS11/ht2019/

session1_task1: session1_task1.cpp 
	$(CC) $(CXXFLAGS) -o session1_task1 session1_task1.cpp $(TPATH)/Snap-2.4/snap-core/Snap.o -I$(TPATH)/Snap-2.4/snap-core -I$(TPATH)/Snap-2.4/glib-core $(LDFLAGS) $(LIBS)


json:
	wget http://dblp.uni-trier.de/xml/dblp.xml.gz
	wget http://dblp.uni-trier.de/xml/dblp.dtd
	python DBLP2graph.py
	gunzip dblp_coauthorship.json.gz
	./prepfile.sh

