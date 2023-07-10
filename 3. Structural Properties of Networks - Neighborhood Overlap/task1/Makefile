# 1. $make synth_data
# 2. ./synth_data
CC = g++
CXXFLAGS += -std=c++98 -Wall
CXXFLAGS += -O3 -DNDEBUG
CXXOPENMP = -fopenmp
LDFLAGS +=
LIBS += -lrt

TPATH = /courses/TSKS11/ht2019/

analysis: analysis.cpp 
	$(CC) $(CXXFLAGS) -o analysis analysis.cpp $(TPATH)/Snap-2.4/snap-core/Snap.o -I$(TPATH)/Snap-2.4/snap-core -I$(TPATH)/Snap-2.4/glib-core $(LDFLAGS) $(LIBS)

synth_data: synth_data.cpp 
	$(CC) $(CXXFLAGS) -o synth_data synth_data.cpp $(TPATH)/Snap-2.4/snap-core/Snap.o -I$(TPATH)/Snap-2.4/snap-core -I$(TPATH)/Snap-2.4/glib-core $(LDFLAGS) $(LIBS)	

