// Program that computes various quantities of a graph and prints to a file
//
// Erik G. Larsson, 2016

#include "Snap.h"

using namespace TSnap;

int main(int argc, char* argv[]) {

  TInt::Rnd.PutSeed(0); // initialize random seed
  
  PUNGraph G = LoadEdgeList<PUNGraph>("_G.edges");

  // Clustering coefficient
  
  TIntFltH CcfH;
  GetNodeClustCf(G, CcfH);  
  FILE *F = fopen("_G-clustering.csv", "wt");
  //  fprintf(F,"NodeId,Degree,ClustCoeff\n");
  for (TUNGraph::TNodeI NI = G->BegNI(); NI < G->EndNI(); NI++) {
    const int NId = NI.GetId();
    const double DegCentr = G->GetNI(NId).GetDeg();
    const double ClustCf = CcfH.GetDat(NId);
    fprintf(F, "%d,%f,%2.15f\n",NId,DegCentr,ClustCf);
  }
  fclose(F);

  // Degree distribution

  TIntPrV DegCntV;
  GetDegCnt(G, DegCntV);
  TIntPrV DegCntVcum = TGUtil::GetCCdf(DegCntV); 
  F = fopen("_G-degree.csv", "wt");
  for (int i = 0; i < DegCntV.Len(); i++) {
    fprintf(F, "%i,%f,%f\n",DegCntV[i].Val1,DegCntV[i].Val2/double(G->GetNodes()),DegCntVcum[i].Val2/double(G->GetNodes()));
  }
  fclose(F);
  
}
