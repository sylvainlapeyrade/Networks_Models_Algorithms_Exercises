// Data generation for the DBLP task in the data analysis lab.  This
// script converts the pre-processed DBLP database file, z7, into an
// edge-list in the SNAP format, and perform some analysis...
//
// Important output files:
// X.gv, graphviz file of the merged ego-1 networks
// X.NET, can be imported into Gephi (seems to be the best format)
//
// Erik G. Larsson, 2016-2019

#include "Snap.h"

using namespace TSnap;

int main(int argc, char* argv[]) {

  TSsParser Ss("/courses/TSKS11/ht2019/data_and_fcns/session1/z7", ssfWhiteSep, true, true, true);
  //  TSsParser Ss("z7", ssfWhiteSep, true, true, true);  // if running locally

  PUNGraph Z7 = TUNGraph::New();
  TStrHash<TInt> StrToNIdH;
  TIntPrIntH el;
  while (Ss.Next()) {
    const int SrcNId = StrToNIdH.AddDatId(Ss[0]);
    if (! Z7->IsNode(SrcNId)) { Z7->AddNode(SrcNId); }
    const int DstNId = StrToNIdH.AddDatId(Ss[1]);
    if (! Z7->IsNode(DstNId)) { Z7->AddNode(DstNId); }
    Z7->AddEdge(SrcNId, DstNId);
    TIntPr a;
    a.Val1 = SrcNId;
    a.Val2 = DstNId;
    if (el.IsKey(a)) {
	el.AddDat(a,el.GetDat(a)+1);
      } else {
      el.AddKey(a);
      el.AddDat(a,1);
    }
    // printf("%d %d \n",a.Val1,a.Val2);
  }
  Z7->Defrag();

  SaveEdgeList(Z7, "Z7.edges", "test");

  // --- Select ego nodes ---
  TVec<TInt> IDvec;
  // Paste two nodes here
  IDvec.Add(StrToNIdH.GetKeyId("Yonina_C._Eldar"));
  IDvec.Add(StrToNIdH.GetKeyId("Andrea_J._Goldsmith"));
  // IDvec.Add(StrToNIdH.GetKeyId("Thomas_L._Marzetta"));
  // IDvec.Add(StrToNIdH.GetKeyId("Emre_Telatar"));
  for (int n=0; n<IDvec.Len(); n++) {
    printf("Ego ID: %i\n",IDvec[n].Val);
  }

  // --- Find the merged ego-1 networks ---
  TIntV NIdV;
  NIdV.Clr(false);
  for (int n=0; n<IDvec.Len(); n++) {
    TBreathFS<PUNGraph> BFS1(Z7);
    BFS1.DoBfs(IDvec[n].Val, true, true, -1, 1);
    NIdV.AddUnique(IDvec[n].Val);
    for (int i = 0; i < BFS1.NIdDistH.Len(); i++) {
      if (BFS1.NIdDistH[i] == 1)  {
	NIdV.AddUnique(BFS1.NIdDistH.GetKey(i));
      }
    }
  }

    PUNGraph Z8 = GetSubGraph(Z7, NIdV);
  TIntStrH NIdLabelH2  = TIntStrH();
  for (TUNGraph::TNodeI NI = Z8->BegNI(); NI < Z8->EndNI(); NI++) {
    NIdLabelH2.AddDat(NI.GetId(), StrToNIdH.GetKey(NI.GetId()));
  }
  SaveGViz(Z8, "X.gv", "test", NIdLabelH2);

  // --- Save to .NET file readable by Gephi ---
  TIntH NIdToIdH(Z8->GetNodes(), true);
  FILE *F = fopen("X.NET", "wt");
  fprintf(F, "*Vertices %d\n", Z8->GetNodes());
  int i = 0;
  for (TUNGraph::TNodeI NI = Z8->BegNI(); NI < Z8->EndNI(); NI++, i++) {
    int n = NI.GetId();
    TStr s = StrToNIdH.GetKey(n);
    TStr s1 = s.Left(1)+". "+s.RightOf('_');
    s1.ChangeChAll('_',' ');
    fprintf(F, "%d  \"%s\"\n", i+1, s1.GetCStr());
    // fprintf(F, "%d  \"%s\"\n", i+1, s.GetCStr());
    NIdToIdH.AddDat(NI.GetId(), i+1);
  }

  fprintf(F, "*Edges %d\n", Z8->GetEdges());
  for (TUNGraph::TEdgeI EI = Z8->BegEI(); EI < Z8->EndEI(); EI++) {
    const int SrcNId = NIdToIdH.GetDat(EI.GetSrcNId());
    const int DstNId = NIdToIdH.GetDat(EI.GetDstNId());
    TIntPr a;
    int w=0;
    a.Val1 = EI.GetSrcNId();
    a.Val2 = EI.GetDstNId();
    if (el.IsKey(a)) {
       w += el.GetDat(a); }
    TIntPr b;
    b.Val2 = EI.GetSrcNId();
    b.Val1 = EI.GetDstNId();
    if (el.IsKey(b)) {
       w += el.GetDat(b); }
    fprintf(F, "%d %d %d \n", SrcNId, DstNId, w);
  }
  fclose(F);

  // --- Perform some analysis using SNAP ---
  PUNGraph Gra = Z8;  // use the merged ego-network

  TIntFltH BtwH, EigH, CcfH;
  printf("Computing clustering coefficients...\n");
  GetNodeClustCf(Gra, CcfH);
  printf("done.\n\n");
  printf("Computing betweenness centrality...\n");
  GetBetweennessCentr(Gra, BtwH, 1.0);
  printf("done.\n\n");
  printf("Computing eigenvector centrality...\n");
  GetEigenVectorCentr(Gra, EigH);
  printf("done.\n\n");

  F = fopen("X-centrality.csv", "wt");
  fprintf(F,"NodeId,Name,Degree,Betweenness,Eig,ClustCoeff\n");
  for (TUNGraph::TNodeI NI = Gra->BegNI(); NI < Gra->EndNI(); NI++) {
    const int NId = NI.GetId();
    const double DegCentr = Gra->GetNI(NId).GetDeg();
    const double BtwCentr = BtwH.GetDat(NId);
    const double EigCentr = EigH.GetDat(NId);
    const double ClustCf = CcfH.GetDat(NId);
    TStr s = StrToNIdH.GetKey(NId);
    fprintf(F, "%d,%s,%f,%f,%f,%f\n",NId,s.GetCStr(),DegCentr,BtwCentr,EigCentr,ClustCf);
  }
  fclose(F);

}
