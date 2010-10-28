
import networkx as nx

G = nx.Graph()

G.add_node("FRP", lobe='FL', sub='lateral surface')
G.add_node("SFG", lobe='FL', sub='lateral surface')
G.add_node("MFG", lobe='FL', sub='lateral surface')
G.add_node("OpIFG", lobe='FL', sub='lateral surface')
G.add_node("ORIFG", lobe='FL', sub='lateral surface')
G.add_node("TrIFG", lobe='FL', sub='lateral surface')
G.add_node("PrG", lobe='FL', sub='lateral surface')
           
G.add_node("MSFG", lobe='FL', sub='medial surface')
G.add_node("SMC", lobe='FL', sub='medial surface')
G.add_node("MFC", lobe='FL', sub='medial surface')
G.add_node("GRe", lobe='FL', sub='medial surface')
G.add_node("SCA", lobe='FL', sub='medial surface')
G.add_node("MPrG", lobe='FL', sub='medial surface')
           
G.add_node("AOrG", lobe='FL', sub='inferior surface')
G.add_node("MOrG", lobe='FL', sub='inferior surface')
G.add_node("LOrG", lobe='FL', sub='inferior surface')
G.add_node("POrG", lobe='FL', sub='inferior surface')
           
G.add_node("FO", lobe='FL', sub='opercular region')
G.add_node("CO", lobe='FL', sub='opercular region')
G.add_node("PO", lobe='FL', sub='opercular region')
           
G.add_node("AIns", lobe='FL', sub='insular region')
G.add_node("PIns", lobe='FL', sub='insular region')
           
           
G.add_node("TMP", lobe='TL', sub='lateral surface')
G.add_node("STG", lobe='TL', sub='lateral surface')
G.add_node("MTG", lobe='TL', sub='lateral surface')
G.add_node("ITG", lobe='TL', sub='lateral surface')
           
G.add_node("PP", lobe='TL', sub='supratemporal surface')
G.add_node("TTG", lobe='TL', sub='supratemporal surface')
G.add_node("PT", lobe='TL', sub='supratemporal surface')
           
G.add_node("FuG", lobe='TL', sub='inferior surface')
           
           
G.add_node("PoG", lobe='PL', sub='lateral surface')
G.add_node("SMG", lobe='PL', sub='lateral surface')
G.add_node("SPL", lobe='PL', sub='lateral surface')
G.add_node("AnG", lobe='PL', sub='lateral surface')
           
G.add_node("MPoG", lobe='PL', sub='medial surface')
G.add_node("PCu", lobe='PL', sub='medial surface')
           
           
G.add_node("SOG", lobe='OL', sub='lateral surface')
G.add_node("IOG", lobe='OL', sub='lateral surface')
G.add_node("MOG", lobe='OL', sub='lateral surface')
G.add_node("OCP", lobe='OL', sub='lateral surface')
           
G.add_node("OFuG", lobe='OL', sub='inferior surface')
           
G.add_node("Cun", lobe='OL', sub='medial surface')
G.add_node("Calc", lobe='OL', sub='medial surface')
G.add_node("LiG", lobe='OL', sub='medial surface')
           
           
G.add_node("ACgG", lobe='LC', sub='cingulate cortex')
G.add_node("MCgG", lobe='LC', sub='cingulate cortex')
G.add_node("PCgG", lobe='LC', sub='cingulate cortex')
           
G.add_node("PHG", lobe='LC', sub='medial temporal cortex')
G.add_node("Ent", lobe='LC', sub='medial temporal cortex')


G.add_edge("FRP","SFG")
G.add_edge("FRP","MFG")
G.add_edge("FRP","OrIFG")
G.add_edge("PrG","MPrG")
G.add_edge("MPrG","SMC")
G.add_edge("PrG","SFG")
G.add_edge("PrG","MFG")
G.add_edge("PrG","OpIFG")
G.add_edge("OrIPG","OFC")
G.add_edge("SMC","MSFG")
G.add_edge("MSFG","MFC")
G.add_edge("MFC","GRe")
G.add_edge("MFC","SCA")
G.add_edge("AIns","PIns")


G.add_edge("TMP","STG")
G.add_edge("TMP","MTG")
G.add_edge("TMP","ITG")
G.add_edge("STG","MTG")
G.add_edge("MTG","ITG")
G.add_edge("ITG","FuG")


G.add_edge("PoG","SPG")
G.add_edge("PoG","SMG")
G.add_edge("SPL","SMG")
G.add_edge("SPL","AnG")
G.add_edge("SMG","AnG")
G.add_edge("MPoG","PCu")


G.add_edge("OCP","SOG")
G.add_edge("OCP","MOG")
G.add_edge("OCP","IOG")
G.add_edge("SOG","MOG")
G.add_edge("SOG","IOG")
G.add_edge("MOG","IOG")
G.add_edge("OFuG","LiG")


G.add_edge("ACgG","MCgG")
G.add_edge("MCgG","PCgG")
G.add_edge("PHG","Ent")
